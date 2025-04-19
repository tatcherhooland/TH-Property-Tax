import tkinter as tk
from tkinter import messagebox


def calculate_tax():
    try:
        actual_value = float(entry_actual_value.get())
        assessment_value = actual_value * 0.6
        property_tax = (assessment_value / 100) * 0.75

        label_assessment_value.config(text=f"Assessment Value: ${assessment_value:,.2f}")
        label_property_tax.config(text=f"Property Tax: ${property_tax:,.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric value.")


# Create main window
root = tk.Tk()
root.title("Property Tax Calculator")
root.geometry("350x200")

# Create widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=10)

tk.Label(frame, text="Enter Actual Property Value: ").grid(row=0, column=0, padx=5, pady=5)
entry_actual_value = tk.Entry(frame)
entry_actual_value.grid(row=0, column=1, padx=5, pady=5)

btn_calculate = tk.Button(frame, text="Calculate", command=calculate_tax)
btn_calculate.grid(row=1, column=0, columnspan=2, pady=10)

label_assessment_value = tk.Label(frame, text="Assessment Value: $0.00")
label_assessment_value.grid(row=2, column=0, columnspan=2)

label_property_tax = tk.Label(frame, text="Property Tax: $0.00")
label_property_tax.grid(row=3, column=0, columnspan=2)

# Run the application
root.mainloop()