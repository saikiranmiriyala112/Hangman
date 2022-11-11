# Hangman Program
# Importing modules for use in program 
from tkinter import * # To draw the GUI
from tkinter import ttk # To make the GUI look nicer
from string import punctuation # To check if a string has punctuation in it
import os # To check if a file is present
import random # To randomize the selected word

'''
		##############################################################
		##################### 				    ######################
		############################################################## 
'''

class HangmanGame: # Defining class
	def __init__(self, master): # Constructor class, always uses root as argument
								# Used mainly for variable defining
								# This always runs when an instance of this class is created
		self.master = master # Define a variable as the parameter, as self. prefixes on variables allow them to be
							 # used over the entire class
		self.master.title("Hangman (by Luke Tang)") # Set the title of the program

		##############################################################
		##################### VARIABLE DEFINING ######################
		##############################################################
		# Note the self. prefix, which is used so that the variables that are defined here can be used in other methods

		# Text file word list 
		self.text_words_list = [] # Empty by default
								 # Will be modified if the text file is found

		# Hardcoded word list
		self.contingency_words_list = ["hanging", "man", "never", "liar", "fantastic", "not", "chance", "always", "your", "program", "smite", "tank",
							"wonderful", "world", "inquisition", "wild", "men", "woman", "male", "female", "progress", "washington", "arizona", "wide", "false",
							"jesus", "loves", "you", "happy", "lovely", "nothing", "inside", "quiet", "loud", "sound", "wave", "angle", "radical", "uncalled",
							"ponder", "preposterous", "catastrophe", "unhinged", "feeling", "delve", "dispenser", "here", "sentry", "gun", "lookout", "door",
							"dragon", "effect", "yonder", "conniptions", "hooked", "me", "soul", "master", "dark", "darkness", "blood", "bloodborne", "tangible",
							"lion", "demon", "unfortunate", "numb", "put", "fury", "treason", "order", "republic", "democracy", "autocracy", "reform", "national",
							"president", "card", "start", "physical", "theoretical", "theory", "science", "scientific", "biological", "fortunate", "lucky",
							"missing", "in", "action", "boy", "girl", "difficult", "insurmountable", "surpass", "metal", "gear", "overdrive", "sunset", "over",
							"memes", "end", "here", "rules", "of", "nature", "otepoti", "new", "bequeath", "defend", "unquestionable", "legacy", "defy", "understand",
							"thought", "thinking", "think", "shoot", "halo", "chieftain", "satisfaction", "brute", "gate", "monday", "tuesday", "wednesday", "thursday",
							"friday", "saturday", "sunday", "days", "weeks", "gone", "nation", "homozygous", "heterozygous", "genetic", "train", "star", "trip",
							"love", "defense", "machine", "edge", "along", "towards", "ruler", "pencil", "upon", "secret", "betrayal", "blind", "synthetic",
							"cream", "smith", "green", "agreement", "android", "replicant", "tortoise", "quantifiable", "blender", "hate", "anger", 
							"force", "senate", "emperor", "snake", "electronic", "electric", "electricity", "surely", "father", "vader", "luke", "james",
							"martin", "shaun", "genesis", "origin", "spider", "web", "blizzard", "watch", "snow", "wall", "battle", "inheritable", "humongous",
							"ginormous", "strike", "jedi", "skywalker", "starkiller", "widow", "fragment", "related", "blade", "uranium", "nuclear",
							"fallout", "strontium", "hydrogen", "mass", "team", "fortress", "unbeknownst", "factorial", "calculus", "mathematics",
							"pythagoras", "triangle", "archimedes", "pie", "abraham", "newton", "lincoln", "jefferson", "thirst", "thirsty", 
							"athirst", "freedom", "redemption", "redeem", "correction", "detection", "detect", "revere", "paul", "revolution",
							"america", "american", "state", "united", "venture", "skull", "biology", "chemistry", "defer", "deference", "darkness",
							"bits", "pieces", "air", "traffic", "control", "harrison", "ford", "orbital", "drop", "shock", "trooper",
							"troopers", "fire", "firefight", "fight", "firefighter", "emergency", "winter", "contingency", "sword", "base",
							"long", "night", "solace", "tip", "spear", "nightfall", "noble", "journey", "remember", "reach", "september", "johnson",
							"arbiter", "chief", "commander", "firelight", "earth", "amid", "ashes", "gears", "war", "dominic", "santiago", "peace",
							"marcus", "phoenix", "fawkes", "history", "historic", "religious", "reference", "captain", "avenge", "mexico", "johannesburg",
							"dunedin", "island", "english", "auckland", "christchurch", "mornington", "valley", "ecological", "eco", "ratchet", "clank",
							"jack", "dexter", "platform", "basis", "play", "station", "classic", "ghost", "grand", "theft", "automatic", "monster",
							"frightening", "frighten", "normal", "abnormal", "monument", "monumental", "achievement", "score", "trophy", "definition",
							"spell", "election", "garden", "process", "sparrow", "group", "mercury", "venus", "mars", "jupiter", "saturn" "uranus", "neptune",
							"pluto", "satellite", "space", "astronomy", "future", "utopia", "dystopia", "dysfunction", "west", "east", "north", "south", "heritage",
							"selection", "difficulty", "unachievable", "defeatist", "cameras", "apartment", "story", "unacceptable", "thanks", "for" "being", "an",
							"amazing", "teacher"] 
							# This is the list that the program will use to generate words if the text file to do so cannot be found

		# Define fonts in a specific format
		self.heading_font = "Helvetica 30 bold"  # Used for the heading
		self.hidden_font = "Helvetica 30 bold" # Used for the hidden/revealed letters
		self.regular_text = "Helvetica 11"

		# Define what color the status message should be if the player guesses correctly/incorrectly
		self.correct_color = "green"
		self.incorrect_color = "red"
		# For visual feedback

		# Define graphic settings for hangman canvas
		self.colour = "black" # Colour of hangman line
		self.width = 2 # Line width of hangman line

		# Define game settings, some parameters are set as variables for added flexibility to the program
		self.hidden_letter = "_" 

		# Define what the file name of the hangman text file should be for the program
		self.hangman_text_file = "hangmanwords.txt" # The text file is assumed to have words already sorted line by line

		# The code below is placed in the __init__ method so it only ever happens once unlike the code in the word generation method
		# I originally put this into the generate_word method, but printing this message would just spam Powershell with these messages
		# every time I generated a word. This spam was unwarranted and didn't make sense with what was said, which was why I put this here
		if os.path.isfile('./' + self.hangman_text_file) == True: # Check if the hangman words file exists in local directory
			print("Hangman file found! Initializing program using words from file.") # Print this message in the console
										 # This information doesn't need to be seen by the user on the GUI
		else:
			print("Hangman file not found. Initalizing program using hardcoded words.") # Otherwise there is no text file to load from, 
																			  			# so use hardcoded words

		# Coordinates used to draw the hangman picture, this will appear whenever the player guesses incorrectly
		self.coordinates = [(2, 99, 99, 99), (2, 98, 2, 3), (2, 2, 99, 2), (3, 81, 20, 98), (3, 19, 19, 3), 
							(51, 3, 51, 21), (44, 22, 58, 36), (51, 37, 51, 62), (52, 63, 59, 70), (50, 63, 43, 70),
							(40, 48, 62, 48)]
		# Total of eleven coordinates, so eleven guesses will be used
		# Amount of guesses depends on how many coordinates for the hangman picture there are -- allows for more flexibility
		
		self.guess_multiplier = 1 # Used in conjunction with guess_count to calculate how many guesses the player will have - Default: 1
								  # Should be left at default value -- otherwise the hangman picture doesn't draw at the right time
		self.guess_limit = int(round(len(self.coordinates) * self.guess_multiplier, 0)) # Default amount of guesses - Default: 10

		# Tkinter text variables e.g. IntVar(), StringVar(), are used so I don't have to configure the widgets every time I want to update
		# the GUI. This way, I only have to update the variable to do just that.

		# Note that all Tkinter variables are empty by default

		# One exception is the "You have {} guesses left" label, as a format() method is used to insert the number of guesses, so a configure()
		# method is used

		self.guess_count = IntVar() # Defining for use later on
		self.guess_count.set(self.guess_limit)

		self.declare_message = StringVar() # Define a string variable that updates whenever the player wins or loses
										   # This will always be set to "" when the game is in progress
										   # Has to be set to "" for it to start

		self.guess = StringVar() # Define a guess variable that will be used to get the player's input

		self.status = StringVar() # Define an empty status message variable for usage later on

		# Pre-defined messages for the declare message variable
		self.win_message_list = ["YOU WIN", "CONGRATULATIONS. YOU WIN", "YOU WIN. WELL DONE"] # List of win messages to randomly pick from
																											   # when the player wins
		self.lose_message = "YOU LOSE"

		self.guess_letters_list = [] # Define empty list for usage later on

		self.guess_letters = StringVar() # Define empty GUI string variable for usage later on
										 # This shows the player's incorrect guesses

		self.hidden_word = StringVar() # Define a hidden word variable that will be used throughout the entirety of the class

		# Calling methods to initialize the game
		self.draw_gui() # Draw the GUI
		self.generate_word() # Generate a word after the method to start the game is called -- otherwise the game breaks

	##############################################################
	##################### 	LOGIC METHODS   ######################
	############################################################## 

	def generate_word(self): # Method for resetting the entire game
							 # Does not take any parameters
		self.declare_message.set("") # Set the declaration message to nothing as the game state has been reset

		self.hangman_count = -1 # Controls how many hangman lines to draw
								# Resets whenever the game generates a new word
								# Goes up by 1 every time the player guesses incorrectly
								# This is -1 because the index of the coordinates list is used

		# Reset the canvas 
		self.picture_canvas = Canvas(self.picture_frame, width=100, height=100)
		self.picture_canvas.grid(row=6, column=1)

		# Reset guess count
		self.guess_count.set(self.guess_limit) # Reset guesses to original amount
		self.guess_label.configure(text="You have {} guesses left.".format(self.guess_count.get())) # Update GUI widget

		# Reset status message
		self.status.set("Enter a letter or a word.")
		self.status_message.configure(foreground="") # Reset text colour

		self.guess_letters_list = [] # Reset previous guesses
		self.guess_letters.set(self.guess_letters_list) # Update GUI

		if os.path.isfile('./' + self.hangman_text_file) == True:
			if not self.text_words_list: # Checks if the text file list is empty before adding on words to it
										# I don't want to append what could be several thousands of words onto the same list
										# every time the player resets, as the program could become unplayable over time
				with open(self.hangman_text_file) as used_words: # Same as if I did used_words = open(self.hangman_text_file)
					word = used_words.readline() # Set the word to whatever is in the first line of the file
					while word: # If the words variable is not empty, as in if it has reached the end of the file
						self.text_words_list.append(word) # Add word onto text_file
						# By using a list inside the program to generate the words from the text file, this alleviates the
						# scenario where the required text file somehow goes missing mid-game and the program cannot find a 
						# word to use. The program can just use the list from within the code to generate its words
						word = used_words.readline() # Read from another line
			self.random_word = random.choice(self.text_words_list).strip().lower() # Generate word from list
			while any(p in self.random_word for p in punctuation) == True: # Check for any punctuation in the text file. The
																		   # program does this because punctuation characters
																		   # are not a valid input in the program 
																		   # Note that this is a while loop so the program will
																		   # keep generating a different word if there is punctuation
																		   # in any of those generated words
				print("Punctuation found in generated word. Generating another word.")
				self.random_word = random.choice(self.text_words_list).strip().lower() # Generate another word because that word
																					  # with punctuation will break the game if used
		else: # Otherwise, use hardcoded words list
			self.random_word = random.choice(self.contingency_words_list).strip().lower() # Strip the displayed word of any loose characters
																						  # Make the word lowercase so it displays as intended

		#self.random_word = "bloodborne" # Line for testing

		self.hidden_word_l = [] # Create an empty list so that things can be appended onto it later
								# Controls how many hidden letters should be added

		for i in range(len(self.random_word)): 
			self.hidden_word_l.append(self.hidden_letter) # Append the list with whatever the hidden letter is

		self.hidden_word.set(self.hidden_word_l) # Set this equal to the hidden_letter 

		# print(self.random_word) # Debug message for easier testing

	def check_word(self, guess): # Method to check the player's input
								 # Take the player's input as a parameter, so that I don't have to type out a self. prefix every time
								 # I want to use the player's input

		guess = guess.strip().lower() # Make the player's input lowercase to broaden the number of accepted inputs
		self.initial_hangman_count = self.hangman_count # How many lines that were drawn at the beginning
		self.correct = False # Use a variable to track whether the player's input was correct or not
							 # This saves me from having to employ the same procedures for every single scenario the
							 # the player guesses correctly or incorrectly

		#print(self.guess.get()) # Debug message
		if self.declare_message.get() == "": # Check if the game is still in progress
											 # The player cannot guess if this variable is not empty as the game would have ended

			if guess.isalpha() == True: # Check if the player's input only uses letters
										# This will return false whenever the player types nothing or a character that is not a letter

				if len(guess) > 1 and (guess in self.guess_letters_list or guess in self.hidden_word_l): # Check if the player has already inputted the same word
																					# This is placed here so it doesn't go ahead and evaluate if the
																					# guess is correct or not before actually checking this
					self.status.set("You have already guessed that word.") # Does not penalize the player
					self.status_message.configure(foreground="") # Neutral color
				elif guess in self.guess_letters_list or guess in self.hidden_word_l: # If the length of the guess is not longer than 1, it must be a letter
																					  # No need to put any len(guess) check here as it is still the same as
																					  # if I put if not len(guess) > 1 or something similar
					self.status.set("You have already guessed that letter.") 
					self.status_message.configure(foreground="") 
				else:

					# Check if the player enters the correct word (more than one letter to qualify)
					if guess == self.random_word: # If the player guesses the whole word
						self.hidden_word_l = list(guess) # The list form of a string is different to the string itself, as making it a list separates all of the letters
														 # So I have to make sure that the displayed word is consistent with what is displayed, otherwise the GUI looks
														 # messy
						self.hidden_word.set(self.hidden_word_l) # Update GUI
						self.correct = True # Set correct variable to True for the proper procedures to be carried out

					elif len(guess) > 1 and (len(guess) < len(self.random_word)): # Check if the player attempts to guess a word
																														# (more than 1 letter) that is longer or shorter
																														# than the actual word
						self.correct = "short" # Set this variable to a hardcoded value, where the player isn't penalized 
					elif len(guess) > 1 and (len(guess) > len(self.random_word)):
						self.correct = "long" # Similar hardcoded value, but results in different status message
					
					# Else the player must have entered a letter
					else: 
						for i in range(0, len(self.random_word)): # i is the index, it starts from 0 so I don't need to deduct the length by 1
							if guess == self.random_word[i]: # Use the looping variable as an index to keep track of where a specific letter is
															 # If the index isn't tracked, then the index() method can be used, though
															 # using this method will only get the index of the first instance of the input.
															 # E.g. index("p") will only get the very first p, nothing else, so only one letter is filled in
								self.hidden_word_l[i] = guess # Set the specific part of the looping variable to the player's guess, because it is correct
								self.hidden_word.set(self.hidden_word_l) # Update the text variable so that the GUI displays properly
								self.correct = True 
					
					# The below code is placed here for efficiency purposes. This way, this doesn't have to be present
					# every time the player guesses correctly/incorrectly

					# Conditions to handle what the program will do depending on the player's input
					if self.correct == True: # Player guesses correctly
						self.status.set("Your guess was correct.")
						self.status_message.configure(foreground=self.correct_color)
					elif self.correct == "short":
						self.status.set("Your guess was not long enough.") 
						self.status_message.configure(foreground="")
					elif self.correct == "long": # Player attempts to guess a word, but that word isn't long enough
												 # so don't count that against them as they were not trying to guess
												 # the word. They already know the length of the word anyway
						self.status.set("Your guess was not short enough.") 
						self.status_message.configure(foreground="")
					else: # Player guesses incorrectly, because nothing has been done to the "correct" variable
						self.guess_count.set(self.guess_count.get() - 1) # Need to do .set() since it has been created with IntVar()
																		 # unlike conventional Python variables which just use =
						self.guess_letters_list.append(guess.lower()) # Add to previous guesses list to be displayed
						self.guess_letters.set(self.guess_letters_list) # Set the GUI variable equal to the internal variable
						self.status.set("Your guess was incorrect.") 
						self.status_message.configure(foreground=self.incorrect_color)
						self.hangman_count += 1

					if self.guess_count.get() == 1: # Accounting for minor grammar error
						self.guess_label.configure(text="You have {} guess left.".format(self.guess_count.get())) 
						# Update GUI widget, because the variable is inserted
						# through .format() and is not a text variable
					else:
						self.guess_label.configure(text="You have {} guesses left.".format(self.guess_count.get())) 

					# Win condition check
					if self.hidden_word_l == list(self.random_word): # Check if the displayed word
																	 # is now equal to the list form of the generated word
						self.win_message = random.choice(self.win_message_list) # May be different every time the player wins
						self.declare_message.set(self.win_message) # Set declaration message accordingly to show the player has won

					# Lose condition check
					if self.guess_count.get() <= 0: # If the player has no guesses left, they have lost
												 	# Less than or equal to sign is used just in case something goes wrong with
												 	# the subtraction of guesses during the game
						self.declare_message.set(self.lose_message) # Set declaration message accordingly to show the player has lost
						self.hidden_word_l = list(self.random_word) # Reveal the word in its entirety
						self.hidden_word.set(self.hidden_word_l)
						self.guess_label.configure(text="You have no guesses left.") 

			elif guess == "": # If the player's input is nothing
				#print("Enter a letter or a word.")
				self.status.set("Enter a letter or a word.")
				self.status_message.configure(foreground="")
			else: # If the player's input has any amount of other characters
				#print("Give a letter or a word. Numbers and other characters are not allowed.")
				self.status.set("Give a letter or a word. Numbers and other characters are not allowed.")
				self.status_message.configure(foreground="")
			self.guess.set("") # Reset entry field no matter what, so the player doesn't have to delete their input every time they guess

			if self.hangman_count != self.initial_hangman_count: # Check if the hangman count value is the same as the initial count value 
				if self.hangman_count == 6: # Seventh value in the list is the hangman's head, which is 6 in the index
					self.picture_canvas.create_oval(self.coordinates[self.hangman_count], fill=self.colour, width=self.width)
				else:
					self.picture_canvas.create_line(self.coordinates[self.hangman_count], fill=self.colour, width=self.width)

		else: # Otherwise the player has won or lost, so there is no point in doing anything to the GUI
			pass # Do nothing

	def draw_gui(self): # Method to generate the GUI
						# Where most of the widgets in the program are stored

		##############################################################
		##################### 	 DRAWING GUI	######################
		##############################################################

		# Coordinates used to draw the hangman's face, but this will only appear if the player loses the game

		# Creating widgets for the program
		# The ttk. prefix is used to ensure that the widget's appearance remains appropriate depending on the operating system, makes the program look more modern

		# Main container frame
		self.main_frame = ttk.Frame(self.master) # This was originally a label frame. This is now simply a frame because I didn't need to insert any text
		self.main_frame.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="NSEW") # The pack method can't be used to organize the frames as well as the
																							 # grid method can

		# Labels are named differently just so I can keep track of them more easily
		self.reset_button = ttk.Button(self.main_frame, text="Reset", command=self.generate_word) # Button to reset the game by generating a new word
		self.reset_button.grid(row=1, column=3, padx=10, pady=10, columnspan=2, sticky="WE")

		self.title_label = ttk.Label(self.main_frame, text="Hangman", font=self.heading_font) # Heading label
		self.title_label.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

		self.status_label = ttk.Label(self.main_frame, textvariable=self.declare_message) # "Declaration" message to tell the player if they have won or lost
		self.status_label.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

		self.letter_label = ttk.Label(self.main_frame, textvariable=self.hidden_word, font=self.hidden_font)
		self.letter_label.grid(row=3, column=1, padx=30, pady=10, columnspan=2)

		self.guess_label = ttk.Label(self.main_frame, text="You have {} guesses left.".format(self.guess_count.get()), font=self.regular_text) # Label to tell the player how 
																																		 # many guesses they have
		self.guess_label.grid(row=4, column=1, padx=10, pady=10, columnspan=2)
		
		self.guess_entry = ttk.Entry(self.main_frame, textvariable=self.guess) # Entry that takes the player's input
		self.guess_entry.grid(row=5, column=1, padx=10, pady=10, sticky="WE")

		self.guess_button = ttk.Button(self.main_frame, text="Guess", command=lambda : self.check_word(self.guess.get()))
																	  # Button that when pushed, checks the player's input and evaluate to see if it is correct or wrong
																	  # Should clear the entry widget as well so the player doesn't have to delete their input before 
																	  # entering in another one
																	  # Lambda is just here so that the program is able to pass a parameter into the check word method
		self.guess_button.grid(row=5, column=2, padx=10, pady=10, columnspan=2, sticky="WE")

		self.master.bind('<Return>', lambda x: self.check_word(self.guess.get())) # Bind the enter key to the guess button, so that they can push Enter instead of having
																				  # to click the guess button every time the player wants to guess
																				  # The x is there to make sure that the bind() method works

		self.status_message = ttk.Label(self.main_frame, textvariable=self.status) # Message to tell the player whether their guess was correct or wrong, if the word
																				   # they guessed was of a correct length or not, and if it was the correct length,
																				   # say if it's correct
		self.status_message.grid(row=6, column=1, padx=10, pady=10, sticky="WE")
		# Guesses frame
		# Wrong guesses go in here
		self.guess_frame = ttk.LabelFrame(self.master, text="Previous Guesses") 
		self.guess_frame.grid(row=6, column=1, padx=10, pady=10, sticky="NSEW")

		self.guess_letters_label = ttk.Label(self.guess_frame, textvariable=self.guess_letters)
		self.guess_letters_label.grid(row=6, column=1)

		# Picture frame
		self.picture_frame = ttk.LabelFrame(self.master, text="Hangman")
		self.picture_frame.grid(row=6, column=2, padx=10, pady=10, sticky="NSEW")

		self.picture_canvas = Canvas(self.picture_frame, width=100, height=100) # No ttk. prefix because there is none for a Canvas widget 
		self.picture_canvas.grid(row=6, column=1)

root = Tk()
Hangman = HangmanGame(root) # Create an instance of the GUI class
root.mainloop()

