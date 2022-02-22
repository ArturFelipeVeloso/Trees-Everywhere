# Trees Everywhere
#### Artur Felipe da Silva Veloso
##### (86) 9 9927-2370
##### arturfdasveloso@gmail.com

## Requisitos
##### - Python 3 - [Baixar](https://www.python.org/downloads/)
##### - Pip 3

## Instalação da máquina virtual
```sh
virtualenv MV_TreesEverywhere
```

## Instalação dos módulos
```sh
pip install -r requirements.txt
```

## Migração das tabelas
```sh
python manage.py migrate
```

## Criação do super usuário
```sh
python manage.py createsuperuser
```

## Subir o servidor para testar
```sh
python manage.py runserver
```

## Acessos


|  |  |
| ------ | ------ |
| Site | http://127.0.0.1:8000/|
| Admin | http://127.0.0.1:8000/admin|
| API | http://127.0.0.1:8000/api|
| Requisição a API | http://127.0.0.1:8000/api/treelist/api/plantedtree/ |

## Header

```sh
Headers
Key=Authorization
Value=token
```

> Obs: Substituir token em `Value` pelo `token gerado no django admin`

