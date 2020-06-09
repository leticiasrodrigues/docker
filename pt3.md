# Redes

docker network ls
  - mostra as redes disponíveis
  - Já há 3 por padrão: bridge (isolamento entre o host e os containers), host (containers direto no host) e none 9nenhuma porta do container exposta)
  - Há um outro possível: Overlay Network (Swarm)

## none
  - Container isolados. Sem acesso entre os containers nem ao mundo exterior

docker container run --rm --net none alpine ash -c "ifconfig"
  - cria o container com a rede none
  - --rm remove o container depois de executar
  - mostra as configurações da rede do container

## brigge (padrão)
  - isolamento da rede do host com a rede dos containers
docker network inspect bridge
docker container exec -it container1 ping 172.17.0.3
  - container1: criado a partir de alguma imagem
  - o endereço é de um container2. Podemos achar isso com: docker container exec -it constainer2 ifconfig

docker network create --driver bridge rede_nova
  - criando uma nova rede, em uma faixa ainda não utilizada

docker container run -d --name container3 --net rede_nova alpine sleep 1000
docker container exec -it container3 ping 172.17.0.2
  - O ping não vai funcionar, pois o container3 não está na mesa rede desse endereço IP

docker network connect bridge container3
  - bridge é o nome da rede do tipo bridge padrão. Ou seja, agora o container3 pode interagir com o endereço IP acima, que era dessa rede. O ping vai funcionar
  - Uma vez conectado, podemos desconectar
docker network disconnect bridge container3

## host
  - sem o bridge como sendo a ponte entre as interfaces de rede do host e as interfaces do container
  - usa diretamente as interfaces de rede do host
  - menos seguro, mais exposto, mas um pequeno ganho de performance

docker container run -d container4 --net host alpine sleep 1000
