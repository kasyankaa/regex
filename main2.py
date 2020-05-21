import re

if __name__ == '__main__':
    log_file = open('log_file', 'r', encoding="ISO-8859-1")
    pattern = r"^.+\[+(01\/Jul\/1995:00:[1][0-9]:[0-5][0-9]|[2]0:00).+\].+NASA.+$"
    pattern2 = r"^.+\[+(01\/Jul\/1995:00:[1][0-9]:[0-5][0-9]|[2]0:00).+\].+$"
    number_of_wanted_strings = 0
    matches = False
    for string in log_file:
        if re.search(pattern, string) is not None:
            number_of_wanted_strings += 1
            matches = True
        elif re.search(pattern2, string) is None and matches == True:
            break

    print(number_of_wanted_strings)
