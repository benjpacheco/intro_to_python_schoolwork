
import numpy as np
import matplotlib.pyplot as plt

def arrayString(name):
  fullname = name + ".png"
  img = plt.imread(fullname)  
                    
  img2 = img.copy()            
  img2[:,:,0] = 0.5       
  img2[:,:,2] = 0.5
  img2[:,:,1] = 0.5

  plt.imshow(img2)         
  plt.show()
              


def main():
  #program that prompts the user for the name of an .png (image)
  name = input('Enter file: ')
  arrayString(name)




#Allow script to be run directly:
if __name__ == "__main__":
  main()
