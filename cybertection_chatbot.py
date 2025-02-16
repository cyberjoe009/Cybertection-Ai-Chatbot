import tkinter as tk
from tkinter import ttk, scrolledtext
import random

class CybertectionAI:
    def __init__(self, master):
        self.master = master
        master.title("Cybertection AI")  # Set the title

        self.responses = {
            "hello": ["Hi there!", "Hello to you too!", "Greetings!"],
            "how are you": ["I'm doing well, thank you.", "I'm fine, how about you?", "Great!"],
            "bye": ["Goodbye!", "See you later!", "Farewell!"],
        }

        # --- Chat Display ---
        self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, height=15)
        self.chat_area.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.chat_area.config(state=tk.DISABLED)  # Initially disabled

        # --- Input Area ---
        self.message_label = ttk.Label(master, text="Your Message:")
        self.message_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.message_entry = ttk.Entry(master)
        self.message_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.send_button = ttk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=1, padx=5, pady=5)


    def send_message(self):
        message = self.message_entry.get().lower()
        self.display_message("You: " + message)
        self.message_entry.delete(0, tk.END)

        response = self.get_response(message)
        self.display_message("Cybertection AI: " + response)

    def get_response(self, message):
        for keyword, options in self.responses.items():
            if keyword in message:
                return random.choice(options)
        return "I'm still learning. Ask me something else."

    def display_message(self, message):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)  # Scroll to the bottom



root = tk.Tk()
chat_assistant = CybertectionAI(root)  # Correct class name
root.mainloop()
