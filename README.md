# Aprendendo Docker

Notas e exercícios do curso **Docker: Ferramentas para desenvolvedores** disponível em [https://www.udemy.com/course/curso-docker/](https://www.udemy.com/course/curso-docker/).

**O que é Docker?**

Não é uma VM. É uma engine de administração de containers. Não é totalmente independente da máquina host, o que não acontece na VM por exemplo. Há um compartilhamento de alguns recursos, embora crie ambientes/processos isolados e controlados.

Utiliza os serviços do LXC (Linux Containers). Assim sendo, você só pode usar containers baseados em Linux.

Virtualização baseada em software, em sistema operacional. O kernel é compartilhado entre host e container.

Existem diferentes níveis de isolamento: memória, rede, CPU, sistema de arquivos, etc.
