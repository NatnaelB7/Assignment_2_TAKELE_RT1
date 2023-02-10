# Assignment 2: Two-Wheeled Mobile Robot
This is a simple, two-wheeled robot that is coded and developed by *Natnael Berhanu Takele*.

## Assignment Description
The two-wheeled mobile robot that will be used in this assignment moves in three dimensions by avoiding obstacles in order to reach the target position. A 3D simulation environment called *Gazebo* allows the user to operate the robot.

The implementation of an action server that moves a two-wheeled mobile robot in the given environment uses the concept of the *bug0 algorithm*.

Bug0 Algorithm:
- head toward goal
- follow obstacles until you can head toward the goal again
- continue

The created package should contain three different nodes:
1. Node a: A node that implements an action client, allowing the user to set a target (x, y) or to cancel it. The node also publishes the robot position and velocity as a custom message (x,y, vel_x, vel_z), by relying on the values published on the topic /odom.
2. Nobe b: A service node that, when called, prints the number of goals reached and cancelled.
3. A node that subscribes to the robot’s position and velocity (using the custom message) and prints the distance of the robot from the target and the robot’s average speed.

Additionally, create a launch file to start the whole simulation.

## The Created Nodes
*Nodes* are processes that perform some computation or task. It is a simple program that publishes or subscribes to a topic or contains a program that enables a ROS service. It should be highly specialized and accomplish a single task. Nodes communicate with other nodes by sending messages. As it is clearly seen, we have six Python files in our package. It is basically our node. 

1. **bug_as.py** - in order to move the robot to the designated place, the action server node known as *bug_as.py* must first receive the intended position from the client.
2. **go_to_point_service.py** - this ROS node in Python implements a navigation algorithm that directs a robot to the designated location. Moreover, it is a python script file that implements a service node.
3. **wall_follow_service.py** -  A service node is implemented in this Python script file. This node can be invoked to enable the robot to maneuver around obstacles. The robot navigates by determining the distance to walls to its left, right, and front using laser scan data.
4. **node_a_action_client.py** - It is another python script file that deals with asking the user to enter the coordinates (x, y) or cancel them that the robot has to reach. It creates a publisher "pub" that publishes a custom message *"Posxy_velxy"* on the topic *"/posxy_velxy"*. The custom message contains four fields *"msg_pos_x"*, *"msg_pos_y"*, *"msg_vel_x"*, *"msg_vel_y"* that represent the position and velocity of the robot.

### Pseudocodes
The **pseudocodes** for this node is provided over here for an overview of the program.

    Initialize the node
    Create publisher and subscriber

    Define publisher callback function:
        Extract position and velocity data from odometry message
        Create custom message with the data
        Publish the custom message

    Define action client function:
        Create action client and connect to action server
        Loop:
            Wait for user input
            If input is "c":
                Cancel goal
            Else:
                Convert input to goal message
                Send goal to the action server

    Call action client function






