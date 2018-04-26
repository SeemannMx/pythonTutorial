if __name__ == "__main__":
    print("")
    print("print content from other textfile in same directory")
    print("---------------------------------------------------")
    
    # w  - write modus
    # a  - append modus
    # r  - read modus
    # r+ - read and write modus
    
    # returns file (contains other functions)
    file = open("text","r")
    
    # get content from text file via read method
    print(file.read())
    file.close()
    
    # only write or read at the time and close process
    newFile = open("text", "w")
    newFile.write("\nadd a new line")
    newFile.close()
    
    # read out text file again
    oldFile = open("text", "r")
    print(oldFile.read())
    oldFile.close()
    
    
    
    
    