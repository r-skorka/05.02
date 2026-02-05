import tkinter as tk
from tkinter import messagebox

class VolunteerForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Formularz Wolontariusza")
        self.data = {}

        # Sekcja Osoby A
        tk.Label(root, text="--- Dane podstawowe ---").pack()
        self.add_field("Imię", "name")
        self.add_field("Nazwisko", "surname")

        # --- MIEJSCE NA KOD OSOBY B ---
        # dfrgbrtebgtrbghtrbgtrbhrh

        # --- MIEJSCE NA KOD OSOBY C ---
        # Tutaj Osoba C doda swoje pola np. Rozmiar koszulki

        tk.Button(root, text="Zapisz", command=self.save).pack(pady=10)

    def add_field(self, label_text, key):
        tk.Label(self.root, text=label_text).pack()
        entry = tk.Entry(self.root)
        entry.pack()
        self.data[key] = entry

    def save(self):
        output = {k: v.get() for k, v in self.data.items()}
        print("Dane wolontariusza:", output)
        messagebox.showinfo("Sukces", "Dane zostały zapisane w konsoli!")

if __name__ == "__main__":
    root = tk.Tk()
    app = VolunteerForm(root)
    root.mainloop()