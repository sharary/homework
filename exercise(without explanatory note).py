class CoordinateValuesError(ValueError):
    pass


class AbsissaValuesError(CoordinateValuesError):
    pass


class Y_coordinateValuesError(CoordinateValuesError):
    pass


class SquareLengthError(CoordinateValuesError):
    pass


class Rectangle():

    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def width(self):
        width = abs(self.x1 - self.x2)
        return width

    def height(self):
        height = abs(self.y1 - self.y2)
        return height

    def area(self):
        area = self.width() * self.height()
        return area

    def circumference(self):
        circumference = 2 * (self.width() + self.height())
        return circumference


class Square(Rectangle):

    def __init__(self,x1,y1,x2,y2):
        super().__init__(x1,y1,x2,y2)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def length(self):
        length = abs(self.x1 - self.x2)
        return length


def RectangleSetter():
    exception = True
    while exception:
        try:
            global RS
            RS = Rectangle(*(map(float, input(
                'please enter two points(4 argumants) of coordinate axis to set up a rectangle(such as:"1 2 3 4")\n>>>').split( ))))
            if RS.x1 == RS.x2 :
                raise AbsissaValuesError
            elif RS.y1 == RS.y2 :
               raise Y_coordinateValuesError
            exception = False
        except AbsissaValuesError:
            print('>>>The values of absissa can not be the same.\n')
            continue
        except Y_coordinateValuesError:
            print('>>>The values of Y_coordinate can not be the same.\n')
            continue
        except ValueError:
            print('>>>Please enter real number(R), but not others.\n')
            continue
        except TypeError:
            print('>>>Require 4 arguments, please enter 4 numbers.\n')
            continue
    return RS


def SquareSetter():
    exception = True
    while exception:
        try:
            global SS
            SS = Square(*(map(float,input(
                'please enter two points(4 argumants) of coordinate axis to set up a square(such as:"1 2 3 4")\n>>>').split( ))))
            if abs(SS.x1 - SS.x2) != abs(SS.y1 - SS.y2):
                raise SquareLengthError
            exception = False
        except SquareLengthError:
            print('>>>The width and height are not equte to other.\n')
            continue
        except ValueError:
            print('>>>Please enter real number(R), but not others.\n')
            continue
        except TypeError:
            print('>>>Require 4 arguments, please enter 4 numbers.\n')
            continue
    return SS


def main():
    print("\n>>>setting two rectangle and calculate thier width and height:\n")
    R1 = RectangleSetter()
    R2 = RectangleSetter()
    print("Rectangle One's width: {} and height: {}".format(R1.width(),R1.height()))
    print("Rectangle Two's width: {} and height: {}".format(R2.width(),R2.height()))
    print("\n>>>setting two square and calculate their length circumference and area:\n")
    S1 = SquareSetter()
    S2 = SquareSetter()
    print("Square One's length: {} circumference: {} and area: {}".format(S1.length(),S1.circumference(),S1.area()))
    print("Square Two's length: {} circumference: {} and area: {}".format(S2.length(),S2.circumference(),S2.area()))


if __name__ == "__main__":
    main()