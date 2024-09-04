import time
import turtle


print("hva vil du gå inn på\n1 = kalkulator\n2 = todolist\n3 = tic-tac-toe\n4 = smiley:)")
appvalg = int(input())

if appvalg == 1:

    print("hva vil du regne ut")
    print("prosent av et tall = 1")
    print("gange, dele, plusse eller minuse to tall = 2")


    calcvalg = float(input())


    if calcvalg == 1:

        prosent = 0
        hele_tallet = 0
        svar = 0

        print("hvilken prosent")
        prosent = float(input())

        print ("hvilket tall")
        hele_tallet = float(input())

        prosentdelen = prosent/100 * hele_tallet
        print(prosent, "% av", hele_tallet, "er", round(prosentdelen, 2))


    if calcvalg == 2:

        print("+ = 1\n- = 2\n* = 3\n/ = 4")
        b = int(input())

        print("skriv ett tall")
        tall1 = float(input())

        print("skriv et til tall")
        tall2 = float(input())


        if b == 1:
            svar = tall1 + tall2

        if b == 2:
            svar = tall1 - tall2

        if b == 3:
            svar = tall1 * tall2

        if b == 4:
            svar = tall1 / tall2
    

        print("ditt svar er:", svar)
        print("ble dette riktig?\n1 = ja\n2 = nei")
        riktig = int(input())


        if riktig == 1:
            print("ok lukker programmet")
            time.sleep(3)
    
        if riktig == 2:
            for i in range(4):
                turtle.penup()
                turtle.home()
                turtle.pendown()
                turtle.pensize(30)
                turtle.setheading(i * -90 - 45)
                turtle.forward(100)
                turtle.right(90)
                turtle.forward(100)
            time.sleep(2)


if appvalg == 2:

    todolist = []

    def nyliste():
        global nylistevalg
        print("vil du lage en ny liste?\n1 = ja\n2 = nei")
        nylistevalg = int(input())


    nyliste()

    if nylistevalg == 1:

        while True:    

            print("vil du:\n1 = legge til noe i listen\n2 = fjerne noe fra listen\n3 = slette listen\n4 = avsluttet programmet")
            listevalg = int(input())


            if listevalg == 1:
                print("vennligst skriv inn hva du vil lagre i listen din")
                ting1 = input()
                print("du skrev inn:", ting1)
                print("ble dette riktig?\n1 = ja\n2 = nei")
                riktig = int(input())


                if riktig == 1:
                    todolist.append(ting1)
                    print("setningen ble lagret i todolisten din")
                    print("din liste nå:", todolist)

                if riktig == 2:
                    print("sletter den nå")


            elif listevalg == 2:

                if len(todolist) > 0:

                    print("her er todolisten din nå:")
                    for i in range(len(todolist)):
                        print(f"{i + 1}: {todolist[i]}")
                    
                    print("skriv nummeret til setningen du vil fjerne")
                    slettvalg = int(input())
                    slettvalg = slettvalg - 1


                    if slettvalg >= 0 and slettvalg <len(todolist):
                        fjernetsetning = todolist.pop(slettvalg)
                        print(f"setningen '{fjernetsetning}' ble fjernet fra todolisten")

                    else:
                        print("du må velge en av setningene sitt tall")

                else:
                    print("todolisten din er tom")


            elif listevalg == 3:
                todolist.clear()
                print("todolisten er slettet")


            elif listevalg == 4:
                print("avslutter programmet")
                break


            else:
                print("du må skrive inn ett av de 4 tallene")


if appvalg == 3:
    print("s")

if appvalg == 4:

    pen = turtle.Turtle()


    def eye(col, rad):
        pen.down()
        pen.fillcolor(col)
        pen.begin_fill()
        pen.circle(rad)
        pen.end_fill()
        pen.up()
 

    pen.fillcolor('yellow')
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()
    pen.up()


    pen.goto(-40, 120)
    eye('white', 15)
    pen.goto(-37, 125)
    eye('black', 5)
    pen.goto(40, 120)
    eye('white', 15)
    pen.goto(40, 125)
    eye('black', 5)


    pen.goto(0, 75)
    eye('black', 8)


    pen.goto(-40, 85)
    pen.down()
    pen.right(90)
    pen.circle(40, 180)
    pen.up()


    pen.goto(-10, 45)
    pen.down()
    pen.right(180)
    pen.fillcolor('red')
    pen.begin_fill()
    pen.circle(10, 180)
    pen.end_fill()
    pen.hideturtle()
    time.sleep(5)