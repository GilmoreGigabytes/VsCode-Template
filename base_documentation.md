
# The Error class

<br>

## typeCheck
Takes a value and a type and checks if that value has that type

- value: variable
- givenType: type -> int, str, bool etc ...

<br>

## throw
Takes a value and will raise a value error formatted with the variable that was passed as an argument

- value: variable -> any
- text: str

<br>

## template
Takes a value and a type relating to movement function arguments

- value: variable -> any
- type: string -> "sensor", "speed", "direction", "distance" or "cm"

<br>

# Ease of use functions

<br>

## resetYawAngle
Resets the yaw angle

- takes no arguments

<br>

## resetMotors
Resets motors so that movement functions can be more accurate.

- takes no arguments

<br>

## clear
Uses the os module to clear the console/terminal.

- takes no arguments

<br>

## count
Takes an integer (time) and while print the motor and colour info for the given time.

- time: int -> >0

<br>

## motion
Will print a formated string with the current yaw, roll and pitch of the spike prime once. It is intended to be used in mission 0 of the mission selector so you can easily check if the gyro is working.

- takes no arguments

<br>

# Movement Functions

<br>

## move
Takes two integers (distance and speed), as well as a string (direction). Speed has a default value of the global variable default speed, and distance must be greater than 0. Direction muste be a string with the value of "forward" or "backward".

- distance: int -> > 0
- speed: int -> > 0
- direction: str -> "left" or "right"

<br>

## moveWithCorrection
Takes a value (cm) that can be either a float or int > 0, and moves forward with correction using the gyro at a set speed as to stop inconcistencies.

- cm: float, int -> > 0

<br>

## turn
Takes an int (deg), string (direction), bool (aggrssive).
This function needs some logical explintaion. If aggressive is true it will turn much faster but will be slightly less accurate. It then will check if the given degrees is < 90. This is because the gyro works by going from 0 ~ 180 ~ -180 ~ 0, meaning that you can't just do a simple while loop. If the degrees is < 90 then it will just turn the given direction for the given degrees. If it is > 90 it will run through a while loop where it will increment a value times and take 45 from deg until it is < 90. Now it will check the remainding degrees to see if it is > 45, if is it will set a variable remainder to the value of deg - 45 (the actual remainder) and take 1 from the times variable. Now it will turn the given direction for the given times. After that it will check if the remainder variable has a type, and if it does it means that it does have remainding degrees and will turn for that remainder. And if it dosent have a value it means that there is no remainding distance to turn and will end the function.


- deg: int -> > 0
- direction: str -> "left", "right"
- aggressive: bool

<br>

## followLine
Takes a str (sensor) and an int or float (cm/distance), note that it splits the distance into degrees making the actual line following very easy. This line follower has been specifically tuned for our spike design so you may need to spend a bit of time adjusting some of the values for yours. You should note that the deg of our motors is being piped through the abs function. This just removes the issue of our motors being on opposite sides.

- sensor: str -> "left" or "right"
- cm: int, float -> > 0

<br>

## moveArm
Takes a string (direction) and int (speed), float or int (distance). Because our spike design uses a scissor lift design we we use fractions to represent our distance but in an integer can used.

- direction: str -> "up", "down"
- speed: int -> > 0
- distance: int > 0

<br>

## moveToLine
Takes two strings (sensor, direction) and will just drive the given direction until the given sensor detects black

- sensor: str -> "right", "left"
- direction: str -> "forward", "backward"

<br>

# Mission

<br>

## start
Takes as string (direction) You need to write your own way of going to the lines based off of the year

- direction: str -> None

<br>

## executeMission
Takes an int (missionId) and uses match case to run the corresponding mission

- missionId: int -> > 0