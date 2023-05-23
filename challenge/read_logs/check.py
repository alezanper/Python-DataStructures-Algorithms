
def get_records(file_name):
    errors = {}

    file = open(file_name, "rt", encoding = "utf-8")

    while True:

        line = file.readline()
        if len(line) == 0:
            break

        words = line.split(",")
        error_code = words[1]

        if error_code not in errors:
            errors[error_code] = 1
        else:
            errors[error_code] += 1

    return errors


def main():
    print(get_records('log.txt'))

if __name__ == '__main__':
    main() 