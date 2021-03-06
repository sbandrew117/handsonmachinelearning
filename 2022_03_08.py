import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
x = iris.data[:, 2:]
y = iris.target
tree_clf = DecisionTreeClassifier(max_depth = 2)
tree_clf,fit(x, y)

from sklearn.tree import export_graphviz
'''
export_graphviz(
    tree_clf,
    out_file = image_path("iris_tree.dot")
    feature_names = iris.feature_names[2:],
    class_names = iris.target_names,
    rounded = True
    filled = True
)
'''

#회귀
from sklearn.tree import DecisionTreeClassifier

tree_reg = DecisionTreeClassifier(max_depth = 2)
tree_reg.fit(x, y)

