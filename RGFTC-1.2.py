"""
Python Certificate: Fall-Winter 2013 Term
Final Project
Iteration 1.2
Catherine Warren

"""

# -- Data -- #
# declare variables and constants. 

import random

# My dictionary will go here. There are 25 cards, each with 4 meanings. The picture + position
# is the key, and its meaning is the value. 

Meaning = {"Cavalier1" : "You will hear pleasant news.", 
"Cavalier2" : "Unexpected happy news.", 
"Cavalier3" : "News that will bring a disappointment.", 
"Cavalier4" : "Unpleasant news.", 
"Clover1" : "Happiness and fulfillment of desires.",
"Clover2" : "Happiness slightly clouded by a misunderstanding.", 
"Clover3" : "Sorrow for a short duration, which will have a satisfactory outcome.", 
"Clover4" : "Considerable grief or disappointment.", 
"Ship1" : "You will receive an inheritance or a winning.",
"Ship2" : "Riches due to trade or labor.",
"Ship3" : "Travel.",
"Ship4" : "Material loss or unsuccessful efforts.",
"House1" : "You will enjoy success in all affairs.",
"House2" : "The right step will bring you success.",
"House3" : "Beware of the people surrounding you.",
"House4" : "Failure in some newly planned project.",
"Firewood1" : "A good state of health.",
"Firewood2" : "Recovery.",
"Firewood3" : "A minor illness.",
"Firewood4" : "A bruise, cut, or illness.",
"Apple1" : "A pleasant happening.",
"Apple2" : "A pleasant unexpected occurrence, a present.",
"Apple3" : "An unpleasant meeting, encounter.",
"Apple4" : "An unpleasant occurrence in the near future.", 
"Snake1" : "A verbal sting by a malicious person.", 
"Snake2" : "Betrayal, unfaithfulness.", 
"Snake3" : "Loss.", 
"Snake4" : "Bitter jealousy.", 
"Hearse1" : "Sickness.", 
"Hearse2" : "A loss of condition, although only temporary.", 
"Hearse3" : "An unquestionable unpleasantness to which you will be subjected or fall prey.", 
"Hearse4" : "You will escape danger in time.", 
"Bouquet1" : "Great success in all affairs.", 
"Bouquet2" : "Winnings.", 
"Bouquet3" : "Fulfillment of a hope.", 
"Bouquet4" : "You will find a means of earning money.", 
"Scythe1" : "Evil fate pursues you.", 
"Scythe2" : "You will hear a threat that will have consequences.", 
"Scythe3" : "You will escape a catastrophe.", 
"Scythe4" : "Quarrel.", 
"Branches1" : "Making up after a quarrel.", 
"Branches2" : "Disagreement in the family.", 
"Branches3" : "A breakup with a close person.", 
"Branches4" : "Tears, an offense.", 
"Birds1" : "Joy, merriment.", 
"Birds2" : "Unexpected pleasure.", 
"Birds3" : "You expect someone not to fulfill a promise and you will be right.", 
"Birds4" : "An obstacle with which you will have to fight.", 
"Boy1" : "Travel in the near future.", 
"Boy2" : "You will find yourself in pleasant company and will have a good time.", 
"Boy3" : "A new friendship is possible.", 
"Boy4" : "An unexpected meeting or a date.", 
"Fox1" : "You are being cunningly deceived.", 
"Fox2" : "A falsity will be revealed.", 
"Fox3" : "It isn't wise to trust a new friendship.", 
"Fox4" : "Be careful not to feel unwarranted trust toward some people.", 
"Bear1" : "With caution, happiness will not elude you.", 
"Bear2" : "Your efforts will bear fruit.", 
"Bear3" : "You will get what you desire, although not in the immediate future.", 
"Bear4" : "Don't have faith in every piece of advice.", 
"Stars1" : "Your guiding star will bring you to your goal.", 
"Stars2" : "Success in dealings.", 
"Stars3" : "Temporary blindness will force you to make a series of mistakes.", 
"Stars4" : "A series of unpleasant occurrences.", 
"Heron1" : "A change in place of residence.", 
"Heron2" : "Circumstances will force you to enter an undesirable path.", 
"Heron3" : "A change in relations with friends.", 
"Heron4" : "An addition to the family.", 
"Dog1" : "You have a faithful and constant friend.", 
"Dog2" : "The help of friends will support you.", 
"Dog3" : "A person you consider a friend is untrue to you.", 
"Dog4" : "A change of friends.", 
"Castle1" : "Fulfillment of hopes, although at the end of your life.", 
"Castle2" : "A refuge in old age.", 
"Castle3" : "A long life.", 
"Castle4" : "A chronic illness.", 
"Forest1" : "Continuous friendship with many worthwhile people.", 
"Forest2" : "Mixing with a purpose in numerous and agreeable society.", 
"Forest3" : "Contact with suspicious people.", 
"Forest4" : "Beware of the nets that are thrown your way.", 
"Mountains1" : "A treacherous enemy is trying to catch you, be on guard.", 
"Mountains2" : "Nearness to a great unpleasantness that can be avoided.", 
"Mountains3" : "After deliberation you will make the right decision.", 
"Mountains4" : "You will receive help from strong people during a difficult moment.", 
"Road1" : "Happy path or road.", 
"Road2" : "A joyful journey.", 
"Road3" : "A lonely and boring road or work.", 
"Road4" : "Difficulties on the road.", 
"Mice1" : "You will find what you have lost.", 
"Mice2" : "An unexpected discovery.", 
"Mice3" : "A theft.", 
"Mice4" : "The stolen goods have disappeared forever.", 
"Heart1" : "Your happiness is in the answer of the person you love.", 
"Heart2" : "Love will ignite your heart.", 
"Heart3" : "Merriment, gaiety, will never leave you.", 
"Heart4" : "You are in agreement with close people.", 
"Ring1" : "A wedding or agreement.", 
"Ring2" : "Engagement to a rich person.", 
"Ring3" : "An interruption of relations between lovers or friends.", 
"Ring4" : "A complete breakup between people in love.", 
"Book1" : "Communication of a secret.", 
"Book2" : "Something that is of importance to you is being hidden from you.", 
"Book3" : "A secret entrusted to you will be disclosed.", 
"Book4" : "Your talkativeness will bring you harm.", 
"Letter1" : "Happiness will come to you from far away.", 
"Letter2" : "Interesting, unexpected news.", 
"Letter3" : "You will hear a long-awaited word.", 
"Letter4" : "Sad news.", 
"Horseshoe1" : "Good fortune awaits you.", 
"Horseshoe2" : "Everything that you undertake in the near future will be successful.", 
"Horseshoe3" : "Your desire will be fulfilled.", 
"Horseshoe4" : "You will walk by happiness not noticing it.", 
"Money1" : "You will receive a substantial sum of money.", 
"Money2" : "You will find success or profit in an undertaking.", 
"Money3" : "An unexpected pleasant windfall.", 
"Money4" : "A long wait before receiving earned money.", 
"Lily1" : "A happy life full of meaning.", 
"Lily2" : "You will know in life faithfulness till death.", 
"Lily3" : "Unearthly happiness.", 
"Lily4" : "Useless doubts about faithfulness, honesty.", 
"Sun1" : "Prosperity, flourishment, life's caress, happiness.", 
"Sun2" : "Warmth and light are within you alone.", 
"Sun3" : "A lack of courage hinders you from obtaining your wish.", 
"Sun4" : "Coldness of the heart will freeze you.", 
"Moon1" : "Although your life is uneventful, you have happiness nonetheless.", 
"Moon2" : "If you are patient, you will obtain that which you desire.", 
"Moon3" : "Do not become despondent over a temporary setback.", 
"Moon4" : "Delay in action will work against you.", 
"Fish1" : "Fortune, especially on the sea.", 
"Fish2" : "If you want success, seek it on the water and not on land.", 
"Fish3" : "Trade will bring profit.", 
"Fish4" : "In a difficult moment you won't sink but will rise to the surface.", 
"Owl1" : "At the present time you want to act unwisely.", 
"Owl2" : "Your cunning schemes will be exposed.", 
"Owl3" : "Your project will be unsuccessful.", 
"Owl4" : "Your plans will not materialize.", 
"Anchor1" : "Success in love; you are loved.", 
"Anchor2" : "Fulfillment of hopes; success on the sea.", 
"Anchor3" : "Disillusionment with the ideal; doubts.", 
"Anchor4" : "Your mistake will be difficult to correct.",
"Handshake1" : "A strong friendship will be a support to you for your entire life.", 
"Handshake2" : "Love will weld you into one with the person you love.", 
"Handshake3" : "The handshake will weaken if you don't make the effort to strengthen it.", 
"Handshake4" : "Your union threatens to come apart.", 
"Angel1" : "A bright, wished-for happiness awaits you.", 
"Angel2" : "Reconciliation will give you joy.", 
"Angel3" : "Love and tenderness will comfort you.", 
"Angel4" : "Heavenly powers will save you from a false step.", 
"Lady1" : "A soft feminine hand will support you in time.", 
"Lady2" : "The helping hand is given to you not in friendship but due to hidden love.", 
"Lady3" : "Don't believe the show of politeness; it is false.", 
"Lady4" : "Having sucked you dry, they will turn away from you.", 
"Horse1" : "You will experience a vivid or traumatic life event.", 
"Horse2" : "Outward appearance and beauty will turn your head.",
"Horse3" : "Hold the reins firmly; otherwise, you will stumble.", 
"Horse4" : "Your feelings will be trampled upon.", 
"Knot1" : "You have tied strong knots for a lifetime.", 
"Knot2" : "The chains binding you will always be sweet.", 
"Knot3" : "You will break the bonds that are entangling you.", 
"Knot4" : "You can achieve freedom only by cutting the Gordian knot.", 
"Cat1" : "Someone will charm you with kindness, which you'll yield to.", 
"Cat2" : "Beware of claws hidden beneath a friendly exterior.", 
"Cat3" : "Having received a blow, you will hide your feelings with dignity.", 
"Cat4" : "You will unexpectedly be badly scratched.", 
"Scales1" : "In your fate, good will outweigh evil.", 
"Scales2" : "Your happiness depends on the decision you make.", 
"Scales3" : "If you maintain your balance, you will come out whole from a predicament.", 
"Scales4" : "Your evil action will have consequences.", 
"Crayfish1" : "Having made too bold a step, you'll back off.", 
"Crayfish2" : "Your pride will be hurt.", 
"Crayfish3" : "Delay is sometimes designed by fate.", 
"Crayfish4" : "Too much haste often defeats the business.", 
"Fire1" : "Fire will envelop your heart.", 
"Fire2" : "Beware of fire, you'll burn your wings.", 
"Fire3" : "Out of the frying pan into the fire.", 
"Fire4" : "You will be warmed by love during difficult, cold days.", 
"Pig1" : "Positively a prosperous and happy year.", 
"Pig2" : " Purely an earthly happiness.", 
"Pig3" : "Your greed will be punished.", 
"Pig4" : "Overindulgence in food will make you sick.", 
"Bridge1" : "A radical change in lifestyle awaits you.", 
"Bridge2" : "You will build a bridge that will draw you together with a loved person.", 
"Bridge3" : "No matter where you go the past will pursue you.", 
"Bridge4" : "If you want freedom, create a bridge of the chasm.",
"Demons1" : "Do not listen to cunning whisperings wishing to hurt you.", 
"Demons2" : "Yielding to the temptation of taking vengeance for an offense, you will only increase the unpleasantness.", 
"Demons3" : "Too much unrestrained merriment occurs before chagrin.", 
"Demons4" : "Your fervor will not lead to any good.", 
"Rooster1" : "Soon you will hear good news.", 
"Rooster2" : "Heart-to-heart sharing of news.", 
"Rooster3" : "A cheerful pastime will force you to forget grief.", 
"Rooster4" : "You will wake up from a sweet sleep to daily activity.", 
"Dagger1" : "You will be protected in time.", 
"Dagger2" : "You will escape danger due to the concern of a friend.", 
"Dagger3" : "You will experience a prick to your pride.", 
"Dagger4" : "Someone will inflict pain on your heart.", 
"Bread1" : "You will be made happy with a present.", 
"Bread2" : "Profit and happiness in the house, success in business affairs.", 
"Bread3" : "Fulfillment of wishes.", 
"Bread4" : "Having received something yourself, do not forget those surrounding you."
}

class Card(object):
    # to define the cards and the rotate method

    def __init__(self, top, right, bottom, left):
        self.picturehalves = [top, right, bottom, left]

    def __repr__(self):
        return "Card(%s)"%self.picturehalves

    def rotate(self):
        # to pop the final tuple out and insert it at the beginning, equalling a quarter turn
        self.picturehalves.insert(0, self.picturehalves.pop())

    def directionStrip(self):
        # to strip out the arrow directionality and return only the image names
        data = [self.picturehalves]
        return [[c[0] for c in group] for group in data]

class Deck(object): 
    # a collection of 25 cards.
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "  "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def printDeck(self):
        return self.cards

class Grid(Deck):
        # define an empty 5x5 grid to hold the 25 cards
        def __init__(self, deck):
            self.deck = deck

        def fill(self):
            self.array = []

            i = 0
            random.shuffle(deck.cards)
            for r in range(5):
                row = []
                for c in range(5):
                    row.append(deck.cards[i])
                    i = i+1
                self.array.append(row)

        def printGrid(self):
            return self.array

        def getCard(self, i, n):
            while i < 6:
                while n < 6:
                    return self.array[i][n].directionStrip()



def PictureMeaning(numberofcards):
# right now this is just to return a random single-picture reading so I know that part works
        for name, meaning in random.sample(Meaning.items(), numberofcards):
                print ("{lhs} : {rhs}".format(lhs=name, rhs=meaning))

                        
# -- Processing -- #

# First, we define 25 card objects with 25 tuples, each composed of four picturehalves. 
# Each picturehalves exists twice and only twice in the set. 
# Directionality must be coded into each picturehalves, because there is neither rhyme nor reason to it.
# So each picturehalves also contains either "clock" for clockwise, or "widdershins" for widdershins (counterclockwise).

ListOfCards = [(("Cavalier", "widdershins"), ("Cat", "clock"), ("Castle", "widdershins"), ("Moon", "widdershins"))
,(("Cavalier", "clock"), ("Fire", "widdershins"), ("Pig", "clock"), ("Owl", "clock"))
,(("Clover", "widdershins"), ("Castle", "clock"), ("Handshake", "clock"), ("Birds", "clock"))
,(("Clover", "clock"), ("Branches", "widdershins"), ("Stars", "widdershins"), ("Hearse", "clock"))
,(("Ship", "clock"), ("Bridge", "widdershins"), ("Knot", "clock"), ("Bouquet", "clock"))
,(("Ship", "widdershins"), ("Mice", "clock"), ("Horse", "clock"), ("Firewood", "widdershins"))
,(("House", "widdershins"), ("Ring", "clock"), ("Heron", "widdershins"), ("Apple", "clock"))
,(("House", "clock"), ("Crayfish", "clock"), ("Scales", "widdershins"), ("Fish", "widdershins"))
,(("Firewood", "clock"), ("Demons", "clock"), ("Fox", "widdershins"), ("Forest", "widdershins"))
,(("Apple", "widdershins"), ("Sun", "clock"), ("Angel", "widdershins"), ("Horseshoe", "widdershins"))
,(("Snake", "clock"), ("Branches", "clock"), ("Scythe", "widdershins"), ("Mountains", "widdershins"))
,(("Snake", "widdershins"), ("Knot", "widdershins"), ("Angel", "clock"), ("Book", "clock"))
,(("Hearse", "widdershins"), ("Lady", "widdershins"), ("Bear", "clock"), ("Moon", "clock"))
,(("Bouquet", "widdershins"), ("Mountains", "widdershins"), ("Letter", "widdershins"), ("Money", "widdershins"))
,(("Scythe", "widdershins"), ("Birds", "widdershins"), ("Ring", "widdershins"), ("Anchor", "clock"))
,(("Boy", "clock"), ("Road", "clock"), ("Sun", "widdershins"), ("Dog", "widdershins"))
,(("Boy", "widdershins"), ("Rooster", "widdershins"), ("Demons", "widdershins"), ("Bread", "clock"))
,(("Fox", "clock"), ("Heart", "clock"), ("Owl", "widdershins"), ("Scales", "clock"))
,(("Bear", "widdershins"), ("Mice", "widdershins"), ("Money", "clock"), ("Fire", "clock"))
,(("Stars", "clock"), ("Book", "widdershins"), ("Road", "widdershins"), ("Dagger", "clock"))
,(("Heron", "clock"), ("Handshake", "widdershins"), ("Lily", "clock"), ("Dog", "clock"))
,(("Forest", "clock"), ("Crayfish", "widdershins"), ("Horseshoe", "clock"), ("Bridge", "clock"))
,(("Heart", "widdershins"), ("Rooster", "clock"), ("Lily", "widdershins"), ("Cat", "widdershins"))
,(("Letter", "clock"), ("Anchor", "clock"), ("Fish", "clock"), ("Pig", "widdershins"))
,(("Lady", "clock"), ("Dagger", "widdershins"), ("Bread", "widdershins"), ("Horse", "widdershins"))]

# Populate the deck with the ListOfCards. 

deck = Deck()

for x in ListOfCards:
    deck.add(Card(*x))

# Just to ensure the data works... 

print "Before shuffling, the deck is: "
print deck

# Fill a 5x5 grid with the shuffled cards and print it.  

grid = Grid(Deck)

grid.fill()

grid.shuffle

print "After adding the deck's cards to the grid and shuffling it, the 5x5 array is: "
print grid.array


# Starting at the top left, we compare the card to the immediate right and immediately beneath it for 
# a match in picturehalves. 

print grid.getCard(0, 0)


# print PictureMeaning(1)
# this is just to prove that I can return a random reading

