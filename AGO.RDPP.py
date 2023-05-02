def precedence(x):  #checks precedence
    if x in '*/':
        return 2 
    elif x in '+-':
        return 1
    else:
        return 0
   #calculate returns the evaluated expression 
def calculate(input):
    #stores values and operators
    array = []     
    operate = []
    
    for x in range(len(input)):
        if input[x] == ' ':   #skip the spaces
            continue
        elif input[x] == '(':  #add to operate list
            operate.append(input[x])
        elif input[x].isdigit():
            val = 0
            while x < len(input) and input[x].isdigit():
                val = (val * 10) + int(input[x])
                x += 1
            array.append(val)      #add to array list
            x -= 1
        elif input[x] == ')':
            while operate[-1] != '(':
                array.append(operate(array.pop(), array.pop(), operate.pop()))
            operate.pop()
            
#If the character is an operator, it compares the precedence of the operator with the most recent operator
        else:
            while operate and precedence(operate[-1]) >= precedence(input[x]):
                array.append(operate(array.pop(), array.pop(), operate.pop()))
            operate.append(input[x])
        
    while operate:
        array.append(operate(array.pop(), array.pop(), operate.pop()))
        
    return array[-1]
