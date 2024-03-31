import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib  # Import joblib for saving and loading model

# Load the data from the CSV file
data = pd.read_csv("all_feature_combinations_with_clusters.csv")

# Encoding categorical features and the target variable
le_diet = LabelEncoder()
le_transport = LabelEncoder()
le_energy = LabelEncoder()
le_waste = LabelEncoder()
le_cluster = LabelEncoder()

data['Dietary Habits Encoded'] = le_diet.fit_transform(data['Dietary Habits'])
data['Transportation Modes Encoded'] = le_transport.fit_transform(data['Transportation Modes'])
data['Energy Consumption Encoded'] = le_energy.fit_transform(data['Energy Consumption'])
data['Waste Management Encoded'] = le_waste.fit_transform(data['Waste Management'])
data['Cluster Encoded'] = le_cluster.fit_transform(data['Cluster'])

# Defining features and target variable
X = data[['Dietary Habits Encoded', 'Transportation Modes Encoded', 'Energy Consumption Encoded', 'Waste Management Encoded']]
y = data['Cluster Encoded']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'random_forest_model.pkl')

# Load the saved model
loaded_model = joblib.load('random_forest_model.pkl')

# Predicting on some example data
example_data = pd.DataFrame({
    'Dietary Habits Encoded': [le_diet.transform(['Omnivore'])[0]],
    'Transportation Modes Encoded': [le_transport.transform(['Public Transport'])[0]],
    'Energy Consumption Encoded': [le_energy.transform(['Low Energy'])[0]],
    'Waste Management Encoded': [le_waste.transform(['Recycles'])[0]]
})

example_prediction = loaded_model.predict(example_data)

# If you want to get the predicted cluster label back into its original form (before encoding), you can use inverse_transform
original_prediction = le_cluster.inverse_transform(example_prediction)

# Print the prediction
print("Predicted Cluster Label for Example Data:")
print(original_prediction)
