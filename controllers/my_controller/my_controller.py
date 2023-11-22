"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import DistanceSensor

if __name__ == "__main__":

    # create the Robot instance.
    robot = Robot()
    front_middle_ds = DistanceSensor('ds_front_middle')
    
    # get the time step of the current world.
    timestep = 64
    max_speed = 7
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)
    
    left_motor = robot.getMotor('motor_1')
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor = robot.getMotor('motor_2')
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    front_middle_ds.enable(10)
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        left_speed = -0.7 * max_speed
        right_speed = -0.7 * max_speed    
        
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
        
        print(front_middle_ds.getValue())