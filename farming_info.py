import streamlit as st

def render_farming_info():
    st.header("Farming Information")

    st.write("""
        Welcome to our Farming Information page! Here you can find valuable information 
        related to farming practices, crop details, and weather forecasts.
    """)

    st.subheader("Farming Practices")
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ullamcorper elit sed 
        velit euismod, sed fringilla nulla volutpat. Sed eu risus tortor. Sed accumsan urna 
        vel diam lobortis, id aliquam justo facilisis. Nunc sit amet dui vestibulum, mollis 
        nulla non, varius ex.
    """)

    st.subheader("Crop Details")
    st.write("""
        In this section, you can learn about various crops such as sugarcane, wheat, rice, 
        and their cultivation techniques. Ut vitae metus in ligula condimentum iaculis. 
        Nulla id libero at metus tincidunt fermentum. Cras vel pretium neque. Nullam vel 
        odio a nulla ultricies blandit.
    """)

    st.subheader("Weather Forecasts")
    st.write("""
        Stay updated with the latest weather forecasts to plan your farming activities. 
        Praesent tincidunt vehicula est, at posuere dui. In hac habitasse platea dictumst. 
        Nullam ut nisi vitae justo varius vestibulum. Integer in nunc quam.
    """)

    st.subheader("Downloadable Resources")
    st.write("""
        Download images or documents related to farming and agriculture:
    """)
    
    # Example downloadable image
    image_url = "https://example.com/farm_image.jpg"
    st.image(image_url, caption='Farm Image', use_column_width=True)
    st.markdown("[Download Farm Image](https://example.com/farm_image.jpg)")

