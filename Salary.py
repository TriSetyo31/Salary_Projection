import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_csv("Salary_Data.csv")
X = df.iloc[:, :-1]
y = df.iloc[:, 1]

# Train the model
regressor = LinearRegression()
regressor.fit(X, y)

# Menambahkan judul
st.title("Salary Prediction")

# Menambahkan deskripsi atau penjelasan
st.write("This app predicts the salary based on years of experience.")

# Membuat input field untuk memasukkan tahun pengalaman
years_experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)

# Tombol prediksi
if st.button("Predict Salary"):
    # Melakukan prediksi menggunakan model
    salary_pred = regressor.predict([[years_experience]])

    # Menampilkan hasil prediksi
    st.write("The predicted salary for {} years of experience is: {}".format(years_experience, salary_pred[0]))

# Menampilkan scatter plot dari data
st.subheader("Scatter Plot")
st.write("This plot shows the relationship between years of experience and salary.")
plt.scatter(X, y, color="green")
plt.title("Years Experience VS Salary")
plt.xlabel("Years Experience")
plt.ylabel("Salary")
st.pyplot()

# Menampilkan plot regresi
st.subheader("Regression Plot")
st.write("This plot shows the regression line fitted to the data.")
plt.scatter(X, y, color="green")
plt.plot(X, regressor.predict(X), color="red")
plt.title("Years Experience VS Salary")
plt.xlabel("Years Experience")
plt.ylabel("Salary")
st.pyplot()
