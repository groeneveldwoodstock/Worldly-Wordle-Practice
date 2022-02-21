import tkinter
import tkinter.messagebox
import tkinter.font as tkFont
import random
from wordlist import words

root = tkinter.Tk()
root.title("Wordly Practice")
root.geometry("500x440")
root['bg']='#806040'
fontStyle = tkFont.Font(family="Lucida Grande", size=14)
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()
#global variables
word = random.choice(words)
guesses = ["_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _"]
count = 0
attempts = 1
welcome = '''Welcome to wordly practice! \n ************************** \nTry and guess a 5 letter word in 6 tries.\nThere are over 5000 random 
words used in this game!\n---------------------------------\nGuess a 5 letter word to begin.'''
alphabetlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
guessscreen = '''GUESS A WORD
--------------------------------------------
Letters in the word are left in the alphabet.
Letters not in the word \nare removed from the alphabet.
Letters in the correct place are added to the word.\n'''
attemptslist = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
attemptssummary = ''
guesslist = []
wordlist = []
letterslist =[]
lettersused = ''

def makeguess(e):
  get_guess()
    
def close():
  root.destroy()

def get_word():
  global word, guesses, count, attempts, alphabetlist, alphabet, letterslist, lettersused
  letterslist =[]
  lettersused = ''
  text.delete(1.0,tkinter.END)
  text.insert(tkinter.END, welcome)
  word = random.choice(words)
  guesses = ["_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _", "_ _ _ _ _"]
  count = 0
  attempts = 1
  alphabetlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  alphabet_label.config(text="Possible letters: "+ alphabet)
  letterslist =[]
  lettersused = ''
  letters_label.config(text = "Letters guessed used in the word: " + lettersused)
    
def checkguess(list1, list2):
  global guesses
  response = ""
  newguess = ""
  for letter in list2:
    newguess += letter
  for i in range(len(list1)):
    if list1[i] == list2[i]:
      response += list1[i] + " "
    else:
      response +="_ " 
  guesses[count] = response + "guessed " + newguess

def get_guess():
  global word, guesses, count, attempts, attemptslist, attemptssummary, alphabet, guesslist, wordlist, letterslist, lettersused, alphabetlist
  text.delete(1.0,tkinter.END)
  theguess = entry_guess.get()

  if len(theguess) == 5:
    entry_guess.delete(0, tkinter.END)
    guess = theguess
    guesslist = list(guess)
    wordlist = list(word)
    text.insert(tkinter.END, guessscreen)
    checkguess(wordlist, guesslist)
    for i in range(6):
      text.insert(tkinter.END, guesses[i] + "\n")
    alphabet = ""
    checkwordlist = list(guess)
    for letter in alphabetlist:
      if letter in checkwordlist and letter in wordlist:
        letter = letter
        if letter in checkwordlist and letter not in letterslist:
            letterslist.append(letter)
            lettersused = ''
            for letters in letterslist:
                lettersused += letters
      elif letter in checkwordlist and letter not in wordlist:
        alphabetlist.remove(letter)
      else: 
        letter= letter
    for letter in alphabetlist:
      alphabet += letter
  else:
    tkinter.messagebox.showwarning(title="Message", message="Guess not in word list. Guess Again")
    count -=1
    entry_guess.delete(0, tkinter.END)
    for i in range(6):
      text.insert(tkinter.END, guesses[i] + "\n")

  if guesslist == wordlist or count ==5: 
    if guesslist == wordlist:
        text.insert(tkinter.END, "You are correct in " + str(attempts)+ " attempts!\n")
        attemptslist.append(attempts)
        sum = 0
        for numbers in attemptslist:
          sum += numbers
        averageAttempts = sum/len(attemptslist)
        text.insert(tkinter.END,"Average number of attempts: " + str(averageAttempts)+ "\n")
    else:
        text.insert(tkinter.END,"Sorry only 6 tries allowed.\n")
        text.insert(tkinter.END, "It was " + word + "!\n")      
  alphabet_label.config(text="Possible letters: "+ alphabet)
  letters_label.config(text = "Letters guessed used in the word: " + lettersused)
  attempts +=1
  count +=1
  
# Create GUI
text = tkinter.Text(frame_tasks, font=fontStyle, bg = '#D8CFC2', height=14, width=50)
text.pack(side=tkinter.LEFT)
text.insert(tkinter.END, welcome)
# available letters in alphabet
alphabet_label = tkinter.Label(root, fg = '#964B00',font=(fontStyle,15, 'bold'), bg = '#D8CFCF', text = "Possible letters: " + alphabet, height=1, width=50)
alphabet_label.pack()
letters_label = tkinter.Label(root, fg = '#006600',font=(fontStyle,15, 'bold'), bg = '#D8CFCF', text = "Letters guessed used in the word: " + lettersused, height=1, width=50)
letters_label.pack()

entry_guess = tkinter.Entry(root, bg = '#FBE6CA', width=50)
entry_guess.pack()
#button for to guess
button_add_guess = tkinter.Button(root, highlightbackground='#c49251', text="Submit Guess", activebackground = "#bfa524", width=48, height=3, command = get_guess)
button_add_guess.pack()
# Button for new word
new_button = tkinter.Button(root, highlightbackground='#c49130',text="New Word", fg='#964B00', width=25, command=get_word)
new_button.pack()
# Button for closing
exit_button = tkinter.Button(root, text="Exit", highlightbackground='#d0b561', fg='#801', width=25, command=close)
exit_button.pack()
# bind enter button to make a guess
root.bind('<Return>',makeguess)
#run it
root.mainloop()
