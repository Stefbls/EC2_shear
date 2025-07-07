import streamlit as st
import numpy as np



def main():
    
    st.header("Verifica di Snellezza di un Pilastro in CLS")
    st.header("Inserisci i dati di input")
    
    b = st.number_input("Larghezza trave (b) [cm]", min_value=0.0, step=0.1, value=30.0)
    h = st.number_input("Altezza trave (h) [cm]", min_value=0.0, step=0.1, value=30.0)
    A = b * h
    st.latex(r"A = b \times h ")
    st.latex(f"A = {b:.1f} \\, \\text{{cm}} \\, \\times \\, {h:.1f} \\, \\text{{cm}} = {A:.1f} \\, \\text{{cm}}^2")


if __name__ == "__main__":
    main()
