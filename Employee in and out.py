# Create Class
class Employee:

    # Initializing
    def __init__(self):
        print("Employee created")
    
    # Calling destructor
    def __del_(self):
        print("Destructor called")
    
def Create_obj():
    print("Making Object...")
    obj = Employee()
    print("function end...")
    return obj

print("Calling Create_pbj() function...")
obj = Create_obj()
print("Program end...")