class parent:
    def __init__(self):
        self.parent_attribute = "I am a parent attribute"

    def parent_method(self):
        return "I am a parent method"
    
class child(parent):
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.child_attribute = "I am a child attribute"

    def child_method(self):
        return "I am a child method"
    
inh = child()
print(inh.parent_attribute)
print(inh.child_attribute)
print(inh.parent_method())
print(inh.child_method())