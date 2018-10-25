#!/usr/bin/env python

import rospy
from uav_abstraction_layer.msg import State

prev_state = State()
prev_state.as_int = -1

def state_callback(state):
    global prev_state
    if state == prev_state:
        return
    prev_state = state
    if state.as_int == State.UNINITIALIZED:
        state_as_string = "UNINITIALIZED"
    elif state.as_int == State.LANDED_DISARMED:
        state_as_string = "LANDED_DISARMED"
    elif state.as_int == State.LANDED_ARMED:
        state_as_string = "LANDED_ARMED"
    elif state.as_int == State.TAKING_OFF:
        state_as_string = "TAKING_OFF"
    elif state.as_int == State.FLYING_AUTO:
        state_as_string = "FLYING_AUTO"
    elif state.as_int == State.FLYING_MANUAL:
        state_as_string = "FLYING_MANUAL"
    elif state.as_int == State.LANDING:
        state_as_string = "LANDING"
    rospy.loginfo(state_as_string)

def main():
	# This node must be called inside ual namespace:
	#   - from console, e.g: rosrun uav_abstraction_layer state_monitor.py __ns:=uav_1 
	# 	- from a launch, e.g: node with ns="uav_1"
    rospy.init_node('state_monitor', anonymous=True)

    # TODO: Add a timeout watchog?
    rospy.Subscriber('ual/state', State, state_callback)
    rospy.spin()

if __name__ == '__main__':
    main()