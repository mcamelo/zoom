# zoom
The Zoom engine. A simple yet powerful game engine designed to teach kids how to program computers.

Zoom is a simple game engine inspired in the hobby 8-bit computers of the early days (my personal experience comes from programming a MSX 1.1). Zoom runs on Python and allows a very tight loop feedback between writing code and seeing the results on the screen. Zoom's API is small and easy to learn and use, still, it is powerful enough to render intricate 2D games. The runtime works within Python's interactive prompt for easy experimentation. It has six subsytesms: screen, resources, audio, input, collision and timer.

## Typical game loop:

```
  from zoom import *
  while run():
    while timer = gettimer():
      # process timer
    while collision = getcollision()
      # process collision
    while key = getkey():
      # process key
    # draw
    show()
```
