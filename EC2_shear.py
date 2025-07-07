import streamlit as st
import numpy as np
import math



def main():
    
    st.header("Verifica taglio trave")
    st.header("Inserisci i dati di input")
    
    b = st.number_input("Larghezza trave (b) [cm]", min_value=0.0, step=0.1, value=30.0)
    h = st.number_input("Altezza trave (h) [cm]", min_value=0.0, step=0.1, value=40.0)
    A = b * h
    col1, col2 = st.columns(2)       
    with col1:
        st.markdown("**Formula simbolica**")
        st.latex(r"A = b \times h ")
    with col2:
        st.markdown("**Formula numerica**")
        st.latex(f"A = {b:.1f} \\, \\text{{cm}} \\, \\times \\, {h:.1f} \\, \\text{{cm}} = {A:.1f} \\, \\text{{cm}}^2")
    
    c = st.number_input("Copriferro (c) [cm]", min_value=0.0, step=0.1, value=3.0)
    n_barre = st.number_input("Numero di barre tese (n_barre) [-]", min_value=1, step=1, value=3.0)
    HA = st.number_input("Diametro barre (HA) [mm]", min_value=0.0, step=0.1, value=3.0)
    A_s = n_barre * (math.pi * HA**2) / (4 * 100)
    st.latex(r"A_s = n_{barre} \cdot \frac{\pi \cdot \phi^2}{4 \cdot 100}")
    st.latex(f"A_s = {n_barre} \\cdot \\frac{{\\pi \\cdot {HA:.0f}^2}}{{4 \\cdot 100}}")




if __name__ == "__main__":
    main()
