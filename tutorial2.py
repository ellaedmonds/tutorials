from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
mycircle = CircleAsset(5, thinline, blue)
xcoordinates = range(100, 300, 10)

# Generate a list of sprites that form a line!
sprites = [Sprite(mycircle, (x, x*2.0 + 50)) for x in xcoordinates]

myapp = App()
myapp.run()
