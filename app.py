import streamlit as st
from transformers import pipeline
import traceback

st.set_page_config(page_title="AI Content Generator", layout="centered")

st.title("🧠 AI Content Generator")
st.write("Generate creative text using a Hugging Face model.")

# Cache the model so it doesn't reload on every interaction
@st.cache_resource
def load_model():
    try:
        pipe = pipeline("text-generation", model="gpt2")
        return pipe
    except Exception as e:
        st.error("🚨 Failed to load model:")
        st.code(traceback.format_exc())
        return None

pipe = load_model()

try:
    if pipe is not None:
        prompt = st.text_area("Enter your prompt", "Once upon a time")
        max_length = st.slider("Max length", min_value=10, max_value=200, value=50)

        if st.button("Generate"):
            with st.spinner("Generating..."):
                output = pipe(prompt, max_length=max_length, do_sample=True, top_k=50, top_p=0.95, num_return_sequences=1)
                st.success("Generated text:")
                st.text_area("Result", output[0]["generated_text"], height=200)
    else:
        st.warning("Model not loaded. Check the error above.")

except Exception as e:
    st.error("🚨 An error occurred while generating text:")
    st.code(traceback.format_exc())
