import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Laptop Price Prediction")
st.write("Enter the details of your laptop to predict its price.")

brand = st.selectbox("Brand", [
    'Acer', 'Apple', 'Asus', 'Dell', 'HP', 'Lenovo',
    'MSI'])

processor = st.selectbox("Processor", [
    'Intel Core i7', 'Intel Celeron', 'Intel Core i3', 'AMD Ryzen 3', 'AMD Ryzen 5', 'AMD Ryzen 7', 'Intel Core i5', 'AMD Ryzen', 'Intel Core i9',
    'AMD Ryzen 9', '8 Core CPU', '10 Core CPU', '11 Core CPU', '12 Core CPU', '14 Core CPU'])

graphics = st.selectbox("Graphics", [
    ' Intel UHD ', 'No Graphics', ' Intel Iris Xe ', ' AMD Radeon ', ' AMD Radeon Vega 8 ', ' NVIDIA GeForce MX550 2GB ', ' NVIDIA GeForce RTX 2050 4GB ',
    ' AMD Radeon RX 6550M 4GB ',' NVIDIA GeForce RTX 3050 6GB ', ' NVIDIA GeForce RTX 3050 4GB ', ' Intel Arc ', ' NVIDIA GeForce RTX 4050 6GB ',' Integrated Intel Iris Xe ', ' NVIDIA RTX 3050Ti ',
    ' NVIDIA GeForce RTX 4060 8GB ', ' NVIDIA GeForce RTX 3060 6GB GDDR6 ', ' NVIDIA GeForce RTX 4070 8GB ', ' NVIDIA RTX 3070 ', ' NVIDIA RTX 3070Ti 8GB ', ' NVIDIA GeForce RTX 4070 8GB GDDR6 ',
    ' NVIDIA GeForce RTX 4080 8GB ', ' NVIDIA GeForce RTX 4080 12GB ', ' NVIDIA GeForce RTX 4090 16GB ',
    '7 Core GPU', '8 Core GPU', '10 Core GPU', '14 Core GPU', '16 Core GPU', '20 Core GPU', '32 Core GPU'])

series = st.selectbox("Series", [
    'IdeaPad V15-IGL', 'Wyse', 'Aspire Series', 'IdeaPad Series',
       'IdeaPad Slim 3 Series', 'Notebook', 'Vostro Series',
       'Inspiron Series', 'Notebook Series', 'VivoBook', 'ThinkBook Series', 'Swift Series', 'Business Series', 'VivoBook Go Series',
       'Pavilion Plus Series', 'Pavilion Series', 'Aspire Lite Series',
       'Envy', 'VivoBook Series', 'Victus Gaming Series',
       'Nitro V 15 Series', ' LOQ Series ', 'Yoga Series', 'Nitro 5 Series', 'Envy Series',
       'TUF Gaming Series', 'Modern 15', 'Zenbook UM3402YA', 'EliteBook Series', 'TUF Series',
       'Cyborg Series', 'IdeaPad 5', 'Vivobook K3405V', 'ThinkPad E14', 'Omen', 'Latitude Series', 'XPS Series',
       'ZenBook Series', 'Predator Series', 'ThinkPad L14'
       'Slim 7 Series', 'Legion Series', 'Legion Slim 5 Series', 'V Gaming Series',
       'Predator Helios Neo 16', 'Predator Triton Series', 'Alienware x14', 'Delta',
       'ROG Strix Series', 'XPS', 'Spectre Series','ROG Zephyrus Series', 'Alienware Series', 'ZenBook Duo Series', 'Creator Series','MacBook Air M1', 'MacBook Air M2',
       'MacBook Air M3', 'MacBook Air M4', 'MacBook Pro 14 M3',
       'MacBook Pro 14 M4', 'MacBook Pro 14 M4 Pro',
       'MacBook Pro 14 M4 Max', 'MacBook Pro 16 M4 Pro'])
ram = st.selectbox("RAM (GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])
ssd = st.selectbox("SSD (GB)", [0, 128, 256, 512, 1024, 2048])

if st.button("Predict Price"):
    data = {
        "Brand": brand,
        "Processor": processor,
        "Graphics": graphics,
        "Series": series,
        "Ram": ram,
        "Storage": ssd
    }
    response = requests.post(API_URL, json=data)
    
    if response.status_code == 200:
        prediction = response.json().get("predicted_price")
        st.success(f"Predicted Price: Rs.{prediction}")
    else:
        st.error("Error in prediction. Please check the input values.")