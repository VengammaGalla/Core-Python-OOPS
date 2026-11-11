from abc import ABC, abstractmethod

class MLModel(ABC):

    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, x):
        pass

    @abstractmethod
    def evaluate(self, test_set):
        pass

class LinearRegressionModel(MLModel):

    def train(self, data):
        print("Training Linear Regression")

    def predict(self, x):
        print("Linear Regression prediction:", x * 2)

    def evaluate(self, test_set):
        print("Linear Regression evaluation")


class DecisionTreeModel(MLModel):

    def train(self, data):
        print("Training Decision Tree")

    def predict(self, x):
        print("Decision Tree prediction:", x + 10)

    def evaluate(self, test_set):
        print("Decision Tree evaluation")


def training_loop(model):
    model.train([1, 2, 3])
    model.predict(5)
    model.evaluate([4, 5])


linear = LinearRegressionModel()
training_loop(linear)

print()

tree = DecisionTreeModel()
training_loop(tree)