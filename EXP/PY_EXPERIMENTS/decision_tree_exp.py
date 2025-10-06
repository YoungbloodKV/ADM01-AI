# Experiment: Decision Tree
# Name: Yash | Reg No: 19255

from sklearn import tree

# Sample dataset: [Weather, Temperature] → Play (Yes/No)
# Features: 0=Sunny,1=Rainy; 0=Hot,1=Cool
X = [[0,0], [0,1], [1,0], [1,1]]
Y = ["No", "Yes", "Yes", "No"]

# Create Decision Tree Classifier
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(X, Y)

# Predict on new data
test = [[0,0], [1,1], [0,1]]
pred = clf.predict(test)

print("Predictions for test cases:", pred)

# Visualize Tree
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))
tree.plot_tree(clf, feature_names=["Weather","Temp"], class_names=["No","Yes"], filled=True)
plt.show()
