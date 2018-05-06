class SingleClassClassifier():
    def __init__(self, class_):
        self.class_ = class_
        self.classes_ = [class_]
    def predict(self):
        return self.class_
    def proba(self, class_):
        return 1 if class_ == self.class_ else 0
    def predict_proba(self, X):
        return [[1]]