#!/usr/bin/env python

import rospy 
from std_msgs.msg import String 

def callback_(msg):
    print (msg)


if __name__ == "__main__":

    rospy.init_node("python_node")
    rospy.Subscriber('/hello_node', String, callback_)
    rospy.spin()

     