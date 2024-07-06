import streamlit as st
from home_page import render_home_page
from sugarcane_calculator import render_sugarcane_calculator
from equipment_rental import render_equipment_rental
from farming_info import render_farming_info
import sqlite3

# Function to create SQLite connection
def create_connection():
    conn = sqlite3.connect('farmers_ecommerce.db')
    return conn

def main():
    st.title("Farmers E-Commerce Website")

    # Create SQLite connection
    conn = create_connection()

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Home", "Sugarcane Calculator", "Equipment Rental", "Farming Info"])

    if page == "Home":
        render_home_page(conn)
    elif page == "Sugarcane Calculator":
        render_sugarcane_calculator(conn)
    elif page == "Equipment Rental":
        render_equipment_rental(conn)
    elif page == "Farming Info":
        render_farming_info()

    # Close SQLite connection
    conn.close()

if __name__ == "__main__":
    main()
