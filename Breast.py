import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('Breast_model.sav', 'rb'))

def Breast_predicton(input_data):


# changing the input_data to numpy array
   input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
   input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)



   prediction = loaded_model.predict(input_data_reshaped)
   print(prediction)

   if (prediction[0] == 0):
     return 'The Breast cancer is Malignant'
   else:
     return 'The Breast Cancer is Benign'
  
  
def main():
      
    st.title('Breast Prediction Model')
      
    radius=st.text_input('mean')
    texture=st.text_input('mean texture')
    perimeter=st.text_input('mean perimeter')
    area=st.text_input('mean area')
    smoothness=st.text_input('mean smoothness')
    compactness=st.text_input('mean compactness')
    concavity=st.text_input('mean concavity')
    points=st.text_input('mean concave points')
    symmetry=st.text_input('mean symmetry')
    dimension=st.text_input('mean fractal dimension')
    error=st.text_input('radius error')
    texture_error =st.text_input('texture error')
    perimeter_error =st.text_input('perimeter error')
    area_error=st.text_input('area error')
    smoothness_error=st.text_input('smoothness error')
    compactness_error=st.text_input('compactness error')
    concavity_error=st.text_input('concavity error')
    points_error=st.text_input('concave points error')
    symmetry_error=st.text_input('symmetry error')
    dimension_error=st.text_input('fractal dimmension error')
    worst_radius=st.text_input('worst radius')
    worst_texture=st.text_input('worst texture')
    worst_perimeter=st.text_input('worst perimeter')
    worst_area=st.text_input('worst area')
    worst_smoothness=st.text_input('worst smoothness')
    worst_compactness=st.text_input('worst compactness')
    worst_concavity=st.text_input('worst concavity')
    concave_points=st.text_input('worst concave points')
    worst_symmetry=st.text_input('worst symmetry')
    fractal_dimension=st.text_input('worst fractal dimension')
      
      
    diagnosis=''
      
    if st.button('Diabetes Test Result'):
          diagnosis= Breast_predicton([radius,texture,perimeter,area,smoothness,compactness,concavity,points,symmetry,dimension,error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,points_error,symmetry_error,dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,concave_points,worst_symmetry,fractal_dimension])                          
        
          
    st.success(diagnosis)
      
      
if __name__=='__main__':
    main()
      
      
      
      
