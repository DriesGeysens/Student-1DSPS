# imports go here
# data used by all functions

def function1():
    string = subfunction()
    print(string)
    #print("This is function 1")
    return "This is function 1"

def function2():
    print("This is function 2")

def subfunction():
    return "Hello World"
def main():
    # Execute functions
    function1()
    function2()
if '__main__'==__name__:
    # Execute main function
    main()