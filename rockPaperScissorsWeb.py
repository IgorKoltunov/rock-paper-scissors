#!/usr/bin/python3
""" Rock, Paper Scissors game against Random.
"""

import random
import cgi

CHOICE_LIST = ['Rock', 'Paper', 'Scissors']
RESULT_LIST = ['Draw', 'Human Wins', 'AI Wins']


def play_round(humanHand, aiHand):

    if humanHand == aiHand:
        result = RESULT_LIST[0]
    elif humanHand == CHOICE_LIST[0] and aiHand == CHOICE_LIST[1]:
        result = RESULT_LIST[2]
    elif humanHand == CHOICE_LIST[0] and aiHand == CHOICE_LIST[2]:
        result = RESULT_LIST[1]
    elif humanHand == CHOICE_LIST[1] and aiHand == CHOICE_LIST[0]:
        result = RESULT_LIST[1]
    elif humanHand == CHOICE_LIST[1] and aiHand == CHOICE_LIST[2]:
        result = RESULT_LIST[2]  
    elif humanHand == CHOICE_LIST[2] and aiHand == CHOICE_LIST[0]:
        result = RESULT_LIST[2]
    elif humanHand == CHOICE_LIST[2] and aiHand == CHOICE_LIST[1]:
        result = RESULT_LIST[1]
    else:
        return print('Error: Computer got mad about losing and broke. :(')
    return result
    

def main():
    form = cgi.FieldStorage()                 # parse form data
    print('Content-type: text/html\n')        # hdr plus blank line
    print('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5">\n')
    print('<title>Result Page</title>')        # html reply page

    with open('scoreFile.txt', 'r') as scoreFile:
        line = scoreFile.read().splitlines()
    numbers = line[0].split(',')

    dbScoreHuman = int(numbers[0])
    dbScoreAI = int(numbers[1])
    dbScoreDraw = int(numbers[2])

    numRounds = 1
    rounds = numRounds
    scoreHuman = 0
    scoreAI = 0
    scoreDraw = 0
    
    while rounds != 0:
        humanChoiceDict = {'r': CHOICE_LIST[0], 'p': CHOICE_LIST[1], 's': CHOICE_LIST[2]}
        if 'user' not in form:
            return print('<a href="http://www.igorkoltunov.com/share/public/RockPaperScissors/RockPaperScissors.html">Click to Play Again!</a>')
        humanChoice = form['user'].value
        humanChoice = humanChoice.lower()
        humanHand = humanChoiceDict[humanChoice]
        
        aiHand = random.choice(CHOICE_LIST)

        roundResult = play_round(humanHand, aiHand)
        if roundResult == RESULT_LIST[1]:
            scoreHuman += 1
        if roundResult == RESULT_LIST[2]:
            scoreAI += 1
        if roundResult == RESULT_LIST[0]:
            scoreDraw += 1
        rounds -= 1
        print('Human: {} vs AI: {}. <b>{}!</b>'.format(humanHand, aiHand, roundResult))

        dbScoreHuman += scoreHuman
        dbScoreAI += scoreAI
        dbScoreDraw += scoreDraw

        with open('scoreFile.txt', 'w') as scoreFile:
            print(dbScoreHuman, dbScoreAI, dbScoreDraw, sep=",", file=scoreFile)
    print('<br><br>Stats since 09/04/1015:')
    print('<br>{} Games have been played.'.format(dbScoreHuman + dbScoreAI + dbScoreDraw))
    print('<br>Humans Won:', dbScoreHuman)
    print('<br>AI Won:', dbScoreAI)
    print('<br>Ties:', dbScoreDraw)
    if dbScoreAI > dbScoreHuman:
        print("<br><br><b>Computers Are Winning! Don't let this stand!</b>")
    if dbScoreAI == dbScoreHuman:
        print("<br><br>Scores are <b>tied</b>! Here is your chance to make a deference!")

    print('<br><br><a href="http://www.igorkoltunov.com/share/public/RockPaperScissors/RockPaperScissors.html">Click to Play Again!</a>')
        

main()
