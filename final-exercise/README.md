# Exercício Final - Envio de emails

**Objetivo:** exercitar os conceitos aprendidos durante o curso.

## 1. Banco de Dados
Usando um banco postgres. A versão será fixa (ao invés de latest) porque isso evita que a aplicação quebre por causa de uma atualização incompatível.

Lembrando: para subir os containers em modo deamon `docker-compose up -d`
Para ver quais serviços estão up: `docker-compose ps`
Rodando uma comando dentro do container: `docker-compose exec email_exercise_db psql -U postgres -c "\l"`
Parando os containers: `docker-compose down`

## 2. Volumes
Criar volumes para poder inicializar nosso banco de dados.
O script de init segue um padrão descrito na documentaão para ser usado na inicialização do banco.
Para checar, criamos um arquivo que executa alguns comandos no banco de dados, também disponível dentro do container. Para executá-lo:
`docker-compose exec email_exercise_db psql -U postgres -f /scripts/check.sql`

## 3. Frontend
Criar o serviço de frontend para o projeto.
Diferente do proposto do curso, foi criado um frontend usando Vue.js, com a seguinte referência:
- https://www.freecodecamp.org/news/how-to-create-a-vue-js-app-using-single-file-components-without-the-cli-7e73e5b8244f/

## 4. Backend
Cria um serviço em python que vai executar as operação pedidas pelo frontend. Por enquanto o frontend se conecta diretamente com o backend, portanto ele precisa ter a porta da aplicação aberta, disponível. Posteriormente será adicionado um proxy, garantindo um pouco mais de segurança.
