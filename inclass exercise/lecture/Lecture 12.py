import math

class Person:
    def _dir_(self):
        return ['age','name','salary']
    
teacher = Person()
print(dir(teacher))
#When u  run the program, the output will be:
#['age','name','salary']

class point(object):
    """ A 2D point ADT using Cartesian coordinates."""

    def _init_(self,x,y):
        """Construct a point object based on (x,y) coordinates.

        Parameters:
            x(float): x coordinate in a 2D cartesian grid.
            y(float): y coordinate in a 2D cartesian grid.
        """
         self._x = x
         self._y = y

    def x(self):
        """(float) Return the x coordinate of the point."""
        return self._x
    def y(self):
        """(float) Return the y coordinate of the point."""
        return self._y
    def move(self, dx, dy):
        """Move the point by(dx,dy).
        Parameters:
            dx(float):Amount to move in the x direction.
            dy(float):Amount to move in the y direction.

        Return:
            None.
        """
        self._x += dx
        self._y += dy

class Car(object):
    """
            bluepoint for car
    """
    def _init_(self,model,color,company,speed_limit):
        self.color = color
        self.model = model
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelarate(self):
        print("accelarating..")
        "accelarator functionality here"
    def change_gear(self,gear_type):
        print("gear changed")
        "gear related functionality here"






























    
        
