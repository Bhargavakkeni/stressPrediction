# File - Predictive System.py

# Imports
import numpy as np
import pickle

# Loading the trained model
loaded_model = pickle.load(open('stress_trained.sav','rb'))
# stress_trained.sav - replace the path of the file along with the file name
# Example: loaded_model = pickle.load(open('C:/Users/jeyasri/Downloads/PROJECT/stress_trained.sav','rb'))



input_data = (25.41,94.41,167) #200
#changing the input data into numpy array
id_np_array = np.asarray(input_data)
id_reshaped = id_np_array.reshape(1,-1)

prediction = loaded_model.predict(id_reshaped)
print(prediction)

if(prediction[0]==0):
    print("Stress Level: LOW")
elif(prediction[0]==1):
    print("Stress Level: MEDIUM")
else:
    print("Stress Level: HIGH")