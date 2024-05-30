Back em django de uma aplicação com processamento de linguagem natural visando relacionar lições aprendidas com incidentes e outros tipos de textos.

Após utilizar o comando docker-compose up --build e o docker estiver rodando, utilizar o seguinte comando : "docker-compose exec web python manage.py migrate" para realizar as migrations.

Caso queria criar um superusuario para acessar o admin do django : "docker-compose exec web python manage.py createsuperuser"
