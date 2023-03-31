# x = 50
# def func():
#     x = 2
#     print('Changing local x on', x)
# func()
# print(x)

# x = 50
# a = 1
# def func():
#     global x, a
#     print('Now x is', x)
#     x = 2
#     print('Changing local x on', x)

# func() 
# print(x)

# def func(a, b=2, c=3):
#     print(f'a = {a}, b = {b}, c = {c}')
# func(c=8, a=3)

# def say(message, times=1):
#     message = message + ' '
#     print(message * times)

# say('Hello', 1)
# say('World', 5)

# def total(a=5, *numbers, **phone_book):
#     print(f'a = {a}')
#     # iterate through the elements in tuple
#     print(f'Args - {numbers}')
#     for single_item in numbers:
#         print(f'Single item - {single_item}')
#     # iterate through the elements in dictionary
#     for firts_part, second_part in phone_book.items():
#         print(firts_part, second_part)
# total(10, 1,2,3,4,5, Jack = 233, Alice = 2332, John = 1111)

subscribers_news = []
subscribers_whats_new = []
subscribers_ads = []
global_list = []
def subscribe(email, is_news=True, is_whats_new=True, is_ads = True):
    global subscribers_ads, subscribers_whats_new, subscribers_news
    if is_news:
        subscribers_news.append(email)
    if is_whats_new:
        subscribers_whats_new.append(email)
    if is_ads:
        subscribers_ads.append(email)

def get_subscribers(subcribers_list, list_name):
    delimeter = '-' * 25
    print(f'На розсилку {list_name} підписалося {len(subcribers_list)} користувачів')
    for user in subcribers_list: 
        print(user)
        print(delimeter)
        print()

subscribe('test@gmail.com')
subscribe('ivanov@ukr.net', True, False, True)
subscribe('ivanova@ukr.net', False, True, True)

get_subscribers(subscribers_news, 'News')
get_subscribers(subscribers_ads, 'Ads')
get_subscribers(subscribers_whats_new, 'Whats new')