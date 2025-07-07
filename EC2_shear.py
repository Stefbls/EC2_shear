import streamlit as st
import numpy as np



def main():
    
    st.header("Verifica di Snellezza di un Pilastro in CLS")
    st.header("Inserisci i dati di input")
    
    b = st.number_input("Larghezza trave (b) [cm]", min_value=0.0, step=0.01, value=2.0)
    h = st.number_input("Altezza trave (h) [cm]", min_value=0.0, step=0.01, value=2.0)
    A = b * h
    st.latex(r" A = {b:.3f} ")
    st.latex(f" A = {b:.3f} × {h:.3f})  = {A:.3f}")
    
    

if __name__ == "__main__":
    main()
