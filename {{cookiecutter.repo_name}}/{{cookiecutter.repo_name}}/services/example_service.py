import datetime
import logging

from {{cookiecutter.repo_name}} import settings
from {{cookiecutter.repo_name}}.commons import ExampleHelper
from {{cookiecutter.repo_name}}.repository import ExampleRepository, ImpalaExampleRepository


class ExampleService:
    @staticmethod
    def example_function():
        data = {'content_id': ['3', '2', '1', '0'], 'title': ['a', 'b', 'c', 'd']}
        df = pd.DataFrame.from_dict(data)
        example_dict = ExampleHelper.clean_dict(df.to_dict('records')[0])
        try:
            ExampleRepository.add_row(example_dict)

        except Exception as e:
            raise e
