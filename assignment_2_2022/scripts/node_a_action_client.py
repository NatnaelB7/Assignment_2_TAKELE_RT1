#!/usr/bin/env python

# Import Libraries
import rospy
import actionlib
import actionlib.msg
import assignment_2_2022.msg
from std_srvs.srv import *
import sys
import select
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Twist
from assignment_2_2022.msg import Posxy_velxy
from colorama import Fore, Style
from colorama import init
init()

def publisher(msg):                           # Subscriber's callback function
    global pub
    posi = msg.pose.pose.position             # get the position information from the msg
    velo = msg.twist.twist.linear             # get the velocity information from the msg
    posxy_velxy = Posxy_velxy()               # create custom message
    
    # set the custom message's parameters
    
    posxy_velxy.msg_pos_x = posi.x
    posxy_velxy.msg_pos_y = posi.y
    posxy_velxy.msg_vel_x = velo.x
    posxy_velxy.msg_vel_y = velo.y
    pub.publish(posxy_velxy)                  # publish the custom message
    
def action_client():
    # create the action client
    action_client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2022.msg.PlanningAction)
    action_client.wait_for_server()           # wait for the server to be started
    status_goal = False

    while not rospy.is_shutdown():
        # Ready the computer keyboard inputs
        print(Fore.WHITE + "Please input the target's position or type C to cancel it ")
        
        # print(Fore.BLUE + "Ideal X Position: ")
        x_posi_input = input(Fore.BLUE + "Ideal X Position: ")
        
        # print(Fore.BLUE + "Ideal Y Position: ")
        y_posi_input = input(Fore.BLUE + "Ideal Y Position: ")
        
 	# If user entered 'c' and the two-wheeled robot is reaching the goal position, just cancel the goal
        if x_posi_input == "c" or y_posi_input == "c":      
            action_client.cancel_goal()      # cancel the goal
            status_goal = False
        else:
            # Convert the data type of the numbers from string to float
            x_posi_conv = float(x_posi_input)
            y_posi_conv = float(y_posi_input)
            
            # Let's create the goal to send to the server
            goal = assignment_2_2022.msg.PlanningGoal()
            goal.target_pose.pose.position.x = x_posi_conv
            goal.target_pose.pose.position.y = y_posi_conv
            action_client.send_goal(goal)                      # send the goal to the action server
            status_goal = True

def main():
    rospy.init_node('node_a_action_client')                    # initialize the node
    global pub                                                 # global publisher
    # publisher: sends a message which contains two parameters (position and velocity) 
    pub = rospy.Publisher("/posxy_velxy", Posxy_velxy, queue_size = 1) 
    # subscriber: get from "Odom" two parameters (position and velocity) 
    sub_from_Odom = rospy.Subscriber("/odom", Odometry, publisher)  
    action_client()                                            # finally, call the function client

if __name__ == '__main__':
    main()
