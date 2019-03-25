from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 30)
    gluLookAt(8, 9, 10,
              0, 0, 0,
              0, 1, 0)

    glClearColor(0, 1, 0, 1)


angle = 0
x = 0
forward = True


def draw():
    global angle
    global x
    global forward

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_QUADS)
    glColor3f(0, 1, 1)
    glVertex(-20, 0, 0)
    glVertex(10, 0, 0)
    glVertex(10, 10, 0)
    glVertex(-20, 10, 0)
    glColor3f(0, 1, 0)
    glVertex(-20, 0, 0)
    glVertex(10, 0, 0)
    glVertex(10, 4, 0)
    glVertex(-20, 4, 0)
    glColor3f(0.7, 0.7, 0.7)  # The Lane
    glVertex(10, 0, -2)
    glVertex(-25, 0, -2)
    glVertex(-20, 0, 2.5)
    glVertex(10, 0, 2.5)
    glColor3f(1, 1, 1)
    for i in range(-40, 20, 10):
        glVertex(i, 0, 0)
        glVertex(i, 0, 1)
        glVertex(i+5, 0, 1)
        glVertex(i+5, 0, 0)

    glEnd()

    glColor3f(0, 0, 0)    #The Wheels
    glLoadIdentity()
    glTranslate(x + 0.5 * 5, -0.5 * 0.25 * 5, 0.5 * 0.5 * 5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x + 0.5 * 5, -0.5 * 0.25 * 5, - 0.5 * 0.5 * 5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x - 0.5 * 5, -0.5 * 0.25 * 5, -0.5 * 0.5 * 5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x - 0.5 * 5, -0.5 * 0.25 * 5, 0.5 * 0.5 * 5)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()    #The Car Body
    glColor3f(1, 0, 0)  #Lower body
    glTranslate(x, 0, 0)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0, 1, 1)  #Upper Body
    glTranslate(x, 5*0.25, 0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()  # The Lights
    glColor3f(1, 1, 0)
    glTranslate(x + 2.5, 0, 1)
    glutSolidSphere(0.15, 100, 100)

    glLoadIdentity()
    glTranslate(x + 2.5, 0, -1)
    glutSolidSphere(0.15, 100, 100)

    glutSwapBuffers()

    if forward:
        angle -= 1
        x += 0.05
        if x > 5:
            forward = False
    else:
        angle += 1
        x -= 0.05
        if x < -10:
            forward = True


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
