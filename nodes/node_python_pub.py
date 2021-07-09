#! /usr/bin/env python

import rospy 
from std_msgs.msg import String


if __name__ == "__main__":

    rospy.init_node("node_publsihers")

    pub = rospy.Publisher("/hello_node", String, queue_size=10)

    rate = rospy.Rate(0.1)

    while not rospy.is_shutdown()  :
        try:
            data = String()
            data.data = "Hello from node"
            pub.publish(data)

            rate.sleep()

        except : 
            pass