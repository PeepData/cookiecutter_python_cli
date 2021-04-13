# {{cookiecutter.project_name}}
![python_version](https://img.shields.io/badge/python-{python_version}-blue)

Template desarrollado con [cookiecutter](https://github.com/cookiecutter/cookiecutter).

Breve descripción acerca del proyecto.

## Installation
Listar las dependencias y requerimentos para poder utilizar el cli.

1-Instalar las dependencias.

```sh
pip3 install -r requirements.txt
pip3 install -e .
```

2-Configurar las variables de entorno.

```sh
MYSQL_USER=<user>
MYSQL_PASSWORD=<password>
MYSQL_HOST=<host>
MYSQL_PORT=<port>
MYSQL_DATABASE=<database>
```

## Usage

Indicar como debe ejecutarse. Por ejemplo el proyecto debe ser utilizado con el siguiente comando:

```sh
{{cookiecutter.project_name}} run <arg1> <arg2>
```

Para más información:

```sh
{{cookiecutter.project_name}} --help
```


## Running test
Para correr los tests existen dos opciones disponibles:

#### Tox
Por defecto `tox` tiene varios virtualenv disponibles para ejecutar. Para sólo ejecutar los tests se debe correr el siguiente comando:

```sh
tox -e test
```

#### Pytest
Se puede usar pytest directamente, se deben instalar las dependencias necesarias en el caso de que no lo estén y luego ejecutar el siguiente comando:

```sh
pytest
```

## Contacto
Cualquier comentario o dudas contactame a thepeepdata@gmail.com.