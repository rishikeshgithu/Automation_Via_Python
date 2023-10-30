#!/usr/bin/env python
# coding: utf-8

# In[5]:


import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    
    try:
        
        print("Text: "+r.recognize_google(audio_text))
    except:
         print("Sorry, I did not get that")


# In[6]:


import pyttsx3
 
engine = pyttsx3.init()
 
engine.say('hello how are you I am fine what about you what you think what am I')
 
engine.runAndWait()


# In[10]:


import speech_recognition as sr
import pyttsx3

def recognize_and_speak():
    r = sr.Recognizer()
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        print("Please start speaking.")
        try:
            audio_text = r.listen(source, timeout=5)
            print("Recording finished. Recognizing...")
            recognized_text = r.recognize_google(audio_text)
            print("Recognized Text: " + recognized_text)

            print("Computer: " + recognized_text)
            engine.say(recognized_text)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, could not understand what you said.")
        except sr.RequestError as e:
            print("Error occurred in connecting to the API. Check your internet connection. Error: ", e)
        except pyttsx3.exceptions.EngineError as e:
            print("Text-to-speech error: ", e)

if __name__ == "__main__":
    recognize_and_speak()


# In[1]:


import speech_recognition as sr
import pyttsx3
import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def recognize_and_speak():
    r = sr.Recognizer()
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        print("Please start speaking.")
        try:
            audio_text = r.listen(source, timeout=5)  # Set a timeout for recording (5 seconds in this example)
            print("Recording finished. Recognizing...")
            recognized_text = r.recognize_google(audio_text)
            print("You: " + recognized_text)

            # Get a response from ChatGPT
            response_text = chat_with_gpt(recognized_text)
            print("ChatGPT: " + response_text)

            # Use text-to-speech to speak back the answer
            print("Computer: " + response_text)
            engine.say(response_text)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, could not understand what you said.")
        except sr.RequestError as e:
            print("Error occurred in connecting to the API. Check your internet connection. Error: ", e)
        except pyttsx3.engine.EngineError as e:
            print("Text-to-speech error: ", e)
        except openai.error.AuthenticationError as e:
            print("OpenAI API authentication error: ", e)
        except openai.error.APIError as e:
            print("OpenAI API error: ", e)

if __name__ == "__main__":
    recognize_and_speak()


# In[13]:


import requests

api_key = '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'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

url = 'https://api.openai.com/v1/chat/completions'  # Use v1/chat/completions for chat models

data = {
    'model': 'gpt-3.5-turbo',  # Replace with a compatible chat model ID, e.g., 'gpt-3.5-turbo'
    'messages': [
        {
            'role': 'system',
            'content': 'You are a helpful assistant.'
        },
        {
            'role': 'user',
            'content': 'hi how are you are you fine'
        }
    ],
    'temperature': 0.8,
    'max_tokens': 100
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    # Extract the assistant's response from the result
    assistant_response = result['choices'][0]['message']['content']
    print("Assistant: ", assistant_response)
else:
    print("Error:", response.status_code, response.text)


# In[1]:


import requests
import speech_recognition as sr
import pyttsx3

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = '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'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

url = 'https://api.openai.com/v1/chat/completions'

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def recognize_and_chat():
    # Initialize the speech recognition object
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please start speaking.")
        audio_text = r.listen(source)
        print("Recording finished. Recognizing...")

        try:
            # Convert speech to text
            recognized_text = r.recognize_google(audio_text)
            print("You: " + recognized_text)

            # Use chat with GPT-3.5 Turbo
            response = chat_with_gpt(recognized_text)

            # Speak out the assistant's response
            engine.say(response)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Error occurred in connecting to the API. Check your internet connection. Error: ", e)

def chat_with_gpt(prompt):
    data = {
        'model': 'gpt-3.5-turbo',  # Replace with a compatible chat model ID, e.g., 'gpt-3.5-turbo'
        'messages': [
            {
                'role': 'system',
                'content': 'You are a helpful assistant.'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        'temperature': 0.8,
        'max_tokens': 100
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        # Extract the assistant's response from the result
        assistant_response = result['choices'][0]['message']['content']
        return assistant_response
    else:
        print("Error:", response.status_code, response.text)
        return "Sorry, I encountered an error while processing your request."

if __name__ == "__main__":
    recognize_and_chat()


# In[6]:


import requests
import speech_recognition as sr
import pyttsx3

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = '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'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

url = 'https://api.openai.com/v1/chat/completions'

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize a variable to store the assistant's response
assistant_response_text = ""

def recognize_and_chat():
    global assistant_response_text  # Declare the variable as global so we can modify it inside the function

    # Initialize the speech recognition object
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please start speaking.")
        audio_text = r.listen(source)
        print("Recording finished. Recognizing...")

        try:
            # Convert speech to text
            recognized_text = r.recognize_google(audio_text)
            print("You: " + recognized_text)

            # Use chat with GPT-3.5 Turbo
            response = chat_with_gpt(recognized_text)

            # Save the assistant's response to the global variable
            assistant_response_text = response

            # Speak out the assistant's response
            engine.say(response)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Error occurred in connecting to the API. Check your internet connection. Error: ", e)

def chat_with_gpt(prompt):
    data = {
        'model': 'gpt-3.5-turbo',  # Replace with a compatible chat model ID, e.g., 'gpt-3.5-turbo'
        'messages': [
            {
                'role': 'system',
                'content': 'You are a helpful assistant.'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        'temperature': 0.8,
        'max_tokens': 100
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        # Extract the assistant's response from the result
        assistant_response = result['choices'][0]['message']['content']
        return assistant_response
    else:
        print("Error:", response.status_code, response.text)
        return "Sorry, I encountered an error while processing your request."

if __name__ == "__main__":
    recognize_and_chat()

    # Print the assistant's response text
    print("Assistant Text Output: ", assistant_response_text)


# In[ ]:


import requests
import speech_recognition as sr
import pyttsx3

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = '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'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

url = 'https://api.openai.com/v1/chat/completions'

engine = pyttsx3.init()

engine.setProperty("runAndWaitTimeout", 10)

assistant_response_text = "Yay speak da fool"

def recognize_and_chat():
    global assistant_response_text

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please start speaking.")
        audio_text = r.listen(source)
        print("Recording finished. Recognizing...")

        try:

            recognized_text = r.recognize_google(audio_text)
            print("You: " + recognized_text)

            response = chat_with_gpt(recognized_text)

            assistant_response_text = response

            engine.say(response)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Error occurred in connecting to the API. Check your internet connection. Error: ", e)

def chat_with_gpt(prompt):
    data = {
        'model': 'gpt-3.5-turbo',  # Replace with a compatible chat model ID, e.g., 'gpt-3.5-turbo'
        'messages': [
            {
                'role': 'system',
                'content': 'You are a helpful assistant.'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        'temperature': 0.8,
        'max_tokens': 100
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()

        assistant_response = result['choices'][0]['message']['content']
        return assistant_response
    else:
        print("Error:", response.status_code, response.text)
        return "Sorry, I encountered an error while processing your request."

if __name__ == "__main__":
    recognize_and_chat()

    print("Assistant Text Output: ", assistant_response_text)


# In[2]:


import requests
import speech_recognition as sr
import pyttsx3

api_key = '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'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

url = 'https://api.openai.com/v1/chat/completions'

engine = pyttsx3.init()
engine.setProperty("rate", 125)
engine.setProperty("runAndWaitTimeout", 10)

def recognize_and_chat():
    global assistant_response_text

    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Please start speaking.")
            audio_text = r.listen(source)
            print("Recording finished. Recognizing...")

            try:
                recognized_text = r.recognize_google(audio_text)
                print("You: " + recognized_text)

                if "stop" in recognized_text.lower():
                    print("Assistant: Stopping the conversation.")
                    engine.say("Stopping the conversation.")
                    engine.runAndWait()
                    break  # Exit the loop and stop the conversation

                response = chat_with_gpt(recognized_text)

                assistant_response_text = response

                engine.say(response)
                engine.runAndWait()

            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print("Error occurred in connecting to the API. Check your internet connection. Error: ", e)

def chat_with_gpt(prompt):
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'system',
                'content': 'You are a helpful assistant.'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        'temperature': 1.4,
        'max_tokens': 50
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()

        assistant_response = result['choices'][0]['message']['content']
        return assistant_response
    else:
        print("Error:", response.status_code, response.text)
        return "Sorry, I encountered an error while processing your request."

if __name__ == "__main__":
    recognize_and_chat()


# In[3]:


import requests
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import Text, Scrollbar

# Initialize the API key
api_key = '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'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

url = 'https://api.openai.com/v1/chat/completions'

engine = pyttsx3.init()
engine.setProperty("rate", 125)
engine.setProperty("runAndWaitTimeout", 10)

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant Chat")
        self.create_gui()

    def create_gui(self):
        self.textbox = Text(self.root, wrap=tk.WORD)
        self.textbox.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = Scrollbar(self.textbox)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.textbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textbox.yview)

        self.api_key_label = tk.Label(self.root, text="API Key:")
        self.api_key_label.pack()

        self.api_key_entry = tk.Entry(self.root)
        self.api_key_entry.pack()

        self.save_api_key_button = tk.Button(self.root, text="Save API Key", command=self.save_api_key)
        self.save_api_key_button.pack()

        self.listen_button = tk.Button(self.root, text="Start Listening", command=self.start_listening)
        self.listen_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack()

    def start_listening(self):
        self.textbox.insert(tk.END, "Please start speaking.\n")
        self.textbox.see(tk.END)

        r = sr.Recognizer()

        with sr.Microphone() as source:
            audio_text = r.listen(source)

        try:
            recognized_text = r.recognize_google(audio_text)
            self.textbox.insert(tk.END, f"You: {recognized_text}\n")
            self.textbox.see(tk.END)

            if "stop" in recognized_text.lower():
                self.textbox.insert(tk.END, "Assistant: Stopping the conversation.\n")
                self.textbox.see(tk.END)
                engine.say("Stopping the conversation.")
                engine.runAndWait()
                return

            response = self.chat_with_gpt(recognized_text)
            self.textbox.insert(tk.END, f"Assistant: {response}\n")
            self.textbox.see(tk.END)

            engine.say(response)
            engine.runAndWait()

        except sr.UnknownValueError:
            self.textbox.insert(tk.END, "Speech Recognition could not understand audio.\n")
            self.textbox.see(tk.END)
        except sr.RequestError as e:
            self.textbox.insert(tk.END, f"Error occurred in connecting to the API. Check your internet connection. Error: {e}\n")
            self.textbox.see(tk.END)

    def save_api_key(self):
        new_api_key = self.api_key_entry.get()
        if new_api_key:
            global api_key
            api_key = new_api_key
            self.textbox.insert(tk.END, "API Key updated.\n")
            self.textbox.see(tk.END)
        else:
            self.textbox.insert(tk.END, "Please enter a valid API Key.\n")
            self.textbox.see(tk.END)

    def chat_with_gpt(self, prompt):
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {
                    'role': 'system',
                    'content': 'You are a helpful assistant.'
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            'temperature': 1.4,
            'max_tokens': 50
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            assistant_response = result['choices'][0]['message']['content']
            return assistant_response
        else:
            return "Sorry, I encountered an error while processing your request."

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()


# In[ ]:




