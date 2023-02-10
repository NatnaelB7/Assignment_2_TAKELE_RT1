# Assignment 2 - Two Wheeled Mobile Robot
This is a simple, two-wheeled robot that is coded and developed by *Natnael Berhanu Takele*.

## Assignment Description
The two-wheeled mobile robot that will be used in this assignment moves in three dimensions by avoiding obstacles in order to reach the target position. A 3D simulation environment called Gazebo allows the user to operate the robot.

The implementation of an action server that moves a two-wheeled mobile robot in the given environment uses the concept of the bug0 algorithm.

Bug0 Algorithm:
- head toward goal
- follow obstacles until you can head toward the goal again
- continue

The created package should contain three different nodes:
1. Node a: A node that implements an action client, allowing the user to set a target (x, y) or to cancel it. The node also publishes the robot position and velocity as a custom message (x,y, vel_x, vel_z), by relying on the values published on the topic /odom.
2. Nobe b: A service node that, when called, prints the number of goals reached and cancelled.
3. A node that subscribes to the robot’s position and velocity (using the custom message) and prints the distance of the robot from the target and the robot’s average speed.
