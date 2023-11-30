class Shoe:
    def __init__(self, brand, size: int):
        self.brand = brand
        assert isinstance(size, int), "Size must be an integer"
        self.size = size
        self.condition = 'New'  

    def repair(self):
        self.condition = 'Repaired'
        self.cobble = True


try:
    my_shoe = Shoe('adidas', '20') 
except AssertionError as e:
    print(e)

# Test repair method
my_shoe = Shoe('nike', 10)
print(my_shoe.condition)  # Output: New

my_shoe.repair()
print(my_shoe.condition)  # Output: Repaired
print(my_shoe.cobble)  # Output: True
