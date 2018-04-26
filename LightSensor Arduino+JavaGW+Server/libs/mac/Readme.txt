lsIf you are upgrading from V 3.x or V4 Beta 2 (i.e. from an older version of RXTX), please remove the file 'libSerial.jnilib' in the '/Library/Java/Extensions' folder 

Please download 'RXTXcomm.jar' and 'librxtxSerial.jnilib' and install them in the '/Library/Java/Extensions' folder to make them available to all users or '¬/Library/Java/Extensions' to be available for the current user only. 
Please download 'fixperm-217-leo.sh' and install it e.g. on the 'Desktop'.

Open a Terminal window (found under Application->Utilities) and type:
$ cd Desktop     (or the folder where you downloaded the script)
$ sudo sh ./fixperm-217-leo.sh
Password: <your administrator password>

This will set the proper privileges for accessing the serial port driver.

chmod -R 755 /Library/Java/Extensions