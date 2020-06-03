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
docker image build -t ex-simple-build:latest .
 - t: tag da imagem a ser criada
 - cria uma imagem a partir de um Dockerfile
