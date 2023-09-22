import tkinter as tk
from tkinter import ttk


def create_gui():
    root = tk.Tk()
    root.title("Currency Checker")

    num_converters = tk.IntVar(value=1)
    base_currencies = []
    target_currencies = []
    max_values = []
    min_values = []

    def add_converter_fields():
        num = num_converters.get()
        for _ in range(num):
            base_currency = tk.StringVar()
            target_currency = tk.StringVar()
            max_value = tk.DoubleVar()
            min_value = tk.DoubleVar()

            base_currencies.append(base_currency)
            target_currencies.append(target_currency)
            max_values.append(max_value)
            min_values.append(min_value)

            frame = ttk.Frame(root, padding=5)
            frame.grid(column=0, sticky=(tk.W, tk.E))

            ttk.Label(frame, text="Base Currency: ").grid(row=0, column=0, sticky=tk.W)
            ttk.Entry(frame, textvariable=base_currency).grid(row=0, column=1)

            ttk.Label(frame, text="Target Currency: ").grid(row=0, column=2, sticky=tk.W)
            ttk.Entry(frame, textvariable=target_currency).grid(row=0, column=3)

            ttk.Label(frame, text="Maximum: ").grid(row=0, column=4, sticky=tk.W)
            ttk.Entry(frame, textvariable=max_value).grid(row=0, column=5)

            ttk.Label(frame, text="Minimum: ").grid(row=0, column=6, sticky=tk.W)
            ttk.Entry(frame, textvariable=min_value).grid(row=0, column=7)

    ttk.Label(root, text="Number of Converters: ").grid(row=0, column=0, sticky=tk.W)
    ttk.Entry(root, textvariable=num_converters).grid(row=0, column=1)
    ttk.Button(root, text="Add", command=add_converter_fields).grid(row=0, column=2)

    ttk.Label(root, text="Enter Conversion Details:").grid(row=1, column=0, columnspan=3)

    final_values = []

    def return_values():
        final_values.append([var.get() for var in base_currencies])
        final_values.append([var.get() for var in target_currencies])
        final_values.append([var.get() for var in max_values])
        final_values.append([var.get() for var in min_values])
        root.quit()
        root.destroy()

    submit_button = ttk.Button(root, text="Submit", command=return_values)
    submit_button.grid(row=2, column=0, columnspan=3)

    root.mainloop()

    return final_values
