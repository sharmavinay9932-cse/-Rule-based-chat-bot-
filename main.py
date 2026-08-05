import datetime
import time

name = input("enter your name ::")
presenttime = datetime.datetime.now().hour

if 5 <= presenttime <= 11:
    print("good morning ", name)
elif 11 <= presenttime <= 17:
    print(f"good afternoon {name}")
elif 17 <= presenttime <= 20:
    print(f"good evening {name}")
else:
    print("good night")

print("🙏 Namaste! Welcome to my Study Buddy Bot.")
print("You can ask me basic questions. Type 'bye' to exit.")










responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi! Nice to meet you.",
    "hey": "Hey! What's up?",
    "how are you": "I'm doing great. What about you?",
    "what is python": "Python is a popular programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "thank you": "You're welcome!",
    "thanks": "My pleasure.",
}

def getresponse(userquestion):
    userquestion = userquestion.lower()

    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]

    return responses["default"]

while True:
    userinput = input("You: ").lower()

    if userinput == "bye":
        print("Bot: Goodbye! 👋")
        break

    print("Bot:", getresponse(userinput))