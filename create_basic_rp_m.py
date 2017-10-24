import resources

clYN = input("Hi, let's get you a new RP. You want to create from the command line? (Y/N):  ")
if clYN == 'Y':
    print("Great - here we go! Just answer these questions.")
    clProj = resources.getProjectCL()
    clProj.writeXLSX()
    print("That was fun - Bye!")
else:
    print("Sorry, file input is not supported yet. Come back soon!")