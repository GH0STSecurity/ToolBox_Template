from pyfiglet import Figlet
import os

RED = '\033[31m'
LIGHTRED = '\033[91m'
RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    f = Figlet(font='Poison')
    banner = f.renderText('ToolBox')
    console_width = os.get_terminal_size().columns
    banner_lines = banner.split('\n')
    centered_banner = '\n'.join(line.center(console_width) for line in banner_lines)
    print(RED + centered_banner + RESET)

def show_options():
    options = ['[1] Option 1', '[2] Option 2', '[3] Option 3', '[4] Option 4',
               '[5] Option 5', '[6] Option 6', '[7] Option 7', '[8] Option 8']
    console_width = os.get_terminal_size().columns
    option_width = 20
    num_options_per_line = 4
    num_lines = (len(options) + num_options_per_line - 1) // num_options_per_line
    padding = (console_width - num_options_per_line * option_width) // (num_options_per_line + 1)

    for i in range(num_lines):
        line_options = options[i*num_options_per_line : (i+1)*num_options_per_line]
        line_text = ' ' * padding
        for j, option in enumerate(line_options):
            line_text += RED + option.center(option_width) + RESET + ' ' * padding
        print(line_text)
        if i == num_lines // 2 - 1:
            print()

    if len(options) % num_options_per_line != 0:
        print()

option_files = {
    1: 'option1.py',
    2: 'option2.py',
    3: 'option3.py',
    4: 'option4.py',
    5: 'option5.py',
    6: 'option6.py',
    7: 'option7.py',
    8: 'option8.py'
}

clear_screen()
show_banner()
show_options()

option_selected = False
option_number = None

while True:
    user_input = input(LIGHTRED + 'Toolbox> ' + RESET)

    if user_input == '':
        continue

    elif user_input == 'exit':
        print(RED + 'Exiting... ' + RESET)
        break

    elif user_input == 'help':
        print('\nAvailable commands:')
        print('help: show this list of commands')
        print('select <option number>: select an option')
        print('run: run the selected option')
        print('exit: exit the program\n')

    elif user_input.startswith('select'):
        try:
            option_number = int(user_input.split()[1])
            if option_number < 1 or option_number > 8:
                print('Invalid option number')
            else:
                option_selected = True
                print(f'Option {option_number} selected')
        except:
            print('Invalid command')

    elif user_input == 'run' or user_input == 'start':
        if option_selected:
            file_name = option_files.get(option_number)
            if file_name is not None and os.path.isfile(file_name):
                print(f'Stopping current script and running {file_name}')
                os.system(f'python {file_name}')
                break
            else:
                print(f'File {file_name} not found')
        else:
            print('No option selected')

    else:
        print('Invalid command')
