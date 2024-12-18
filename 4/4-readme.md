# Rick And Morty Api
---
# task 4 helm
1. run project on minikube
2. deploy service ingress

download:
1. download folder 4 
2. navigate to the folder $(pwd)/3/helm
3. run commands

start minikube
```
minikube start
```
apply the prject :
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
nvigate to hosts :   

`C:\Windows\System32\drivers\etc\hosts` 
 - Add the following line to the file:   
```
<minikube-ip>  rick-morty
```

from Nodeport for defult(arg) open url and get  < minikube-ip > : < nodeport >:
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
```
<minikube-ip>  rick-morty
```
run app on url with dns:

defult arg:
```
http://rick-morty
```
new arg:
```
http://rick-morty/?species=Human&status=Dead&origin=Earth
```
check-helth
```
http://rick-morty/health
```

