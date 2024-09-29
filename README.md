# bookbot
Boot.dev bookbot thingy

BookBot is my first project!

#Bookbot - Read file
Now that you've got your machine all configured, let's build "bookbot"! Bookbot is a simple command-line program that reads text from a file and generates a report about the text.

##Download "Frankenstein"
The "Frankenstein" book by Mary Shelley is in the public domain, so we can use it for our project.

You can find the full text here.

Create a directory in your bookbot project called books. Right-click the text on the webpage and choose Select All, then copy and paste it into a text editor. Save it as frankenstein.txt in the books directory.

##Use a .gitignore file
We don't want to save the entire book in our Git repository. Generally speaking, Git is for code, not for data.

Create a .gitignore file in the root of your project and add this text to it:

##books/
Copy icon
You should see the filename turn dark gray in your VS Code file explorer. Now, whenever you run git add . from the root of your project, all the files in the books directory will be automatically ignored!

##Read the book
Change main.py so that instead of printing "hello world", it reads the contents of the "frankenstein.txt" and prints it all to the console.

#Hints
Use a with block to open a file:

with open(path_to_file) as f:
    # ...
Copy icon
Keep in mind that path_to_file needs to be relative to wherever you're running the program from. If you're running the program from the root of your project, you would use books/frankenstein.txt. The path to the file is a string so it needs to be in quotes!

Once you have an open file, read the contents into a string within the with block:

file_contents = f.read()
Copy icon
Use a main function to wrap the logic and call main() at the bottom of your file to execute your program.

When you're satisfied it's working, you can move on.