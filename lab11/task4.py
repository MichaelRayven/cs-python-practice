# Напишите программу "Рандом". В программе должно быть три поля. Два для ввода границ рандома.
# Третье для вывода псевдослучайного числа. И одна кнопка "Сгенерировать". А также графический
# интерфейс должен включать один рисунок. 
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint
import playsound
import os

working_dir = os.path.join(os.path.dirname(__file__), "resources")

window = tk.Tk()
window.title("Randomizer")
window.resizable(width=False, height=False)

# Center image
image = Image.open(os.path.join(working_dir, "dice.png"))
resize_img = image.resize((256, 256))
img = ImageTk.PhotoImage(resize_img)
image_label = tk.Label(master=window, image=img)
image_label.pack()

# Create a frame for inputs
limits_frame = tk.Frame(master=window)
limits_frame.pack(pady=10)

# Input labels
label_min = tk.Label(master=limits_frame, text="Min:")
label_max = tk.Label(master=limits_frame, text="Max:")
label_min.grid(row=0, column=0, sticky="w", padx=2)
label_max.grid(row=0, column=1, sticky="w", padx=2)

# Input validation
def callback(input): 
    if input.isdigit(): 
        return True              
    elif input == "": 
        return True
    else: 
        return False
vcmd = (window.register(callback), "%P")

# Input configuration
entry_max = tk.Entry(master=limits_frame)
entry_min = tk.Entry(master=limits_frame)
entry_max.config(validate="key", validatecommand=vcmd)
entry_min.config(validate="key", validatecommand=vcmd)
entry_min.grid(row=1, column=0, sticky="ew", padx=5)
entry_max.grid(row=1, column=1, sticky="ew", padx=5)

# Output label
output_label = tk.Label(master=window)

# Button
def generate_random():
    min_value = entry_min.get()
    max_value = entry_max.get()

    if not min_value:
        messagebox.showerror("Error", "Please provide a minimum value!")
        return
    if not max_value:
        messagebox.showerror("Error", "Please provide a maximum value!")
        return
    if int(min_value) > int(max_value):
        messagebox.showerror("Error", "Minimum value cannot be larger than the maximum!")
        return
    
    playsound.playsound(os.path.join(working_dir, "dice_roll.mp3"))
    random = randint(int(min_value), int(max_value))
    output_label["text"] = f"The random value is: {random}"
    
button = tk.Button(
    master=window, 
    text="Generate",
    bg="green",
    fg="white",
    command=generate_random
)
button.pack(fill="both", padx=5)
output_label.pack(pady=5)



if __name__ == "__main__":
    window.mainloop()