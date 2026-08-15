import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="Укажите ссылку"
    )
    parser.addoption(
        "--status_code",
        default="200",
        help="Выберите ожидаймый статус"
    )

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
