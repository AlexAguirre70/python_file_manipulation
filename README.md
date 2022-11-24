# Getting Started
<br>
First, let's explore the code we already have. We have provided you with some starter code that asks for a file name, reads the file line by line, closes the file, and then prints the stored content.<br><br>

Unfortunately, this program is far from complete. <br>
What happens if, for example, the file name given by the user is spelled wrong or doesn't exist? <br>
The open() function can raise a FileNotFoundError, a TypeError, or an OSError. We need to fix the program to handle any of those errors gracefully.

## Error Handling
<br><br>
Your task for this activity is to complete the program by gracefully handling any errors that might come your way.<br>
 There are many ways to do this, but for this activity you will be creating a class to manipulate files, called FileManipulator. To successfully create this class, complete the following steps:<br><br>

* Create the FileManipulator class and implement the constructor. <br><br>

* The constructor should accept the name of a file to read in and should continually prompt for input if the name given causes an error.<br><br>

* Make sure that you give an informative message if an error is raised.<br><br>

* Implement the reverse() function. <br><br>
This function should accept the name of a file to write to and should write each line of the original file to this new file. <br><br>

However, in the new file, although the line order will be the same, the string that makes each line will be reversed. <br><br>

So "cheese" will become "eseehc". Be careful not to add an extra newline character at the beginning of the file. Make sure that errors are handled elegantly, and appropriate error messages are given.

## Testing your FileManipulator class
After you have created it, test your FileManipulator class by running the given code.

**f = FileManipulator("tm.txt")<br>
<class 'FileNotFoundError'> [Errno 2] No such file or directory: 'tm.txt'<br><br>

Please enter a valid file name: tmp.txt<br><br>

>>>print(f.contents)<br><br>

['I like cheese<br>
', 'Do You?']<br><br>

>>>f.reverse("tmp2.txt")
