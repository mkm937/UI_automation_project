# Simple UI Automation Project
## About
In this day and age, no one should have to manually transfering large ammounts of data from a spreadsheet to GUI form. This project offers software to automate such tasks when GUIs lack functionality to recieve data in bach. At present, the project consists of a single .py file which, when run, opens a small window for the user to fill out. The user must specify a file path for the spreadsheet and add control parameters - called _steps_. Note that the user **must** specify the file path for the spreadsheet and submit it before adding steps. The user can add as many steps as they need and they can choose between four different types, outlined below.
* _Find_: Allows user to specify an image path corresponding to a snip of a section of the screen and to specify a four element tuple. The image is where the user wants the mouse to move to and the tuple are the coordinates representing the section of the screen they would like the OS to search. Following the usual convention, the tuple will be given by (x1, y1, x2, y2) where the coordinates (0, 0) represent the top left of the screen.
* _Click_: Tells the OS to mouse click.
* _Type_: Allows user to specify a string they would like the OS to type. Note that at present, if the user types "tab" it will be interpreted by the OS as the special keystroke tab, not the actual word _tab_.
* _Fill_: Allows the user to specify the field (column) of the spreadsheet they would like the OS to fill from.

When the _Process Steps_ button is clicked, the users OS will begin processing each record (row) in the spreadsheet in accordance with the steps specified. It will begin with the first record, process each step from first to last, then move on to the next record and so on until there are no more records in the spreadsheet.

## 
