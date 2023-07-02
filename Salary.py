import streamlit as st

# Menambahkan judul
st.title("Salary Prediction")

# Menambahkan deskripsi atau penjelasan
st.write("This app predicts the salary based on years of experience.")

# Membuat input field untuk memasukkan tahun pengalaman
years_experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)

# Tombol prediksi
if st.button("Predict Salary"):
    # # Melakukan prediksi menggunakan model
    # salary_pred = regressor.predict([[years_experience]])

    # Menampilkan hasil prediksi
    st.write("The predicted salary for {} years of experience is: {}".format(years_experience, salary_pred))

# Menampilkan scatter plot dari data
st.subheader("Scatter Plot")
st.write("This plot shows the relationship between years of experience and salary.")
st.scatter_chart()

# Menampilkan plot regresi
st.subheader("Regression Plot")
st.write("This plot shows the regression line fitted to the data.")
st.line_chart()

