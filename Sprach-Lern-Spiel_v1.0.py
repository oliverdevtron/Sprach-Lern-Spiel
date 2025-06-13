import tkinter as tk
from tkinter import messagebox
from random import choice
import pygame

# Initialize pygame mixer for sound effects
pygame.mixer.init()

# Wortlisten für verschiedene Sprachen
words_en_de = {
    "Apple": "Apfel",
    "Banana": "Banane",
    "Cat": "Katze",
    "Dog": "Hund",
    "Elephant": "Elefant",
    "Fish": "Fisch",
    "Grape": "Traube",
    "House": "Haus",
    "Ice cream": "Eis",
    "Juice": "Saft",
    "Kite": "Drachen",
    "Lion": "Löwe",
    "Monkey": "Affe",
    "Nest": "Nest",
    "Orange": "Orange",
    "Pencil": "Bleistift",
    "Queen": "Königin",
    "Rabbit": "Kaninchen",
    "Sun": "Sonne",
    "Tree": "Baum",
    "Umbrella": "Regenschirm",
    "Violin": "Geige",
    "Whale": "Wal",
    "Xylophone": "Xylophon",
    "Yacht": "Yacht",
    "Zebra": "Zebra"
}

words_es_de = {
    "Manzana": "Apfel",
    "Banana": "Banane",
    "Gato": "Katze",
    "Perro": "Hund",
    "Elefante": "Elefant",
    "Pez": "Fisch",
    "Uva": "Traube",
    "Casa": "Haus",
    "Helado": "Eis",
    "Jugo": "Saft",
    "Cometa": "Drachen",
    "León": "Löwe",
    "Mono": "Affe",
    "Nido": "Nest",
    "Naranja": "Orange",
    "Lápiz": "Bleistift",
    "Reina": "Königin",
    "Conejo": "Kaninchen",
    "Sol": "Sonne",
    "Árbol": "Baum",
    "Paraguas": "Regenschirm",
    "Violín": "Geige",
    "Ballena": "Wal",
    "Xilófono": "Xylophon",
    "Yate": "Yacht",
    "Cebra": "Zebra"
}

class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sprach-Lernsoftware")
        self.root.geometry("600x600")
        self.current_word = None
        self.score = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.language = None
        self.words = None
        self.rewards = []

        self.create_language_selection()

    def create_language_selection(self):
        self.language_label = tk.Label(self.root, text="Wähle die Sprache, die du lernen möchtest:", font=("Comic Sans MS", 18), fg="blue")
        self.language_label.pack(pady=20)

        self.english_button = tk.Button(self.root, text="Englisch", command=self.select_english, font=("Comic Sans MS", 18), bg="yellow")
        self.english_button.pack(pady=10)

        self.spanish_button = tk.Button(self.root, text="Spanisch", command=self.select_spanish, font=("Comic Sans MS", 18), bg="yellow")
        self.spanish_button.pack(pady=10)

    def select_english(self):
        self.language = "Englisch"
        self.words = words_en_de
        self.start_learning()

    def select_spanish(self):
        self.language = "Spanisch"
        self.words = words_es_de
        self.start_learning()

    def start_learning(self):
        self.language_label.pack_forget()
        self.english_button.pack_forget()
        self.spanish_button.pack_forget()

        self.create_widgets()
        self.next_word()

    def create_widgets(self):
        self.label = tk.Label(self.root, text=f"Lerne {self.language}!", font=("Comic Sans MS", 24), fg="green")
        self.label.pack(pady=20)

        self.word_label = tk.Label(self.root, text="", font=("Comic Sans MS", 18), fg="black")
        self.word_label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Comic Sans MS", 18))
        self.entry.pack(pady=10)

        self.check_button = tk.Button(self.root, text="Prüfen", command=self.check_answer, font=("Comic Sans MS", 18), bg="cyan")
        self.check_button.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Punktzahl: 0", font=("Comic Sans MS", 18), fg="blue")
        self.score_label.pack(pady=20)

        self.stats_label = tk.Label(self.root, text="Richtige Antworten: 0 | Falsche Antworten: 0", font=("Comic Sans MS", 18), fg="blue")
        self.stats_label.pack(pady=10)

        self.reward_label = tk.Label(self.root, text="Belohnungen: Keine", font=("Comic Sans MS", 18), fg="green")
        self.reward_label.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Nächstes Wort", command=self.next_word, font=("Comic Sans MS", 18), bg="yellow")
        self.next_button.pack(pady=10)

    def next_word(self):
        self.current_word = choice(list(self.words.keys()))
        self.word_label.config(text=self.current_word)
        self.entry.delete(0, tk.END)

    def play_sound(self, sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    def check_answer(self):
        answer = self.entry.get()
        if answer.lower() == self.words[self.current_word].lower():
            self.play_sound('correct_sound.mp3')
            self.score += 1
            self.correct_answers += 1
            messagebox.showinfo("Richtig!", "Das ist korrekt!")
            self.check_rewards()
        else:
            self.play_sound('wrong_sound.mp3')
            self.wrong_answers += 1
            messagebox.showinfo("Falsch", f"Das ist nicht korrekt. Die richtige Antwort ist: {self.words[self.current_word]}")
        self.update_score()
        self.next_word()

    def check_rewards(self):
        if self.correct_answers == 10:
            self.rewards.append("10 richtige Antworten!")
            messagebox.showinfo("Belohnung!", "Du hast 10 richtige Antworten erreicht!")
        elif self.correct_answers == 20:
            self.rewards.append("20 richtige Antworten!")
            messagebox.showinfo("Belohnung!", "Du hast 20 richtige Antworten erreicht!")
        self.reward_label.config(text=f"Belohnungen: {', '.join(self.rewards) if self.rewards else 'Keine'}")

    def update_score(self):
        self.score_label.config(text=f"Punktzahl: {self.score}")
        self.stats_label.config(text=f"Richtige Antworten: {self.correct_answers} | Falsche Antworten: {self.wrong_answers}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()
