# Repositorio do sistema Consulta de Processos Unificados
Site para consulta de processos de varios bancos unificados

## REQUISITOS

1 - Git

2 - Python 3.9

2 - pip

3 - PostgreSQL ou SQlite

## PASSO A PASSO PARA CONFIGURAR AMBIENTE DE DEV LOCAL

1 - Faça o clone deste repositório.
```
$ git clone ...
```

2 - Crie / ative um ambiente virtual
```
$ python3 -m venv venv
```

3 - Para instalar as dependencias do projeto
```
$ pip install -r requirements-dev.txt
```

4 - Criar seu banco de dados postgres(funciona também com outros bancos de dados) necessario criar um arquivo .env para e inserir sua string de conexão,
seguir o .envExemple


5 - Executar as migrações para atualizar seu banco local

```
python manage.py migrate  --database=scup_db 
python manage.py migrate  --database=pad_db
python manage.py migrate  --database=users_db 
python manage.py migrate  --database=lebre_db

```

6 - Crie o Super Usuario. Siga as instruções do comando abaixo.
```
$ python manage.py createsuperuser --database=users_db
```

7 - Execute o servidor de aplicação
```
python manage.py runserver
```

### URL o Admin Django
* http://localhost:8000/admin/



Serviços

NGINX
```
Iniciar / Parar / Reiniciar

systemctl start nginx
systemctl stop nginx
systemctl restart nginx
```



