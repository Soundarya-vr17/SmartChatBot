import customtkinter as ctk

# ---------------- Window ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Smart AI Chatbot")
app.geometry("700x550")

# ---------------- Chat Area ---------------- #

chat_box = ctk.CTkTextbox(app, width=650, height=420)
chat_box.pack(pady=20)

chat_box.insert("end", "🤖 Smart AI Chatbot\n")
chat_box.insert("end", "Hello! Ask me anything.\n\n")

# ---------------- Responses ---------------- #

responses = {
    "hi":"Hello! 👋",
    "hello":"Hi there!",
    "how are you":"I'm doing great!",
    "what is python":"Python is a programming language.",
    "what is ai":"AI stands for Artificial Intelligence.",
    "who created you":"I was created using Python.",
    "bye":"Goodbye! 👋", 
    "what is python": "Python is a programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "who created you": "I was created using Python.",
    "what is sql": "SQL is used to manage databases.",
    "what is power bi": "Power BI is a data visualization tool.",
    "tell me a joke": "Why do programmers hate nature? It has too many bugs! 😂",
    "who is ms dhoni": "MS Dhoni is a former Indian cricket captain.",
    "what is machine learning": "Machine Learning allows computers to learn from data.",
    
    
}

# ---------------- Function ---------------- #

def send():

    
        user = entry.get()
        if user == "":
              return
        chat_box.insert("end", f"You : {user}\n")
        reply = responses.get(user.lower(),
                          "Sorry, I don't know that yet.")
        chat_box.insert("end", f"Bot : {reply}\n\n")
        with open("chat_history.txt", "a") as file:
              file.write(f"You : {user}\n")
        file.write(f"Bot : {reply}\n\n")
        entry.delete(0, "end")

# ---------------- Input ---------------- #

entry = ctk.CTkEntry(app, width=500)
entry.pack(side="left", padx=20, pady=10)

button = ctk.CTkButton(app,
                       text="Send",
                       command=send)

button.pack(side="right", padx=20)

app.mainloop()