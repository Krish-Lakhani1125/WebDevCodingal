class Employee:
    #innitializing (Constructor)
    def __init__(self):
        print('Employee created.')

    #deleting (Destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')

obj = Employee()
del obj