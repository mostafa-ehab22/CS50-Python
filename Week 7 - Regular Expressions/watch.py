import re


def main():
    user_input = input("HTML: ")
    result = parse(user_input)

    if result:
        print(result)
    else:
        print("No valid YouTube embed URL found")


def parse(string):
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/(.+)"'

    if matches := re.search(pattern,string):
        return f"https://youtu.be/{matches.group(1)}"

    return None


if __name__ == "__main__":
    main()
