import streamlit as st

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

# Button 1
button1 = st.button("Button 1")
if button1:
    
    st.session_state.button_clicked = True
    st.write("abcdef")

# Button 2
button2 = st.button("Button 2")
if button2:
    st.session_state.button_clicked = True

# Display the current state
st.write(f"Button Clicked: {st.session_state.button_clicked}")
