from datetime import date, timedelta, datetime

# my_set_1 = {1, 2, 3, 4, 5, 6, 7}
# my_set_2 = {4, 5, 6, 7, 8, 9, 10}
#
# res = my_set_1 - my_set_2
# print(res)
#
# my_set_1 -= my_set_2
# print(my_set_1)


# a = 'abcdefgh'.split()
# b = ['b']
# print(b > a)
# '''
# '''
# list_1 = [0, 1, 2, 3]
# list_2 = list_1
# list_1.append(4)
# print(list_2)


# tomorrow_day = date.today() + timedelta(days=1)
# tomorrow_begining = datetime(tomorrow_day.year, tomorrow_day.month, tomorrow_day.day)
# tomorrow_end = tomorrow_begining + timedelta(days=1)
# print(tomorrow_begining, tomorrow_end)


# tomorrow = date.today() + timedelta(days=1)
# midnight_today = datetime(tomorrow.year, tomorrow.month, tomorrow.day)
# midnight_tomorrow = midnight_today + timedelta(days=1)
# sql = f'''
#             SELECT datetime, event, user_id FROM reminders
#             WHERE datetime BETWEEN {midnight_today} AND {midnight_tomorrow};
#         '''
#
# print(sql)

import test_1

a = 1

print(test_1.b)
