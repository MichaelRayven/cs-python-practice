import PySimpleGUI as sg

theme_menu = ['theme_menu', ["LightGrey1", "LightGreen8", "DarkGrey8", "random"]]
buttons = [f"-BUTTON{x}-" for x in range(10)]
operators = ["-MULT-", "-DIVIDE-", "-ADD-", "-SUBTRACT-"]
button_size = (6,2)

current_num = []
full_operation = []

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Calibri 18')

    layout = [
        [sg.Text(
            "", 
            key="-BACKLOG-", 
            font="Calibri 18",
            justification="right", 
            expand_x=True, 
            pad=((10, 10), (20, 0)), 
            background_color="#dfdfdf",
            right_click_menu=theme_menu,
            text_color="#5f5f5f"
        )],
        [sg.Text(
            "", 
            key="-OUTPUT-", 
            font="Calibri 24",
            justification="right", 
            expand_x=True, 
            pad=((10, 10), (0, 20)), 
            background_color="#dfdfdf",
            right_click_menu=theme_menu,
            size=(6, 1)
        )],
        [sg.Button("Enter", key="-ENTER-", expand_x=True, size=button_size), sg.Button("C", key="-CLEAR-", size=button_size), sg.Button("🐸", key="-DELETE-", size=button_size)],
        [sg.Button("7", key="-BUTTON7-", size=button_size), sg.Button("8", key="-BUTTON8-", size=button_size), sg.Button("9", key="-BUTTON9-", size=button_size), sg.Button("*", key="-MULT-", size=button_size)],
        [sg.Button("4", key="-BUTTON4-", size=button_size), sg.Button("5", key="-BUTTON5-", size=button_size), sg.Button("6", key="-BUTTON6-", size=button_size), sg.Button("/", key="-DIVIDE-", size=button_size)],
        [sg.Button("1", key="-BUTTON1-", size=button_size), sg.Button("2", key="-BUTTON2-", size=button_size), sg.Button("3", key="-BUTTON3-", size=button_size), sg.Button("+", key="-ADD-", size=button_size)],
        [sg.Button("0", key="-BUTTON0-", expand_x=True, size=button_size), sg.Button(".", key="-DOT-", size=button_size), sg.Button("-", key="-SUBTRACT-", size=button_size)]
    ]

    return sg.Window("Calculator", layout=layout, finalize=True)

window = create_window("LightGrey1")

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in buttons:
        current_num.append(window[event].ButtonText)
        num_string = "".join(current_num)  

    if event in operators:
        num_string = "".join(current_num)

        # If backlog already contains a full expression
        # calculate it and save it there
        if len(full_operation) > 0 and num_string:
            full_operation.append("".join(current_num))
            result = eval(" ".join(full_operation))

            full_operation = [str(result), window[event].ButtonText]
            current_num = []

        # If backlog already has an operation selected
        # Replace it with the new one
        elif len(full_operation) > 0 and not full_operation[-1].isnumeric():
            full_operation[-1] = window[event].ButtonText

        # Just add number and operaton to backlog
        else:
            full_operation.append("".join(current_num))
            full_operation.append(window[event].ButtonText)

            current_num = []

    if event == "-DELETE-" and current_num:
        current_num.pop(len(current_num) - 1)

    # Clear all the fields 
    # and state variables
    if event == "-CLEAR-":
        current_num = []
        full_operation = []

    if event == "-ENTER-" and current_num:
        full_operation.append("".join(current_num))
        result = eval(" ".join(full_operation))

        current_num = list(str(result))
        full_operation = []

    if event == "-DOT-" and "." not in current_num:
        current_num.append(".")

    # Update user interface
    window["-BACKLOG-"].update("".join(full_operation))
    window["-OUTPUT-"].update("".join(current_num))

window.close()