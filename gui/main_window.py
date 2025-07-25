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

    tkinter.Label(root, text="Pregunta del día:", font=("Helvetica", 16)).pack(pady=10)