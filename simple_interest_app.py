import streamlit as st
import time  # Import time module for sleep functionality

# Function to calculate Simple Interest
def calculate_simple_interest(principal, rate, years):
    # Formula: SI = (P * R * T) / 100
    return (principal * rate * years) / 100

# Title of the web app
st.title('Simple Interest Calculator')

# Input fields for principal, rate of interest, and time (renamed to years)
principal = st.number_input('Enter the principal amount ($)', min_value=0.0, value=1000.0, step=100.0)
rate = st.number_input('Enter the rate of interest (%)', min_value=0.0, value=5.0, step=0.1)
years = st.number_input('Enter the time period (in years)', min_value=0.0, value=1.0, step=0.1)

# Button to calculate and display the result
if st.button('Calculate Simple Interest'):
    with st.spinner('Calculating...'):
        time.sleep(2)  # Simulate a loading time for better UX
        simple_interest = calculate_simple_interest(principal, rate, years)
    
    # Display the result
    st.write(f'The simple interest is: ${simple_interest:.2f}')
