import os 


while True:
    print("1.Snake an Apple game\n2.PingPong game\n3.Space Shooting game\n4.Tetris game")
    choice = int(input("Which game do you want to play?: "))
    if choice == 1:
        os.system('python snake.py')
    elif choice == 2:
        os.system('python pingpong.py')
    elif choice == 3:
        os.system('python space_shoot.py')
    elif choice == 4:
        os.system('python tetris.py')