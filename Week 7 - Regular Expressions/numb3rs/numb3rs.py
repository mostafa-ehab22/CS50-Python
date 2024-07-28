import re


def main():
    ip_address = input("IPv4 Address: ")
    print(validate(ip_address))


def validate(ip):
    pattern = r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"


    if re.match(fr"^{pattern}\.{pattern}\.{pattern}\.{pattern}$", ip):
        return True
    else:
        return False



if __name__ == "__main__":
    main()
