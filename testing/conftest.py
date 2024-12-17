import pytest
from beautiful_calc import *
import time


@pytest.fixture()
def app():
    time.sleep(1)
    window = create_app()[0]
    window.update()
    window.after(100)
    yield window
    window.quit()
    window.destroy()


@pytest.fixture()
def mode_calc():
    time.sleep(1)
    window = create_app()[0]
    mode_calc = create_app()[1](window)
    window.children['!ctkbutton'].invoke()
    yield window, mode_calc
    window.destroy()


@pytest.fixture()
def mode_rand():
    time.sleep(1)
    window = create_app()[0]
    mode_rand = create_app()[2](window)
    window.children['!ctkbutton2'].invoke()
    yield window, mode_rand
    window.destroy()


@pytest.fixture()
def mode_numsys():
    time.sleep(1)
    window = create_app()[0]
    mode_numsys = create_app()[3](window)
    window.children['!ctkbutton3'].invoke()
    yield window, mode_numsys
    window.destroy()


@pytest.fixture()
def mode_ipcalc():
    time.sleep(1)
    window = create_app()[0]
    mode_ipcalc = create_app()[4](window)
    window.children['!ctkbutton5'].invoke()
    yield window, mode_ipcalc
    window.destroy()