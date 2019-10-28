import socket
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

def recieve_vars(host):
    s = socket.socket()
    host = str(host)
    port = 8080
    s.connect((host,port))

    file = open('/home/pi/python3d_game_dev/vars.info', 'wb')
    file_data = s.recv(1024)
    file.write(file_data)
    file.close

def draw():
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
        
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.K_ESC:
                pygame.quit()
                quit()

        recieve_vars('raspberrypi')
        
        read = open('/home/pi/python3d_game_dev/vars.info','r')

        readline = read.readline()
        x = float(readline)
        readline = read.readline()
        y = float(readline)
        readline = read.readline()
        z = float(readline)
        readline = read.readline()
        angle = float(readline)
        readline = read.readline()
        tx = float(readline)
        readline = read.readline()
        ty = float(readline)
        readline = read.readline()
        tz = float(readline)

        read.close
        
        glTranslate(x, y, z)
        glRotatef(angle, tx, ty, tz)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)

main()
