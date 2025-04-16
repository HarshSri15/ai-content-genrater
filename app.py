import streamlit as st
from transformers import pipeline

# Load the model
generator = pipeline("text2text-generation", model="google/flan-t5-large")

def generate_content(topic, platform):
    prompt = f"Generate an engaging piece of content about '{topic}' for the platform '{platform}'."
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']

# Streamlit App
st.title("AI Content Generator")

topic = st.text_input("Enter the topic:")
platform = st.selectbox("Choose the platform:", ["Twitter", "Instagram", "LinkedIn", "Blog"])

if st.button("Generate"):
    if topic and platform:
        with st.spinner("Generating..."):
            result = generate_content(topic, platform)
            st.success("Here is your content:")
            st.write(result)
    else:
        st.warning("Please enter a topic and select a platform.")
