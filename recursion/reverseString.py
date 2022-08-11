def revString(word):
    if word == "":
        return ""
    
    part = revString(word[1:])
    print(part)
    first = word[0:1]
    result = part + first
    return result

def main():
    print(revString("Alexander"))

if __name__ == "__main__":
    main() 