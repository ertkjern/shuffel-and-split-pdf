from PyPDF2 import PdfFileMerger
from random import *

numberOfPages = 20
pageCounter = 0

while pageCounter < numberOfPages:
    merger = PdfFileMerger()

    totalCharCards = 17
    totalTechCards = 51

    charCardsInDeck = 4
    techCardsInDeck = 31

    # Create char cards
    i = 0
    while i < charCardsInDeck:
        randomNumber = randint(0, totalCharCards)
        merger.append(open('char/' + str(randomNumber) + '.pdf', 'rb'))
        i += 1

    # Add char back card
    merger.append(open('CharacterCardBack.pdf', 'rb'))

    # Create Tech cards
    i = 0
    while i < techCardsInDeck:
        randomNumber = randint(0, totalTechCards)
        merger.append(open('tech/' + str(randomNumber) + '.pdf', 'rb'))
        i += 1

    # Add tech card back
    merger.append(open('TechCardBack.pdf', 'rb'))

    with open('result/result' + str(pageCounter) + '.pdf', 'wb') as fout:
        merger.write(fout)
    
    print('Generated PDF result' + str(pageCounter) + '.pdf')
    pageCounter +=1
