# import module
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


# sidebar
with st.sidebar:
    selected = option_menu('SONAR Rock vs Mine Prediction', [
        'Home',
        'About',
        'Contact'
    ],
        icons=['house', 'person', 'phone'],
        default_index=0)
    # home prediction page
if selected == 'Home':  # pagetitle
    st.title("SONAR Rock vs Mine Prediction")
    image = Image.open('static/images/home.jpg')
    st.image(image, caption='SONAR Rock vs Mine Prediction')
    # columns
    # no inputs from the user
    # name = st.text_input("Name:")
    # col1, col2, col3 = st.columns(3)

    # with col1:
    #     Pregnancies = st.number_input("Number of Pregnencies")
    # with col2:
    #     Glucose = st.number_input("Glucose level")
    # with col3:
    #     BloodPressure = st.number_input("Blood pressure  value")

    # # code for prediction
    # diabetes_dig = ''

    # # button
    # if st.button("Diabetes test result"):
    #     diabetes_prediction=[[]]
    #     diabetes_prediction = diabetes_model.predict(
    #         [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreefunction, Age]])

    #     # after the prediction is done if the value in the list at index is 0 is 1 then the person is diabetic
    #     if diabetes_prediction[0] == 1:
    #         diabetes_dig = "we are really sorry to say but it seems like you are Diabetic."
    #         image = Image.open('positive.jpg')
    #         st.image(image, caption='')
    #     else:
    #         diabetes_dig = 'Congratulation,You are not diabetic'
    #         image = Image.open('negative.jpg')
    #         st.image(image, caption='')
    #     st.success(name+' , ' + diabetes_dig)

    # home prediction page
if selected == 'About':  # pagetitle
    st.title("About Us")
    image = Image.open('static/images/Aboutus.png')
    st.image(image, caption='About us')
if selected == 'Contact':  # pagetitle
    st.title("Contact Us")
    image = Image.open('static/images/Contactus.png')
    st.image(image, caption='contact us')
