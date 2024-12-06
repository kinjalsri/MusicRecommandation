import csv
import tkinter as tk
from tkinter import ttk, messagebox
import random

# Load Dataset
try:
    with open("musicdata.csv", "r") as file:
        reader = csv.DictReader(file)
        music_data = list(reader)
except FileNotFoundError:
    messagebox.showerror("Error", "Dataset not found! Ensure 'musicdata.csv' is in the same directory.")
    exit()

# Helper Functions
def filter_data(key, value):
    return [row for row in music_data if row[key].strip().lower() == value.strip().lower()]

# Functionality
def recommend_by_mood():
    mood = mood_var.get()
    results = filter_data("Mood", mood)
    if not results:
        messagebox.showinfo("Recommendation", f"No songs found for mood '{mood}'.")
    else:
        show_recommendations(results)

def recommend_by_genre():
    genre = genre_var.get()
    results = filter_data("Genre", genre)
    if not results:
        messagebox.showinfo("Recommendation", f"No songs found for genre '{genre}'.")
    else:
        show_recommendations(results)

def recommend_by_artist():
    artist = artist_var.get()
    results = filter_data("Artist", artist)
    if not results:
        messagebox.showinfo("Recommendation", f"No songs found for artist '{artist}'.")
    else:
        show_recommendations(results)

def calculate_compatibility():
    name = quiz_name_var.get()
    if not name:
        messagebox.showwarning("Error", "Please enter a name!")
        return
    quiz_answers = [quiz_var1.get(), quiz_var2.get(), quiz_var3.get()]
    preferred_songs = [
        row for row in music_data
        if row["Mood"].strip().lower() == quiz_answers[0].strip().lower()
        or row["Genre"].strip().lower() == quiz_answers[1].strip().lower()
        or row["Artist"].strip().lower() == quiz_answers[2].strip().lower()
    ]
    compatibility_score = random.randint(50, 100)  # Randomized for fun
    messagebox.showinfo(
        "Compatibility",
        f"Your compatibility score with {name} is {compatibility_score}%!\n\n"
        f"Recommended Songs:\n" +
        "\n".join([row["Song Title"] for row in preferred_songs[:5]])
    )

def show_recommendations(results):
    result_text = "\n".join([row["Song Title"] for row in results[:5]])
    messagebox.showinfo("Recommendation", f"Top Recommendations:\n{result_text}")

# GUI
root = tk.Tk()
root.title("Music Recommendation System")
root.geometry("500x600")

# Title
ttk.Label(root, text="Music Recommendation System", font=("Arial", 16)).pack(pady=10)

# Mood Recommendation
ttk.Label(root, text="Select Mood:").pack(pady=5)
mood_var = tk.StringVar()
ttk.Entry(root, textvariable=mood_var).pack(pady=5)
ttk.Button(root, text="Recommend by Mood", command=recommend_by_mood).pack(pady=10)

# Genre Recommendation
ttk.Label(root, text="Select Genre:").pack(pady=5)
genre_var = tk.StringVar()
ttk.Entry(root, textvariable=genre_var).pack(pady=5)
ttk.Button(root, text="Recommend by Genre", command=recommend_by_genre).pack(pady=10)

# Artist Recommendation
ttk.Label(root, text="Select Artist:").pack(pady=5)
artist_var = tk.StringVar()
ttk.Entry(root, textvariable=artist_var).pack(pady=5)
ttk.Button(root, text="Recommend by Artist", command=recommend_by_artist).pack(pady=10)

# Compatibility Quiz
ttk.Label(root, text="Compatibility Quiz", font=("Arial", 14)).pack(pady=10)
quiz_name_var = tk.StringVar()
ttk.Label(root, text="Your Name:").pack(pady=5)
ttk.Entry(root, textvariable=quiz_name_var).pack(pady=5)

quiz_var1 = tk.StringVar()
ttk.Label(root, text="Favorite Mood:").pack(pady=5)
ttk.Entry(root, textvariable=quiz_var1).pack(pady=5)

quiz_var2 = tk.StringVar()
ttk.Label(root, text="Favorite Genre:").pack(pady=5)
ttk.Entry(root, textvariable=quiz_var2).pack(pady=5)

quiz_var3 = tk.StringVar()
ttk.Label(root, text="Favorite Artist:").pack(pady=5)
ttk.Entry(root, textvariable=quiz_var3).pack(pady=5)

ttk.Button(root, text="Calculate Compatibility", command=calculate_compatibility).pack(pady=20)

# Run App
root.mainloop()

