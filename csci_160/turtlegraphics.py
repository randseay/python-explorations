"""
turtlegraphics.py

This module supports simple Turtle Graphics.  The Turtle class represents
a turtle object in a graphics window.  To instantiate a turtle, enter

turtle = Turtle()                   # Default window size 200 x 200

or 

turtle = Turtle(width = 500, height = 500)  # Window size 500 x 500

The turtle's home position is (0,0), initial color is blue, initial
width is 2 pixels, and initial direction is north (90 degrees).

Turtle methods:

home()                Returns turtle to initial position and direction 
up()                  Lifts turtle above drawing area
down()                Lowers turtle to drawing area
move(aDistance)       Moves turtle aDistance in current direction
move(xPos, yPos)      Moves to position (xPos, yPos)
turn(degrees)         + degrees is counterclockwise, - degrees is clockwise
setDirection(degrees) Changes turtle's direction
setWidth(width)       Changes turtle's pen width in pixels
setColor(r, g, b)     Changes tutle's color to RGB value
isDown() -> aBoolean  True if turtle can draw, False otherwise
getWidth() -> anInt   The width of tutle's drawing window
getHeight() -> anInt  The heignt of tutle's drawing window

LICENSE: This is open-source software released under the terms of the
GPL (http://www.gnu.org/licenses/gpl.html).  It is based in part on 
John Zelle's open source graphics module.

PLATFORMS: The package is a wrapper around Tkinter and should run on
any platform where Tkinter is available.

INSTALLATION: Put this file somewhere where Python can see it.

"""
import Tkinter
import math
import os, sys, time
tk = Tkinter

##########################################################################
# Module Exceptions

import exceptions

class TurtleError(exceptions.Exception):
    """Generic error class for turtlegraphics module exceptions."""
    def __init__(self, args=None):
        self.args=args

DEAD_THREAD = "Turtle Graphics thread quit unexpectedly"

###########################################################################
# Support to run Tk in a separate thread

from Queue import Queue
import thread
import atexit

_tk_request = Queue(0)
_tk_result = Queue(1)
_POLL_INTERVAL = 10

_root = None
_thread_running = True
_exception_info = None

def _tk_thread():
    global _root
    _root = tk.Tk()
    _root.withdraw()
    _root.after(_POLL_INTERVAL, _tk_pump)
    _root.mainloop()

def _tk_pump():
    global _thread_running
    while not _tk_request.empty():
        command,returns_value = _tk_request.get()
        try:
            result = command()
            if returns_value:
                _tk_result.put(result)
        except:
            _thread_running = False
            if returns_value:
                _tk_result.put(None) # release client
            raise # re-raise the exception -- kills the thread
    if _thread_running:
        _root.after(_POLL_INTERVAL, _tk_pump)

def _tkCall(f, *args, **kw):
    # execute synchronous call to f in the Tk thread
    # this function should be used when a return value from
    #   f is required or when synchronizing the threads.
    # call to _tkCall in Tk thread == DEADLOCK !
    if not _thread_running:
        raise TurtleError, DEAD_THREAD
    def func():
        return f(*args, **kw)
    _tk_request.put((func,True),True)
    result = _tk_result.get(True)
    return result

def _tkExec(f, *args, **kw):
    # schedule f to execute in the Tk thread. This function does
    #   not wait for f to actually be executed.
    if not _thread_running:
        raise TurtleError, DEAD_THREAD
    def func():
        return f(*args, **kw)
    _tk_request.put((func,False),True)

def _tkShutdown():
    # shutdown the tk thread
    global _thread_running
    _thread_running = False
    time.sleep(.5) # give tk thread time to quit

# Fire up the separate Tk thread
thread.start_new_thread(_tk_thread,())

# Kill the tk thread at exit
atexit.register(_tkShutdown)

class Turtle(tk.Canvas):
    def __init__(self, width=200, height=200):
        _tkCall(self.__init_aux, "Turtle Graphics", width, height)

    
    def __init_aux(self, title, width, height):
        master = tk.Toplevel(_root)
        master.protocol("WM_DELETE_WINDOW", self.__close_aux)
        tk.Canvas.__init__(self, master,
                           width=width, height=height)
        self.master.title(title)
        self.pack()
        master.resizable(0, 0)
        self.foreground = "blue"
        self.color = "blue"
        self.lineWidth = 2
        self._isDown = True
        self.home()
        self.items = []
        self.height = height
        self.width = width
        self.autoflush = False
        self.closed = False
        if self.autoflush: _root.update()

    def close(self):
        if self.closed: return
        _tkCall(self.__close_aux)

    def __close_aux(self):
        """Close the window"""
        self.closed = True
        self.master.destroy()
        _root.update()

    def isClosed(self):
        return self.closed

    def __autoflush(self):
        if self.autoflush:
            _tkCall(_root.update)

    def flush(self):
        """Update drawing to the window"""
        _tkCall(self.update_idletasks)

    def getHeight(self):
        """Return the height of the drawing area"""
        return self.height - 8

    def getWidth(self):
        """Return the width of the drawing area"""
        return self.width - 8

    def home(self):
        self.xPos = 0
        self.yPos = 0
        self.direction = 90.0

    def down(self):
        self._isDown = True

    def up(self):
        self._isDown = False

    def move(self, x, y = None):
        """
        If one argument exists, use it as a distance
        Otherwise, use the two arguments as a position
        """
        if self.closed:
            raise TurtleError, "window is closed"
        if y != None:
            self.turn(x, y)
            self.drawLine(x, y)
        else:
            self.drawLine(self.xDestination(x), self.yDestination(x))

    def isDown(self):
        return self._isDown

    def setColor(self, c, g = None, b = None):
        """Expects a single string or three ints as args."""
        if g == None:
            self.color = c
        else:
            self.color = self.color_rgb(c, g, b)

    def color_rgb(self, r,g,b):
        """r,g,b are intensities of red, green, and blue in range(256)
        Returns color specifier string for the resulting color"""
        return "#%02x%02x%02x" % (r, g, b)

    def setDirection(self, d):
        self.direction = d % 360

    def setWidth(self, w):
        self.lineWidth = w

    def turn(self, x, y = None):
        """
        If y is None, view x as degrees to turn,
        otherwise, view x and y as factors to compute a direction
        for moving a distance.
        """
        if y == None:
            self.direction = (self.direction + x) % 360.0
        elif self.xPos == x and self.yPos == y:
            return
        else:
            deltaX = x - self.xPos
            deltaY = y - self.yPos
            distance = math.sqrt(deltaX * deltaX + deltaY * deltaY)
            self.direction = math.degrees(math.asin(abs(deltaY) / distance))
            if deltaY < 0:
                self.direction = - self.direction
            if deltaX < 0:
                self.direction = 180.0 - self.direction

    def xDestination(self, distance):
        return self.xPos + distance * math.cos(math.radians(self.direction))

    def yDestination(self, distance):
        return self.yPos + distance * math.sin(math.radians(self.direction))

    def __str__(self):
        return "Position: ("  + str(self.xPos) + ", " + str(self.yPos) + \
               ")\nDirection: " + str(self.direction) + \
              "\nColor: " + self.color + \
               "\nLine Width: " + str(self.lineWidth) + \
               "\nIs Down: "   + str(self.isDown())
 
    def drawLine(self, x, y):
        if self.isDown():
            _tkExec(self.create_line,
                    self.adjustX(self.xPos, self.width),
                    self.adjustY(self.yPos, self.height),
                    self.adjustX(x, self.width),
                    self.adjustY(y, self.height),
                    fill = self.color,
                    width = self.lineWidth)
        self.xPos = x
        self.yPos = y

    def adjustX(self, x, width):
        return int(round(x + width / 2.0))

    def adjustY(self, y, height):
        return int(round(height / 2.0 - y))    


  

   
