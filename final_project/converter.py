import PySimpleGUI as sg

layout = [
    [sg.Input(key="-INPUT-", enable_events=True), sg.OptionMenu(["km to mile", "kg to pound", "sec to min"], default_value="km to mile", key="-UNITS-"), sg.Button("Convert", key="-CONVERT")],
    [sg.Text('Output:', key="-OUTPUT-")]
]

window = sg.Window("Converter", layout=layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if values["-INPUT-"] and event == "-INPUT-":
        try:
            float(values["-INPUT-"])
        except:
            if len(values["-INPUT-"]) == 1 and values["-INPUT-"][0] == "-":
                continue
            window["-INPUT-"].update(values["-INPUT-"][:-1])
            

    if event == "-CONVERT":
        input_value = values["-INPUT-"]
        if input_value.isnumeric():
            match values["-UNITS-"]:
                case "km to mile":
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f"{input_value} km are {output} miles"
                case "kg to pound":
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f"{input_value} kg are {output} pound"
                case "sec to min":
                    output = round(float(input_value) / 60, 2)
                    output_string = f"{input_value} seconds are {output} minutes"

            window["-OUTPUT-"].update(output_string)
        else:
            window["-OUTPUT-"].update("Please, enter a number")

window.close()