#-------------------------------------------------#
# Title: Pickling and Functions (Homework 7)
# Dev: Catherine Warren
# Date: July 25-29, 2013
# ChangeLog: (Who, When, What)
#   none yet
#-------------------------------------------------#

#-- Data --#
# declare variables and constants

import pickle, random, io

# I read about pickling in the textbook. I did read some other pages about
# pickling just to ensure I was on the right track:
# http://wiki.python.org/moin/UsingPickle
# http://docs.python.org/2/library/pickle.html#pickle-example
# http://stackoverflow.com/questions/7501947/understanding-pickling-in-python
# http://stackoverflow.com/questions/11218477/how-to-use-pickle-to-save-a-dict
# http://pymotw.com/2/pickle/

# I imported the random module so that later I can generate a random card
# from the deck.

# I imported io because I was having a hard time unpickling the file without it.

strFileName = "C:\\_PythonClass\\TarotCards.pkl" # The name and path of the pickled data file
TarotCards= {} # A dictionary of Tarot cards and their divinatory meanings

#-- Processing --#

def LoadTarotData(TarotCards):
    """Load a pickled Python dictionary"""
    try:
        pkl_file = io.open(strFileName, 'rb')
        TarotCards = pickle.load(pkl_file)
        pkl_file.close()
        return TarotCards
    except Exception as e:
        raise e

    # I added a try/except to the file loading part in case the filepath was corrupted
    # or missing.

def DisplayTarotData(TarotCards):
    """ Display all cards to user """
    print("******* Tarot Cards ********")
    print(TarotCards)
    print("***********************************")
    # I never call this function... but I like having it, just in case.
    # Someday I will make this program better, and I might need to use it then!

def PrintTarotReading(numberOfCards):
     for name, meaning in random.sample(TarotCards.items(), numberOfCards):
            print ("{lhs} : {rhs}".format(lhs=name, rhs=meaning))

def Main():
    """ Coordinates I/O and actions for this script """
    global strFileName
    global TarotCards
    try:
        # Loading the dictionary data into memory
        TarotCards = LoadTarotData(strFileName)
        # The try / except is to catch errors.

        # Display one random card and its meaning
        print("Your daily reading \n")
        PrintTarotReading(1)
        print("\nCome back tomorrow for another daily reading!")

        # I researched random functions for the above part...
        # http://stackoverflow.com/questions/4859292/how-to-get-a-random-value-in-python-dictionary
        # http://answers.yahoo.com/question/index?qid=20091021050807AAaUA5L
        # http://bytes.com/topic/python/answers/41803-how-can-i-randomly-choose-keys-dictionary

        # I had a difficult time with the function to pick a random card.
        # It seemed I triggered every error in the book! And a few more!
        # Finally I found that I had to convert from dictionary to a list before
        # I could use the random.choice function. D'oh!
        # reading = random.choice(list(TarotCards.items())) is the first
        # way I tried to print out the card choice, but it had too many extra
        # characters.

    except Exception as e:
        print("There was a unexpected error!")
        print("Python's error info: ")
        print(e)

    # The except exception as e part turned out to be REALLY useful,
    # since it told me specifically what was wrong each time I errored out.
    # I must have generated dozens of errors, all told, while getting it this far.
    # Who knew 'pick a card, any card' would be so complicated! :)

    # In the future I want to write a function to choose 10 cards from the deck
    # and display them to the user in the standard 10-card Celtic spread,
    # together with information about what each position means.

Main()
