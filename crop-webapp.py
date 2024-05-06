import streamlit as st
import pickle
from PIL import Image

LogReg_model = pickle.load(open('LogReg_model.pkl', 'rb'))
DecisionTree_model = pickle.load(open('DecisionTree_model.pkl', 'rb'))
NaiveBayes_model = pickle.load(open('NaiveBayes_model.pkl', 'rb'))
RF_model = pickle.load(open('RF_model.pkl', 'rb'))

def classify(answer):
    crop_name = answer[0].upper()
    return f"**{crop_name}** is the best crop for cultivation here."

def main():
    st.title("GraMitra (Crop Recommender)...")
    image = Image.open('cc.jpg')
    st.image(image)
    html_temp = """
    <div style="background-color:#85c532; padding:7px">
    <h2 style="color:#fff;text-align:center;">Find the most suitable crop using GraMitra's crop recommender.</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Add logo to the top left corner
    st.sidebar.image('logo.png', width=150, caption='')
    
    activities = ['Naive Bayes', 'Logistic Regression', 'Decision Tree', 'Random Forest']
    option = st.sidebar.selectbox("Which model would you like to use?", activities)
    st.subheader(option)
    sn = st.slider('NITROGEN (N) in (kg/ha)', 0.0, 150.0)
    sp = st.slider('PHOSPHOROUS (P) in (kg/ha)',
