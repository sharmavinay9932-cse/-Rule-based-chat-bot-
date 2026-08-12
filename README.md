@@ -0,0 +1,155 @@
# 🤖 Rule-Based Chatbot

A simple **Rule-Based Chatbot** built with Python that interacts with users using predefined rules and responses.

The chatbot identifies specific keywords or phrases in the user's input and provides an appropriate predefined response. It does not use machine learning or AI models.

## 📌 Features

* 💬 Interactive conversation with the user
* 🔍 Keyword-based input matching
* 🤝 Predefined responses for common questions
* 👋 Greeting and farewell handling
* ❓ Default response for unknown questions
* 🐍 Built using Python
* ⚡ Simple and beginner-friendly implementation

## 🛠️ Technologies Used

* **Python**
* Python conditional statements (`if`, `elif`, `else`)
* String manipulation
* Loops
* Functions

## 📂 Project Structure

```text
Rule-Based-Chatbot/
│
├── chatbot.py
└── README.md
```

## ⚙️ How It Works

The chatbot follows a simple rule-based approach:

```text
User Input
    ↓
Convert input to lowercase
    ↓
Check for keywords / phrases
    ↓
Match a predefined rule
    ↓
Return predefined response
    ↓
Continue conversation
```

For example:

```text
User: hello

Chatbot: Hello! How can I help you?
```

Another example:

```text
User: what is your name?

Chatbot: I am a rule-based chatbot.
```

If the chatbot does not recognize the input:

```text
User: Tell me about quantum computing

Chatbot: Sorry, I don't understand that question.
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project folder

```bash
cd Rule-Based-Chatbot
```

### 3. Run the chatbot

```bash
python chatbot.py
```

## 💻 Example Conversation

```text
=================================
       RULE-BASED CHATBOT
=================================

You: hello
Bot: Hello! How can I help you?

You: what is your name?
Bot: I am a rule-based chatbot.

You: how are you?
Bot: I'm doing great! Thanks for asking.

You: bye
Bot: Goodbye! Have a great day!
```

## 🎯 Purpose of the Project

This project was created to understand the fundamentals of **Python programming and chatbot logic**.

It demonstrates how simple conversational systems can be created using predefined rules without using machine learning or large language models.

## 📚 Concepts Learned

Through this project, I practiced:

* Python functions
* Conditional statements
* Loops
* String methods
* User input handling
* Basic program structure
* Rule-based decision making
* Error/default handling

## 🔮 Future Improvements

Some possible improvements are:

* Add more conversation rules
* Add a graphical user interface
* Store conversation history
* Add more natural language processing
* Use NLP libraries such as NLTK or spaCy
* Add machine learning capabilities
* Connect the chatbot to an API or database

## 👨‍💻 Author

**Vinay Sharma**

B.Tech CSE — AI & ML

---

⭐ If you found this project useful, consider giving the repository a star!
