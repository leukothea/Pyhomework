import pickle

f = open("C:\\_PythonClass\\TarotCards.pkl", "rb")
TarotCards = pickle.load(f)
f.close()

print(TarotCards)
