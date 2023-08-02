from math import pi


class Pizza:
    def __init__(self, name, diameter, price, num_slices):
        self.name = str(name)
        self.diameter = float(diameter)
        self.price = float(price)
        self.slices = int(num_slices)

    @property
    def radius(self):
        return self.diameter / 2

    @property
    def area(self):
        return self.radius**2 * pi

    def area_per_slice(self):
        return self.area / self.slices

    def cost_per_slice(self):
        return self.price / self.slices

    def cost_per_square_inch(self):
        return self.price / self.area

    def __str__(self):
        return f"Your {self.name} pizza has a diameter of {self.diameter} inches, a price of ${self.price}, and {self.slices} slices per pie"
