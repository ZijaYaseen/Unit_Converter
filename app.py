import streamlit as st

# Page configuration
st.set_page_config(page_title="Unit Converter 🚀", layout="centered")
st.title("Advanced Unit Converter 🚀")
st.markdown("Convert units effortlessly with advanced options and fun emojis! 😎")

# Sidebar: Category Selection
conversion_category = st.sidebar.selectbox(
    "Select Conversion Category:",
    ["Length 📏", "Mass ⚖️", "Temperature 🌡️", "Volume 🥤", "Speed 🚀"]
)

# Length Conversion
if conversion_category.startswith("Length"):
    st.header("Length Conversion 📏")
    units = ["Meter", "Kilometer", "Mile", "Foot"]
    from_unit = st.selectbox("From Unit", units, key="length_from")
    to_unit = st.selectbox("To Unit", units, key="length_to")
    value = st.number_input("Enter value:", value=1.0)
    
    conversion_factors = {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Mile": 1609.34,
        "Foot": 0.3048,
    }
    
    # Convert input value to meters then to target unit
    value_in_meters = value * conversion_factors[from_unit]
    result = value_in_meters / conversion_factors[to_unit]
    st.success(f"Result: {result:.3f} {to_unit}")

# Mass Conversion
elif conversion_category.startswith("Mass"):
    st.header("Mass Conversion ⚖️")
    units = ["Kilogram", "Gram", "Pound", "Ounce"]
    from_unit = st.selectbox("From Unit", units, key="mass_from")
    to_unit = st.selectbox("To Unit", units, key="mass_to")
    value = st.number_input("Enter value:", value=1.0)
    
    conversion_factors = {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
    }
    
    # Convert input value to kilograms then to target unit
    value_in_kg = value * conversion_factors[from_unit]
    result = value_in_kg / conversion_factors[to_unit]
    st.success(f"Result: {result:.3f} {to_unit}")

# Temperature Conversion
elif conversion_category.startswith("Temperature"):
    st.header("Temperature Conversion 🌡️")
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit", units, key="temp_from")
    to_unit = st.selectbox("To Unit", units, key="temp_to")
    value = st.number_input("Enter temperature value:", value=0.0)
    
    def convert_temperature(val, f_unit, t_unit):
        if f_unit == t_unit:
            return val
        # Convert to Celsius first
        if f_unit == "Fahrenheit":
            val = (val - 32) * 5 / 9
        elif f_unit == "Kelvin":
            val = val - 273.15
        # Convert from Celsius to target unit
        if t_unit == "Fahrenheit":
            return val * 9 / 5 + 32
        elif t_unit == "Kelvin":
            return val + 273.15
        else:
            return val

    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"Result: {result:.2f} {to_unit}")

# Volume Conversion
elif conversion_category.startswith("Volume"):
    st.header("Volume Conversion 🥤")
    units = ["Liter", "Milliliter", "Gallon"]
    from_unit = st.selectbox("From Unit", units, key="vol_from")
    to_unit = st.selectbox("To Unit", units, key="vol_to")
    value = st.number_input("Enter value:", value=1.0)
    
    conversion_factors = {
        "Liter": 1.0,
        "Milliliter": 0.001,
        "Gallon": 3.78541,
    }
    
    # Convert input value to liter then to target unit
    value_in_liter = value * conversion_factors[from_unit]
    result = value_in_liter / conversion_factors[to_unit]
    st.success(f"Result: {result:.4f} {to_unit}")

# Speed Conversion
elif conversion_category.startswith("Speed"):
    st.header("Speed Conversion 🚀")
    units = ["m/s", "km/h", "mph"]
    from_unit = st.selectbox("From Unit", units, key="speed_from")
    to_unit = st.selectbox("To Unit", units, key="speed_to")
    value = st.number_input("Enter speed value:", value=1.0)
    
    conversion_factors = {
        "m/s": 1.0,
        "km/h": 3.6,
        "mph": 2.23694,
    }
    
    # Convert input value to m/s then to target unit
    value_in_ms = value / conversion_factors[from_unit]
    result = value_in_ms * conversion_factors[to_unit]
    st.success(f"Result: {result:.4f} {to_unit}")

else:
    st.error("Please select a conversion category.")
