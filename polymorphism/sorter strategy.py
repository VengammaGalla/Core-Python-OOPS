class BS:
    def sort(self, data):
        print("Sorting using Bubble Sort")

class MS:
    def sort(self, data):
        print("Sorting using Merge Sort")

class QS:
    def sort(self, data):
        print("Sorting using Quick Sort")

class Sorter:
    def change(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        self.strategy.sort(data)


sorter = Sorter()

sorter.change(BS())
sorter.sort([3, 1, 2])

sorter.change(MS())
sorter.sort([3, 1, 2])

sorter.change(QS())
sorter.sort([3, 1, 2])