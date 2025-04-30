from tkinter import Tk, Label, Button, Entry, StringVar, END
import math
import random

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("🎨 Stylish Calculator")

        self.expression = ""
        self.input_text = StringVar()

        master.configure(bg="#2b2d42")

        # Styled Entry widget
        self.entry = Entry(master, textvariable=self.input_text, font=("Arial", 20), 
                           justify='right', bd=10, bg="#edf2f4", fg="#2b2d42")
        self.entry.grid(row=0, column=0, columnspan=6, ipadx=8, ipady=15, padx=8, pady=8)

        # Emojis to mimic button icons
        icon_map = {
            '+': '➕', '-': '➖', '*': '✖️', '/': '➗',
            'sqrt': '🧮', 'cbrt': '📦', '^': '🔼', 'root': '🌀',
            'sin': '📐', 'cos': '🌗', 'tan': '📏',
            '=': '✅', 'C': '❌'
        }

        # Styled buttons
        buttons = [
            '7', '8', '9', '/', 'sqrt', 'cbrt',
            '4', '5', '6', '*', '^', 'root',
            '1', '2', '3', '-', 'sin', 'cos',
            '0', '.', '=', '+', 'tan', 'C'
        ]

        row_val = 1
        col_val = 0

        for btn in buttons:
            icon = icon_map.get(btn, '')
            display_text = f"{icon} {btn}" if icon else btn

            # Assign background colors by category
            if btn.isdigit() or btn == '.':
                bg_color = "#8d99ae"
            elif btn in ['+', '-', '*', '/', '^', '=', 'C']:
                bg_color = "#ef233c"
            else:
                bg_color = "#d90429"

            action = lambda x=btn: self.on_button_click(x)
            Button(master, text=display_text, width=6, height=2, font=("Arial", 13), 
                   command=action, bg=bg_color, fg="white", activebackground="#ffb703")\
                .grid(row=row_val, column=col_val, sticky="nsew", padx=2, pady=2)

            col_val += 1
            if col_val > 5:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        try:
            if char == 'C':
                self.expression = ""
            elif char == '=':
                expr = self.expression.replace('^', '**')
                self.expression = str(eval(expr))
            elif char == 'sqrt':
                self.expression = str(math.sqrt(eval(self.expression)))
            elif char == 'cbrt':
                self.expression = str(eval(self.expression) ** (1/3))
            elif char == 'root':
                base, n = self.expression.split(',')
                self.expression = str(float(base) ** (1/float(n)))
            elif char == 'sin':
                self.expression = str(math.sin(math.radians(eval(self.expression))))
            elif char == 'cos':
                self.expression = str(math.cos(math.radians(eval(self.expression))))
            elif char == 'tan':
                self.expression = str(math.tan(math.radians(eval(self.expression))))
            else:
                self.expression += str(char)
        except:
            self.expression = "Error"

        self.input_text.set(self.expression)


# Launch the app
root = Tk()
calc = Calculator(root)
root.mainloop()