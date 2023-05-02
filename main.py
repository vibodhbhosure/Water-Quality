import streamlit as st
from joblib import load
import warnings
warnings.filterwarnings("ignore")
model = load("random_forest_model.joblib")
st.set_page_config(page_title="Water Quality Monitoring System")
st.title("Water Quality Monitoring System")
valid_string = True
try:
    ph_text = st.number_input("Enter ph value 👇", max_value=14.00, min_value=0.00)
    if ph_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    ph = float(ph_text)
except: st.error("Please enter a valid integer.")
try:
    hardness_text = st.number_input("Enter Hardness value 👇", min_value=0.00)
    if hardness_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    hardness = float(hardness_text)
except: st.error("Please enter a valid integer.")
try:
    solids_text = st.number_input("Enter Solids value 👇",min_value=0.00)
    if solids_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    solids = float(solids_text)
except: st.error("Please enter a valid integer.")
try:
    chloramines_text = st.number_input("Enter Chloramines value 👇", min_value=0.00)
    if chloramines_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    chloramines = float(hardness_text)
except: st.error("Please enter a valid integer.")
try:
    sulfate_text = st.number_input("Enter Sulfates value 👇", min_value=0.00)
    if sulfate_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    sulfate = float(sulfate_text)
except: st.error("Please enter a valid integer.")
try:
    conductivity_text = st.number_input("Enter Conductivity value 👇", min_value=0.00)
    if conductivity_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    conductivity = float(conductivity_text)
except: st.error("Please enter a valid integer.")
try:
    organic_carbon_text = st.number_input("Enter Organic Carbon value 👇", min_value=0.00)
    if organic_carbon_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    organic_carbon = float(organic_carbon_text)
except: st.error("Please enter a valid integer.")
try:
    trihalomethanes_text = st.number_input("Enter Trihalomethanes value 👇", min_value=0.00)
    if trihalomethanes_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    trihalomethanes = float(trihalomethanes_text)
except: st.error("Please enter a valid integer.")
try:
    turbidity_text = st.number_input("Enter Turbidity value 👇", min_value=0.00)
    if turbidity_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    turbidity = float(turbidity_text)
except: st.error("Please enter a valid integer.")

submit_button = st.button('Predict Potability')

if submit_button and valid_string:
    try:
        pred = model.predict([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
        if int(pred) == 0:
            st.write("The water is consumable.")
        else:
            st.write("The water is not consumable.")
    except NameError: st.error("Incomplete Data provided!")
else:
    st.write("Please enter valid values!")

