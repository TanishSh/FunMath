import arcade
from config import*

class Rectangle:
    def __init__(self, position_x, position_y, width, height, color):
        self. position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)

class FunMath(arcade.Window):
    # Main application class
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        # create rectangle (selection box)
        self.rect = Rectangle(1010, 330, 145, 65, arcade.color.WHITE_SMOKE)

    def on_draw(self):
        # renders the screen
        arcade.start_render()
        # ----- Drawing Commands ---------
        arcade.draw_text("How Many Groups", intro_text_start_x, intro_text_start_y, arcade.color.BLACK, 55, font_name = comic_sans)
        self.rect.draw()

    def on_mouse_motion(self, x, y, dx, dy):

        if( (rect_lower__x < x < rect_upper_x) and (rect_lower__y < y < rect_upper_y) ):
            self.rect.color = arcade.color.LIGHT_GREY
        else:
            self.rect.color = arcade.color.WHITE_SMOKE


def main():
    FunMath(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()