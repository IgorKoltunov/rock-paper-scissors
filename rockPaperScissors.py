""" Rock, Paper Scissors game against Random.
"""

import random

CHOICE_LIST = ['Rock', 'Paper', 'Scissors']
RESULT_LIST = ['Draw', 'Human Wins', 'AI Wins']

def play_round(humanHand, aiHand):
    

    if humanHand == aiHand:
        result = RESULT_LIST[0]
    if humanHand == CHOICE_LIST[0] and aiHand == CHOICE_LIST[1]:
        result = RESULT_LIST[2]
    if humanHand == CHOICE_LIST[0] and aiHand == CHOICE_LIST[2]:
        result = RESULT_LIST[1]
    if humanHand == CHOICE_LIST[1] and aiHand == CHOICE_LIST[0]:
        result = RESULT_LIST[1]
    if humanHand == CHOICE_LIST[1] and aiHand == CHOICE_LIST[2]:
        result = RESULT_LIST[2]  
    if humanHand == CHOICE_LIST[2] and aiHand == CHOICE_LIST[0]:
        result = RESULT_LIST[2]
    if humanHand == CHOICE_LIST[2] and aiHand == CHOICE_LIST[1]:
        result = RESULT_LIST[1]

    return result
    

def main():
    with open('scoreFile.txt', 'r') as scoreFile:
        line = scoreFile.read().splitlines()
    numbers = line[0].split(',')

    dbScoreHuman = int(numbers[0])
    dbScoreAI = int(numbers[1])
    dbScoreDraw = int(numbers[2])




    numRounds = 1
    round = numRounds
    scoreHuman = 0
    scoreAI = 0
    scoreDraw = 0
   
    
    print('Playing', numRounds, 'rounds of Rock, Paper, Scissors!')
    
    while round != 0:
        humanChoiceDict = {'r': CHOICE_LIST[0], 'p': CHOICE_LIST[1], 's': CHOICE_LIST[2]}
        humanChoice = input('Enter "r" for Rock, "p" for Paper or "s" for Scissors: ')

        humanHand = humanChoiceDict[humanChoice]
        aiHand = random.choice(CHOICE_LIST)

        roundResult = play_round(humanHand, aiHand)
        if roundResult == RESULT_LIST[1]:
            scoreHuman += 1
        if roundResult == RESULT_LIST[2]:
            scoreAI += 1
        if roundResult == RESULT_LIST[0]:
            scoreDraw += 1
        sessionScoreTuple = scoreHuman, scoreAI, scoreDraw
        round -= 1
        print('Human: {} vs AI: {}. {}!'.format(humanHand, aiHand, roundResult))
    
    print('At the end of {} rounds: AI Score: {} vs Human Score {}'.format(numRounds, scoreAI, scoreHuman))



    with open('scoreFile.txt', 'w') as scoreFile:
         print(dbScoreHuman + scoreHuman, dbScoreAI + scoreAI, dbScoreDraw + scoreDraw, sep=",", file=scoreFile)

    
main()
