# acivity for errors
# fileName = input("Please enter hte name of the file you would like to read: ")
# myfile = open(fileName, 'r') # Open a file for reading.
# contents = myfile.readlines() # Read in the content by line.
# myfile.close() # Explicitly close the file
# print(contents) #print the contents of the file

class FileManipulator:
        def __init__(self,fileName):
            self.contents = None
            self.open_file= None
            try:
                self.open_file= open(fileName, 'r')
                self.contents=self.open_file.readlines()
                print(self.contents)
            except(FileNotFoundError,TypeError,OSError) as e:
                print(f"Invalid File Name: {e}") 
                new_file = input("Please enter the name of the file you would like to read: ")
                FileManipulator(new_file)
            finally:
                if self.open_file:
                    self.open_file.close()

# test code:

f = FileManipulator("temp.txt")
# 
print(f.contents)
#f.reverse("tmp2.txt")
