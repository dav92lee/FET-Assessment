import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os
import pygame
import sys
import time

import config
from obj_loader import *


def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)


def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1

    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def DrawGLScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslate(obj.trs[0] / 20., obj.trs[1] / 20., obj.trs[2])
    glRotate(obj.rot[0], 1, 0, 0 )
    glRotate(obj.rot[1], 0, 1, 0)
    glRotate(obj.rot[2], 0, 0, 1)
    glCallList(obj.gl_list)
    glutSwapBuffers()


def keyPressed(*args):
    key = args[0]
    if key == '\033': #escape
        glutDestroyWindow(window)
        sys.exit()
    elif key == 'q':
        obj.rot[0] -= 15
        DrawGLScene()
    elif key == 'w':
        obj.rot[0] += 15
        DrawGLScene()
    elif key == 'a':
        obj.rot[1] -= 15
        DrawGLScene()
    elif key == 's':
        obj.rot[1] += 15
        DrawGLScene()
    elif key == 'z':
        obj.rot[2] -= 15
        DrawGLScene()
    elif key == 'x':
        obj.rot[2] += 15
        DrawGLScene()
    elif key == 'p':
        print 'current orientation'
        print 'rotation: (' + ','.join(str(i) for i in obj.rot) + ')'
        print 'translation: (' + ','.join(str(i) for i in obj.trs) + ')'
    elif key == 'i':
        obj.rot[1] = 90
        DrawGLScene()


def main():
    global window
    global obj

    config.win_h = 440
    config.win_w = 660

    glutInit("")
    glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(config.win_w, config.win_h)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Project Indra")
    glutDisplayFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(config.win_w, config.win_h)
    obj = OBJ(sys.argv[1])

    # Start Event Processing Engine
    glutMainLoop()

if __name__ == "__main__":
    main()
