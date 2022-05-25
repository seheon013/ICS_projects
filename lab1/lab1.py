"""
Name: Seheon 
UCINetID: seheonj
"""
class IntegerOutOfRangeException(Exception):
    pass
class NoStaircaseSizeException(Exception):
    pass
''' This functions asks the user for the number of steps
they want to climb, gets the value provided by the user
and returns it to the calling function. This function will
raise any exceptions related to none integer user inputs.'''
def getUserInput():
    input_num = input("How many steps do you want to move?")
    if input_num == "DONE":
        return "DONE"
    return int(input_num)
    

    
''' This function takes the number of steps as an input parameter,
creates a string that contains the entire steps based on the user input
and returns the steps string to the calling function. This function will raise
any exceptions resulting from invalid integer values.
'''
def printSteps(stepCount):
    if stepCount > 999 or stepCount < 0:
        raise IntegerOutOfRangeException()
    
    # handle == 0
    if stepCount == 0:
        raise NoStaircaseSizeException()

    num1 = stepCount
    list1 = []
    for i in range(num1):
        list1.append(i)
    list1.reverse()

    if len(list1) not in (1,2):
        str1 = ''
        for i in list1:
            if i == list1[0]:
                str1 = str1+ '  '*(i) + '+-+' + '\n' + '  '*(i) + '| |' + '\n'+'  '*(i-1) + '+-+-+' + '\n'
                
            elif i != list1[0] and i != list1[-1]:
                str1 = str1+ '  '*(i) + '| |'+ '\n' + '  '*(i-1) + '+-+-+' + '\n'
            
            elif i == list1[-2]:
                str1 = str1+ '  '+'| |' +'\n'
                
            elif i == list1[-1]:
                str1 = str1+ '| |'+ '\n' + '+-+'
    
                
    elif len(list1) == 1:
        str1 = '+-+' + '\n' +'| |'+ '\n' + '+-+'
    elif len(list1) == 2:
        str1 = '   +-+' + '\n'+  '   | |'+ '\n' + '+-+-+' + '\n' +'| |'+ '\n' + '+-+'
    
    return str1


'''This function kicks off the running of your program. Once it starts
it will continuously run your program until the user explicitly chooses to
end the running of the program based on the requirements. This function returns
the string "Done Executing" when it ends. Additionally, all exceptions will be
handled (caught) within this function.'''
def runProgram():
    isRunning = True
    #your code belongs here
    while isRunning:
        try:
            a = getUserInput()
            if a =="DONE":
                isRunning = False
            else:    
                b = printSteps(a)
                print(b)
        except NoStaircaseSizeException:
            print("I cannot draw a staircase with no steps.")
        except IntegerOutOfRangeException:
            print("That staircase size is out of range.")
        except ValueError:
            print("Invalid staircase value entered.")
    return "Done Executing"
    
'''Within this condition statement you are to write the code that kicks off
your program. When testing your code the code below this
should be the only code not in a function and must be within the if
statement. I will explain this if statement later in the course.'''
if __name__ == "__main__": 
    #your code belongs here
    runProgram()
