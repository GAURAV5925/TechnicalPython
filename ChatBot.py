# Importing necessary modules
import random

# Defining a dictionary of responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thanks for asking!", "Not bad, how are you?"],
    "goodbye": ["Goodbye!", "See you later!"],
    "default": ["I'm sorry, I didn't understand what you said."]
}

# Defining a function that generates a response based on the user's input
def respond(message):
    if message.lower() in responses:
        return random.choice(responses[message.lower()])
    else:
        return random.choice(responses["default"])

# Setting up a loop to continuously prompt the user for input
while True:
    user_input = input("You: ")
    bot_response = respond(user_input)
    print("Bot:", bot_response)
