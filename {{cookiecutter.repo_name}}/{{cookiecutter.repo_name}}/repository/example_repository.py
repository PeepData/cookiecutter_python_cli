from {{cookiecutter.repo_name}}.models import Connection, ExampleModel

_mysql = Connection("mysql").create_session()


class ExampleRepository:
    @staticmethod
    def add_row(data):
        try:
            _mysql.add(ExampleModel(**data))
            _mysql.commit()
        except Exception:
            _mysql.rollback()
            raise
        finally:
            _mysql.close()
