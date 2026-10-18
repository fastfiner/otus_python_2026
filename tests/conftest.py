import pytest
from selenium import webdriver
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://prestashop.com",
        help="Укажите ссылку"
    )
    parser.addoption(
        "--status_code",
        default="200",
        help="Выберите ожидаймый статус"
    )
    parser.addoption(
        "--browser",
        default="chrome",
        help="Выберите браузер: chrome, firefox, edge"
    )
    
@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")

@pytest.fixture
def driver(request):
    """
    Создаёт браузер, передаёт в тест, закрывает после теста.
    """
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Браузер {browser} не поддерживается")

    driver.maximize_window()
    yield driver
    driver.quit()