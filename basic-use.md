docker container run hello-world

docker run - é a concatenação de:
  - docker image pull
  - docker container create
  - docker container start
  - docker container exec

docker container run debian bash --version
  - executa bash --version no container criado
  - cada vez que roda isso cria um novo container por causa do run
  - nesse caso, está no modo iterativo - vemos as saídas da execução

docker container ps
  - containers ativos

docker container ps -a
  - todos os containers que já foram executados. Se eu rodar o debian duas vezes, como ele finaliza logo após a execução, vão ter dois containers desse listados

docker container run --rm debian bash --version
  - com essa nova flag, ele remove o container depois que o processo é finalizado

docker container run -it debian bash
  - i: modo iterativo
  - t: terminal

docker container run --name mydeb -it debian
  - como cada run cria um container, existe esse modo para dar nomes a deles
  - os nomes devem ser únicos. Rodar o mesmo comando acima duas vezes vai gerar um erro na segunda vez.

docker container ls -a
  - mostra todos os container independente do status
  - alias: ps/list

docker container start -ai mydeb
  - a: attach
  - equivalente ao -ti
  - inicia um container

docker container run -p 8080:80 nginx
  - p: porta. Para mapear uma porta com o host
  - [porta host]:[porta container]

docker container run -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html nginx
  - v: volume. Mapear volumes entre o host e o container
  - [path host]:[path container]

docker container run -d -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html nginx
  - d: deamon - execução em background

docker container stop <name>
  - parar um container que esteja em background

docker container restart <name>
  - reiniciar um container

docker container logs <name>
  - logs do container

docker container inspect
  - informaões sobre o container

docker container exec <name> <comand>
  - executa um comando dentro do container
