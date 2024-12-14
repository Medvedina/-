import pytest
import customtkinter as ctk
from beautiful_calc import create_app

def test_widget_visibility(app):
    app.update()

    assert app.children
    assert app.children['!ctkbutton'].cget('text') == 'Калькулятор'
    assert app.children['!ctkbutton2'].cget('text') == 'Рандомайзер'
    assert app.children['!ctkentry'].winfo_ismapped()

def test_entry_state(app):
    entry = app.children['!ctkentry']
    assert entry.cget('state') == ctk.DISABLED