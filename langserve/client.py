import streamlit as st
import requests

# Set up the Streamlit app
st.title("Dynamic API Invoker")

# Input fields for 'stats' and 'topic'
stats = st.text_input("Enter the stats endpoint (e.g.,'history' 'stats'):", "stats")
topic = st.text_input("Enter the player name (e.g., 'KL Rahul'):")

# Button to trigger the API call
if st.button("Invoke API"):
    if stats and topic:
        try:
            # Construct the API endpoint dynamically
            endpoint = f"http://localhost:8000/{stats}/invoke"
            
            # API request
            response = requests.post(
                endpoint,
                json={'input': {'topic': topic}}
            )
            
            # Display the response
            if response.status_code == 200:
                output = response.json().get('output', {}).get('content', 'No content found')
                st.success("API Response:")
                st.write(output)
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please provide both 'stats' and 'topic'.")
