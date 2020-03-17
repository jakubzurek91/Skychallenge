# import datetime
# def school_break(start = datetime.datetime(2020, 3, 11, 8, 0), nb_of_lessons = 6, free_time = 5):
#     for i in range(nb_of_lessons):
#         end = start + datetime.timedelta(0, 2700)
#         print(f"{start.time()} - {end.time()}")
#         start = end + datetime.timedelta(0, free_time * 60)
#
# if __name__=='__main__':
#     a = input("podaj godzine: ").split(":")
#     nb_of_lessons = int(input("podaj ilość lekcji: "))
#     free_time = int(input("długość przerwy: "))
#     a[0] = int(a[0])
#     a[1] = int(a[1])
#     start = datetime.datetime(2020, 3, 11, a[0], a[1])
#     school_break(start, nb_of_lessons, free_time)
#     # school_break(datetime.datetime(2020,3,11,12,30),8,15)

def sortowanie():
    slowa = input("podaj słowa: ").split(', ')
    slowa.sort()
    for i in slowa:
        print(i)

sortowanie()