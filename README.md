# Aprendendo Docker

Notas e exercícios do curso **Docker: Ferramentas para desenvolvedores** disponível em [https://www.udemy.com/course/curso-docker/](https://www.udemy.com/course/curso-docker/).

**O que é Docker?**

Não é uma VM. É uma engine de administração de containers. Não é totalmente independente da máquina host, o que não acontece na VM por exemplo. Há um compartilhamento de alguns recursos, embora crie ambientes/processos isolados e controlados.

Utiliza os serviços do LXC (Linux Containers). Assim sendo, você só pode usar containers baseados em Linux.

Virtualização baseada em software, em sistema operacional. O kernel é compartilhado entre host e container.

Existem diferentes níveis de isolamento: memória, rede, CPU, sistema de arquivos, etc.

**O que são Containers?**
- Segregação de processos no mesmo kernel (isolamento)
- Sistemas de arquivos criados a partir de uma imagem
- Ambientes leves e portáteis no qual as aplicações são executadas
- Encapsula todos os binários e bibliotecas necessárias para a execução de uma aplicação
- Algo entre um chroot e uma VM

Processo segregado com seu próprio sistema de arquivos separado da máquina host, com todos os binários e bibliotecas necessários para a aplicação.
É recomendado que cada container tenha uma responsabilidade específica, ao invés de colocar vários processos distintos em apenas um. Isso também possibilita escalar cada um deles individualmente.

Chroot é um comando para redefinir a pasta raiz para um determinando processo. 'Aprisiona' o processo a essa pasta raiz e não tem acesso a outras pastas do sistemas.

VM é o outro extremo, onde o isolamento é completo, inclusive do SO.
