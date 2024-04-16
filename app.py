import openai
import streamlit as st

# Read OpenAI API key from file
with open("keys/.openai_api_key.txt", "r") as f:
    key = f.read().strip()

# Create OpenAI client
openai.api_key = key

st.snow()
st.title("GenAI Code Reviewer")

# Take user input
prompt = st.text_area("Input a python Code...")

# Generate response when button is clicked
if st.button("Check"):
    response = openai.Completion.create(
        engine="davinci-codex",  # Use the Codex engine for code-related tasks
        prompt=prompt,
        max_tokens=150  # Adjust max tokens as needed
    )

    # Display response
    st.write(response.choices[0].text)
