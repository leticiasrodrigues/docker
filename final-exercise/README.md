# Exercício Final - Envio de emails

**Objetivo:** exercitar os conceitos aprendidos durante o curso.

## 1. Banco de Dados
Usando um banco postgres. A versão será fixa (ao invés de latest) porque isso evita que a aplicação quebre por causa de uma atualização incompatível.

Lembrando: para subir os containers em modo deamon `docker-compose up -d`
Para ver quais serviços estão up: `docker-compose ps`
Rodando uma comando dentro do container: `docker-compose exec email_exercise_db psql -U postgres -c "\l"`
Parando os containers: `docker-compose down`
