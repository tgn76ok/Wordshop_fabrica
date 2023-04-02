<h1> Desafio-GRUD</h1>
 
 ## Sobre

Escolhi o tema escola, pelo qual fiz implementei uma paginação com a biblioteca django-seed.

<p>Aplicação se base em cadastrar um aluno que possui um endereço e um curso no banco de dados,apois isso ser facilmente Acessado por meio de um requisição get.</p>


## Este projeto foi feito com:

* [Python 3.11.1](https://www.python.org/)
* [Django 4.1.7](https://www.djangoproject.com/)

* [Django Rest Framework 3.14.0](https://www.django-rest-framework.org/)

## Como rodar?
* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py createsuperuser 
python manage.py makemigrations
python manage.py migrate
```


