# importing the libraries
import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

# Define the list of available languages
languages = [
    "English",
    "Hindi",
    "French",
    "Albanian",
    "Vietnamese",
    "Spanish",
    "Russian",
    "Portuguese",
    "Japanese",
    "Italian",
    "Indonesian",
    "German",
    "Filipino",
    "Dutch",
    "Chinese",
    "Arabic",
    "Turkish",
    "Tamil",
    "Swedish",
    "Sanskrit",
    "Romanian",
    "Polish",
    "Korean",
    ]

def translate_text(text, source_language, target_language):
    # Create a conversation with the chat model
    conversation = [
        {"role": "system", "content": f"You are a helpful assistant, your only job is to translate from {source_language} to {target_language}. Translate simple, do not make it complex."},
        {"role": "user", "content": f"Translate this text for me: {text}", "language": target_language}, 
    ]

    # Use the chat model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Get the assistant's reply
    translation = response.choices[0].message.content

    return translation

# Streamlit web app
def main():
    st.title("Translate My Text")

    # Input text
    text = st.text_area("Enter the text to translate")

    # Source language dropdown to select the languages
    source_language = st.selectbox("Select source language", sorted(languages))

    # Target language dropdown to select the languages
    target_language = st.selectbox("Select target language", sorted(languages))

    # Translate button to translate
    if st.button("Translate"):
        translation = translate_text(text, source_language, target_language)
        st.markdown(f'<p style="color: white; font-size: 25px;"> \
                    Result: {translation} </p>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()