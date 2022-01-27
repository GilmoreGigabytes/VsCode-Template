from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import Timer
from sys import platform 
from math import *
import os

hub = PrimeHub()
timer = Timer()

movepair = MotorPair("F", "A")

rightMotor = Motor("A")
leftMotor = Motor("F")

arm = Motor("E")

colourL = ColorSensor("B")
colourR = ColorSensor("C")

force = ForceSensor("D")

defaultSpeed = 60

class error:
    def typeCheck(value, givenType) -> bool:
        if type(value) != givenType:
            return True
        return False


    def throw(value, text : str):
        raise ValueError(f"Error: {value} is invalid \n{text}")


    def template(value, type : str):
        if type == "sensor":
            if value != "left" and value != "right":
                error.throw(value, "Sensor must be a string with the value of 'left' or 'right'")
            return
        if type == "speed":
            if error.typeCheck(value, int) == False or value <= 0:
                error.throw(value, "Speed must be an integer greater than 0")
            return
        if type == "direction":
            if value <= "left" and value != "right":
                error.throw(value, "Direction must be a string with the value of 'left' or 'right'")
            return
        if type == "distance":
            if error.typeCheck(value, int) == False  or value <= 0:
                error.throw(value, "Distance must an integer greater than 0")
            return
        if type == "cm":
            if error.typeCheck(value, int) == False or value <= 0:
                error.throw(value, "Cm must be an int greater than 0")


def resetYawAngle():
    hub.motion_sensor.reset_yaw_angle()


def resetMotors():
    rightMotor.set_degrees_counted(0)
    leftMotor.set_degrees_counted(0)
    arm.set_degrees_counted(0)


def clear():
    if platform == "linux":
        os.sytem("clear")
    else:
        os.system("cls")

def count(time : int):
    resetMotors()
    timer.reset()

    while timer.now() < time:
        print(f"Left Motor: {leftMotor.get_degrees_counted()} | Right Motor: {rightMotor.get_degrees_counted()} | Arm: {arm.get_degrees_counted()} | Left Colour Sensor: {colourL.get_color()} | Right Colour Sensor: {colourR.get_color()}")
    clear()


def motion():
    yaw = hub.motion_sensor.get_yaw_angle()
    roll = hub.motion_sensor.get_roll_angle()
    pitch = hub.motion_sensor.get_pitch_angle()

    print(f"Yaw: {yaw} | Pitch: {pitch} | Roll: {roll}")


def move(distance : int, direction : str, speed : int  = defaultSpeed):
    error.template(distance, "distance")
    error.template(direction, "direction")
    error.template(speed, "speed")

    resetMotors()
    resetYawAngle()

    if direction == "forward":
        movepair.move(distance, "cm", 0, speed)
    elif direction == "backward":
        movepair.move(-distance, "cm", 0, speed)

    movepair.stop()


def moveWithCorrection(cm : float or int):
    error.template(cm, "cm")

    resetMotors()
    resetYawAngle()

    newDegrees = cm / 0.077

    while rightMotor.get_degrees_counted() < newDegrees or leftMotor.get_degrees_counted() > newDegrees:
        correction = 0 - hub.motion_sensor.get_yaw_angle()
        movepair.start_tank_at_power((defaultSpeed + correction), (defaultSpeed - correction))
    movepair.stop()


def turn(deg : int, direction : str, aggressive : bool = False):
    error.template(deg, "deg")
    error.template(direction, "direction")

    if type(aggressive) != bool:
        error.throw(aggressive, "Aggressive mode must be a boolien")

    resetMotors()
    resetYawAngle()

    if aggressive == True:
        turnSpeed = 100
    else:
        turnSpeed = 20

    times = 1
    i = 0

    if deg <= 90:
        if direction == "left":
            while hub.motion_sensor.get_yaw_angle() > -deg:
                movepair.start_tank_at_power(-turnSpeed, turnSpeed)
            movepair.stop()
            return
        elif direction == "right":
            while hub.motion_sensor.get_yaw_angle() < deg:
                movepair.start_tank_at_power(turnSpeed, -turnSpeed)
            movepair.stop()
            return

    while deg >= 90:
        times += 1
        deg -= 45

    if deg > 45:
        times = 0
        remainder = deg - 45

    var = 44  # Adjusts for give in the wheels

    if direction == "left":
        while i < times:
            while hub.motion_sensor.get_yaw_angle() > -var:
                movepair.start_tank_at_power(-turnSpeed, turnSpeed)
            i += 1
            movepair.stop()
            resetYawAngle()
        if remainder != None:
            while hub.motion_sensor.get_yaw_angle() > -remainder:
                movepair.start_tank_at_power(-turnSpeed, turnSpeed)
            movepair.stop()
            resetYawAngle()
        return
    elif direction == "right":
        while i < times:
            while hub.motion_sensor.get_yaw_angle() < var:
                movepair.start_tank_at_power(turnSpeed, -turnSpeed)
            i += 1
            movepair.stop()
            resetYawAngle()
        if remainder != None:
            while hub.motion_sensor.get_yaw_angle() < var:
                movepair.start_tank_at_power(turnSpeed, -turnSpeed)
            movepair.stop()
            resetYawAngle()
        return


def followLine(sensor : str, cm : int or float):
    error.template(sensor, "sensor")
    error.template(cm, "cm")

    resetMotors()

    deg = cm / 0.077
    kp = 0.2  
    ki = 0
    kd = 0.22
    integral = 0
    lastError = 0
    error = 0
    speed = 30
    if sensor == "left":
        while abs(leftMotor.get_degrees_counted()) < deg or abs(rightMotor.get_degrees_counted()) < deg:
            light = ((colourL.get_reflected_light() - 20) / (87 - 10)) * 100
            error = light - 52
            integral = (integral + error) * 0.5
            correction = int((kp * error)+(ki * integral) +(kd * (error - lastError)))
            left = speed - correction
            right = speed + correction
            lastError = error
            movepair.start_tank_at_power(left, right)
    elif sensor == "right":
        while abs(leftMotor.get_degrees_counted()) < deg or abs(rightMotor.get_degrees_counted()) < deg:
            light = ((colourR.get_reflected_light() - 20) / (87 - 10)) * 100
            error = light - 52
            integral = (integral + error) * 0.5
            correction = int((kp * error)+(ki * integral) +(kd * (error - lastError)))
            left = speed - correction
            right = speed + correction
            lastError = error
            movepair.start_tank_at_power(left, right)

    movepair.stop()


def moveArm(direction : str, speed : int, distance : int or float):
    error.template(direction, "direction")
    error.template(speed, "speed")
    error.template(distance, "distance")

    resetMotors()

    if direction == "down":
        arm.run_for_rotations(distance, speed)
        return
    elif direction == "up":
        arm.run_for_rotations(-distance, speed)


def moveToLine(sensor : str, direction : str):
    error.template(sensor, "sensor")
    error.template(direction, "direction")

    resetMotors()
    resetYawAngle()

    if sensor == "right":
        if direction == "forward":
            while colourR.get_color() != "black":
                correction = 0 - hub.motion_sensor.get_yaw_angle()
                speed = 30
                movepair.start_tank_at_power( (speed + correction), (speed - correction))
            movepair.stop()
            return
        elif direction == "backward":
            while colourR.get_color() != "black":
                correction = 0 - hub.motion_sensor.get_yaw_angle()
                speed = -30
                movepair.start_tank_at_power((speed + correction), (speed - correction))
            movepair.stop()
            return
    elif sensor == "left":
        if direction == "forward":
            while colourL.get_color() != "black":
                correction = 0 - hub.motion_sensor.get_yaw_angle()
                speed = 30
                movepair.start_tank_at_power((speed + correction), (speed - correction))
            movepair.stop()
            return
        elif direction == "backward":
            while colourL.get_color() != "black":
                correction = 0 - hub.motion_sensor.get_yaw_angle()
                speed = -30
                movepair.start_tank_at_power((speed + correction), (speed - correction))
            movepair.stop()
            return


def start(direction : str):
    match direction:
        case 0:
            pass

        
def executeMission(missionId : int):
    match missionId:
        case 1:
            pass


def missionSelector():
    missionId = 0
    maxMissions = 7
    hub.status_light.on("blue")
    hub.light_matrix.show_image("GIRAFFE", brightness = 100)

    exit = False

    while True:
        if hub.right_button.was_pressed():
            if missionId == maxMissions:
                exit = True
                hub.light_matrix.show_image("SQUARE_SMALL", brightness = 100)
            else:
                exit = False
                missionId += 1
                hub.light_matrix.write(str(missionId))
        elif hub.left_button.was_pressed():
            if missionId == 0:
                exit = False
            else:
                exit = True
                missionId -= 1
                hub.light_matrix.write(str(missionId))
        elif force.is_pressed():
            if exit == True and missionId == maxMissions:
                raise SystemExit(clear())
            else:
                executeMission(missionId)


# Begin mission execution.
if __name__ == "__main__":
    missionSelector()
else:
    raise SystemExit(clear())
