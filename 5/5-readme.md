# 5. git hub action
---
yaml path in rp :   
- .github/workflow/work.yml

workflow :   
- the workflow have 1 job and 7 steps  
- work on ubuntu-latest  
- trigger on push to main + manual buttonS

step 1: get the checkout the code  
step 2: install minikube from store (uses)  
step 3: start minikube on docker driver  
step 4: wait in loop until minikube get ip  
step 5: apply yml deploiment and service from folder 3  
step 6: wait for pods create  
step 7: get minikube ip and port from nodeport  as varibels  
     	get new var to string of http:ip:port  
    	test by crul the new var(http.. string )  