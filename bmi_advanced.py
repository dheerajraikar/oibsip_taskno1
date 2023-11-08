import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    result_label.config(text=f'BMI: {bmi:.2f}')

app = tk.Tk()
app.title("BMI Calculator")

weight_label = tk.Label(app, text="Weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(app)
weight_entry.pack()
height_label = tk.Label(app, text="Height (m):")
height_label.pack()

height_entry = tk.Entry(app)
height_entry.pack()

calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()

