import pandas as pd
import joblib  # Import joblib for loading model
from sklearn.preprocessing import LabelEncoder
# Load the example data
example_data = pd.DataFrame({
    'Dietary Habits': ['Omnivore'],
    'Transportation Modes': ['Public Transport'],
    'Energy Consumption': ['Low Energy'],
    'Waste Management': ['Recycles']
})

# Load the saved model
loaded_model = joblib.load('random_forest_model.pkl')

le_diet = LabelEncoder()
le_transport = LabelEncoder()
le_energy = LabelEncoder()
le_waste = LabelEncoder()
le_cluster = LabelEncoder()

# Encode the example data
example_data['Dietary Habits Encoded'] = le_diet.transform(example_data['Dietary Habits'])
example_data['Transportation Modes Encoded'] = le_transport.transform(example_data['Transportation Modes'])
example_data['Energy Consumption Encoded'] = le_energy.transform(example_data['Energy Consumption'])
example_data['Waste Management Encoded'] = le_waste.transform(example_data['Waste Management'])

# Select features for prediction
example_data_for_prediction = example_data[['Dietary Habits Encoded', 'Transportation Modes Encoded', 'Energy Consumption Encoded', 'Waste Management Encoded']]

# Perform prediction
example_prediction = loaded_model.predict(example_data_for_prediction)

# If you want to get the predicted cluster label back into its original form (before encoding), you can use inverse_transform
original_prediction = le_cluster.inverse_transform(example_prediction)

# Print the prediction
print("Predicted Cluster Label for Example Data:")
print(original_prediction)
