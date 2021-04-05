import re


def main():
    date = "17/May/2015"
    keep_word = "GET /presentations"
    keep_status = " 200 "
    counter = 0
    hour = date + ':' + "\w\w"
    checking_text = open('apache_logs', 'r')

    for line in checking_text:
        if date in line and keep_word in line and keep_status in line:
            match = re.search(hour, str(line))
            if (int(match.group().replace("17/May/2015:", '')) >= 1) and (int(match.group().replace("17/May/2015:", '')) <= 21):
                counter += 1
    print(counter)
    checking_text.close()


if __name__ == '__main__':
    main()
