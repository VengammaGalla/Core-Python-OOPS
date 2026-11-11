class LightDevice:
    def operate(self):
        print("Light is ON")
        super().operate()


class SecurityDevice:
    def operate(self):
        print("Security system is ON")
        super().operate()


class SmartCamera(LightDevice, SecurityDevice):
    def __init__(self):
        self.__logs = []

    def operate(self):
        self.__logs.append("Camera started")
        print("Smart camera is ON")
        super().operate()


camera = SmartCamera()
camera.operate()

print(SmartCamera.mro())


class Device:
    def operate(self):
        pass


class LightDevice(Device):
    def operate(self):
        print("Light is ON")
        super().operate()


class SecurityDevice(Device):
    def operate(self):
        print("Security system is ON")
        super().operate()


class SmartCamera(LightDevice, SecurityDevice):
    def __init__(self):
        self.__logs = []

    def operate(self):
        self.__logs.append("Camera started")
        print("Smart camera is ON")
        super().operate()


camera = SmartCamera()
camera.operate()
print(SmartCamera.mro())