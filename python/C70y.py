N = int(input())

answer = []
card = []

for num in range(N):
    card.append(input()) 

for arrynum in range(len(card)):
    count = 0
    different = 0
    for pcards in range(4):
        if card[arrynum].count(card[arrynum][pcards]) == 4:
            print("Four Card")
            break
        elif card[arrynum].count(card[arrynum][pcards]) == 3:
            print("Three Card")
            break
        elif card[arrynum].count(card[arrynum][pcards]) == 2:
            count += 1
        else:
            different += 1

    if count == 4:
        print("Two Pair")
    elif count == 2 and different == 2:
        print("One Pair")
    elif different == 4:
        print("No Pair")