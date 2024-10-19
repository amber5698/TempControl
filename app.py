import streamlit as st

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

# Streamlit app layout
st.title("Temperature Converter")

# Celsius to Fahrenheit conversion
st.header("Celsius to Fahrenheit")
celsius_temp = st.number_input("Enter temperature in Celsius:", value=0.0, key="celsius_input")
if st.button("Convert Celsius to Fahrenheit", key="c_to_f_button"):
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    st.write(f"{celsius_temp}°C is {fahrenheit_temp:.2f}°F")

# Fahrenheit to Celsius conversion
st.header("Fahrenheit to Celsius")
fahrenheit_temp_input = st.number_input("Enter temperature in Fahrenheit:", value=32.0, key="fahrenheit_input")
if st.button("Convert Fahrenheit to Celsius", key="f_to_c_button"):
    celsius_temp_output = fahrenheit_to_celsius(fahrenheit_temp_input)
    st.write(f"{fahrenheit_temp_input}°F is {celsius_temp_output:.2f}°C")
