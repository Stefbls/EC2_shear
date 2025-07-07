import streamlit as st
import numpy as np



def main():
    
    st.header("Verifica taglio trave")
    st.header("Inserisci i dati di input")
    
    b = st.number_input("Larghezza trave (b) [cm]", min_value=0.0, step=0.1, value=30.0)
    h = st.number_input("Altezza trave (h) [cm]", min_value=0.0, step=0.1, value=30.0)
    A = b * h

    col1, col2 = st.columns(2)
            
    with col1:
        st.markdown("**Formula simbolica**")
        st.latex(r"A = b \times h ")

    with col2:
        st.markdown("**Formula numerica**")
        st.latex(f"A = {b:.1f} \\, \\text{{cm}} \\, \\times \\, {h:.1f} \\, \\text{{cm}} = {A:.1f} \\, \\text{{cm}}^2")

if __name__ == "__main__":
    main()
