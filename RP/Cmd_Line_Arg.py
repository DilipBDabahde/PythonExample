import sys

'''
in this program we are demonstrating how to use cmd line argv


'''
print("Welcome to command line argument test")


print("Application name: ",sys.argv[0])

val1 = int(sys.argv[1])

val2 = int(sys.argv[2])

print("First val is: ",val1)

print("Second val is: ",val2)

print("Sum of both value is: ", val1 + val2)

print("Len of cmd :",len(sys.argv))
