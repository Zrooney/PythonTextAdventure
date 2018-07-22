def keyWordChecker(keyWord):
    userInput = input('>')
    keyWord = keyWord.lower().strip()
    while userInput.lower().strip() != keyWord:
        userInput = input('>I didn\'t quite get that Dave \n>')
    return userInput



def listChecker(keyWord):
    counter = len(keyWord)
    loopCount = 0
    userInput = input('>')
    while userInput.lower().strip() != keyWord:
        for itrKeyWord in keyWord:
            loopCount = loopCount + 1
            if itrKeyWord == userInput:
                return userInput
            elif loopCount > counter:
                userInput = input('>I didn\'t quite get that Dave \n>')
                loopCount = 0
                # try:
                #     thing_index = keyWord.index(userInput)
                # except ValueError:
                #     thing_index = -1
                # if thing_index == -1:
                #     print('sorry dave')