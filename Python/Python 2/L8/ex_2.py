
import tkinter as tk



def increase_counter():
    current_value = int(label_counter['text'])

    label_counter.config(text=str(current_value +1))


def decrease_counter():
    current_value = int(label_counter['text'])

    label_counter.config(text=str(current_value - 1))



window = tk.Tk()

window.title("Räkna")

window.geometry("800x600")


label_counter = tk.Label(window, text="0", font=("arial", 24))
label_counter.pack(pady=20)

button_increase = tk.Button(window, text="+", command=increase_counter, font=("arial", 14))
button_increase.pack(side=tk.LEFT, padx=60 )

button_decrease = tk.Button(window, text="-", command=decrease_counter, font=("arial", 14))
button_decrease.pack(side=tk.RIGHT, padx=60)









window.mainloop()

