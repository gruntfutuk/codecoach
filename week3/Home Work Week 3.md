# Home Work Week 3

Create an empty text file on your hard drive using your text editor.
(on macOS/Linux you can enter, `touch filename` on the command line.)

Create a python script that takes 3 extra arguments on the command line, and
each time the script is called:
* create a new dictionary
* store a copy of the arguments in the new dictionary
* open the text file created earlier

If the file is empty,
* create a new list
* add the dictionary of arguments created above to the new list
* save the new list to the empty file

If the file already has data saved to it,
* read the file
* convert the data read from the file back to a new list
* append the new dictionary to the new list
* save the new list back to the file overwritting previous data

Remember to finally close the file.
