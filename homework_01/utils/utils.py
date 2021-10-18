import random as r

MIN_NUMBER = 89000000000
MAX_NUMBER = 89999999999

def get_random_name():
    names = ["Valera ", "Dima ", "Oleg ", "Alex ", "Andrey "]
    lastnames = ["Vinokurshin ", "Ivanov ", "Petrov ", "Sidorov "]
    patronymics = ["Sergeevich", "Stanislavovich", "Olegovich", "Yurievich"]
    
    return lastnames[r.randint(0, 3)] + names[r.randint(0, 4)] + patronymics[r.randint(0, 3)]

def get_random_number():
    return str(r.randint(MIN_NUMBER, MAX_NUMBER))