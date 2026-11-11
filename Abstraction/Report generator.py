from abc import ABC, abstractmethod

class ReportGenerator(ABC):

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def export(self):
        pass

class PDFReport(ReportGenerator):

    def load_data(self):
        print("Loading data for PDF")

    def process(self):
        print("Processing PDF data")

    def export(self):
        print("Exporting PDF report")

class ExcelReport(ReportGenerator):

    def load_data(self):
        print("Loading data for Excel")

    def process(self):
        print("Processing Excel data")

    def export(self):
        print("Exporting Excel report")

def generate_report(report):
    report.load_data()
    report.process()
    report.export()


pdf = PDFReport()
generate_report(pdf)

print()

excel = ExcelReport()
generate_report(excel)

print()