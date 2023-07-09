#! /usr/bin/env python
import rospy
import actionlib
from demo_action.msg import *

class MyAction:
    def __init__(self):
        self.server = actionlib.SimpleActionServer("addInts", AddIntsAction, self.cb, False)
        self.server.start()
        rospy.loginfo("Action server started")

    def cb(self,goal):
        goal_num = goal.num
        rospy.loginfo("Goal received: %d", goal_num)
        rate = rospy.Rate(10)
        sum = 0
        for i in range(1, goal_num+1):
            sum += i
            ##seed feedback contiuously
            fb_obj = AddIntsFeedback()
            fb_obj.progress_bar = i/goal_num
            rospy.loginfo("Feedback sent: %f", fb_obj.progress_bar)
            self.server.publish_feedback(fb_obj)
            rate.sleep()

        result = AddIntsResult()
        result.result = sum
        self.server.set_succeeded(result)
        rospy.loginfo("Result sent: %d", result.result)

if __name__ == "__main__":

    rospy.init_node("action_server_p")
    
    myAction = MyAction()
   
   
   
   
   
    rospy.spin()
