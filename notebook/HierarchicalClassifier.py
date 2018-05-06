from time import time
from queue import PriorityQueue
import pandas as pd

from SingleClassClassifier import SingleClassClassifier

from sklearn.base import clone

class HierarchicalClassifier:
    def __init__(self, clf, max_level = None, min_proba = None):
        self.clf = clf
        self.max_level = max_level 
        self.min_proba = min_proba
        self.models = {}

    def fit(self, X, Y):
        self.fit_branch(X, Y, ['root'])
            
    def fit_branch(self, X, Y, branch):
        print('fiting branch', branch)
        
        level = len(branch) - 1
        y = Y.iloc[:, level]

        branch_classes = y.unique()

        model_idx = '::'.join(branch)
        
        if len(branch_classes) > 1:
            clf_branch = clone(self.clf)
            clf_branch.fit(X, y)
            self.models[model_idx] = clf_branch
        elif len(branch_classes) == 1:
            self.models[model_idx] = SingleClassClassifier(branch_classes[0])
            
        if len(branch) < len(Y.columns):
            for branch_class in branch_classes:
                if branch_class != '':
                    sub_branch = branch[:]
                    sub_branch.append(branch_class)
                    X_sub_branch = X[y == branch_class]
                    Y_sub_branch = Y[y == branch_class]
                    self.fit_branch(X_sub_branch, Y_sub_branch, sub_branch)

    def predict(self, X):
        
        result = []
        
        for x in X:
            hierarchical_proba = self.__predict_hierarchical_proba(x)
            classification = '::'.join([level_proba[0] for level_proba in hierarchical_proba])
            result.append(classification)
        
        return result
    
    def predict_proba(self, X):
        
        result = []
        
        for x in X:
            hierarchical_proba = self.__predict_hierarchical_proba(x)
            result.append(hierarchical_proba)
        
        return result
    
    def __predict_hierarchical_proba(self, x):

        queue = PriorityQueue()
        queue.put((0, ['root']))

        predict_by_level = []

        while True:

            priority, branch = queue.get()
            model_idx = '::'.join(branch)

            probability = 1 - priority
            level = len(branch)

            if self.min_proba and probability < self.min_proba:
                return predict_by_level
            elif len(predict_by_level) <= level and level > 1:
                predict_by_level.append((branch[-1], probability))

            if model_idx not in self.models:
                return predict_by_level

            if self.max_level and level == self.max_level:
                return predict_by_level
            
            model = self.models[model_idx]
            branch_classes = model.classes_
            branch_classes_proba = model.predict_proba([x])[0]

            for branch_class, branch_class_proba in zip(branch_classes, branch_classes_proba):
                sub_branch = branch[:]
                sub_branch.append(branch_class)
                sub_branch_proba = probability * branch_class_proba
                sub_branch_priority = 1 - sub_branch_proba
                queue.put((sub_branch_priority, sub_branch))