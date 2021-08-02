def sort_dictionary():
    dictionary = {
        "hello": 10,
        "world": 50,
        "alex": 37
    }

    print(dictionary)
    print(sorted(dictionary))

    sort_dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse = True)

    print(sort_dictionary)
    print(sort_dictionary[0])



sort_dictionary()