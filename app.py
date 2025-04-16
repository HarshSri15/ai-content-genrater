import streamlit as st
from transformers import pipeline

# Load model and tokenizer
generator = pipeline("text2text-generation", model="google/flan-t5-large")

def generate_content(topic, platform):
    prompt = f"Write a {platform} post about {topic}"
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']

# Streamlit app interface
st.title("AI Content Generator")
topic = st.text_input("Enter a topic:")
platform = st.selectbox("Select a platform:", ["Twitter", "LinkedIn", "Instagram"])

if st.button("Generate"):
    if topic and platform:
        with st.spinner("Generating content..."):
            result = generate_content(topic, platform)
            st.success("Here's your AI-generated content:")
            st.write(result)
    else:
        st.warning("Please enter a topic and select a platform.")