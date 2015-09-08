################
# RUNTIME
################

def init(w,h):
  '''Initializes zoom, resizing the backbuffer to the given width and height.
  '''


def run():
  '''Returns true if game is running, false if game has ended.
  '''


def time():
  '''Returns the number of seconds between the beginning of the last frame and this. 
  '''

################
# Resources
################

def loadresources(filename):
  '''Load resources file to memory.
  '''


def getdata(name):
  '''Retrieves a data block by the given name.
  '''

################
# Screen
################

def doublebuffer():
  '''Toogles double buffer mode on and off (defaults to off). When not in double
  buffer mode, all drawing primitives are executed to the visible screen buffer
  for immediate viewing by the user. Ideal for experimenting within the Python
  interactive console.
  '''


def makesprite(data):
  '''Makes a sprite object out of the given data block.
  '''


def target(buffer):
  '''Sets the target buffer for drawing. By default, the target buffer
  is the backbuffer, but sprites are buffers and are valid targets too.
  '''


def clear():
  '''Clears the target buffer.
  '''


def point(x,y):
  '''Draws a point at the given x and y coordinates.
  '''


def line(x0, y0, x1, y1):
  '''Draws a line from x0, y0 to x1, y1.
  '''


def putsprite(sprite, x, y):
  '''Draws the sprite, putting the top-left corner at the given x and y
  coordinates.
  '''


def show():
  '''Shows the content of the backbuffer on the screen.
  '''

################
# Audio
################

class Clip:
  '''
  '''


def makeclip(data):
  '''Creates a playable audio clip from the given data block.
  '''


def playclip(clip):
  '''Plays the given clip once.
  '''

def loopclip(clip):
  '''Loop the given clip repeatedly.
  '''

################
# Input
################

class KeyEvent:
  '''
  '''
  def code():
  def down():
  def up():

def getkey():
  '''Gets a next key event in the queue.
  '''

################
# Collision
################

class CollisionEvent:
  def name1():
  def name2():

def makecollisionmask(data, name):
  '''Creates a collision mask from the given datablock. 
  '''


def putmask(mask, x, y):
  '''Positions the collision mask in the arena.
  '''


def getcollisions():
  '''Returns the next detected collision in the queue.
  '''

################
# Timer
################

class TimerEvent:
  def name():


def settimer(secs, name):
  '''Sets a new timer.
  '''


def gettimer():
  '''Returns the next timer event in the queue.
  '''
