import streamlit as st

st.write("""
# Checking if the number is odd or even
""")

#Get Input
st.header('User Input Parameters')

def user_input_features():
    num1 = st.number_input("Number 1",step=1)
    if num1 % 2 == 0:
        return f'{num1} is Even'
    else:
        return f'{num1} id Odd'

result = user_input_features()

st.subheader('Result')
st.write(result)
