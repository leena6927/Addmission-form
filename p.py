import streamlit as st 
st.set_page_config(page_title="Addmission APP",layout="wide")
st.title("📩 ADDMISSION FORM ")
st.write("Welcome .....")
st.header("Self Information 📄")

name = st.text_input("Enter Your Name")
age = st.number_input("Enter Your age", min_value=1, step=1)
st.write(f"You are {age} years old.")
contact_number= st.text_input("Enter your Contact Number:")
Email_ID= st.text_input("Enter Your Email_ID")
gender = st.radio("select your Gender:", ["Female","Male","Other"])
st.write(f"your Gender is {gender}")
Address= st.text_input("Enter Your current Address")
Caste=st.selectbox("Select Your cast:",["ST","SC","OBC","Open","Other"])

st.markdown("---")
st.header("Information About Your Education 📚")

Education_status= st.selectbox("select your Education:",["10th pass","12th pass","Diploma Student","Other"])
st.write(f"you selected your:{Education_status}")
student_id = st.text_input("Enter your student_id")
school_name= st.text_input("Enter Your School Name")
percentage= st.text_input("Enter your Marks")
seat_number=st.text_input("Enter your seat Number")

agree = st.checkbox("Ready To Submit 👍")
if st.button(" Done !"):
    st.success("You Clicked The Button!")

massage = st.text_area("Write a massgage:")

st.success("Thank You ! You've successfully Done Your Addmission Form.")