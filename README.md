# Trabalho de conclusão de curso - IFES - Serra

O trabalho consiste em uma arquitetura com o objetivo de automatizar a alocação de recurso de forma dinâmica com o objetivo de adequar o numero de instâncias necessárias para dar vazão ao fluxo de entrada da aplicação, com isso o custo computacional só é aumentado no momento do trafego elevado, e logo é reduzido quando o trafego é reduzido.

## À FAZER

- Cenário 1: 

Aumentar o trafego até determinado ponto, segurar o trafego e depois descer o trafego
Anotar as atividaes que foram realizadas durante o processo de construção.
Estudar melhor como funciona os graficos do Jmeter.

- Terminar de implementar os testes

A ferramenta de testes a ser utilizada é o Jmeter, ela inclusive gera graficos de como foi o experimento.

### Implementações futuras mas fora do escopo

- Cenario 2 : Trafego alto constante

- Cenario 3 : Trafego em rajadas

- Criar um endpoint mais elaborado

Cenaríos que possuem aumento de trafego momentâneo:
- Receita federal no Imposto de renda.
- Enem proximo da data de fim da inscrição.
- Ver se eu consigo obter um graficos do escalonamento das maquinas no kubernetes


## Configurando o ambiente do cluster

Primeiramente é necessário subir um cluster kubernetes, eu utilizei a ferramenta Docker Desktop para subir um cluster. Após a instalação vá em configuração, clique em kubernetes e clique em "enable Kubernetes". Aguarde ele configurar e reiniciar o Docker Desktop e pronto.

Para conseguir subir todas as configurações é necessário primeiro buildar a imagem da API que está no Dockerfile ou utilizar a imagem que eu já subi no Dockerhub, é possível que a imagem não esteja mais disponível caso tenha se passado muito tempo sem ser baixada, nesse caso é necessário gerar o build.

Gerando a imagem:

    docker build -t coudbenks/tcc_aplication:v0.4 .

Após isso vamos subir os componentes necessários pro projeto

    cd /projeto_tcc/Manifestos
    kubectl apply -f .

Mapear a porta do computador para a porta do cluster ou aplicar no deployment

    kubectl port-forward <pod_name> 8000:80
    kubectl port-forward deployment/<deploy_name> 8000:80

Para verificar se a aplicação está funcionando tente acessar ela pela URL:
localhost:8000

## Verificando se o ambiente está disponível

Para verificar se a API está funcionando devidamentem, tente consumir o endpoint de teste com o seguinte comando:

```bash
curl -X 'GET' 'http://localhost:8000/healthz' -H 'accept: application/json'
```

O resultado deve ser algo como: 

    {"message":"24"}

## Executando o teste de estresse

Os testes realizados utilizam como base a ferramenta Apache Jmeter ou apenas [Jmeter](https://jmeter.apache.org). é um software open source feito 100% em java que tem como objetivo de simular comportamento de testes de carga e medir a performance. É originalmente desenvolvido para testes em aplicações web mas podem ser expandidos para outros tipos de teste.

## Monitorando o teste de estresse

É possível monitorar o funcionamento da aplicação através do programa de linha de comando do kubernetes (kubectl) combinador

    watch kubectl get hpa


### Explicação do Jmeter

A ferramenta possui uma gama muito grande de variações e casos de uso, aqui eu vou especificar apenas os parametros e definições que eu precisei para realizar o teste de carga do meu cenário.

**Ramp up:** É o tempo no qual todos os usuário vão chegar no seu servidor, nesse caso, o aumento é:

numero_total_usuario / tempo_necessário_chegar_todos_usuário = aumento_usuario_por_segundo

**Sampler:** Simulam uma requisição especificamente.

**Thread:** Simula os usuários da aplicação.


Please note - The total number of requests are related to throughput, Whereas the number of active threads performing the same activity is related to concurrency.

From your requirements, I assume you want to measure the throughput which is related to the requests/second not the users per second. To achieve this, you can use a Constant Throughput Timer at your test plan level.

Constant Throughput timer allows you maintain throughput of your server (requests/sec). Here requests are samplers. Threads are users/clients which are requesting server using samplers.


## Variáveis do teste

URL:
QPS:
Duration:
Thread/Simultaneous connections:
Connection reuse range: ????
Uniform:
Jitter:
No Catch-up (qps is a ceiling):
Percentiles:
Histogram Resolution:

--------------------

Formato da conexão: (tcp,udp,http, tipo do cliente[go ou fastclient])
http request
timeout:

### Especificação dos componentes:

## Funcionamento do HPA

Da perspectiva mais basica, o controller HPA(HorizontalPodAutoscaler) opera em uma razão entre 

desiredReplicas = ceil[currentReplicas * ( currentMetricValue / desiredMetricValue )]

## Deixando a aplicação disponível "externamente" ao cluster.

### Usando NodePort

### Usando ingress

#### Instalando o Helm

Para isso o ideal é configurar através do ingress-controller

    $ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    $ chmod 700 get_helm.sh
    $ ./get_helm.sh

Após essa etapa, o healm já deve estar instalado na sua maquina, agora vamos instalar o ingress-controller.

#### Instalando Ingress-Controller

Após a instalação do Helm é necessário apenas digitar o seguinte comando que será baixado e instanciado um NGINX com ingress-controller já configurado.

    helm install nginx-ingress ingress-nginx/ingress-nginx

Após a instalação do ingress-controller é possível verificar se a instalação foi concluida com sucesso utilizando o seguinte comando:

    kubectl --namespace default get services -o wide -w nginx-ingress-ingress-nginx-controller

Com isso já temos as configurações do cluster para suportar acesso externo, no meu cenário do trabalho, como foi feito em um cluster local, o localhost será o meu acesso. Caso o ingress-controller seja instalado e configurado em uma cloud como AWS, Azure, etc, é gerado um IP publico associado ao ingress-controller, com isso é possível acessar o cluster externamente através de chamadas HTTP e HTTPs.

#### Configurando o ingress da aplicação.

O ingress-controller é responsável por fazer funcionar os recursos chamados ingress, existem diversos tipos de ingress-controller implementados com diversas tecnologicas, o que será utilizado nesse trabalho é o que utiliza o NGINX como proxy reverso.

#### Configurando acesso a aplicação através do ingress

- Configura o arquivo hosts com o IP que mapeia pra dentro do cluster. (kubectl get svc -n kube-system | grep kube-dns)
- Criar o ingress e enviar para o service que aponta para serviço correto.
- Lembrar de configurar no ingress a classe do ingress controller que foi instalado.



### Instalação do grafana e do prometheus
```bash
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update
    helm repo add grafana https://grafana.github.io/helm-charts
    helm repo update

    helm install prometheus prometheus-community/prometheus
```
#### Dados após instalação do prometheus.

```bash
    # The Prometheus PushGateway can be accessed via port 9091 on the following DNS name from within your cluster:
    # prometheus-prometheus-pushgateway.default.svc.cluster.local

    # Get the PushGateway URL by running these commands in the same shell:
    export POD_NAME=$(kubectl get pods --namespace default -l "app=prometheus-pushgateway,component=pushgateway" -o jsonpath="{.items[0].metadata.name}")
    kubectl --namespace default port-forward $POD_NAME 9091
```
#### Instalação do Grafana
```bash
    helm install grafana grafana/grafana

    kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```
DNS: grafana.default.svc.cluster.local

A senha é gerada durante o comando, no seu cenário a senha será outra.
pass: SGkV5obOfd4lz2uTEiL01yBHOEklD42FkkxAXJ94
```bash
    kubectl port-forward svc/grafana 3000:80
```
Foi feito um ingress para habilitar o grafana por fora. é importante adicionar no arquivo de hosts do sistema operacional pra voce conseguir acessar efetivamente (Adicionar a url para o ip 127.0.0.1)


### Instalação do prometheus STACK

Instalação:

    helm upgrade --install prometheus prometheus-community/kube-prometheus-stack -f values.yaml

Correção do bug de montagem:

    kubectl patch ds prometheus-prometheus-node-exporter --type "json" -p '[{"op": "remove", "path" : "/spec/template/spec/containers/0/volumeMounts/2/mountPropagation"}]'


# Dúvidas


Mapeando eventos com port-foward
https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/


kubectl patch deployment metrics-server -n kube-system --type 'json' -p '[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'

O scale down do kubernetes por padrão é 5 minutos.

Não descobri ainda como ele faz para escolher qual dos PODs ele derruba quando vai fazer o scale down, provavelemtne sem estado ele deve escolher arbitrariamente, procurar na documentação sobre isso.
https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-cooldown-delay


### Sobre NGINX

Sobre a arquitetura e funcioanamento
https://www.nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/

Sobre o funcionamento do ingress-controller
https://docs.nginx.com/nginx-ingress-controller/intro/how-nginx-ingress-controller-works/

