import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

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

# Predicting the test set results
y_pred = model.predict(X_test)

# Calculating the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")

# Exporting the model as a joblib file
joblib.dump(model, "random_forest_model.joblib")
