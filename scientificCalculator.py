import tkinter as tk
import json
import math  # imported to handle scientific calculations


def btn_clear():
    global expression
    expression = ""
    input_text.set("")


def btn_equal():
    global expression
    try:
        # Evaluate the expression and handle scientific functions
        result = str(eval(expression))
        input_text.set(result)
    except ZeroDivisionError:
        input_text.set("Error: Division by Zero")
    except Exception as e:
        input_text.set(f"Error: {str(e)}")
    expression = ""


def save_state():
    global expression
    if expression == "":
        input_text.set("Error: No expression to save")
        return
    state = {"expression": expression}
    with open("calculator_state.json", "w") as f:
        json.dump(state, f)


def load_state():
    global expression
    try:
        with open("calculator_state.json", "r") as f:
            state = json.load(f)
            expression = state["expression"]
            input_text.set(expression)
    except FileNotFoundError:
        expression = ""
        input_text.set("")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def btn_delete():
    global expression
    expression = expression[:-1]
    input_text.set(expression)


def btn_end():
    root.quit()
    root.destroy()


def scientific_click(func):
    global expression
    try:
        if func == 'sqrt':
            result = str(math.sqrt(float(expression)))
        elif func == 'log':
            result = str(math.log10(float(expression)))
        elif func == 'ln':
            result = str(math.log(float(expression)))
        elif func == 'sin':
            result = str(math.sin(math.radians(float(expression))))
        elif func == 'cos':
            result = str(math.cos(math.radians(float(expression))))
        elif func == 'tan':
            result = str(math.tan(math.radians(float(expression))))
        input_text.set(result)
        expression = result
    except ValueError:
        input_text.set("Error")
        expression = ""


# Creates the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x400")

expression = ""
input_text = tk.StringVar()

input_frame = tk.Frame(root, width=400, height=50, bd=0,
                       highlightbackground="black",
                       highlightcolor="black",
                       highlightthickness=5)
input_frame.pack(side="top")

input_field = tk.Entry(input_frame, font=("Helvetica", 18), textvariable=input_text, width=50, bg="light grey", bd=0, justify="right")
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = tk.Frame(root, width=10, height=20, bg="pink")
btns_frame.pack()

clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=1, bg="light pink", cursor="hand2", command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3)
divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3)
sqrt = tk.Button(btns_frame, text="√", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: scientific_click('sqrt')).grid(row=0, column=4)

seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=1, bg="pink", cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0)
eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=1, bg="pink", cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1)
nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=1, bg="pink", cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2)
multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3)
log = tk.Button(btns_frame, text="log", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: scientific_click('log')).grid(row=1, column=4)

four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=1, bg="pink", cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0)
five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=1, bg="pink", cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1)
six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=1, bg="pink", cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2)
minus = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3)
ln = tk.Button(btns_frame, text="ln", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: scientific_click('ln')).grid(row=2, column=4)

one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=1, bg="pink", cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0)
two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=1, bg="pink", cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1)
three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=1, bg="pink", cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2)
plus = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3)
sin = tk.Button(btns_frame, text="sin", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: scientific_click('sin')).grid(row=3, column=4)

zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=1, bg="pink", cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2)
point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2)
equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: btn_equal()).grid(row=4, column=3)
tan = tk.Button(btns_frame, text="tan", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: scientific_click('tan')).grid(row=4, column=4)

delete = tk.Button(btns_frame, text="DEL", fg="black", width=21, height=3, bd=1, bg="pink", cursor="hand2", command=lambda: btn_delete()).grid(row=5, column=0, columnspan=2)
save = tk.Button(btns_frame, text="Save", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: save_state()).grid(row=5, column=2)
load = tk.Button(btns_frame, text="Load", fg="black", width=10, height=3, bd=1, bg="light grey", cursor="hand2", command=lambda: load_state()).grid(row=5, column=3)
end = tk.Button(btns_frame, text="End", fg="black", width=10, height=3, bd=2, bg="light grey", cursor="hand2", command=lambda: btn_end()).grid(row=5, column=4)

root.mainloop()
