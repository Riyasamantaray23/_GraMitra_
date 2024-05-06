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
    
    # Display your logo
    st.sidebar.image('logo.png', width=150, caption='')
    
    image = Image.open('cc.jpg')
    st.image(image)
    html_temp = """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    footer {
        visibility: hidden !important;
    }
    </style>
    <div style="background-color:#85c532; padding:7px">
    <h2 style="color:#fff;text-align:center;font-size:20px;">Find the most suitable crop using GraMitra's crop recommender.</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    
    activities = ['Naive Bayes', 'Logistic Regression', 'De
