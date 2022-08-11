from abc import ABC, abstractmethod


class TextBox():
    pass


class DropDownList():
    pass


def draw(controls):
    for control in controls:
        control.draw()
