from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route("/health")
def health_check():
    return jsonify(status="healthy"), 200


@app.route('/', methods=['GET'])
def get_characters():
    
    species = request.args.get('species', default='Human')
    status = request.args.get('status', default='Alive')
    origin = request.args.get('origin', default='Earth')

   
    url = f"https://rickandmortyapi.com/api/character/?species={species}&status={status}&origin={origin}"
    res = requests.get(url)
    
    if res.status_code != 200:
        return jsonify({"error": f"Error talking to Rick and Morty API: {res.status_code}"}), res.status_code
    else:
        data = res.json()
        characters = []
        
        for i in data['results']:
            if i['species'] == species and i['status'] == status and origin in i['origin']['name']:
                character = {
                    "name": i["name"],
                    "location": i["location"]["name"],
                    "image": i["image"]
                }
                characters.append(character)
        
        return jsonify(characters) 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
