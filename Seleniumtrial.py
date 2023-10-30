import speech_recognition as sr
import pyttsx3
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def recognize_and_open_website():
    # Initialize the speech recognition object
    r = sr.Recognizer()

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        print("Please start speaking.")
        audio_text = r.listen(source)
        print("Recording finished. Recognizing...")

        try:
            # Convert speech to text
            recognized_text = r.recognize_google(audio_text)
            print("You: " + recognized_text)

            if "open browser" in recognized_text.lower():
                engine.say("Sure, please tell me the website you want to visit.")
                engine.runAndWait()

                # Listen for the website name
                audio_text = r.listen(source)
                print("Recording finished. Recognizing...")

                # Convert speech to text
                website_name = r.recognize_google(audio_text)
                print("Website: " + website_name)

                # Open the specified website using Selenium
                url = f"https://www.{website_name.lower()}"
                browser = webdriver.Firefox()
                browser.get(url)

                engine.say(f"Opened {website_name} successfully!")
                engine.runAndWait()

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Error occurred in connecting to the API. Check your internet connection. Error: ", e)
        except WebDriverException as e:
            print("Error occurred in opening the website or browser. Make sure the input is correct. Error: ", e)

if __name__ == "__main__":
    recognize_and_open_website()