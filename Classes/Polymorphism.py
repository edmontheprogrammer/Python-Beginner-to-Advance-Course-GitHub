# Polymorphism means many forms
# Poly means many
# morphism means forms

from abc import ABC, abstractclassmethod
from curses.textpad import Textbox

# UIControl is an abstract class because it inherits from 'ABC'
# class and 'draw()' method has the 'abstractclassmethod' decroter


class UIControl(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
print(isinstance(ddl, UIControl))
draw([ddl, textbox])
