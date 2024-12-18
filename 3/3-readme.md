# Rick And Morty Api
---
# task 3
1. run project on minikube
2. deploy service ingress

download:
1. download folder 3 
2. navigate to the folder $(pwd)/3/yamls
3. run commands

start minikube
```
minikube start
```
install addon ingress
```
minikube addons enable ingress
```


applay the yamls:
--------------------------
run :
```
kubectl apply -f Deployment.yaml -f Service.yaml -f Ingress.yaml

```

check command:

```
kubectl get all
```
```
kubectl get pods
```

apply the app on url :
---------------------

from Nodeport for defult(arg):
get: http://<minikube-ip>:<nodeport>
```
minikube service rick-morty-api-service --url
```
to set arg add to the path with new arg:
http://<minikube-ip>:<nodeport>/?species=Human&status=Alive&origin=Earth



use ingerss:
---------------

1.install minikube addons enable ingress
2.get the node ip
```
minikube ip
```
3. nvigate to hosts 
C:\Windows\System32\drivers\etc\hosts 
 - Add the following line to the file:
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

