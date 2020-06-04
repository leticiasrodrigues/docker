# Construindo suas próprias imagens

## Container x Imagem
A partir de uma imagem pode-se criar vários containers.
Imagem: sistema de arquivos
Container: processo

docker image pull [image]:[tag]

tag = ponteiros para imagens específicas

docker image tag redis:latest cod3r-redis
  - cria uma nova imagem com o mesmo hash de redis:latest

## Primeiro build
FROM
  - A imagem para ser baseada
RUN
  - Adiciona uma layer à imagem base
  - cada comando é uma nova layer
docker image build -t ex-simple-build:latest .
  - t: tag da imagem a ser criada
  - cria uma imagem a partir de um Dockerfile

## Build com argumentos

docker image build -t ex-build-arg .
docker container run ex-build-arg bash -c 'echo $S3_BUCKET'
  - Criando a imagem sem o argumento

docker image build --build-arg S3_BUCKET=myapp -t ex-build-arg .
docker container run ex-build-arg bash -c 'echo $S3_BUCKET'
  - Agora vemos o argumento passado na criação da imagem

docker image inspect --format="{{index .Config.Labels \"maintener\}}" ex-build-arg
  - Vendo alguma informação específica da imagem

## Build com copy
COPY
  - copiar um arquivo para dentro do docker

## Build dev
RUN
  - Observe que aqui encadeamos vários comandos, portanto não será criada um alayer para cada um, apenas uma para todos
WORKDIR
  - define onde estamos no container
ENTRYPOINT
  - configura o container como executável. Não é ignorado e podemos passar parâmetros diferentes dos padrões que estão no CMD
CMD
  - comandos/parâmetros. É sobrescrito se outros comandos forem passados na linha de comando.

docker container run -it -v $(pwd):/app -p 80:8000 --name python-server ex-build-dev
  - mapeia um volume local para o container

docker container run -it --volumes-from=python-server debian cat /log/http-server.log
  - Lendo o volume de um container em um outro container. Note que o arquivo que vamos ler é o mesmo que foi definido onde os logs serão registrados no servidor python.
