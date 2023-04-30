import streamlit as st
from joblib import load
import warnings
warnings.filterwarnings("ignore")
model = load("random_forest_model.joblib")
st.set_page_config(page_title="Water Quality Monitoring System")
st.title("Water Quality Monitoring System")
valid_string = True
try:
    ph_text = st.text_input("Enter ph value 👇", placeholder='ph')
    if ph_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    ph = float(ph_text)
except: st.error("Please enter a valid integer.")
try:
    hardness_text = st.text_input("Enter Hardness value 👇", placeholder='Hardness')
    if hardness_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    hardness = float(hardness_text)
except: st.error("Please enter a valid integer.")
try:
    solids_text = st.text_input("Enter Solids value 👇", placeholder='Solids')
    if solids_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    solids = float(solids_text)
except: st.error("Please enter a valid integer.")
try:
    chloramines_text = st.text_input("Enter Chloramines value 👇", placeholder='Chloramines')
    if chloramines_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    chloramines = float(hardness_text)
except: st.error("Please enter a valid integer.")
try:
    sulfate_text = st.text_input("Enter Sulfates value 👇", placeholder='Chloramines')
    if sulfate_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    sulfate = float(sulfate_text)
except: st.error("Please enter a valid integer.")
try:
    conductivity_text = st.text_input("Enter Conductivity value 👇", placeholder='Chloramines')
    if conductivity_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    conductivity = float(conductivity_text)
except: st.error("Please enter a valid integer.")
try:
    organic_carbon_text = st.text_input("Enter Organic Carbon value 👇", placeholder='Organic Carbon')
    if organic_carbon_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    organic_carbon = float(organic_carbon_text)
except: st.error("Please enter a valid integer.")
try:
    trihalomethanes_text = st.text_input("Enter Trihalomethanes value 👇", placeholder="Trihalomethanes")
    if trihalomethanes_text is None:
        st.error("Please enter a valid integer.")
        valid_string = False
    trihalomethanes = float(trihalomethanes_text)
except: st.error("Please enter a valid integer.")
try:
    turbidity_text = st.text_input("Enter Turbidity value 👇", placeholder="Turbidity")
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

