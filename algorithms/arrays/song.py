# phrase = "Every breath you take Every move you make"
# station = "boom"

def is_possible(phrase, station):

    phrase_split = phrase.lower().split(" ")
    station_length = len(station)

    i = 0
    for word in phrase_split:
        if (station[i] in word):
            i += 1
        if i >= station_length:
            break
    
    if i == station_length:
        return True
    else:
        return False


print(is_possible("Every breath you take Every move you make", "boom"))