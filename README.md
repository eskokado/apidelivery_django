# apidelivery-django

## Description

The created API has the following requirements:

- Create an item delivery.
- Search for delivery of a specific item.
- Search for deliveries by recipient or by sender.
- Update status as delivered.
- Cancel a delivery.
- Consume another existing REST API to fetch data, such as neighborhood, street and geolocation, from zip code and number entered.
- Authentication flow using bearer token.
- Documentation using Swagger.

This API allows you to manage item deliveries, allowing you to create, query and update the delivery status, as well as search for deliveries by recipient or sender. Furthermore, it consumes an external API to fetch additional information about delivery addresses.

API security is ensured by an authentication flow, which requires the use of a valid authentication token to access protected resources.

API documentation is provided by Swagger, making it easy to use and understand the features available in the API.

## Como Executar o Projeto

- Clone o repositório do projeto para o seu computador, utilizando o comando git clone https://github.com/eskokado/apidelivery-django.git.
- Acesse a pasta do projeto e crie um ambiente virtual Python utilizando o comando ```python -m venv venv```. Esse comando criará uma pasta chamada venv com as dependências do projeto
- Ative o ambiente virtual Python utilizando o comando ```source venv/bin/activate```. Isso garantirá que as dependências do projeto sejam instaladas e executadas corretamente.
- Instale as dependências do projeto utilizando o comando ```pip install -r requirements.txt```. Isso garantirá que todas as dependências do projeto sejam instaladas corretamente.
- Crie o banco de dados SQLite utilizando o comando ```python manage.py migrate```. Isso criará o banco de dados SQLite e as tabelas necessárias para o funcionamento da aplicação.
- Inicie o servidor local do Django utilizando o comando ```python manage.py runserver```. Certifique-se de que o servidor esteja funcionando corretamente e que a API esteja acessível.
- Acesse a URL da documentação Swagger, que geralmente é http://localhost:8000/api/docs/swagger-ui/. Isso deve abrir a interface do Swagger, com uma lista de endpoints disponíveis na API.
- Utilize a interface do Swagger para testar os endpoints da API, realizando operações como criação, atualização e busca de entregas. É possível enviar dados de teste para os endpoints diretamente pela interface do Swagger.
- Verifique os resultados e certifique-se de que a API esteja funcionando corretamente.