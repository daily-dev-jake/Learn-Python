# blocks of code
# try{} --> block of code to be attempted
# except{} --> block of code to be executed when theres an error within the try block
# finally{} --> Final block of code to be executed, regardless of the error.
# change the w into r (from write into only read permission file)
""" try:
    # Attempt this code
    # might have an error
    f = open('testfile','w')
    f.write("Write a test line")
except TypeError:
    print("Encountered a type error!")
except OSError:
    print("Encountered an OS error!")
except:
    print('All other exceptions!')
finally:
    print('I always run') """
    
def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number!")
            continue
        else:
            print('Thanks!')
            break
        finally:
            print("End of try/except/finally block")
            
ask_for_int()