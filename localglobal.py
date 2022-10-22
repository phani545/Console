##Find out number of local variables in function

#local variable inside the function
#Global variables are outside of vaiables

def phani():
    a=2;
    b=3;
    s="phani";
    x=a+b;
print(phani.__code__.co_nlocals)
