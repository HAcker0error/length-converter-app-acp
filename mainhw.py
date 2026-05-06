import tkinter as tk
from tkinter import messagebox

def convert_inches_to_cm():
    try:
        inches = float(entry_inches.get())
        centimeters = inches * 2.54
        label_result.config(text=f"{inches} inches = {centimeters:.2f} cm", fg="#1e7e34")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numerical value.")

root = tk.Tk()
root.title("Inches to Cm Converter")
root.geometry("350x200")
root.resizable(False, False)
root.configure(bg="#f8f9fa")

label_title = tk.Label(root, text="Inches to Centimeters", font=("Arial", 14, "bold"), bg="#f8f9fa", fg="#343a40")
label_title.pack(pady=10)

input_frame = tk.Frame(root, bg="#f8f9fa")
input_frame.pack(pady=5)

label_instruction = tk.Label(input_frame, text="Enter Inches:", font=("Arial", 10), bg="#f8f9fa")
label_instruction.pack(side=tk.LEFT, padx=5)

entry_inches = tk.Entry(input_frame, font=("Arial", 10), width=10)
entry_inches.pack(side=tk.LEFT, padx=5)
entry_inches.focus()

btn_convert = tk.Button(root, text="Convert", command=convert_inches_to_cm, font=("Arial", 10, "bold"), bg="#007bff", fg="white", padx=10, pady=2)
btn_convert.pack(pady=15)

label_result = tk.Label(root, text="", font=("Arial", 11, "bold"), bg="#f8f9fa")
label_result.pack(pady=5)

root.mainloop()