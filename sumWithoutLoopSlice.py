# Let's try this again! I'm going to take a crack at slicing.
# I feel like a real smuggler on Nar Shadaa.
# I also didn't ask for any help with this code whatsoever!
# That being said, we just learned a ton about scope and initializing,
# particularly about passing initial arguments and overriding them.


def sumRecurBri(userList, tot=0):
    if userList:
        return sumRecurBri(
            userList[1:],
            tot + userList[0]
        )
    return tot


def easter_egg():
    print("This is amazing")


# The most efficient version so far!
def sumRecur(userList, tot = 0, i = 0):
    if len(userList) > i:
        return(sumRecur(userList, tot + userList[i], i+1))
    else:
        return(tot)


# This was also good, but it's better with an if? uses less memory?
def sumRecurTry(userList, tot = 0, i = 0):
    try:
        return(sumRecurTry(userList, tot + userList[i], i+1))
    except:
        return(tot)


# Create a basic CMD user menu
def sumListMenu():
    # I decided to stick with the if/else version, vs try/except
    
    # Menu display String (indented on purpose)
    menuDisplay = """
    Please select an option.
    
    Type a number: this will put a number onto the end of your list.
    Type "a": Auto-fill the end of the list with the numbers 1-10.
    Type "d": Display the list without adding any new numbers.
    Type "c": Clear your list.
    Type "r": Remove the last item on your list.
    Type "s": Display the sum of your list.
    Type "b": Display the sum of your list in Bri mode.
    Type "t": Display the sum of your list in Try mode.
    Type "x": Exit the program.
    """
    
    # Initialize menu values, list, and then display menu
    sel = ""
    sumList = []
    print("\n	Welcome to sumList!\n	Starting with a blank list." + menuDisplay)
    
    while sel != 'x':
        # Await user instruction
        sel = input("       ")
        # Acceptable values to add
        if sel == 's':
            print(sumRecur(sumList))
        elif sel == 'b':
            print(sumRecurBri(sumList))
        elif sel == 't':
            print(sumRecurTry(sumList))
        elif sel == 'a':
            i = 0
            while i < 10:
                i += 1
                sumList.append(i)
        elif sel == 'd':
            print(sumList)
        elif sel == 'x':
            break
        elif sel == 'c':
            sumList = []
        elif sel == 'r':
            # Try to delete the last item
            try:
                sumList.pop(-1)
            except:
                print("	List already empty.")
        else:
            # Try to append an int to the end
            try:
                sel = int(sel)
                sumList.append(sel)
            except:
                # Try to append a float to the end
                try:
                    sel = float(sel)
                    sumList.append(sel)
                except:
                    print(" INVALID SELECTION." + menuDisplay)

    #Exit message
    print("	Thanks for using sumList!")


# sumListMenu()
sum_array = [1,2,3,4,5,6,7,8,9]
print(sumRecur(sum_array))
print(sumRecurTry(sum_array))
print(sumRecurBri(sum_array))

