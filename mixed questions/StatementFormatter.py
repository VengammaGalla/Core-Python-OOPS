from abc import ABC, abstractmethod
import json

class StatementFormatter(ABC):
    @abstractmethod
    def format(self, data):
        pass

    def __call__(self, data):
        return self.format(data)


class PDFFormatter(StatementFormatter):
    def format(self, data):
        return "PDF: " + str(data)

    def __repr__(self):
        return "PDFFormatter()"


class JSONFormatter(StatementFormatter):
    def format(self, data):
        return json.dumps(data)

    def __repr__(self):
        return "JSONFormatter()"


class TextFormatter(StatementFormatter):
    def format(self, data):
        return "\n".join(f"{k}: {v}" for k, v in data.items())

    def __repr__(self):
        return "TextFormatter()"


data = {"name": "Ravi", "salary": 30000}

formatters = [
    PDFFormatter(),
    JSONFormatter(),
    TextFormatter()
]

for formatter in formatters:
    print(repr(formatter))
    print(formatter(data))