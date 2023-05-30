#!/usr/bin/python3
"""
aaaa
"""


from sys import stdin

statusCode = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

size = 0


def print_stats():
    """
    aaaa
    """
    print("File size: {}".format(size))
    for status in sorted(statusCode.keys()):
        if statusCode[status]:
            print("{}: {}".format(status, statusCode[status]))


if __name__ == "__main__":
    count = 0
    try:
        for line in stdin:
            try:
                items = line.split()
                size += int(items[-1])
                if items[-2] in statusCode:
                    statusCode[items[-2]] += 1
            except:
                pass
            if count == 9:
                print_stats()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()