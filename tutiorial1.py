from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, .7)
green = Color(0x00ff00, .7)
blue = Color(0x0000ff, .7)
black = Color(0x000000, .7)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
ellipse = EllipseAsset(50, 20, thinline, blue)

# Now display a rectangle
Sprite(ellipse, (10,40))


# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
Polygon = PolygonAsset([(5, 30), (0,60), (45,70),(40,65)], thinline, red)

# Now display a rectangle
Sprite(polygon, (10,40))


myapp = App()
myapp.run()
