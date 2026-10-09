import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

df = pd.read_csv("./csv_files/Iris.csv")

# X = the 4 measurements, y = the species name.
# Id is just a row number, so it is left out of the features.
X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
y = df["Species"]

# Hold out 20% of the data for testing.
# stratify=y keeps the species mix equal in both sets.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Train the tree on the training set, then predict on the unseen test set
clf = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Accuracy:  share of all predictions that were correct
# Precision: of flowers predicted as a species, how many truly were it
# Recall:    of flowers that truly are a species, how many were found
# average="macro" averages the 3 classes; use average=None for per-class values
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average="macro"))
print("Recall   :", recall_score(y_test, y_pred, average="macro"))

# Per-class precision, recall, F1 and sample counts in one table
print(classification_report(y_test, y_pred))