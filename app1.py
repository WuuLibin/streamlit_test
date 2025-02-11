#python3 -m venv myenv
#source myenv/bin/activate
#pip install -r requirements.txt
import streamlit as st
# Create a text input box
text_input = st.text_input("Enter some text:")
# Create a submit button
if st.button("Submit"):
    st.write("You've inputted:", text_input)