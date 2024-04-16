import openai
import streamlit as st

f = open(".openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.snow()
st.title("GenAI Code Reviewer")

## Take the user input
prompt = st.text_area("Input a python Code...")

## if the button is clicked generate the responses
if st.button("Check") == True:
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": """figure out all the bugs and error. 
                                            and Display the correct code.
                                          """},
            {"role": "user", "content": prompt}
        ]
    )
    ## print the response on the web page
    st.write(response.choices[0].message.content)
