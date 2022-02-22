#Trees Everywhere
##Artur Felipe da Silva Veloso
##(86) 9 9927-2370
##arturfdasveloso@gmail.com

#Requisitos
Python 3
Pip 3

Instalação da máquina virtual
virtualenv MV_TreesEverywhere

Instalação dos módulos
pip install -r requirements.txt

Migração das tabelas
python manage.py migrate

Criação do super usuário
python manage.py createsuperuser

Sobir o servidor para testar
python manage.py runserver

Acessar o site
http://127.0.0.1:8000/

Acessar ao admin
http://127.0.0.1:8000/admin/

Acessar a API
http://127.0.0.1:8000/api/

Requisição a API
http://127.0.0.1:8000/api/treelist/api/plantedtree/

Headers
Key=Authorization
Value=token (token gerado no django admin)