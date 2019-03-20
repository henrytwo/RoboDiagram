import sys
import time
from networktables import NetworkTables
from pygame import *

# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)

ip = '10.49.3.2'

NetworkTables.initialize(server=ip)

table = NetworkTables.getTable("diagram")
screen = display.set_mode((800, 600))

i = 0

pytimer = time.Clock()

def drawRobot(screen, robotState):

    W = 400
    H = 400

    robo_surface = Surface((W, H))

    robo_surface.fill((250, 250, 250))

    # Frame
    draw.polygon(robo_surface, (0, 0, 255), [(W // 2, H - 100), (W // 2 - 100, H - 80), (W // 2 - 100, H - 50), (W // 2, H - 70), (W // 2 + 100, H - 50), (W // 2 + 100, H - 80)])

    # Elevator thing
    draw.rect(robo_surface, (0, 0, 0), (W // 2 + 50, H - 50, 10, 50))

    screen.blit(robo_surface, (screen.get_width() // 2 - robo_surface.get_width() // 2, screen.get_height() // 2 - robo_surface.get_height() // 2))

    pass

# Points
#
# Elevator
# Back Climb
# Front Climb
# Hook
# Tilt
# Ball Mech

while True:
    print('robotTime:', table.getNumber('robotTime', 'N/A'))

    robotState = {
        'elevator': table.getNumber('elevator', -1000),
        'backClimb': table.getNumber('backClimb', -1000),
        'frontClimb': table.getNumber('frontClimb', -1000),
        'hook': table.getNumber('hook', -1),
        'tilt': table.getNumber('tilt', -1),
        'cargo': table.getNumber('cargo', -1)
    }

    screen.fill((255, 255, 255))

    drawRobot(screen, robotState)

    display.flip()

    pytimer.tick(60)

