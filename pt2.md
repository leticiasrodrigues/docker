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
