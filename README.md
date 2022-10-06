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
    

## Executando o teste de estresse

Comando para rodar o teste de estresse

```bash
kubectl run -it fortio --rm --image=fortio/fortio -- load -qps 800 -t 120s -c 2 "api-svc/docs"

```



# Dúvidas


Mapeando eventos com port-foward
https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/


kubectl patch deployment metrics-server -n kube-system --type 'json' -p '[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'

O scale down do kubernetes por padrão é 5 minutos.

Não descobri ainda com oele faz para escolher qual dos PODs ele derruba quando vai fazer o scale down, provavelemtne sem estado ele deve escolher arbitrariamente, procurar na documentação sobre isso.
https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-cooldown-delay
