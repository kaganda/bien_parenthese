 # fonction principale

def Bien_parenthese(Str):
    
    stack = []

    for char in Str:
       
        if char == '{' or char == '(' or char == '[':
            stack.append(char) # push
       
        elif char == '}' or char == ')' or char == ']':
            if len(stack) == 0:
                return False
            sommet = stack.pop() # pop
            
            if not Paire(sommet, char):
                return False
     
    if len(stack) != 0:
        return False
              
    return True

# fonction de parite

def Paire(ouvrant, fermant):
    if ouvrant == '(' and fermant == ')':
        return True
    if ouvrant == '[' and fermant == ']':
        return True
    if ouvrant == '{' and fermant == '}':
        return True  
    return False

# test

phrase = input("ajouter la phrase\n")
if Bien_parenthese(phrase) == True:
    print("la phrase est bien parenthesee")
else:
    print("la pharse n'est pas bien parenthesee")