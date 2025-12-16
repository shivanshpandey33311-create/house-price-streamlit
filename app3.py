import streamlit as st
import pickle
import pandas as pd
model = pickle.load(open("linear_model.pkl", "rb"))
area = st.number_input("Area (sqft)")
bathrooms = st.number_input("Bathrooms", step=1)
bedrooms = st.number_input("Bedrooms", step=1)
stories = st.number_input("Stories", step=1)
parking = st.number_input("Parking", step=1)
guestroom = st.selectbox("Guest Room", [0, 1])
basement =st.selectbox("Basement", [0, 1])
hotwaterheating = st.selectbox("Hot Water Heating", [0, 1])
airconditioning = st.selectbox("Air Conditioning", [0, 1])
prefarea = st.selectbox("Preferred Area", [0, 1])
furn_semi = st.selectbox("Semi Furnished", [0, 1])
furn_unfurn = st.selectbox("Unfurnished", [0, 1])
if st.button("Predict Price"):
    input_data = pd.DataFrame([[area, bathrooms,parking, stories,
                                airconditioning, bedrooms,
                                furn_unfurn, prefarea, basement,
                                guestroom, hotwaterheating, furn_semi]],
 columns=[
                                  "area", "bathrooms","parking", "stories",
                                  "airconditioning", "bedrooms",
                                  "furnishingstatus_unfurnished", "prefarea",
                                  "basement", "guestroom",
                                  "hotwaterheating",
                                  "furnishingstatus_semi-furnished"
                              ])
prediction = model.predict(input_data)
st.success(f"Predicted House Price: ₹ {int(prediction[0])}")





