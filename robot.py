import wpilib as wpi
from wpilib.drive import DifferentialDrive
#from math import pi

class Robot(wpi.SampleRobot):

    def robotInit(self):
        #update channels
        self.frontR = wpi.Talon(1)
        self.frontL = wpi.Talon(2)
        self.rearR = wpi.Talon(0)
        self.rearL = wpi.Talon(3)
        self.gyro = wpi.AnalogGyro(0)
        self.joystick = wpi.Joystick(0)
        self.right = wpi.SpeedControllerGroup(self.frontR, self.rearR)
        self.left = wpi.SpeedControllerGroup(self.frontL, self.rearL)
        self.dTrain = wpi.drive.DifferentialDrive(self.right, self.left)
        self.xDeadZone = .05
        self.yDeadZone = .05
        self.xConstant = .55
        self.yConstant = .85

    def autonomous(self):
        while self.isAutonomous() and self.isEnabled():
            pass #update later

    def disabled(self):
        while self.isDisabled():
            self.dTrain.arcadeDrive(0.0, 0.0)

    def operatorControl(self):
        while self.isOperatorControl() and self.isEnabled():
            angle = self.joystick.getX()
            speed = self.joystick.getY()
            if abs(angle) <= self.xDeadZone:
                angle = 0.0
            else:
                angle = self.xConstant*angle**3
            if abs(speed) <= self.yDeadZone:
                speed = 0.0
            else:
                speed = speed * self.yConstant
            self.dTrain.arcadeDrive(xSpeed = speed, zRotation = -angle)

if __name__ == '__main__':
    wpi.run(Robot)
