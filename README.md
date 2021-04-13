# Template python cli

[cookiecutter](https://github.com/audreyr/cookiecutter) es un package de Python que te permite crear templates. Este template esta dedicado a proyectos del tipo CLI. Se seguirán buenos prácticas indicadas en este [blogpost](https://sourcery.ai/blog/python-best-practices/).


## Features

- Testing con [pytest](https://docs.pytest.org/en/latest/)
- Formatting con [black](https://github.com/psf/black)
- Import sorting con [isort](https://github.com/timothycrosley/isort)
- Linting con [flake8](http://flake8.pycqa.org/en/latest/)
- Git hooks con [pre-commit](https://pre-commit.com/)
- Deployment con [Docker](https://docker.com/)


## Installation
El primer requerimiento para poder utilizar el template es instalar `cookiecutter`.

```sh
pip3 install cookiecutter
```

A continuación lo que tenemos que hacer es crear el proyecto. Para esto se debe ejecutar el siguiente comando:

```sh
cookiecutter https://github.com/PeepData/cookiecutter_python_cli.git
```
Luego se deberán completar dos valores: `project_name` y `repo_name`. El primero hace referencia al nombre del proyecto y el segundo tienen que ver con la naming convention a nivel directorios.

Luego se deberá ingresar al directorio donde se creó el proyecto e instalar las dependencias:

```sh
cd <repo_name>
pip3 install -r requirements.txt
pip3 install -e .
```

Para listar los comandos se deberá ejecutar la siguiente línea:

```sh
<repo_name> --help
```

Por el momento solo existe un comando que es el `run`. Queda a libertad de cada uno agregar los que crea necesario para una mayor comodidad en el uso.


## Initialise git repo

```sh
git init
git add --all
```

Crear en Bitbucket un repositorio con el mismo nombre. Y seguir los siguientes pasos:

```sh
git remote add origin YOUR_LINK_TO_REPO
git commit -m "my first commit"
git push -u origin master
```


## Setup pre-commit and pre-push hooks

```sh
pre-commit install -t pre-commit
pre-commit install -t pre-push
```


## Running test

Existe la posibilidad de crear test unitarios y ejecutarlos en diferentes caminos.

#### Tox
Es una forma sencilla de ejecuar test. Se crean virtualenv para los test donde se instalarán todas las dependencias y luego se ejecutan los tests.

```sh
tox
```

Por defecto `tox` tiene varios virtualenv disponibles para ejecutar. Para sólo ejecutar los tests se debe correr el siguiente comando:

```sh
tox -e test
```

#### Pytest
Se puede usar pytest directamente, se deben instalar las dependencias necesarias en el caso de que no lo estén y luego ejecutar el siguiente comando:

```sh
pip3 install pytest
pytest
```

## Contacto
Cualquier comentario o dudas contactame a thepeepdata@gmail.com.
