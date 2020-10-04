import pygame

pygame.init()  # open game
screen = pygame.display.set_mode((500, 500))  # screen size
pygame.display.set_caption("XO")  # game title
clock = pygame.time.Clock()  # FPS clock
bg = pygame.image.load("BackGroundWithGrid.jpg")  # game BackGround
pygame.display.set_icon(pygame.image.load("icon.png"))  # setting the game icon
Oimage = pygame.image.load('O.png')
Ximage = pygame.image.load('X.png')
chalkBoardBackGround = pygame.image.load(
    "BackGround.jpg")  # chalk Board without the tiles
font = pygame.font.SysFont('comicsans', 60)  # the font we are typing with


def checkEqual(lst):  # return True if each element in the list havs the same value
    return lst[1:] == lst[:-1]


def drawX(screen, x, y):
    screen.blit(Ximage, (x+15, y+15))


def drawO(screen, x, y):
    screen.blit(Oimage, (x+15, y+15))


def drawXandO():  # draw the XO grid
    global drawPositions

    screen.blit(bg, (0, 0))
    if StartTurn == p1.turn:
        player1Turn = font.render("player 1 ", 1, (255, 255, 255))
        screen.blit(player1Turn, (0, 0))
    else:
        player2Turn = font.render("player 2 ", 1, (255, 255, 255))
        screen.blit(
            player2Turn, (500 - player2Turn.get_width(), 0))
    for rows in drawPositions:
        for drawPosition in rows:
            if drawPosition[0] != -1 and drawPosition[1] != -1:
                if drawPosition[2] == True:
                    drawX(screen, drawPosition[0], drawPosition[1])

                elif drawPosition[2] == False:
                    drawO(screen, drawPosition[0], drawPosition[1])

    pygame.display.update()


def gameOver():  # game Over Screen Data
    global StartTurn, winner, p1, p2, gridRow, gridColumn, drawPositions, gridRowFull
    gridRowFull = 0
    p1.turn = not p1.turn
    p2.turn = not p2.turn
    winner = None
    playAgainButton.value = False
    QuitButton.value = False
    for i in range(3):  # initializing the grid wth plank spaces (None)
        gridRow[i] = [-1, -1, -1]
        gridColumn[i] = [-1, -1, -1]
        drawPositions[i] = [[-1, -1, -1], [
            -1, -1, -1], [-1, -1, -1]]
    StartTurn = not StartTurn


def drawgameOver():  # draw the Game Over screen
    global QuitButton
    global playAgainButton

    screen.blit(chalkBoardBackGround, (0, 0))
    playAgainButton.draw(screen)
    QuitButton.draw(screen)

    player1Score = font.render(
        "player 1: " + str(p1.score), 1, (255, 255, 255))
    player2Score = font.render(
        "player 2: " + str(p2.score), 1, (255, 255, 255))

    screen.blit(player1Score, (0, 0))
    screen.blit(player2Score, (500-player2Score.get_width(), 0))
    pygame.display.update()


class player(object):  # player Object
    def __init__(self):
        self.score = 0
        self.turn = 0


class button():  # button Object
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textColour = (255, 255, 255)
        self.value = None

    def draw(self, win):
        # Call this method to draw the button on the screen
        pygame.draw.rect(win, self.color, (self.x, self.y,
                                           self.width, self.height), 0)

        text = font.render(self.text, 1, self.textColour)
        win.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                        self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


# game loop
running = True
gridColumn = [[], [], []]  # XO Column grid
gridRow = [[], [], []]  # XO Row grid
gridRowFull = 0
gridDiagonals = [[], []]  # XO Diagonals
drawPositions = [[], [], []]
for i in range(3):  # initializing the grid wth plank spaces (None)
    gridRow[i] = [-1, -1, -1]
    gridColumn[i] = [-1, -1, -1]
    drawPositions[i] = [[-1, -1, -1], [
        -1, -1, -1], [-1, -1, -1]]


position = []

QuitButton = button((0, 0, 0), 195, 240, 110, 80, "QUIT")
QuitButton.value = False  # as the Quit Button is not clicked
playAgainButton = button((0, 0, 0), 115, 146, 270, 70, "PLAY AGAIN")
playAgainButton.value = True  # as the play again Button is already clicked
StartTurn = True  # X starts first
winner = None  # indicates the winner
p1 = player()
p1.turn = True  # player 1 is the X for the first game
p2 = player()
p2.turn = False  # player 2 is the O for the first game

drawXandO()
while running:
    clock.tick(30)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION and playAgainButton.value == False:
            hoverPos = pygame.mouse.get_pos()

            if QuitButton.isOver(hoverPos):
                QuitButton.color = (255, 255, 255)
                QuitButton.textColour = (0, 0, 0)
            else:
                QuitButton.color = (0, 0, 0)
                QuitButton.textColour = (255, 255, 255)

            if playAgainButton.isOver(hoverPos):
                playAgainButton.color = (255, 255, 255)
                playAgainButton.textColour = (0, 0, 0)
            else:
                playAgainButton.color = (0, 0, 0)
                playAgainButton.textColour = (255, 255, 255)
            drawgameOver()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            if playAgainButton.value == True:

                if clickPos[0] > 0 and clickPos[1] > 0 and clickPos[0] < 160 and clickPos[1] < 176 and gridRow[0][0] == -1:
                    position = [0, 0]
                    drawPositions[0][0] = [0, 20, StartTurn]
                elif clickPos[0] > 0 and clickPos[1] > 176 and clickPos[0] < 160 and clickPos[1] < 321 and gridRow[1][0] == -1:
                    position = [1, 0]
                    drawPositions[1][0] = [0, 176, StartTurn]

                elif clickPos[0] > 0 and clickPos[1] > 321 and clickPos[0] < 160 and clickPos[1] < 500 and gridRow[2][0] == -1:
                    position = [2, 0]
                    drawPositions[2][0] = [0, 321, StartTurn]
                elif clickPos[0] > 160 and clickPos[1] > 0 and clickPos[0] < 315 and clickPos[1] < 176 and gridRow[0][1] == -1:
                    position = [0, 1]
                    drawPositions[0][1] = [160, 20, StartTurn]

                elif clickPos[0] > 160 and clickPos[1] > 176 and clickPos[0] < 315 and clickPos[1] < 321 and gridRow[1][1] == -1:
                    position = [1, 1]
                    drawPositions[1][1] = [160, 176, StartTurn]

                elif clickPos[0] > 160 and clickPos[1] > 321 and clickPos[0] < 315 and clickPos[1] < 500 and gridRow[2][1] == -1:
                    position = [2, 1]
                    drawPositions[2][1] = [160, 321, StartTurn]

                elif clickPos[0] > 315 and clickPos[1] > 0 and clickPos[0] < 500 and clickPos[1] < 176 and gridRow[0][2] == -1:
                    position = [0, 2]
                    drawPositions[0][2] = [315, 20, StartTurn]

                elif clickPos[0] > 315 and clickPos[1] > 176 and clickPos[0] < 500 and clickPos[1] < 321 and gridRow[1][2] == -1:
                    position = [1, 2]
                    drawPositions[1][2] = [315, 176, StartTurn]

                elif clickPos[0] > 315 and clickPos[1] > 321 and clickPos[0] < 500 and clickPos[1] < 500 and gridRow[2][2] == -1:
                    position = [2, 2]
                    drawPositions[2][2] = [315, 321, StartTurn]

                else:
                    position = [-1, -1]
                    continue

                gridRow[position[0]][position[1]] = StartTurn
                gridColumn[position[1]][position[0]] = StartTurn
                StartTurn = not StartTurn
                drawXandO()

            elif playAgainButton.value == False:
                if clickPos[0] > QuitButton.x and clickPos[1] > QuitButton.y and clickPos[0] < QuitButton.x + QuitButton.width and clickPos[1] < QuitButton.y + QuitButton.height:
                    running = False
                if clickPos[0] > playAgainButton.x and clickPos[1] > playAgainButton.y and clickPos[0] < playAgainButton.x + playAgainButton.width and clickPos[1] < playAgainButton.y + playAgainButton.height:
                    playAgainButton.value = True

                    StartTurn = not StartTurn
                    drawXandO()

    gridDiagonals[1] = [gridRow[0][2], gridRow[1]
                        [1], gridRow[2][0]]  # filling grid Diagonals
    gridDiagonals[0] = [gridRow[0][0], gridRow[1][1], gridRow[2][2]]

    for i in range(len(gridRow)):
        if - 1 not in gridRow[i]:  # check the rows
            if checkEqual(gridRow[i]):
                winner = gridRow[i][0]
            gridRowFull += 1  # check if the grid is full but no one won
        if - 1 not in gridColumn[i]:  # check the columns
            if checkEqual(gridColumn[i]):
                winner = gridColumn[i][0]
        if i < 2 and - 1 not in gridDiagonals[i]:  # check the diagonals
            if checkEqual(gridDiagonals[i]):
                winner = gridDiagonals[i][0]
        if i == 2 and gridRowFull != 3:
            gridRowFull = 0

    if winner != None:
        if winner == p1.turn:
            p1.score += 1
        else:
            p2.score += 1
        gameOver()
        drawgameOver()

    elif winner == None and playAgainButton.value == True and gridRowFull == 3:
        gameOver()
        drawgameOver()

pygame.quit()
