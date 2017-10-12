'''
this is a story based // text based adventure game test
'''

key = 0

def mainGate():
    input('You stand before a great and old gate, covered in twisted vines \n rotted wood')
    input('Behind you is the thick forest through which you have traveled')
    print()
    print('1 = Open the gate \n2 = Look around \n3 = Head Back \n4 = Go deeper into the woods')
    print()
    action = str(input('What do you do? '))

    if action == '1':
        if key >= 1:
            print('You slide the key into the lock and turn it \nit opens with ease')
            winGame()
        else:
            print('You push against the gate but it will not budge')
            print('You notice a small key hole hidden behind the thick vines')
            print()
            print()
            mainGate()

    elif action == '2':
        print()
        mainGate()

    elif action == '3':
        print()
        print('You decide to turn around and head back home')
        loseGame()

    elif action == '4':
        print('You decide to head deeper into the woods \nleaving the old gate behind for now')
        print()
        print('You soon come to a quiet grassy clearing')
        goDeeper()

    else:
        print('Please enter 1,2,3 or 4')
        mainGate()

def goDeeper():
    input('The air is still. Shafts of sunlight break through the canopy above the clearing. \nIn the middle of the clearing is a small moss covered stump')
    print()
    print('1 = Investigate the stump \n2 = Head back to the gate \n3 = Look around')
    print()
    action = int(input('What do you do? '))

    if action == 1:
        global key
        key =+ 1
        print('In a hollow in the stump you find an old rusty key. You pick it up and keep it')
        goDeeper()

    if action == 2:
        print('You decide to head back to the gate')
        print()
        if key >= 1:
            print('Maybe this key will work in the gate')
            print()
        else:
            print()
            mainGate()
        print()
        mainGate()

def winGame():
    print('YOU WIN!!')
    for x in range(25):
        print('!')
    print('Great Work!')

def loseGame():
    print('YOU LOSE!!')
    for x in range(25):
        print('*')
    print('Oh well')
    runAgain()

def runAgain():
    print()
    _input = str(input('Play Again? y/n '))
    if _input == 'y':
        mainGate()
    else:
        print('Thanks for playing')



mainGate()
