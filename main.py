import re


def main():
    date = "17/May/2015"
    keep_word = "GET"
    keep_status = " 200 "
    counter = 0
    hour = date + ':' + "\w\w"

    with open("apache_logs", 'rb') as readfile:
        checking_text = readfile.readlines()

    for line in checking_text:
        if (bytes(date, encoding='utf8') in line) and (bytes(keep_word, encoding='utf8') in line) and (bytes(keep_status, encoding='utf8') in line):
            match = re.search(hour, str(line))
            if (int(match.group().replace("17/May/2015:", '')) >= 1) and (int(match.group().replace("17/May/2015:", '')) <= 21):
                counter += 1
    print(counter)


if __name__ == '__main__':
    main()
