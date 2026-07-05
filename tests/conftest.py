import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--env",           # имя параметра
        action="store",    # что делать с переданным значением
        default="dev",     # значение по умолчанию
        help="Выберите окружение: dev, test, prod"  # подсказка
    )

@pytest.fixture
def env(request):
    return request.config.getoption("--env")