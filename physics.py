from pyfrc.physics import motor_cfgs, tankmodel
from pyfrc.physics.units import units


class PhysicsEngine(object):

    def __init__(self, physics_controller):
        self.physics_controller = physics_controller

        # Change these parameters to fit your robot!
        bumper_width = 3.25*units.inch

        self.drivetrain = tankmodel.TankModel.theory(
            motor_cfgs.MOTOR_CFG_CIM,           # motor configuration
            110*units.lbs,                      # robot mass
            10.71,                              # drivetrain gear ratio
            2,                                  # motors per side
            22*units.inch,                      # robot wheelbase
            23*units.inch + bumper_width*2,     # robot width
            32*units.inch + bumper_width*2,     # robot length
            6*units.inch                        # wheel diameter
        )

    def update_sim(self, hal_data, now, tm_diff):

        # Simulate the drivetrain
        lr_motor = hal_data['pwm'][1]['value']
        rr_motor = hal_data['pwm'][2]['value']

        # Not needed because front and rear should be in sync
        #lf_motor = hal_data['pwm'][3]['value']
        #rf_motor = hal_data['pwm'][4]['value']

        x, y, angle = self.drivetrain.get_distance(lr_motor, rr_motor, tm_diff)
        self.physics_controller.distance_drive(x, y, angle)
