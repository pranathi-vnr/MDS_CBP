import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import pickle

# Load dataset
df = pd.read_csv("phishing.csv")

# X = 30 features, y = Result column
X = df.drop(['Result'], axis=1)
y = df['Result']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = GradientBoostingClassifier()
model.fit(X_train, y_train)

print("Training complete!")
print("Accuracy:", model.score(X_test, y_test))

# Save model
pickle.dump(model, open("pickle/model.pkl", "wb"))

print("model.pkl saved successfully!")
