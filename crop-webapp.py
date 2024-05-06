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
    <style>
    img[src*="github"] {
        display: none;
    }
    </style>
    <div style="background-color:#85c532; padding:7px">
    <h2 style="color:#fff;text-align:center;font-size:20px;">Find the most suitable crop using GraMitra's crop recommender.</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Add logo to the top left corner
    st.sidebar.image('logo.png', width=150, caption='')
    
    # Show/hide sidebar based on button click
    if st.button('Toggle Sidebar'):
        st.sidebar.title("Sidebar Content")
        # Add sidebar content here
    
    activities = ['Naive Bayes', 'Logistic Regression', 'Decision Tree', 'Random Forest']
    option = st.sidebar.selectbox("Which model would you like to use?", activities)
    st.subheader(option)
    sn = st.slider('NITROGEN (N) in (kg/ha)', 0.0, 150.0)
    sp = st.slider('PHOSPHOROUS (P) in (kg/ha)', 0.0, 150.0)
    pk = st.slider('POTASSIUM (K) in (kg/ha)', 0.0, 210.0)
    pt = st.slider('TEMPERATURE in °C', 0.0, 50.0)
    phu = st.slider('HUMIDITY in %', 0.0, 100.0)
    pPh = st.slider('pH', 0.0, 14.0)
    pr = st.slider('RAINFALL in mm', 0.0, 300.0)
    inputs = [[sn, sp, pk, pt, phu, pPh, pr]]
    if st.button('Classify'):
        if option == 'Logistic Regression':
            st.success(classify(LogReg_model.predict(inputs)))
        elif option == 'Decision Tree':
            st.success(classify(DecisionTree_model.predict(inputs)))
        elif option == 'Naive Bayes':
            st.success(classify(NaiveBayes_model.predict(inputs)))
        else:
            st.success(classify(RF_model.predict(inputs)))   

if __name__ == '__main__':
    main()


    

