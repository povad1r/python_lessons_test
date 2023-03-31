# def change(num):
#     return str(num)
# print(type(change(42)))

# def bool(a):
#     if a == True:
#         return 'Yes'
#     else:
#         return 'No'

# def reverse(a):
#     return list(int(b) for b in str(a)[::-1])
# print(reverse(35543))

# def game(player_1,player_2):
#     if player_1 == player_2:
#         print('Draw!')
#     elif player_1 == 'scissors' and player_2 == 'paper':
#         print('Player 2 win')
#     elif player_1 == 'paper' and player_2 == 'rock':
#         print('Player 2 win')
#     elif player_1 == 'rock' and player_2 == 'scissors':
#         print('Player 2 win')
#     else:
#         print('Player 2 win')

# game('rock', 'paper')

# s = input()
# def number(s):
#     if str(s).isdigit:
#         return s == True
#     else:
#         return s == False
# print(number)

surname_1 = input('Enter your surname: ')
surname_2 = input('Enter your surname: ')
booking_book = {}
def booking(surname, amount=2):
    booking_book[surname] = amount
    if amount == 4: 
        print(f'Table for 4 people booked by {surname}')
    elif amount == 2: 
        print(f'Table for 2 people booked by {surname}')
    else:
        print('Sorry, but we have tables only for 2 and 4 people')
booking(surname_1)
booking(surname_2, 4)
