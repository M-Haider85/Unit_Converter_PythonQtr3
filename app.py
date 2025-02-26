import streamlit as st
from pint import UnitRegistry
import pyperclip

# Initialize unit registry
ureg = UnitRegistry()

# Define unit categories
unit_categories = {
    "Length": ["meters", "kilometers", "miles", "inches", "feet", "yards"],
    "Weight": ["grams", "kilograms", "pounds", "ounces"],
    "Volume": ["liters", "milliliters", "gallons"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
}

# Streamlit UI
st.title("🌍 Unit Converter")
st.markdown("Convert between different units easily. 🚀")

# Select category
category = st.selectbox("Select Category", list(unit_categories.keys()))

# Select units based on category
from_unit = st.selectbox("From Unit", unit_categories[category])
to_unit = st.selectbox("To Unit", unit_categories[category])

# User input
quantity = st.number_input("Enter value:", min_value=0.0, format="%.6f")

# Conversion logic
if st.button("Convert"):
    try:
        if category == "Temperature":
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (quantity * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (quantity - 32) * 5/9
            elif from_unit == "celsius" and to_unit == "kelvin":
                result = quantity + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                result = quantity - 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                result = (quantity - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                result = (quantity - 273.15) * 9/5 + 32
            else:
                result = quantity  # Same unit, no conversion
        else:
            result = (quantity * ureg(from_unit)).to(to_unit)

        # Display result
        st.success(f"Result: {result}")
        
        # Copy button
        if st.button("Copy to Clipboard"):
            pyperclip.copy(str(result))
            st.success("Copied to clipboard! ✅")

    except Exception as e:
        st.error(f"Conversion error: {e}")
