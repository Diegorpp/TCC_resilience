#!/bin/bash

docker build -t coudbenks/tcc_aplication:v0.4 .

kubectl delete -f Manifestos/api.yaml 
kubectl apply -f Manifestos/api.yaml 

sleep(4)

kubectl port-forward deploy/api-server 8000:80