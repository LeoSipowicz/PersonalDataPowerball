import random
import sys


def hasDuplicates(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

def randomLottoBalls():
    seed = random.randrange(sys.maxsize)
    rng = random.Random(seed)

    duplicates = True

    while duplicates:
        ball1 = rng.randrange(1, 69)
        ball2 = rng.randrange(1, 69)
        ball3 = rng.randrange(1, 69)
        ball4 = rng.randrange(1, 69)
        ball5 = rng.randrange(1, 69)
        if hasDuplicates([ball1, ball2, ball3, ball4, ball5]):
            duplicates = True
        else:
            duplicates = False

    print("lottoballs seed was:", seed)

    return sorted([ball1, ball2, ball3, ball4, ball5])


def randomLottoPowerBall():
    seed = random.randrange(sys.maxsize)
    rng = random.Random(seed)

    powerball = rng.randrange(1, 26)

    print("powerball seed was:", seed)
    return powerball
