import unittest
from weakref import proxy

from rover import Rover
from kata import Proxy

"""
Mars rover moves through


                       N
        --------------------------------
        |   0,2   |   1,2   |   2,2    |
        -------------------------------- 
    W   |   0,1   |   1,1   |   2,1    |    E
        -------------------------------- 
        |   0,0   |   1,0   |   2,0    |
        --------------------------------
                       S
                   
"""


class MarsRoverTestCase(unittest.TestCase):
    def test_rover_move_forward(self):
        rover = Rover(
            start_x=1,
            start_y=1,
            orientation='N'
        )

        proxy = Proxy(rover, 3, 3)
        movements = ['f']


        expected_position = (1, 2)
        proxy.move(movements)

        self.assert_rover_position(expected_position, rover)

    def assert_rover_position(self, expected_position, rover):
        self.assertEqual(expected_position[0], rover.x)
        self.assertEqual(expected_position[1], rover.y)
