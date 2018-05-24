#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('begin', anonymous=True)
    r = rospy.Rate(10) #10hz
    msg = JointState()

    msg.name = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6', 'joint7']
    msg.velocity = [1, 1, 1, 1, 1, 1, 1]
    msg.position = [1, 1, 1, 1, 1, 1, 1]

    while not rospy.is_shutdown():
        msg.header.stamp = rospy.Time.now()
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
