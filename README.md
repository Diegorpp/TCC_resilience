## Executando o projeto

    cd /projeto_tcc

    docker build -t tcc_api .

    docker run -p 8000:8000 -d tcc_api

Subir imagem 

    docker build -t coudbenks/tcc_aplication:v?.? .
    docker push coudbenks/tcc_aplication:v?.?

Aplicar o service para mapear a porta 8000 do cluster para a porta 8000 do Pod.

    kubectl apply api_svc.yaml

Mapear a porta do computador para a porta do cluster ou aplicar no deployment

    kubectl port-forward <pod_name> 8000:8000
    kubectl port-forward deployment/<deploy_name> 8000:8000
    

# Dúvidas


Mapeando eventos com port-foward
https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/


kubectl patch deployment metrics-server -n kube-system --type 'json' -p '[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'
