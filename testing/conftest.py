import pytest
from beautiful_calc import create_app


@pytest.fixture(scope='module', autouse=True)
def app():
    window = create_app()
    yield window
    window.quit()
    window.destroy()