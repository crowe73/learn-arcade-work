"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the Arcade library.
import arcade

# Open up a window and set window size.
arcade.open_window(600, 600, "Drawing Example")

# Set the background color.
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw.
arcade.start_render()

# Draw a rectangle.
arcade.draw_lrbt_rectangle_filled(0, 599, 0, 300, arcade.csscolor.GREEN)

# Tree trunk.
arcade.draw_rect_filled(arcade.rect.XYWH(100, 320, 20, 60), arcade.csscolor.SIENNA)

# Tree top.
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# Another tree with a trunk and ellipse for top.
arcade.draw_rect_filled(arcade.rect.XYWH(200, 320, 20, 60), arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# Another tree with a trunk and arc for top.
arcade.draw_rect_filled(arcade.rect.XYWH(300, 320, 20, 60), arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Another tree with a trunk and a triangle for top.
arcade.draw_rect_filled(arcade.rect.XYWH(400, 320, 20, 60), arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430,320, arcade.csscolor.DARK_GREEN)

# Draw a tree using a polygon.
arcade.draw_rect_filled(arcade.rect.XYWH(500, 320, 20, 60), arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                                    (480, 360),
                                    (470, 320),
                                    (530, 320),
                                    (520, 360)
                                    ),
                                    arcade.csscolor.DARK_GREEN)

# Draw a sun.
arcade.draw_circle_filled(500, 550, 40, arcade.csscolor.YELLOW)
# Rays left, right, up, and down.
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
#Diagonal rays.
arcade.draw_line(500, 550, 650, 700, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 400, 650, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)

# Draw text at (150, 230) with a font size of 24 pts.

arcade.draw_text("Arbor Day - Plant a Tree!",
                 150, 230,
                 arcade.color.BLACK, 24)

# Finish drawing.
arcade.finish_render()

# Keep the window open until user closes it.
arcade.run()
