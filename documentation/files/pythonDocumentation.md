
<h1 align="center">Documentation <h3>

<br>

# Clear
Uses the os module to clear the console/terminal.

- takes no arguments

---

<br>

# Count
Takes an integer (time) and while print the motor and colour info for the given time.

- time: int -> >0

---
<br>

# Motion
Will print a formated string with the current yaw, roll and pitch of the spike prime once. It is intended to be used in mission 0 of the mission selector so you can easily check if the gyro is working.

- takes no arguments

---

<h1 align="center">Movement Functions <h1>

<br>

# Move
Will move your spike prime forward or backward using motor degrees.

- distance: int -> > 0
- speed: int -> > 0
- direction: str -> "left" or "right"

---
<br>

# MoveWithCorrection
Moves forward with correction using the gyro at a set speed as to stop inconcistencies.

- cm: float, int -> > 0

---
<br>

# Turn
This function needs alot more explintaion. If aggressive is true it will turn much faster but will be slightly less accurate. It then will check if the given degrees is < 90. This is because the gyro works by going from 0 ~ 180 ~ -180 ~ 0, meaning that you can't just do a simple while loop. If the degrees is < 90 then it will just turn the given direction for the given degrees. If it is > 90 it will run through a while loop where it will increment a value (times) and take 45 from deg until it is < 90. Now it will check the remainding degrees to see if it is > 45, if is it will set a variable remainder to the value of deg - 45 (the actual remainder) and take 1 from the times variable. Now it will turn the given direction for the given times. After that it will check if the remainder variable has a type, and if it does it means that it does have remainding degrees and will turn for that remainder. And if it dosent have a value it means that there is no remainding distance to turn and will end the function.


- deg: int -> > 0
- direction: str -> "left", "right"
- aggressive: bool

---
<br>

# FollowLine
Using pid it will follow the ege of a black line. Note that it splits the distance into degrees making the actual line following very easy. This line follower has been specifically tuned for our spike design so you may need to spend a bit of time adjusting some of the values for yours. You should note that the deg of our motors is being piped through the abs function. This just removes the issue of our motors being on opposite sides.

- sensor: str -> "left" or "right"
- cm: int, float -> > 0
---
<br>

# MoveArm
Because our spike design uses a scissor lift design we we use fractions to represent our distance but in an integer can used.

- direction: str -> "up", "down"
- speed: int -> > 0
- distance: int > 0

---
<br>

# MoveToLine
Will just drive the given direction until the given sensor detects black.

- sensor: str -> "right", "left"
- direction: str -> "forward", "backward"

<br>

---
<h1 align="center">Mission Functions <h3>

<br>

# Start
You need to write your own way of going to the lines based off of the your spike prime design.

- direction: str -> None

---
<br>

# ExecuteMission
Uses match case to run the corresponding mission using an argument passed from the mission selector.

- missionId: int -> > 0

<br>

---
<h1 align="center">Error Class <h3>
<br>

# TypeCheck
Takes a value and a type and checks if that value has that type

- value: variable
- givenType: type -> int, str, bool etc ...

<br>

# Throw
Takes a value and will raise a value error formatted with the variable that was passed as an argument

- value: variable -> any
- text: str

<br>

# Template
Takes a value and a type relating to movement function arguments

- value: variable -> any
- type: string -> "sensor", "speed", "direction", "distance" or "cm"

---
<br>

<h1 align="center">Vscode<h3>

# Errors

If you get an error relating to motors you most likely have not setup the motor ports properly, or those motors are broken. 

If you try and run the code using vscodes builtin python compiler you will get an error.
This is because vscode does not have the spike modules installed.
If you want to run your code look at read the README.

