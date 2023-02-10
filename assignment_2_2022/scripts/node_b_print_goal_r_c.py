#! /usr/bin/env python

# Import Libraries
import rospy 
from assignment_2_2022.srv import goal_rc, goal_rcResponse 
import actionlib   
import actionlib.msg  
import assignment_2_2022.msg  

class Service:
    def __init__(self):
        # Initialize the counters for reached and cancelled goals
        self.reached_goal = 0
        self.cancelled_goal = 0
        
        # Create the service
        self.srv = rospy.Service('node_b_print_goal_r_c', goal_rc, self.data) 
        
        # Subscribe to the result topic
        self.sub_result = rospy.Subscriber('/reaching_goal/result', assignment_2_2022.msg.PlanningActionResult, self.outcome_callback)
        
    def outcome_callback(self, msg):
        status = msg.status.status             # Obtain the result's status from the msg
        
        # Cancelled goal (status = 2)
        if status == 2:
            self.cancelled_goal += 1
        # Reached goal (status = 3)
        elif status == 3:
            self.reached_goal += 1
    def data(self, req):
        # Send back a message with the most recent values for the goals that were canceled and reached
        return goal_rcResponse(self.reached_goal, self.cancelled_goal)
        
def main():
    rospy.init_node('node_b_print_goal_r_c')          # Initialize the node
    node_b_print_goal_r_c = Service()                 # Create an instance of the Service class
    rospy.spin()                                      # Await messages
if __name__ == "__main__":
    main()
