import streamlit as st

st.set_page_config(page_title="Google Unit Converter", layout="centered")
st.title("🔄 Google-style Unit Converter")

# Category dropdown
category = st.selectbox("Select conversion type", ["Length", "Mass", "Temperature"])

# Conversion dictionaries
length_units = {
    "Metre": 1.0,
    "Kilometre": 1000.0,
    "Centimetre": 0.01,
    "Millimetre": 0.001,
    "Mile": 1609.34,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254,
}

mass_units = {
    "Kilogram": 1.0,
    "Gram": 0.001,
    "Milligram": 0.000001,
    "Pound": 0.453592,
    "Ounce": 0.0283495,
}

temp_units = ["Celsius", "Fahrenheit", "Kelvin"]

# User input and layout
col1, col2 = st.columns(2)
with col1:
    input_value = st.number_input(
        " ", value=1.0, format="%.4f", label_visibility="collapsed", key="input_number"
    )
with col2:
    result_display = st.empty()

# Unit selection
col3, col4 = st.columns(2)
with col3:
    from_unit = st.selectbox(
        " ", 
        length_units.keys() if category == "Length" else
        mass_units.keys() if category == "Mass" else temp_units,
        key="from_unit_select"
    )
with col4:
    to_unit = st.selectbox(
        " ", 
        length_units.keys() if category == "Length" else
        mass_units.keys() if category == "Mass" else temp_units,
        key="to_unit_select"
    )

# Conversion logic
def convert_length(val, from_u, to_u):
    result = val * length_units[from_u] / length_units[to_u]
    formula = f"multiply the length value by {length_units[from_u] / length_units[to_u]:.4f}"
    return result, formula

def convert_mass(val, from_u, to_u):
    result = val * mass_units[from_u] / mass_units[to_u]
    formula = f"multiply the mass value by {mass_units[from_u] / mass_units[to_u]:.4f}"
    return result, formula

def convert_temperature(val, from_u, to_u):
    if from_u == to_u:
        return val, "no conversion needed"
    if from_u == "Celsius":
        if to_u == "Fahrenheit":
            return val * 9 / 5 + 32, "C × 9/5 + 32"
        elif to_u == "Kelvin":
            return val + 273.15, "C + 273.15"
    elif from_u == "Fahrenheit":
        if to_u == "Celsius":
            return (val - 32) * 5 / 9, "(F - 32) × 5/9"
        elif to_u == "Kelvin":
            return (val - 32) * 5 / 9 + 273.15, "(F - 32) × 5/9 + 273.15"
    elif from_u == "Kelvin":
        if to_u == "Celsius":
            return val - 273.15, "K - 273.15"
        elif to_u == "Fahrenheit":
            return (val - 273.15) * 9 / 5 + 32, "(K - 273.15) × 9/5 + 32"
    return val, "unsupported conversion"

# Perform conversion
if category == "Length":
    result, formula = convert_length(input_value, from_unit, to_unit)
elif category == "Mass":
    result, formula = convert_mass(input_value, from_unit, to_unit)
else:
    result, formula = convert_temperature(input_value, from_unit, to_unit)

# Show output
with col2:
    result_display.number_input(
        " ", 
        value=result, 
        format="%.4f", 
        label_visibility="collapsed", 
        disabled=True,
        key="output_number"
    )

# Show formula
st.markdown(
    f"<span style='color:#eab308; font-weight:bold;'>Formula</span> &nbsp;&nbsp; {formula}",
    unsafe_allow_html=True
)
