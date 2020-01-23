class Parrot:
    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")
        
class Penguin:
    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")
        
# Common interface
def flying_test(bird):
    bird.fly()
    
# Instantiate objects
blue = Parrot()
peggy = Penguin()

flying_test(blue)
flying_test(peggy)
