import streamlit as st
import sqlite3

# Establish connection to SQLite database
conn = sqlite3.connect('agriculture.db')
c = conn.cursor()

# Function to create initial database tables if they don't exist
def create_db():
    c.execute("CREATE TABLE IF NOT EXISTS crops (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, price REAL)")
    c.execute("CREATE TABLE IF NOT EXISTS equipment (id INTEGER PRIMARY KEY, name TEXT, price REAL)")
    c.execute("CREATE TABLE IF NOT EXISTS machinery (id INTEGER PRIMARY KEY, name TEXT, rent_per_day REAL)")
    conn.commit()

def sell_crops(name, quantity, price):
    c.execute("INSERT INTO crops (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()
    st.success(f"Successfully added crop: {name}, Quantity: {quantity}, Price: {price}")

def buy_equipment(name, price):
    c.execute("INSERT INTO equipment (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    st.success(f"Successfully bought equipment: {name}, Price: {price}")

def rent_machinery(name, rent_per_day):
    c.execute("INSERT INTO machinery (name, rent_per_day) VALUES (?, ?)", (name, rent_per_day))
    conn.commit()
    st.success(f"Successfully rented machinery: {name}, Rent per day: {rent_per_day}")

def main():
    st.title("Agriculture Marketplace")
    st.markdown(
        """
        <style>
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.title("Operations")
    operation = st.sidebar.selectbox("Select Operation", ["Create Database", "Sell Crops", "Buy Equipment", "Rent Machinery"])

    if operation == "Create Database":
        create_db()
        st.sidebar.success("Database created successfully.")

    elif operation == "Sell Crops":
        st.header("Sell Crops")
        crop_name = st.text_input("Crop Name")
        crop_quantity = st.number_input("Quantity", min_value=1)
        crop_price = st.number_input("Price per unit", min_value=0.0)

        if st.button("Sell"):
            sell_crops(crop_name, crop_quantity, crop_price)

    elif operation == "Buy Equipment":
        st.header("Buy Equipment")
        equipment_name = st.text_input("Equipment Name")
        equipment_price = st.number_input("Price", min_value=0.0)

        if st.button("Buy"):
            buy_equipment(equipment_name, equipment_price)

    elif operation == "Rent Machinery":
        st.header("Rent Machinery")
        machinery_name = st.text_input("Machinery Name")
        rent_per_day = st.number_input("Rent per day", min_value=0.0)

        if st.button("Rent"):
            rent_machinery(machinery_name, rent_per_day)

    conn.close()

if __name__ == "__main__":
    main()
