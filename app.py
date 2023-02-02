import streamlit as st

# Store messages in memory
messages = []

st.title("Streamlit Chat App")

# Create a chat interface
username = st.text_input("Enter your username:")
message = st.text_input("Enter message:")

# Send message
if st.button("Send"):
    messages.append((username, message))
    st.write("Sent!")

# Display messages
for msg in messages:
    st.write("[{}]: {}".format(msg[0], msg[1]))
    st.write(msg)

    
