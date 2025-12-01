class Robot:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hello! My name is {self.name}.")

# Create objects (instances) for Tom and Jerry
tom = Robot(name="Tom")
jerry = Robot(name="Jerry")

# Call the introduce method on each object to make them speak
tom.introduce()
jerry.introduce()