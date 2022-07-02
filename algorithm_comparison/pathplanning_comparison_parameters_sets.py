""" Sets of parameters to test for each pathplanning algorithm.

    forward_straight_speed: speed of the drone when moving straight forward
                            (in length units per second)
    forward_rotation_speed: speed of the drone when moving foward during a turn
                            (in length units per second)
    rotation_speed: speed of the drone's rotation (in degrees per second)
"""

parameters_set = [
    {
        'forward_straight_speed': 2,
        'forward_rotation_speed': 1,
        'rotation_speed': 0.01111,
    },
    {
        'forward_straight_speed': 3,
        'forward_rotation_speed': 1,
        'rotation_speed': 0.02222,
    },
]