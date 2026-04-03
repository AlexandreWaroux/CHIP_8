BLACK_COLOR="\033[30;1m"
RED_COLOR="\033[31;1m"
GREEN_COLOR="\033[32;1m"
YELLOW_COLOR="\033[33;1m"
BLUE_COLOR="\033[34;1m"
CYAN_COLOR="\033[36;1m"
VIOLET_COLOR="\033[35;1m"
NO_COLOR="\033[0m"

def display_msg (msg , color="info"):
    match(color):
        case 'info': print (f'{CYAN_COLOR}{msg}{NO_COLOR}')
        case 'danger' | 'error':  print(f'{RED_COLOR}{msg}{NO_COLOR}')
        case 'Warning' : print(f'{YELLOW_COLOR}{msg}{NO_COLOR}')
        case 'attention': print(f'{BLUE_COLOR}{msg}{NO_COLOR}')
        case 'x': print(f'{VIOLET_COLOR}{msg:04X}{NO_COLOR}')
        case _: print(f'{GREEN_COLOR}{msg}{NO_COLOR}')
