# signalMetadata
script to parse XML meta data from Signal messenger and convert to CSV (e.g. to use in data analysis or visualization)

## How to use?
you will need to install lxml library for python.  
on a mac:  
    $ brew install libxml2  
your signal metadata can be exported as xml in the signal app on your phone (menu in upper right corner > import/export). 
transfer the file from the root directory of your phone to your computer. you can transfer it directly via usb or send it to yourself with signal. be careful not to send it through an unencrypted channel - all of your communication and metadata is in that file!  
put the file in the same directory as this script.
