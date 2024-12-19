# Rick And Morty Api
---

# task 2 
1. turn the app to rest api
2. dockerfile the project 

download:
1. download folder 2 
2. navigate to the download folder
3. build image 
4. run container
5. run command
6. jason result at url
7. check at url

run command :

build image
```
docker build -t rick-morty-api .
```

run container 
```
docker run -p 5000:5000 rick-morty-api
```

output :

1. with default args:
```
http://localhost:5000   
```
Human Alive Earth  
Species= human    
Status = Alive   
Origin = Earth

1. url can change the Query  :  
Species= arg1    
Status = arg2   
Origin = arg3

```
http://localhost:5000/?species=Human&status=Alive&origin=Earth
```
1. check health 

```
http://localhost:5000/health
```