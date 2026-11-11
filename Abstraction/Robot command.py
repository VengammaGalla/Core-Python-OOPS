from abc import ABC, abstractmethod

class RobotCommand(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class PickCommand(RobotCommand):

    def execute(self):
        print("Robot picked the object")

    def undo(self):
        print("Robot put the object back")


class PlaceCommand(RobotCommand):

    def execute(self):
        print("Robot placed the object")

    def undo(self):
        print("Robot removed the object")


class MoveCommand(RobotCommand):

    def execute(self):
        print("Robot moved")

    def undo(self):
        print("Robot moved back")


commands = [PickCommand(), PlaceCommand(), MoveCommand()]

for command in commands:
    command.execute()
    command.undo()