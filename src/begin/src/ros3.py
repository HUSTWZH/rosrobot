#!/usr/bin/env python3
# license removed for brevity
import rospy
from urdf_parser_py.urdf import URDF
print('xxx')
robot = URDF.from_xml_file("/media/dubing/DATA/test/src/begin/src/solidsinglearm.urdf")
print(robot)
