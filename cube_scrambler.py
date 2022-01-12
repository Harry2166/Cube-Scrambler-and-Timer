import random
import keyboard
import time

size = random.randint(20, 25) # gives the length of the scramble

def length(size:int): #this creates the scramble
    
    count = 0
    
    moves = ["R", "L", "U", "D", "B"] # 1
    moves_prime = ["R'", "L'", "U'", "D'", "B'"] # 2
    moves_double = ["R2", "L2", "U2", "D2", "B2"] # 3
    
    scramble = [" "] #this is where the computer will store the scramble
    scramble_index = [" "] #lets the computer store the randomly generated indices
    scramble_dam = [" "] #lets the computer keep track of the generated type of move
    
    for i in range(size):
        dam = random.randint(1,3) #this lets the computer pick what type of move will be used
        scramble_dam.append(dam)
        
        if dam == 1:
            lmao = random.choice(moves)
            index = moves.index(lmao)
            count += 1
            
            wow = scramble_index[count - 1] # accesses the previous randomly generated index
            
            while wow == index: #checks to see if the index is equal to the previous index; 
                lmao = random.choice(moves) # if it is, it will loop through until it is not the same;
                index = moves.index(lmao) # this allows it to not have consutive R and R'
            
            scramble_index.append(index) 
            scramble.append(lmao)
            
        elif dam == 2:
            lmao = random.choice(moves_prime)
            index = moves_prime.index(lmao)
            count += 1
            
            wow = scramble_index[count - 1] # accesses the previous randomly generated index
            
            while wow == index: #same as line 29 
                lmao = random.choice(moves_prime)
                index = moves_prime.index(lmao)
            
            scramble_index.append(index)
            scramble.append(lmao)
            
        elif dam == 3:
            lmao = random.choice(moves_double)
            index = moves_double.index(lmao)
            count += 1
            
            wow = scramble_index[count - 1] # accesses the previous randomly generated index
            
            while wow == index: #same as line 29 
                lmao = random.choice(moves_double)
                index = moves_double.index(lmao) 
                
            scramble_index.append(index)
            scramble.append(lmao)
            
    return " ".join(scramble)

def time_convert(s): #code for the timer
    
  m = s // 60
  s = s % 60
  m = m % 60
  
  print("Time Solved = {0}:{1}".format(int(m),s))
  
  python_file = open("deez.txt", "a") #opens a separate txt file
  python_file.write(("Time = {0}:{1}\n".format(int(m),s))) #puts the time in a txt file
  python_file.close()

#code to activate the scrambler + timer
def main():
        
        print("Press shift if you want to show the scramble or press q if you want to quit!")
        if keyboard.read_key() == "shift":  
            print(length(size)) #activates the scramble
            
        elif keyboard.read_key() == "q":
            print("Thank you for accessing!")
            quit()
            
        input("Press enter to start the timer. ")
        start_time = time.time()

        input("Press enter to stop the timer. ")
        end_time = time.time()
        print("You stopped the timer!")

        time_lapsed = end_time - start_time
        time_convert(time_lapsed) #prints the time
        
        print("Nice try!")
        
main()