import streamlit as st
import requests
st.title("Weather")
city = st.text_input("enter city name")
if st.button("get weather"):
    apikey = "df5ad00fbd5917004f81677e6a176035"
    url=f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={apikey}"
    response=requests.get(url)
    if response.status_code == 200:
        data=response.json()
        latitude=data[0]["lat"]
        longitude=data[0]["lon"]
        temp_api=f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={apikey}"
        response=requests.get(temp_api)
        if response.status_code == 200:
            data=response.json()
            temp=data["main"]["temp"]
            st.success(f"Temperature : {temp}K")
