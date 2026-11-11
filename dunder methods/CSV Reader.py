class CSVReader:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            line = self.data[self.index]
            self.index = self.index + 1
            return line
        else:
            raise StopIteration


def parse_records(csv_reader):
    headers = next(csv_reader).split(",")

    for line in csv_reader:
        values = line.split(",")

        record = {}

        for i in range(len(headers)):
            record[headers[i]] = values[i]

        yield record


data = [
    "name,age,city",
    "Vennela,22,Hyderabad",
    "Ravi,23,Chennai",
    "Sita,21,Bangalore"
]


for record in parse_records(CSVReader(data)):
    print(record)