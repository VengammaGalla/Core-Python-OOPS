from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, data):
        pass


class LinearRegressionModel(Model):
    def train(self, data):
        print("Training Linear Regression")

    def predict(self, data):
        return [x * 2 for x in data]


class DecisionTreeModel(Model):
    def train(self, data):
        print("Training Decision Tree")

    def predict(self, data):
        return [1 if x > 5 else 0 for x in data]


class Pipeline:
    def __init__(self, model, steps):
        self.__model = model
        self.__steps = steps

    def __call__(self, data):
        for step in self.__steps:
            data = step(data)
        return self.__model.predict(data)

    def train(self, data):
        self.__model.train(data)


def double_values(data):
    return [x * 2 for x in data]


pipeline = Pipeline(
    LinearRegressionModel(),
    [double_values]
)

pipeline.train([1, 2, 3])
print(pipeline([1, 2, 3]))