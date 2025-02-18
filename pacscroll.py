import time
import numpy.random as random

#github/gyphonic/pacscroll

#Python script to just scroll terminal messages for screen fluff
#Pulled from a pacman log running on Arch Linux

#Function to scroll lines at a random interval from given file
def scroll_terminal_messages(file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:
                print(line.strip())
                time.sleep(random.rand() / 2)

    #File not found            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    #Other error    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    
    #static file path
    file_path = "pacman.txt"

    #scroll endlessly
    while(True):
        scroll_terminal_messages(file_path)