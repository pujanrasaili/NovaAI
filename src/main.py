import customtkinter as ctk
from datetime import datetime
import pyttsx3
import webbrowser
import os
import customtkinter as ctk
from datetime import datetime
import pyttsx3
import webbrowser
import os
import speech_recognition as sr

# ---------------- VOICE ENGINE ----------------
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------------- SETTINGS ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- WINDOW ----------------
app = ctk.CTk()
app.title("NovaAI Assistant")
app.geometry("1200x700")

# ---------------- AI LOGIC ----------------
def ai_reply(message):

    msg = message.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello Pujan 👋"

    elif "how are you" in msg:
        return "I'm functioning perfectly 🚀"

    elif "time" in msg:
        current = datetime.now().strftime("%I:%M %p")
        return f"Current time is {current}"

    elif "open youtube" in msg:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open google" in msg:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open github" in msg:
        webbrowser.open("https://github.com")
        return "Opening GitHub"

    elif "open vscode" in msg:
        os.system("code")
        return "Opening VS Code"

    elif "your name" in msg:
        return "I am NovaAI, your desktop assistant."

    elif "bye" in msg:
        return "Goodbye Pujan 👋"

    else:
        return f"You said: {message}"

# ---------------- SIDEBAR ----------------
sidebar = ctk.CTkFrame(app, width=240, corner_radius=0)
sidebar.pack(side="left", fill="y")

logo = ctk.CTkLabel(
    sidebar,
    text="NovaAI",
    font=("Arial", 34, "bold")
)
logo.pack(pady=40)

status = ctk.CTkLabel(
    sidebar,
    text="● ONLINE",
    text_color="lightgreen",
    font=("Arial", 16, "bold")
)
status.pack(pady=5)
new_chat_btn = ctk.CTkButton(
    sidebar,
    text="New Chat",
    height=45,
    corner_radius=12
)
new_chat_btn.pack(padx=20, pady=20)

settings_btn = ctk.CTkButton(
    sidebar,
    text="Settings",
    height=45,
    corner_radius=12
)
settings_btn.pack(padx=20, pady=10)

# ---------------- MAIN AREA ----------------
main_frame = ctk.CTkFrame(app)
main_frame.pack(side="right", fill="both", expand=True)

chat_box = ctk.CTkTextbox(
    main_frame,
    font=("Consolas", 16),
    corner_radius=15
)
chat_box.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)

chat_box.insert(
    "end",
    "🤖 NovaAI: Hello Pujan 👋\n"
)
chat_box.insert(
    "end",
    "🤖 NovaAI: Voice assistant activated.\n\n"
)

# ---------------- INPUT AREA ----------------
input_frame = ctk.CTkFrame(main_frame)
input_frame.pack(fill="x", padx=20, pady=20)

user_input = ctk.CTkEntry(
    input_frame,
    placeholder_text="Ask NovaAI anything...",
    height=50,
    corner_radius=12,
    font=("Arial", 15)
)
user_input.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 10)
)

def send_message():

    message = user_input.get()

    if message.strip():

        chat_box.insert(
            "end",
            f"🧑 You: {message}\n"
        )

        response = ai_reply(message)

        chat_box.insert(
            "end",
            f"🤖 NovaAI: {response}\n\n"
        )

        speak(response)

        chat_box.see("end")

    user_input.delete(0, "end")

send_button = ctk.CTkButton(
    input_frame,
    text="Send",
    width=130,
    height=50,
    corner_radius=12,
    command=send_message
)
send_button.pack(side="right")

app.bind("<Return>", lambda event: send_message())

# ---------------- RUN APP ----------------
app.mainloop()

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        chat_box.insert("end", "🎤 Listening...\n")
        chat_box.see("end")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        chat_box.insert(
            "end",
            f"🧑 You (Voice): {command}\n"
        )

        response = ai_reply(command)

        chat_box.insert(
            "end",
            f"🤖 NovaAI: {response}\n\n"
        )

        speak(response)

    except:

        chat_box.insert(
            "end",
            "🤖 NovaAI: Sorry, I could not understand.\n\n"
        )