# signalMetadata
a script to parse XML meta data from Signal messenger conversations and convert it to CSV (e.g. to use in data analysis or visualization)

## How to use?
you will need to install lxml library for python.  
on a mac:  


    $ pip install lxml  
your signal metadata can be exported as an xml file in the signal app on your phone (menu in upper right corner > import/export). 
transfer the file from the root directory of your phone to your computer. you can transfer it directly via usb or send it to yourself with signal. be careful not to send it through an unencrypted channel - all of your communication and metadata is in that file!  
put the xml file in the same directory as this script and run


    $ python signalXmlToCsv.py
