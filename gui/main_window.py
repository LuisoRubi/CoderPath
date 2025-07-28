import tkinter as tkinter
from tkinter import messagebox
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '...', 'easy.json')

def load_question():
    with open(DATA_PATH, 'r') as f:
        questions = json.load(f)
    return questions[0]

def evaluate_answer(user_inpt, correct_answer):
    return user_input.strip().lower() == correct_answer.strip().lower()

def launch_app():
    root = tkinter.Tk()
    root.title("CoderPath: La senda del brujo programador")
    
    question = load_question()
    
    # Widgets

    tk.Label(root, text="Pregunta del día:", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(root, text=question["question"], wraplength=100, font=("Helvetica", 12)).pack(pady=5)

    answer_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=answer_var, font=('Helvetica', 12), width=40)
    entry.pack(pady=5)
    
    def on_submit():
        user_answer = answer_var.get()
        if evaluate_answer(user_answer, question["answer"]):
            messagebox.showinfo("Resultado", "✅ ¡Correcto! Bien hecho.")
        else:
            messagebox.showerror("Resultado", f"❌ Incorrecto. La respuesta correcta era: {question['answer']}")

    tk.Button(root, text="Verificar", command=on_submit, font=('Helvetica', 12)).pack(pady=10)

    root.mainloop()