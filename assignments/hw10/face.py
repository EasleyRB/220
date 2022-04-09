from graphics import Circle, Line


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        mouth_center = self.mouth.getCenter()
        mouth_center_clone = mouth_center.clone()
        mouth_center_clone.move = (7, mouth_center / 2)
        mouth_one = self.mouth.getP1()
        mouth_two = self.mouth.getP2()
        mouth_s_one = Line(mouth_one, mouth_center_clone)
        mouth_s_two = Line(mouth_two, mouth_center_clone)
        mouth_s_one.draw(self.window)
        mouth_s_two.draw(self.window)

    def shock(self):
        circle_c = self.mouth.getCenter()
        mouth_sh = self.left_eye.clone()
        mouth_sh.move(circle_c)
        mouth_sh.draw(self.window)

    def wink(self):
        mouth_c = self.mouth.getCenter()
        mouth_c_clone = mouth_c.clone()
        mouth_c_clone.move(2, mouth_c / 2)
        mouth_one = self.mouth.getP1()
        mouth_two = self.mouth.getP2()
        mouth_s_one = Line(mouth_one, mouth_c_clone)
        mouth_s_two = Line(mouth_two, mouth_c_clone)
        mouth_s_one.draw(self.window)
        mouth_s_two.draw(self.window)
        eye_c = self.left_eye.getCenter()
        eye_t = eye_c.getX()
        eye_b = eye_c.getY()
        eye_r = self.left_eye.getRadius()
        eye_an = eye_t + eye_c
        eye_nn = eye_b + eye_c
        self.left_eye.undraw()
        line = Line(Point(eye_an, eye_t), Point(eye_nn, eye_b))
        line.draw(self.window)
