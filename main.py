import tkinter as tk
from tkinter import filedialog, messagebox
import time

# Sample text for typing test
sample_text = "The quick brown fox jumps over the lazy dog."

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        self.sample_label = tk.Label(root, text=sample_text, font=('Arial', 14))
        self.sample_label.pack(pady=20)

        self.input_text = tk.Text(root, height=5, font=('Arial', 14))
        self.input_text.pack(pady=20)
        self.input_text.bind("<KeyRelease>", self.check_text)

        self.start_button = tk.Button(root, text="Start", command=self.start_test)
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=('Arial', 14))
        self.result_label.pack(pady=20)

        self.start_time = 0
        self.end_time = 0

    def start_test(self):
        self.input_text.delete('1.0', tk.END)
        self.result_label.config(text="")
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)

    def check_text(self, event):
        current_time = time.time()
        typed_text = self.input_text.get('1.0', tk.END).strip()

        if typed_text == sample_text:
            self.end_time = current_time
            self.calculate_results()
            self.start_button.config(state=tk.NORMAL)

    def calculate_results(self):
        total_time = self.end_time - self.start_time
        word_count = len(sample_text.split())

        wpm = (word_count / total_time) * 60
        accuracy = self.calculate_accuracy(sample_text, self.input_text.get('1.0', tk.END).strip())

        self.result_label.config(text=f"WPM: {wpm:.2f}, Accuracy: {accuracy:.2f}%")

    def calculate_accuracy(self, sample, typed):
        sample_words = sample.split()
        typed_words = typed.split()

        correct_words = 0
        for sample_word, typed_word in zip(sample_words, typed_words):
            if sample_word == typed_word:
                correct_words += 1

        accuracy = (correct_words / len(sample_words)) * 100
        return accuracy

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
