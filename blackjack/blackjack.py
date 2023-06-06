import random


adding = ""
game = "y"
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]




while game=="y":
    player_cards =[]
    computer_cards = []
    total_p = 0
    total_c =0
    c_p = 0
    c_c = 0
    for i in range(2):
        rndp = random.choice(cards)
        player_cards.append(rndp)
        rndc = random.choice(cards) 
        computer_cards.append(rndc)

    print("Your cards: "+str(player_cards))
    print("Computer's first card: "+str(computer_cards[0]))

    adding = input("Type 'y' to get another card, type 'n' to pass: ")
    while adding == "y":
        add = random.choice(cards)
        player_cards.append(add)
        print("Your final hand: "+str(player_cards))

        for i in computer_cards:
            total_c += i
        if(total_c <17):
            add = random.choice(cards)
            computer_cards.append(add)


        for i in player_cards:
            total_p += i
        else:
            adding = input("Type 'y' to get another card, type 'n' to pass: ")
    total_p = 0
    total_c =0

    print("Your final hand: "+str(player_cards))
    print("Computer's final hand: "+str(computer_cards))

    for i in player_cards:
        total_p += i
        if(total_p > 21):
            for i in player_cards:
                if i == 11:
                    total_p += 1
                else:
                    total_p += i
    
    for i in computer_cards:
        total_c += i

    if(total_p>21):
            print("You lose!")
            game = input("Dou you want to play a game of Blackjack? Type 'y' or 'n': ")

    elif total_p > total_c:
        print("You win!")
        game = input("Dou you want to play a game of Blackjack? Type 'y' or 'n': ")

    elif total_p < total_c:
        print("You lose!")
        game = input("Dou you want to play a game of Blackjack? Type 'y' or 'n': ")
    
    else:
        for i in player_cards:
            c_p+=1
        for i in computer_cards:
            c_c+=1
        
        if c_p < c_c:
            print("You win!")
            game = input("Dou you want to play a game of Blackjack? Type 'y' or 'n': ")

        elif c_p > c_c:
            print("You lose!")
            game = input("Dou you want to play a game of Blackjack? Type 'y' or 'n': ")

        else:
            print("Draw!")
            game = input("Dou you want to play a game of Blackjack? Type 'y' or 'n': ")
            


        


    



