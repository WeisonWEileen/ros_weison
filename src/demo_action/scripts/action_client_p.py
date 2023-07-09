#!/usr/bin/env python
import rospy
import actionlib
from demo_action.msg import *
import argparse



def done_cb(status, result):
    if status == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("Succeeded with result: %d", result.result) 
    else:
        rospy.loginfo("Failed with status")

def active_cb():
    rospy.loginfo("the connection has been accepted by the action server")

def feedback_cb(feedback):
    rospy.loginfo("Feedback received: %f", feedback.progress_bar)

def argumentParser(argument_):
    parser = argparse.ArgumentParser(description="Input an integer")
    parser.add_argument("integer", type=int, help="Input an integer")
    args = parser.parse_args(argument_)
    return args


if __name__ == "__main__":
    rospy.init_node("action_client_p")
    client = actionlib.SimpleActionClient("addInts", AddIntsAction)
    client.wait_for_server()
    goal_obj = AddIntsGoal()
    args = argumentParser(None)
    goal_obj.num = args.integer
    client.send_goal(goal_obj,done_cb,active_cb,feedback_cb)
    rospy.spin()

