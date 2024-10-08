import time
import turtle


while True:

    print("hva vil du gå inn på\n1 = kalkulator\n2 = todolist\n3 = tic-tac-toe\n4 = smiley:)\n5 = avslutt")
    appvalg = int(input())

    if appvalg == 1:
        #calc app
        while True:

            print("hva vil du regne ut")
            print("prosent av et tall = 1")
            print("gange, dele, plusse eller minuse to tall = 2")

            calcvalg = int(input())


            if calcvalg == 1:

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

            tilbake = int(input("Vil du gå tilbake til hovedmenyen? 1 = Ja, 2 = Nei "))
            if tilbake == 1:
                break


    if appvalg == 2:
        #todolist app
        while True:

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


            tilbake = int(input("Vil du gå tilbake til hovedmenyen? 1 = Ja, 2 = Nei "))
            if tilbake == 1:
                break


    if appvalg == 3:
        #tic-tac-toe

        brett = [str(x+1) for x in range(9)]

        def print_brett():
            rad1 = "| {} | {} | {} |".format(brett[0], brett[1], brett[2])
            rad2 = "| {} | {} | {} |".format(brett[3], brett[4], brett[5])
            rad3 = "| {} | {} | {} |".format(brett[6], brett[7], brett[8])

            print()
            print(rad1)
            print(rad2)
            print(rad3)
            print()


        def bruker_bevegelse(icon):
            if icon == "X":
                nummer = 1

            elif icon == "O":
                nummer = 2

            while True:

                print("Din tur spiller {}".format(nummer))
                valg = int(input("Skriv inn ditt trekk (1-9): ").strip())

                if brett[valg - 1] not in ["X", "O"]:
                    brett[valg - 1] = icon
                    break
                else:
                    print()
                    print("Den plassen er allerede okkupert! Velg en ny en")
        

        def vinner(icon):
            if  (brett[0] == icon and brett[1] == icon and brett[2] == icon) or \
                (brett[3] == icon and brett[4] == icon and brett[5] == icon) or \
                (brett[6] == icon and brett[7] == icon and brett[8] == icon) or \
                (brett[0] == icon and brett[3] == icon and brett[6] == icon) or \
                (brett[1] == icon and brett[4] == icon and brett[7] == icon) or \
                (brett[2] == icon and brett[5] == icon and brett[8] == icon) or \
                (brett[0] == icon and brett[4] == icon and brett[8] == icon) or \
                (brett[2] == icon and brett[4] == icon and brett[6] == icon):
                return True
            
            else:
                return False
        

        def likt():
            if all(x in ["X", "O"] for x in brett): 
                return True
            
            else:
                return False


        while True:
            print_brett()
            bruker_bevegelse("X")
            print_brett()

            if vinner("X"):
                print("X vinner!")
                break

            elif likt():
                print("Det er uavgjort!")
                break

            bruker_bevegelse("O")
            if vinner("O"):
                print_brett()
                print("O vinner!")
                break

            elif likt():
                print("Det er uavgjort!")
                break


        tilbake = int(input("Vil du gå tilbake til hovedmenyen? 1 = Ja, 2 = Nei "))
        if tilbake == 1:
            break


    if appvalg == 4:
        #smiley app
        while True:

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

            tilbake = int(input("Vil du gå tilbake til hovedmenyen? 1 = Ja, 2 = Nei "))
            if tilbake == 1:
                break

    
    if appvalg == 5:
        print("avslutter...")
        time.sleep(1)
        break