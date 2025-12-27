import streamlit as st
import requests

st.set_page_config(page_title="توقع أسعار المنازل", page_icon="🏠")
st.title("🏠 نظام توقع أسعار المنازل الذكي")

st.write("أدخل بيانات الحي للحصول على تقدير لسعر المنزل:")

# تقسيم الواجهة لأعمدة لجعلها أجمل
col1, col2 = st.columns(2)

with col1:
    lon = st.number_input("خط الطول (Longitude)", value=-122.23)
    lat = st.number_input("خط العرض (Latitude)", value=37.88)
    age = st.number_input("عمر المنزل المتوسط", value=41.0)
    rooms = st.number_input("إجمالي الغرف", value=880.0)

with col2:
    bedrooms = st.number_input("إجمالي غرف النوم", value=129.0)
    pop = st.number_input("السكان", value=322.0)
    households = st.number_input("عدد الأسر", value=126.0)
    income = st.number_input("متوسط الدخل", value=8.32)

if st.button("توقع السعر الآن"):
    # البيانات المرسلة للـ API
    payload = {
        "longitude": lon, "latitude": lat, "housing_median_age": age,
        "total_rooms": rooms, "total_bedrooms": bedrooms,
        "population": pop, "households": households, "median_income": income
    }

    response = requests.post("http://127.0.0.1:8000/predict",json=payload)

    if response.status_code==200:
        res=response.json()
        st.success(f"💰 السعر المتوقع للمنزل هو: ${res['estimated_value']:,}")
        st.balloons()
    else:
            st.error("حدث خطأ في الاتصال بالسيرفر")

