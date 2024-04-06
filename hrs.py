import pandas as pd
import streamlit as st

def load_dataset():
    hospital_data = pd.read_csv('hospital1.csv', encoding='utf-8')
    return hospital_data




def recommend_hospitals(city, data):
    recommended_hospitals = data[data['District'] == city]
    return recommended_hospitals

def main():
    st.title("Health-Genie's Hospital Recommendation System")
    st.sidebar.title('Health Genie')
    st.sidebar.header('User Input-')
    
    cities = ['South Andaman','Nagpur', 'Mumbai', 'Pune','Delhi','Amritsar','Bengaluru Urban','Wardha']  
    city = st.sidebar.selectbox('Select District', cities)  

    data = load_dataset()

    recommended_hospitals = recommend_hospitals(city, data)

    st.subheader('Recommended Hospitals')

    if recommended_hospitals.empty:
        st.write('No hospitals found in the specified district')
    else:
        st.table(recommended_hospitals[['Hospital_Name', 'Address_Original_First_Line','District','Mobile_Number','Telephone','Emergency_Num','Hospital_Primary_Email_Id']])
    
    st.write('|Above are some Hospitals/Clinics based on your provided location.|')
    
if __name__ == "__main__":
    main()
