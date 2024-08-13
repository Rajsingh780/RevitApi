__title__ = "Hello BIM World"
__Author__ ="Raj Singh"
__doc__ =""" This is Hello Button.
Click on it to see what happens..."""

uidoc = __revit__.ActiveUIDocument

from Snippets._selection import get_selected_elements



if __name__ == '__main__':
    print(get_selected_elements(uidoc))