# a = dict()

months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

report_date = '21.06.2022'

month = int(report_date[3:5])

month_name = months.get(month)

print('Report from', month_name)

# a = months.pop(3)
# print(a)

# d = months.pop(12)
# print(d)
# currencies = {
#     '$': 39.5,
#     '€': 42.00,
#     '£': 48.00
# }

# print(currencies.get('PLN', 'Currency doesn`t exist'))

# months[6] = 'June'
# months[7] = 'July'
# months[8] = 'August'
# months[9] = 'September'
# months[12] = 'December'