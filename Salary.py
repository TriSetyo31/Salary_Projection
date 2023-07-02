import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_csv("Salary_Data.csv")

# Split the data into features (X) and target (y)
X = df.iloc[:, :-1]
y = df.iloc[:, 1]

# Train the model
regressor = LinearRegression()
regressor.fit(X, y)

# Create the Streamlit app
def main():
    st.title("Salary Prediction")
    st.markdown("## Years of Experience vs. Salary")

    # Sidebar inputs
    years_experience = st.sidebar.number_input("Years of Experience", min_value=0.0, step=0.1)

    # Make prediction
    salary_pred = regressor.predict([[years_experience]])

    # Display the prediction
    st.write("The salary for {} years of experience is: $".format(years_experience), salary_pred[0])

    # Plot the data and regression line
    plt.scatter(X, y, color="green")
    plt.plot(X, regressor.predict(X), color="red")
    plt.title("Years of Experience vs. Salary")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    st.pyplot()

if __name__ == "__main__":
    main()
