import math
import pandas as pd

data = {
    'Outlook':  ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
    'PlayTennis': ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy_val = 0
    for i in range(len(elements)):
        prob = counts[i]/np.sum(counts)
        entropy_val += -prob * math.log2(prob)
    return entropy_val

def info_gain(data, split_attribute, target_attribute="PlayTennis"):
    # Total entropy
    total_entropy = entropy(data[target_attribute])
    
    # Weighted entropy after split
    vals, counts = np.unique(data[split_attribute], return_counts=True)
    weighted_entropy = 0
    for i in range(len(vals)):
        subset = data[data[split_attribute] == vals[i]]
        weighted_entropy += (counts[i]/np.sum(counts)) * entropy(subset[target_attribute])
    
    return total_entropy - weighted_entropy

def id3(data, target_attribute="PlayTennis", attributes=None):
    from collections import Counter
    if len(np.unique(data[target_attribute])) == 1:
        return np.unique(data[target_attribute])[0]
    
    if len(data) == 0:
        return None
    
    if attributes is None:
        attributes = data.columns.drop(target_attribute)
    if len(attributes) == 0:
        return Counter(data[target_attribute]).most_common(1)[0][0]
    
    gains = [info_gain(data, attr, target_attribute) for attr in attributes]
    best_attr = attributes[np.argmax(gains)]
    
    tree = {best_attr: {}}
    
    for val in np.unique(data[best_attr]):
        sub_data = data[data[best_attr] == val]
        subtree = id3(sub_data.drop(columns=[best_attr]),
                      target_attribute=target_attribute,
                      attributes=[a for a in attributes if a != best_attr])
        tree[best_attr][val] = subtree
    
    return tree

import numpy as np
decision_tree = id3(df)

print("\n✅ Final Learned Decision Tree (ID3):")
print(decision_tree)

def predict(tree, sample):
    # If tree is a leaf
    if not isinstance(tree, dict):
        return tree
    attr = list(tree.keys())[0]
    val = sample[attr]
    if val in tree[attr]:
        return predict(tree[attr][val], sample)
    else:
        return "Unknown"

test_sample = {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'High', 'Wind': 'Strong'}
print("\nPrediction for test sample:", test_sample, "→", predict(decision_tree, test_sample))
