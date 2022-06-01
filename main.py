from prettytable import PrettyTable
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
x = PrettyTable()
x.field_names = ["Pokemon name", "Type"]
x.add_row(["Pickachu", "Electric"])
x.add_row(["Squirtle", "Water"])
x.add_row(["Charmander", "Fire"])
x.align="c"
print(x)