
print('===================================21 CARD GAME=================================')
import random
def shuffledDeck():
    return random.shuffle(deck)
def dealCard(deck,participant):
       participant=deck.pop(0)
       return participant
def total(Κ):
    x=len(Κ)
    price=0
    if player[0]==11 and player[1]==11:
        price=21
    elif x==5:
        for i in range(0,x):
            price+=Κ[i]
        if price <=21:
            price=21
    else:
        for i in range(0,x):
            price+=Κ[i]
    return price
def compareHands(houseprice, playerprice):
    if houseprice>=playerprice:
        return -1
    elif houseprice<playerprice:
        return 1
def printHistory(history):
    names = '%-*s%-*s%-*s%-*s%-*s%-*s'
    numbers = '%-*s%-*s%-*s%-*s%-*s%-*s'
    print ('=' *70)
    print('                       HISTORY "21 CARD GAME"')
    print ('_' *70)
    print (names % (8, 'ROUND',8, 'BET($)',10,'PLAYER',8,'MOTHER',10,'WINNER',15,'BANK($)'))
    print ('_' *70)
    for i in range(history[0]):
        if history[3][i]!=0:
            print (numbers % (8,i+1, 8,history[1][i],10,history[2][i],8,history[3][i],10,history[4][i],15, history[5][i]))
            print ('_' *70)
        else:
            print (numbers % (8,i+1, 8,history[1][i],10,history[2][i],8,'',10,history[4][i],15, history[5][i]))
            print ('_' *70)
    print ('=' *70)





r=input('For New game press "n" or for Continue previous game "c"') 
while r!='c' and r!='n':
    r=input('For New game press "n" or for Continue previous game "c"')

if r=='c':
    file=open('history.txt','r')
    hh1=file.read()
    hh2=hh1.split()
    file.close()
    if int(hh2[len(hh2)-3])>=30:
        r=input('For New game press "n" or for Exit game press "x"') 
        while r!='x' and r!='n':
            r=input('For New game press "n" or for Exit game press "x"')
    else:
        file=open('history.txt','r')
        hh1=file.read()
        hh2=hh1.split()
        file.close()
        if int(hh2[len(hh2)-2])==0 :
            r=input('For New game press "n" or for Exit game press "x"') 
            while r!='x' and r!='n':
                r=input('For New game press "n" or for Exit game press "x"')
        else:
            playerbankprice=int(hh2[len(hh2)-1])
if r=='n':
    playerbankprice=eval(input('Give me your money in bank'))
    while playerbankprice<=0 :
        playerbankprice=eval(input('Give me your money in bank'))
T=0

while r=='c' or r=='n' :
    history=[]
    for i in range (7):
        history.append('')
    ROUND=0
    BET=[]
    PLCARD=[]
    MCARD=[]
    WINNER=[]
    BNK=[]
    M=1
    if r=='c':
        file=open('history.txt','r')
        pp1=file.read()
        pp2=hh1.split()
        ro=int(pp2[0])
        file.close()
        ROUND=int(pp2[0])
        for i in range (1,ro+1):
            BET.append(int(pp2[i]))
        ro1=ro
        for i in range (ro1+1,ro1+ro+1):
            PLCARD.append(int(pp2[i]))
        ro1=ro1+ro
        for i in range (ro1+1,ro1+ro+1):
            MCARD.append(int(pp2[i]))
        ro1=ro1+ro
        for i in range (ro1+1,ro1+ro+1):
            WINNER.append(pp2[i])
        ro1=ro1+ro
        for i in range (ro1+1,ro1+ro+1):
            BNK.append(int(pp2[i]))
        ro1=ro1+ro
        M=2
    if r=='n':    
        startprice=10 
        print('Startprice is :',startprice)
    else:
        startprice=BNK[len(BNK)-1]  
        print('Startprice is :',startprice)
    while startprice<30 and startprice!=0:  
        houseprice=0
        ROUND+=1
        deck=[2,2,2,2,3,3,3,3,4,4,4,4,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11]#ΕΔΩ ΟΡΙΖΩ ΤΟ DECK ΟΠΟΥ 11 ΕΙΝΑΙ ΤΟ 'Α'
        R=[]
        shuffledDeck()
        participant=''
        player=[]
        player.append(dealCard(deck,participant))
        if player[0]!=11:
            R.append(random.choice('♣♦♥♠'))
            print ('You got:',player[0],R[0])
        else :
            R.append(random.choice('♣♦♥♠'))
            print ('You got: A',R[0])
        bet=eval(input('bet money:'))
        if M==1:
            while bet>=startprice or bet>playerbankprice or bet <0 :
                bet=eval(input('bet money:'))
            M=2
        else:
            while bet>startprice or bet>playerbankprice or bet <0 :
                bet=eval(input('bet money:'))
        BET.append(bet)
        player.append(dealCard(deck,participant))
        if player[1]!=11:
            R.append(random.choice('♣♦♥♠'))
            while player[1]==player[0]and R[0]==R[1] :
                R[1]=random.choice('♣♦♥♠')
            print('You got:',player[1],R[1])
        else :
            R.append(random.choice('♣♦♥♠'))
            while player[1]==player[0]and R[0]==R[1] :
                R[1]=random.choice('♣♦♥♠')
            print('You got: A',R[1])
        playerprice=total(player)
        print('Your total now is:',playerprice)
        if playerprice==21 :
            print('YOU WIN!!!!!')
            k='W'
        else:
            k=''
            while k!='Y' and k!='N':
                k=input('You want card? press "Y" for YES or "N" for NO:')
            i=2 
            while k=='Y':
                player.append(dealCard(deck,participant))
                R.append(random.choice('♣♦♥♠'))
                for q in range(i):
                    while player[q]==player[i] and R[q]==R[i]:
                        R[i]=random.choice('♣♦♥♠')                    
                if player[i]!=11:
                    print ('You got:',player[i],R[i])
                else :
                    print ('You got: A',R[i])
                playerprice=total(player)
                print('Your total now is:',playerprice)
                if playerprice<21:
                    k=input('You want card? press "Y" for YES or "N" for NO:')
                if playerprice>21:
                    k='L'
                elif playerprice==21:
                    k='W'
                elif player[0]==7 and player[1]==7 and player[2]==7:
                    k='WIN ALL'
                i+=1
            pl=i-1
            h=0
            if k!='L' and k!='W'and k!=''and k!='WIN ALL':
                R1=[]
                house=[]
                house.append(dealCard(deck,participant))
                R1.append(random.choice('♣♦♥♠'))
                for q in range(pl):
                    while player[q]==house[h] and R[q]==R1[h]:
                        R1[h]=random.choice('♣♦♥♠')
                if house[h]!=11:
                    print('House got:',house[h],R1[h])
                else :
                     print('House got: A',R1[h])
                h+=1
                house.append(dealCard(deck,participant))
                R1.append(random.choice('♣♦♥♠'))
                for q in range(pl):
                    while player[q]==house[h] and R[q]==R1[h]:
                        R1[h]=random.choice('♣♦♥♠')
                if house[h]!=11:
                    print('House got:',house[h],R1[h])
                else :
                     print('House got: A',R1[h])
                houseprice=total(house)
                print('House total now is:',houseprice)
                p=houseprice
                while p<17:
                    h+=1
                    house.append(dealCard(deck,participant))
                    R1.append(random.choice('♣♦♥♠'))
                    for q in range(pl):
                        while player[q]==house[h] and R[q]==R1[h]:
                            R1[h]=random.choice('♣♦♥♠')
                    if house[h]!=11:
                        print('House got:',house[h],R1[h])
                    else :
                        print('House got: A',R1[h])
                    houseprice=total(house)
                    print('House total now is:',houseprice)
                    p=houseprice
                if houseprice>21:
                    print('MOTHER',houseprice,'MOTHER BURN AND YOU WIN!!!!')
                    k='W'
                elif houseprice<=21:
                    k=''
                else:
                    print('YOU LOST')
                print('MOTHER HAVE:',houseprice)
                print('YOU HAVE:',playerprice)
        MCARD.append(houseprice)
        PLCARD.append(playerprice)
        if k=='': 
            T=compareHands(houseprice, playerprice)
        if T==1 or k=='W':
            print('YOU WIN!!!!! TAKE YOUR BET ')
            startprice-=bet
            playerbankprice+=bet
            WINNER.append('PLAYER')
        elif T==-1 or k=='L':
            print('YOU LOST! GIVE ME YOUR BET')
            startprice+=bet
            playerbankprice-=bet
            WINNER.append('MOTHER')
        elif k=='WIN ALL':
            playerbankprice+=startprice
            startprice=0
            WINNER.append('PLAYER')
        print("Bank's balance now is:",startprice,'$')
        print("Player Bank's balance now is:",playerbankprice,'$')
        BNK.append(startprice)
        history[0]=ROUND
        history[1]=BET
        history[2]=PLCARD
        history[3]=MCARD
        history[4]=WINNER
        history[5]=BNK
        history[6]=playerbankprice
        file=open('history.txt','w')
        file.write(str(history[0]))
        file.write('\n')
        for i in range(len(history[1])):
            file.write(str(history[1][i]))
            file.write(" ")
        file.write('\n')           
        for i in range(len(history[2])):
            file.write(str(history[2][i]))
            file.write(" ")
        file.write('\n')
        for i in range(len(history[3])):
            file.write(str(history[3][i]))
            file.write(" ")
        file.write('\n')
        for i in range(len(history[4])):
            file.write(str(history[4][i]))
            file.write(" ")
        file.write('\n')
        for i in range(len(history[5])):
            file.write(str(history[5][i]))
            file.write(" ")
        file.write('\n')
        file.write(str(history[6]))        
        file.close()
        if startprice!=0:
            r=input('For Continue pres "c",for  print History press "h" or for exit game press "x":') 
            while r!='c' and r!='h' and r!='x':
                r=input('For Continue pres "c",for  print History press "h" or for exit game press "x":')  
            if r=='x':
                break
            elif r=='h':
                printHistory(history)
                r=input('For Continue pres "c" or for exit game press "x":') 
                while r!='c' and r!='x':
                    r=input('For Continue pres "c" or for exit game press "x":')
                if r=='x':
                    break
        elif startprice==0:
            r=input('For Start new game "n",for  print History press "h" or for exit game press "x":') 
            while r!='n' and r!='h' and r!='x':
                r=input('For Start new game "n",for  print History press "h" or for exit game press "x":')  
            if r=='x':
                break
            elif r=='h':
                printHistory(history)
                r=input('For Start new game "n" or for exit game press "x":') 
                while r!='n' and r!='x':
                    r=input('For Start new game "n" or for exit game press "x":')
                if r=='x':
                    break
        if playerbankprice==0 and (r=='c' or r=='h'):
            playerbankprice=eval(input('YOU MAST GIVE MONEY IN YOUR BANK :'))
            while playerbankprice<=0:
                playerbankprice=eval(input('YOU MAST GIVE MONEY IN YOUR BANK :'))
        
    if startprice>=30 and r!='x':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LAST ROUND~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        houseprice=0
        deck=[2,2,2,2,3,3,3,3,4,4,4,4,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11]
        R=[]
        shuffledDeck()
        participant=''
        player=[]
        player.append(dealCard(deck,participant))
        if player[0]!=11: 
            R.append(random.choice('♣♦♥♠'))
            print ('You got:',player[0],R[0])
        else :
            R.append(random.choice('♣♦♥♠'))
            print ('You got: A',R[0])
        bet=eval(input('bet money:'))
        if M==1:
            while bet>=startprice or bet>playerbankprice or bet <0 :
                bet=eval(input('bet money:'))
            M=2
        else:
            while bet>startprice or bet>playerbankprice or bet <0 :
                bet=eval(input('bet money:'))
        BET.append(bet)
        player.append(dealCard(deck,participant))
        if player[1]!=11:
            R.append(random.choice('♣♦♥♠'))
            while player[1]==player[0]and R[0]==R[1] : 
                R[1]=random.choice('♣♦♥♠')
            print('You got:',player[1],R[1])
        else :
            R.append(random.choice('♣♦♥♠'))
            while player[1]==player[0]and R[0]==R[1] :
                R[1]=random.choice('♣♦♥♠')
            print('You got: A',R[1])
        playerprice=total(player)
        print('Your total now is:',playerprice)
        if playerprice==21 :
            print('YOU WIN!!!!!')
            k='W'
        else:
            k=''
            while k!='Y' and k!='N':
                k=input('You want card? press "Y" for YES or "N" for NO:')
            i=2 
            while k=='Y':
                player.append(dealCard(deck,participant))
                R.append(random.choice('♣♦♥♠'))
                for q in range(i):
                    while player[q]==player[i] and R[q]==R[i]:
                        R[i]=random.choice('♣♦♥♠')                    
                if player[i]!=11:
                    print ('You got:',player[i],R[i])
                else :
                    print ('You got: A',R[i])
                playerprice=total(player)
                print('Your total now is:',playerprice)
                if playerprice<21:
                    k=input('You want card? press "Y" for YES or "N" for NO:')
                if playerprice>21:
                    k='L'
                elif playerprice==21:
                    k='W'
                elif player[0]==7 and player[1]==7 and player[2]==7:
                    k='WIN ALL'
                i+=1
            pl=i-1
            h=0
            if k!='L' and k!='W'and k!=''and k!='WIN ALL':
                R1=[]
                house=[]
                house.append(dealCard(deck,participant))
                R1.append(random.choice('♣♦♥♠'))
                for q in range(pl):
                    while player[q]==house[h] and R[q]==R1[h]:
                        R1[h]=random.choice('♣♦♥♠')
                if house[h]!=11:
                    print('House got:',house[h],R1[h])
                else :
                     print('House got: A',R1[h])
                h+=1
                house.append(dealCard(deck,participant))
                R1.append(random.choice('♣♦♥♠'))
                for q in range(pl):
                    while player[q]==house[h] and R[q]==R1[h]:
                        R1[h]=random.choice('♣♦♥♠')
                if house[h]!=11:
                    print('House got:',house[h],R1[h])
                else :
                     print('House got: A',R1[h])
                houseprice=total(house)
                print('House total now is:',houseprice)
                p=houseprice
                while p<17:
                    h+=1
                    house.append(dealCard(deck,participant))
                    R1.append(random.choice('♣♦♥♠'))
                    for q in range(pl):
                        while player[q]==house[h] and R[q]==R1[h]:
                            R1[h]=random.choice('♣♦♥♠')
                    if house[h]!=11:
                        print('House got:',house[h],R1[h])
                    else :
                        print('House got: A',R1[h])
                    houseprice=total(house)
                    print('House total now is:',houseprice)
                    p=houseprice
                if houseprice>21:
                    print('MOTHER',houseprice,'MOTHER BURN AND YOU WIN!!!!')
                    k='W'
                elif houseprice<=21:
                    k=''
                else:
                    print('YOU LOST')
                print('MOTHER HAVE:',houseprice)
                print('YOU HAVE:',playerprice)
        MCARD.append(houseprice)
        PLCARD.append(playerprice)
        if k=='': 
            T=compareHands(houseprice, playerprice)
        if T==1 or k=='W':
            print('YOU WIN!!!!! TAKE YOUR BET ')
            startprice-=bet
            playerbankprice+=bet
            WINNER.append('PLAYER')
        elif T==-1 or k=='L':
            print('YOU LOST! GIVE ME YOUR BET')
            startprice+=bet
            playerbankprice-=bet
            WINNER.append('MOTHER')
        elif k=='WIN ALL':
            playerbankprice+=startprice
            startprice=0
            WINNER.append('PLAYER')
        print('Startprice now is :',startprice,'$')
        
        if 10-startprice<0: 
            lost=startprice-10
            print('YOU HAVE LOST :',lost,'$')
            print ('HOUSE HAVE WIN:',lost,'$')
        else:
            print('YOU HAVE WIN:',10,'$')
            print ('HOUSE HAVE LOST:',10,'$')
        print("Bank's balance now is:",startprice,'$')
        print("Player Bank's balance now is:",playerbankprice,'$')
        ROUND+=1
        BNK.append(startprice)
        history[0]=ROUND
        history[1]=BET
        history[2]=PLCARD
        history[3]=MCARD
        history[4]=WINNER
        history[5]=BNK
        history[6]=playerbankprice
        file=open('history.txt','w')
        file.write(str(history[0]))
        file.write('\n')
        for i in range(len(history[1])):
            file.write(str(history[1][i]))
            file.write(" ")
        file.write('\n')           
        for i in range(len(history[2])):
            file.write(str(history[2][i]))
            file.write(" ")
        file.write('\n')
        for i in range(len(history[3])):
            file.write(str(history[3][i]))
            file.write(" ")
        file.write('\n')
        for i in range(len(history[4])):
            file.write(str(history[4][i]))
            file.write(" ")
        file.write('\n')
        for i in range(len(history[5])):
            file.write(str(history[5][i]))
            file.write(" ")
        file.write('\n')
        file.write(str(history[6]))        
        file.close()
        r=input('For Start new game "n",for  print history press "h" or for exit game press "x":') 
        while r!='n' and r!='h' and r!='x':
            r=input('For Start new game "c",for  print history press "h" or for exit game press "x":')  
        if r=='h':
            printHistory(history)
            r=input('For Start new game "n" or for exit game press "x":') 
            while r!='n' and r!='x':
                r=input('For Start new game "n" or for exit game press "x":')
            if r=='x':
                break
    if playerbankprice==0 and (r=='c' or r=='h'):
        playerbankprice=eval(input('YOU MAST GIVE MONEY IN YOUR BANK :'))
        while playerbankprice<=0:
            playerbankprice=eval(input('YOU MAST GIVE MONEY IN YOUR BANK :'))
print('====================================GAME OVER!!!!!!=============================')
