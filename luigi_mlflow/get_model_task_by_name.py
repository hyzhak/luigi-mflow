import luigi

ROOT_PATH = 'src.models'


def get_model_task_by_name(name: str) -> luigi.Task:
    """
    get a model luigi task by its name

    :param name:
    :return:
    """
    try:
        m = __import__(f'{ROOT_PATH}.{name}', fromlist=[''])
    except ModuleNotFoundError:
        raise Exception(f'There is no such model as {name}')

    if 'Model' not in dir(m):
        raise Exception(f'Model {name} should define Model class')

    return m.Model
