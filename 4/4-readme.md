# Rick And Morty Api
---
# task 4 helm
1. run project on minikube with helm tool
2. deploy service ingress
3. need helm to be is install 

download:
1. download folder 4 
2. navigate to the folder $(pwd)/3/helm
3. run commands

start minikube
```
minikube start
```
apply to helm tool :
```
helm upgrade --install rick-morty-api .
```

check source running:
```
kubectl get all
```

for run on url:

get the ip:
```
minikube ip
```

get: http://<minikube-ip>:<nodeport>
```
minikube service rick-morty-api-service --url
```
to set arg add to the path with new arg:   
```
http://<minikube-ip>:<nodeport>/?species=Human&status=Alive&origin=Earth
```

use ingerss:
---------------

navigate to hosts :   

`C:\Windows\System32\drivers\etc\hosts` 
 - Add the following line to the file:   
```
<minikube-ip>  rick-morty
```

run app on url with dns:

default arg:
```
http://rick-morty
```
new arg:
```
http://rick-morty/?species=Human&status=Dead&origin=Earth
```
check-health
```
http://rick-morty/health
```

