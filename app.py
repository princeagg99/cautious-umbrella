import streamlit as st

# Function to initialize session state
def initialize_session_state():
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = {'button1': False, 'button2': False}

# Main function to run the Streamlit app
def main():
    initialize_session_state()

    st.title("Nested Buttons with Session States")

    # Nested button 1
    if st.button("Outer Button 1"):
        st.session_state.button_clicked['button1'] = not st.session_state.button_clicked['button1']

    if st.session_state.button_clicked['button1']:
        st.write("Inner Button 1 is clicked!")

    # Nested button 2
    if st.button("Outer Button 2"):
        st.session_state.button_clicked['button2'] = not st.session_state.button_clicked['button2']

    if st.session_state.button_clicked['button2']:
        st.write("Inner Button 2 is clicked!")

# Run the app
if __name__ == "__main__":
    main()
