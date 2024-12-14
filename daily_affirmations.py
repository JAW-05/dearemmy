import streamlit as st
import random

affirmations = {
    "Happy": [
        "You radiate positivity and light wherever you go.",
        "Your happiness is contagious and inspires others.",
        "You deserve all the joy that life has to offer."
    ],
    "Sad": [
        "It's okay to feel sad; your feelings are valid.",
        "You are stronger than you think, and this too shall pass.",
        "Even on your hardest days, you are loved beyond measure."
    ],
    "Anxious": [
        "Take a deep breath; you are capable of handling this moment.",
        "You are resilient and have overcome so much already.",
        "Everything you need is within you to face today."
    ],
    "Loved": [
        "You are deeply loved and cherished every single day.",
        "Your presence brings warmth and happiness to those around you.",
        "You are the center of someone's universe, and you matter so much."
    ],
    "Motivated": [
        "You have the power to achieve anything you set your mind to.",
        "Your determination and focus are truly inspiring.",
        "Every step you take is a step closer to your goals."
    ]
}

songs = {
    "Happy": ["antihoney - 'Lush'", "Lana Del Rey - 'Young and Beautiful'", "Sophie Woodhouse - 'Tides'"],
    "Sad": ["antihoney - 'Crumble'", "Lana Del Rey - 'Summertime Sadness'", "Sophie Woodhouse - 'Lost'"],
    "Anxious": ["antihoney - 'Chill'", "Lana Del Rey - 'Born to Die'", "Sophie Woodhouse - 'Echoes'"],
    "Loved": ["antihoney - 'Sunset'", "Lana Del Rey - 'Love'", "Sophie Woodhouse - 'Forever'"],
    "Motivated": ["antihoney - 'Drive'", "Lana Del Rey - 'Ride'", "Sophie Woodhouse - 'Brave'"]
}

choices = ["Rock", "Paper", "Scissors"]

def rock_paper_scissors():
    st.subheader("Rock, Paper, Scissors Game")
    st.write("Choose Rock, Paper, or Scissors!")

    user_choice = st.selectbox("Your choice:", choices)
    computer_choice = random.choice(choices)

    if st.button("Play"):
        st.write(f"You chose: {user_choice}")
        st.write(f"The computer chose: {computer_choice}")

        if user_choice == computer_choice:
            st.write("It's a draw!")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            st.write("You win! 😁")
        else:
            st.write("You lose! ☹️")

def sticky_notes():
    st.subheader("Sticky Notes")

    if 'notes' not in st.session_state:
        st.session_state.notes = []

    new_note = st.text_input("Write something down maybe a love note or something 😉:")
    if st.button("Add Note"):
        if new_note.strip():
            st.session_state.notes.append(new_note)
            st.success("Added!")
        else:
            st.warning("Cannot add an empty note.")

    if st.session_state.notes:
        st.write("### Whats the tea? 🍵 :")
        for i, note in enumerate(st.session_state.notes):
            st.write(f"{i + 1}. {note}")

        if st.button("Clear All Notes"):
            st.session_state.notes = []
            st.success("All notes cleared!")

def affirmation_generator():
    feeling = st.selectbox("How are you feeling today?", list(affirmations.keys()))

    if st.button("Affirmations from Jerrybear"):
        affirmation = random.choice(affirmations[feeling])
        st.markdown(f'<div class="stSuccess">{affirmation}</div>', unsafe_allow_html=True)

        recommended_song = random.choice(songs[feeling])
        st.write(f"Song recommendation: {recommended_song} 🎶")

def main():
    st.set_page_config(page_title="Dear Emmy", page_icon="❤️", layout="centered")

    st.markdown(
        """
        <style>
        body {
            background-color: #ffe6f2;
            color: #800040;
            font-family: 'Georgia', cursive;
        }
        .stButton>button {
            background-color: #ffccdd;
            color: #800040;
            border-radius: 15px;
            border: 2px solid #ff99bb;
            font-size: 16px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #ff99bb;
            color: white;
        }
        .stSelectbox label {
            font-weight: bold;
            color: #800040;
        }
        .stSuccess {
            background-color: #ff99bb;
            color: white;
            border-left: 6px solid #ff66a3;
            padding: 15px;
            font-size: 16px;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            font-size: 14px;
            color: #800040;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image("banner.png",  use_container_width=True)


    st.write("Happy 2 years to us baby!! I just wanted to do something for you so I decided to do this using the things I have learnt in school 🤓 I hope you like it!")

    choice = st.selectbox("What would you like to do?", ["Affirmations from Jerrybear", "Manage Sticky Notes", "Play Rock, Paper, Scissors"])

    if choice == "Affirmations from Jerrybear":
        affirmation_generator()
    elif choice == "Manage Sticky Notes":
        sticky_notes()
    else:
        rock_paper_scissors()

    st.markdown(
        """
        <div class="footer">
            2 YEARS <3 WE ARE FOREVER 18/12/22
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
