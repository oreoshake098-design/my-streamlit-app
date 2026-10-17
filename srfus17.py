import streamlit as st 
 
st.title("Student Registration Form") 
 
name = st.text_input("Student Name") 
age = st.number_input("Age", min_value=1, max_value=100) 
course = st.selectbox( 
    "Select Course", 
    ["BCA", "BSc Computer Science", "BBA", "BA"] 
) 
email = st.text_input("Email") 
 
if st.button("Register"): 
    if name and email: 
        st.success("Registration Successful!") 
        st.write("Name:", name) 
        st.write("Age:", age) 
        st.write("Course:", course) 
        st.write("Email:", email) 
    else: 
        st.warning("Please fill all required fields.")  