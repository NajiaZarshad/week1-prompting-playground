import streamlit as st
import google.generativeai as genai

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-flash-latest")  # Replace with the desired model name

st.set_page_config(page_title="Prompting Basics Playground", page_icon="🔮💻🔮")
st.title("🔮💻🔮 Prompting Basics Playground")
st.write("Type a prompt below and click Submit to see how the LLM responds.")

user_prompt = st.text_area("Enter your prompt here:", height=150)

if st.button("Submit"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt before submitting.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(user_prompt)
                st.subheader("LLM Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
