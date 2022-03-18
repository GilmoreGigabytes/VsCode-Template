from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import Timer
from sys import platform 
from math import *
import os

hub = PrimeHub()
timer = Timer()

movepair = MotorPair("A", "D")

rightMotor = Motor("D")
leftMotor = Motor("A")

arm = Motor("C")

colourL = ColorSensor("F")
colourR = ColorSensor("B")

defaultSpeed = 60

class error:
    def typeCheck(value, givenType) -> bool:
        if type(value) != givenType:
            return True
        return False


    def throw(value, text : str):
        raise ValueError("Error: " + str(value) + " is invalid \n" + str(text))


    def template(value, typeVar : str):
        if str(typeVar) == "sensor":
            if value != "left" and value != "right":
                error.throw(value, "Sensor must be a string with the value of 'left' or 'right'")
            return
        if str(typeVar) == "speed":
            if error.typeCheck(value, int and float) == False or value <= 0:
                error.throw(value, "Speed must be an integer greater than 0")
            return
        if str(typeVar) == "direction":
            if value != "left" and value != "right":
                error.throw(value, "Direction must be a string with the value of 'left' or 'right'")
            return
        if str(typeVar) == "moveDirection":
            if value != "forward" and value != "backward":
                error.throw(value, "Direction must be a string with the value of 'forward' or 'backward'")
            return
        if str(typeVar) == "armDirection":
            if error.typeCheck(value, str) or value != "up" and value != "down":
                error.throw(value, "Direction must be a string with the value of 'up' or 'down'")
        if str(typeVar) == "distance":
            if error.typeCheck(value, float) == False and error.typeCheck(value, int) == False or value <= 0:
                error.throw(value, "Distance must an integer greater than 0")
            return
        if str(typeVar) == "armDistance":
            if error.typeCheck(value, int) == False and error.typeCheck(value, float) == False:
                error.throw(value, "Distance must an integer or float")
            return
        if str(typeVar) == "cm":
            if error.typeCheck(value, int and float) == False or value <= 0:
                error.throw(value, "Cm must be an integer greater than 0")


def resetYawAngle():
    hub.motion_sensor.reset_yaw_angle()


def resetMotors():
    rightMotor.set_degrees_counted(0)
    leftMotor.set_degrees_counted(0)
    arm.set_degrees_counted(0)


def clear():
    if platform == "linux" or "darwin":
        os.sytem("clear")
    else:
        os.system("cls")

def waitLight(time : int, i : int, step : int, on : bool):
    timer.reset()
    
    if on == False:
        while timer.now() < time:
            hub.light_matrix.show_image("SQUARE_SMALL", brightness = i)
            i -= step
    if on == True:
        while timer.now() < time:
            hub.light_matrix.show_image("SQUARE_SMALL", brightness = i)
            i += step
            
def count(time : int):
    resetMotors()
    timer.reset()

    while timer.now() < time:
        print("Left Motor: " + str(leftMotor.get_degrees_counted()) + " | Right Motor: " + str(rightMotor.get_degrees_counted()) + " | Arm: " + str(arm.get_degrees_counted()) + " | Left Colour Sensor: " + str(colourL.get_color())) + " | Right Colour Sensor: " + str(colourR.get_color())
    clear()


def motion():
    yaw = hub.motion_sensor.get_yaw_angle()
    roll = hub.motion_sensor.get_roll_angle()
    pitch = hub.motion_sensor.get_pitch_angle()

    print("Yaw: " + str(yaw) + " | Pitch: " + str(pitch) + " | Roll: " + str(roll))


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

    remainder = None

    if type(aggressive) != bool:
        error.throw(aggressive, "Aggressive mode must be a boolien")

    resetMotors()
    resetYawAngle()

    if aggressive == True:
        turnSpeed = 100
    else:
        turnSpeed = 45

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

    var = 45 

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
    if direction == "none" :
        pass
        
def executeMission(missionId : int):
    if missionId == 0:
        pass

def missionSelector():
    missionId = 0
    maxMissions = 3
    turn = 10

    exit = False

    while True:
        resetMotors()
        if hub.right_button.was_pressed():
            if missionId >= maxMissions:
                if missionId == maxMissions + 1:
                    pass
                else:
                    missionId += 1
                exit = True
            else:
                exit = False
                missionId += 1
        if hub.left_button.was_pressed():
            if missionId != 0:
                missionId -= 1
                exit = False
        if abs(rightMotor.get_degrees_counted()) >= turn:
            if exit == True and missionId >= maxMissions:
                clear()
                waitLight(1.5, 1, 100, False)
                raise SystemExit("Exiting...")
            else:
                executeMission(missionId)
        if exit == True:
            hub.light_matrix.show_image("SQUARE_SMALL", brightness = 100)
        else:
            hub.light_matrix.write(str(missionId))    
        hub.status_light.on("blue")

# Begin mission execution.
missionSelector()