# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
# Example:
# strings = ["hello", "world", "from", "python", "python"]
# queries = ["hello", "alex", "python"]
# results = [1,0,2]


def matchingStrings(strings, queries):
    
    d = {}
    results = [0]*len(queries)
    
    for i in range(len(strings)):
        if strings[i] not in d:
            d[strings[i]] = 1
        else: 
            d[strings[i]] += 1

    for i in range(len(queries)):
        if queries[i] in d:
            results[i] = d[queries[i]]
        else:
            results[i] = (0)

    return results

strings = ["hello", "world", "from", "python", "python"]
queries = ["hello", "alex", "python"]

print(matchingStrings(strings, queries))    # [1,0,2]