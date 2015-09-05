# zoom
The Zoom engine. A simple yet powerful game engine designed to teach kids how to program computers.

Zoom is a simple game engine inspired in the hobby 8-bit computers of the early days (my personal experience comes from programming a MSX 1.1). Zoom runs on Python and allows a very tight feedback loop between writing code and seeing the results on the screen. Zoom's API is small and easy to learn and use, still, it is powerful enough to render intricate 2D games. The runtime works within Python's interactive prompt for easy experimentation. It has the six subsytesms required to build a complete game: screen, resources, audio, input, collision and timer.

## Typical game loop:

```
  from zoom import *
  doublebuffer()
  init(50, 50)
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
