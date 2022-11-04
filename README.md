# Desafio Sifat

Criar um sistema CRUD para um Blog, usando Django Framework no backend.

## Tecnologias

* Django
* Rest Framework
* Django Filters

## Como executar

* Clone este repositório
   ```console
    git clone https://github.com/DandaraF/desafio_sifat_backend.git
    ```

* Entre dentro da pasta do projeto (desafio_sifat_backend)


* Renomeei o arquivo "env.example":
    ```console
    mv env.example .env
    ```
  
* Instale a máquina virtual:
    ```console
    virtualenv venv
    ```
* Ative a máquina virtual:
    ```console
    source venv/bin/activate
    ```
* Instalar o dependências:
    ```console
    pip install -r requirements.txt
    ```
* Starte o projeto:
    ```console
    python manage.py runserver
    ```
* Clique no link abaixo ou digite o link no navegador:
   * http://127.0.0.1:8000/api
   
## Informações da API
* A API foi hospedada em dandarafonseca.pythonanywhere.com, é possivel fazer o CRUD e filtrar as informações por texto, titulo e categoria.
