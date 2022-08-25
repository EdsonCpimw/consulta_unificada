# Repositorio do sistema Consulta de Procesos Unificados
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
IMPORTANTE: Necessário criar um .env com as configurações antes do proximo comando
python manage.py migrate

```

7 - Crie o Super Usuario. Siga as instruções do comando abaixo.
```
$ python manage.py createsuperuser
```

8 - Execute o servidor de aplicação
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



