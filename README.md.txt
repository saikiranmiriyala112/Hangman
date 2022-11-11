# Hangman
A GUI-based implementation of the Hangman game written in Python as part of a high school project.

Run `hangmanltFINAL.py` to start playing the game. 

The game will randomly choose a word from a dictionary contained in the [hangmanwords.txt](https://github.com/62firelight/hangman-python/blob/main/hangmanwords.txt) file if it exists, or its own internal dictionary if [hangmanwords.txt](https://github.com/62firelight/hangman-python/blob/main/hangmanwords.txt) does not exist.

In theory, you can add your own dictionary by making your own `hangmanwords.txt` file as long as it adheres to the format in the repo's [hangmanwords.txt](https://github.com/62firelight/hangman-python/blob/main/hangmanwords.txt) (i.e. words separated by new lines). However, I have not tested the program with any file larger than [hangmanwords.txt](https://github.com/62firelight/hangman-python/blob/main/hangmanwords.txt), which contains about 40k words.

## Screenshots

![image](https://user-images.githubusercontent.com/54054879/184562354-6a049f4d-17b4-4c4d-8e6e-d938f214cff4.png)

![image](https://user-images.githubusercontent.com/54054879/184562375-9a0d3667-35c4-4052-8194-a50e0827c341.png)

![image](https://user-images.githubusercontent.com/54054879/184562433-319a0688-da24-4cc7-ad49-2d4a318e4cb2.png)

![image](https://user-images.githubusercontent.com/54054879/184562479-73870741-3dd9-4584-8013-be95b0ab5d40.png)

## Notes
* Pretty much all of the code is left unmodified from when the program was finalized in April 2018, along with all the (rather excessive) comments. However, I have commented out a debug statement that would print out the answer every round, along with a win message called "You're winner." 
* The `old` folder contains all of the older versions of the program. I had no idea that Git existed at the time, so I resorted to the rather painful method of saving the program as a new file with a different version number.
