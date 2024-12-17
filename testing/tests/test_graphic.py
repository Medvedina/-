import pytest
import customtkinter as ctk
from beautiful_calc import *
from testing.conftest import *


@pytest.mark.usefixtures('app')
def test_widget_visibility(app):
    assert app.children['!ctkbutton'].cget('text') == 'Калькулятор'
    assert app.children['!ctkbutton2'].cget('text') == 'Рандомайзер'
    assert app.children['!ctkbutton3'].cget('text') == 'Калькулятор IP'
    assert app.children['!ctkbutton4'].cget('text') == 'Системы счисления'
    assert app.children['!ctkentry'].winfo_ismapped()
    assert app.children['!ctkentry'].cget('state') == ctk.DISABLED



@pytest.mark.usefixtures('app')
def test_mode_change_visibility(app):
    app.update()
    button_mode_calc = app.children['!ctkbutton']
    button_mode_calc.invoke()
    widget_list = ['!ctkbutton', '!ctkbutton2', '!ctkbutton3', '!ctkbutton4', '!ctkentry']
    for widget in widget_list:
        assert app.children[widget].winfo_ismapped() is 0


@pytest.mark.usefixtures('mode_calc')
def test_mode_change_calc(mode_calc):
    window = mode_calc[0]
    mode_calc = mode_calc[1]
    assert window is not None
    widget_list = {mode_calc.label_calc, mode_calc.label_example, mode_calc.label_answer, mode_calc.entry_calc,
                   mode_calc.answer_box, mode_calc.button_calc, mode_calc.button_back}
    for widget in widget_list:
        assert widget is not None


@pytest.mark.usefixtures('mode_rand')
def test_mode_change_rand(mode_rand):
    window = mode_rand[0]
    mode_rand = mode_rand[1]
    assert window is not None
    widget_list = {mode_rand.label_ban, mode_rand.label_finish, mode_rand.label_start, mode_rand.label_answer,
                   mode_rand.entry_start, mode_rand.entry_finish, mode_rand.entry_ban, mode_rand.entry_finish,
                   mode_rand.checkbox_ban, mode_rand.button_rand, mode_rand.button_back}
    for widget in widget_list:
        assert widget is not None


@pytest.mark.usefixtures('mode_numsys')
def test_mode_change_numsys(mode_numsys):
    window = mode_numsys[0]
    mode_numsys = mode_numsys[1]
    assert window is not None
    widget_list = {mode_numsys.button_numsys, mode_numsys.label_numsys, mode_numsys.entry_input,
                   mode_numsys.menu_numsys, mode_numsys.answer_box, mode_numsys.button_back}
    for widget in widget_list:
        assert widget is not None


@pytest.mark.usefixtures('mode_ipcalc')
def test_mode_change_ipcalc(mode_ipcalc):
    window = mode_ipcalc[0]
    mode_ipcalc = mode_ipcalc[1]
    assert window is not None
    widget_list = {mode_ipcalc.entry_mask, mode_ipcalc.entry_ip, mode_ipcalc.answer_box, mode_ipcalc.menu_mask,
                   mode_ipcalc.label_mask, mode_ipcalc.label_ip, mode_ipcalc.label_answer}
    for widget in widget_list:
        assert widget is not None

