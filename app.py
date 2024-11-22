import streamlit as st
import math as mt  # Consistent with the alias

st.set_page_config(layout="wide", page_title="Transformer")

def Tran_Eff(vsc, isc, wsc):
    zsc = vsc / isc
    r1 = wsc / (isc ** 2)
    x1 = mt.sqrt((zsc ** 2) - (r1 ** 2))  # Corrected: Use zsc instead of z1
    return r1, x1

st.title("2205A21020-PS8")
st.write("Calculates the winding resistance (r1) and reactance (x1) of a transformer based on short circuit test measurements like vsc, isc, wsc.")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):  # First container for the left column
        vsc = st.number_input("Enter the short circuit voltage (vsc)", value=5.0, step=1.0)
        isc = st.number_input("Enter the short circuit current (isc)", value=3.0, step=1.0)
        wsc = st.number_input("Enter the short circuit power (wsc)", value=1.0, step=1.0)

with col2:
    with st.container(border=True):  # Second container for the right column
        r1, x1 = Tran_Eff(vsc, isc, wsc)
        st.write("Transformer function Results:")
        st.write(f"Resistance (r1) = {r1:.4f} Ohms")
        st.write(f"Reactance (x1) = {x1:.4f} Ohms")
