from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Bot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("Bot:", response)