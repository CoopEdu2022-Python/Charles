"""
https://pynative.com/python-file-objects/#h-file-object-attributes
"""
"""
File Object Attributes:
File object has the following attributes that we can use to accessing various details of a file, 
such as a file name and under which mode the file is opened.

name: 
    Return the name of the file. It is a read-only attribute and may not be present on all file-like objects. 
    If the file object was created using the open() function, the file’s name is returned. 
    Otherwise, some string indicates the source of the file object is returned.
encoding: 
    It returns the encoding this file uses, such as UTF-8. This attribute is read-only. 
    When Unicode strings are written to a file, they will be converted to byte strings using this encoding. 
    It may also be None. In that case, the file uses the system default encoding for converting Unicode strings.
mode: 
    Returns the file access mode used while opening a file.
closed: 
    Returns True if a file is closed. It is a boolean value indicating the current state of the file object.
newline: 
    Files opened in universal newline read mode keep track of the newlines encountered while reading the file. 
    The values are ‘\r’, ‘\n’, ‘\r\n’, None (no newlines read yet), or a tuple containing all the newline types seen. 
    For files not opened in universal newline read mode, the value of this attribute will be None
"""
"""
File Object Methods
read():         Returns the file content.
readable():     Returns whether the file stream can be read or not.
readline():     Read single line 
readlines():    Read file into a list 
truncate(size): Resizes the file to a specified size.
writable():     Returns whether the file can be written to or not.
write():        Writes the specified string to the file.
writelines():   Writes a list of strings to the file.
close():        Closes the opened file.
seek():         Set file pointer position in a file 
seekable():     Returns whether the file allows us to change the file position.
tel1():         Returns the current file location.
detach():       Returns the separated raw stream from the buffer 
fileno():       Returns a number that represents the stream, from the operating system's perspective.
flush():        Flushes the internal buffer.
isatty():       Returns whether the file stream is interactive or not.
"""