#CSci 127 Teaching Staff
#A program that uses functions to print out days.
#Modified by:  ADD YOUR NAME HERE

def dayString(dayNum):
     """
     Takes as input a number, dayNum, and
     returns the corresponding day name as a string.
     Example: dayString(1) returns "Monday".
     Assumes that input is an integer ranging from 1 to 7
     """
     
     dayString = ""

     if dayNum == 1:
          mon = Monday
     elif dayNum == 2:
          tue == Tuesday 
     elif dayNum == 3:
          wed = Wednesday
     elif dayNum == 4:
          thu = Thursday
     elif dayNum == 5:
          fri = Friday
     elif dayNum == 6:
          sat = Saturday
     else dayNum == 7:
          sun = Sunday
    

     return(dayString)



def main():
     n = int(input('Enter the number of the day: '))
     dString = dayString(n)
     print('The day is', dString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
