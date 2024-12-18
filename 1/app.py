from flask import Flask, render_template
import requests
import os
import csv

CSV_FILENAME='RickMortyApi.csv'
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

with open(os.path.join(STATIC_FOLDER, CSV_FILENAME), "w", newline='', encoding='utf-8') as csvfile:
    fieldnames = ["Name", "Location", "Image"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # Write headers to the CSV file

    url = f"https://rickandmortyapi.com/api/character/?species=Human&status=Alive&origen=Earth"

    res = requests.get(url)
    if res.status_code != 200:
        print(f"ERROR talking to Rick and Morty API: {res.status_code}")

    else:
        data = res.json()
        for i in data['results']:
            species =(i['species'])
            status = (i['status'])
            origin = (i['origin']['name'])

            # clean result 
            if species == "Human" and "Earth" in origin:
                name = i["name"]
                location = i["location"]["name"]
                image = i["image"]

            writer.writerow({"Name": name, "Location": location, "Image": image})
    
print("RickMortyApi.csv file generated successfully!")


app = Flask(__name__)

@app.route("/")
def hello():
    return  render_template("index.html") 

if __name__ == "__main__": 
    app.run(debug=True)