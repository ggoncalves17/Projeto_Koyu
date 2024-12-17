# Projeto_Koyu

## *Requisitos*

A primeira coisa a ser feita é o clone do repositório, utilizando, num local à escolha, o comando:

`git clone https://github.com/ggoncalves17/Projeto_Koyu.git` 

Para dar run à aplicação, aconselha-se a criação de um ambiente virtual para se poder isolar as dependências do mesmo recorrendo ao comando:

`python -m venv venv`

Depois, para se ativar o mesmo coloca-se `venv\Scripts\activate` e para se instalar as dependências necessárias coloca-se:

`pip install -r requirements.txt`

Para a criação da base de dados e respetivas tabelas (caso se tenham definidas nos modelos) coloca-se o comando:

`python manage.py migrate`

(Opcional) É possível a criação de uma conta superuser através do:

`python manage.py createsuperuser`

Por fim, para darmos o run da aplicação em si para verificar as alterações efetuadas faz-se:

`python manage.py runserver`
