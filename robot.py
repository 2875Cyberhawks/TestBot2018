import wpilib as wpi
from wpilib.drive import DifferentialDrive
#from math import pi

class Robot(wpi.SampleRobot):

    def robotInit(self):
        #update channels
        self.frontR = wpi.Talon(0)
        self.frontL = wpi.Talon(1)
        self.rearR = wpi.Talon(2)
        self.rearL = wpi.Talon(3)
        self.gyro = wpi.AnalogGyro(0)
        self.joystick = wpi.Joystick(0)
        self.right = wpi.SpeedControllerGroup(self.frontR, self.rearR)
        self.left = wpi.SpeedControllerGroup(self.frontL, self.rearL)
        self.dTrain = wpi.drive.DifferentialDrive(self.right, self.left)

    def autonomous(self):
        while self.isAutonomous() and self.isEnabled():
            pass #update later

    def disabled(self):
        while self.isDisabled():
            self.dTrain.arcadeDrive(0.0, 0.0)

    def operatorControl(self):
        while self.isOperatorControl() and self.isEnabled():
            self.dTrain.arcadeDrive(self.joystick)
            '''angle = joystick.getDirectionRadians()
            print(angle * (180 / pi))
            speed = self.joystick.getY()
            if speed <= 0:
                self.dTrain.arcadeDrive(speed, angle)
            else:
                self.dTrain.arcadeDrive(speed, -angle)'''

if __name__ == '__main__':
    wpi.run(Robot)
