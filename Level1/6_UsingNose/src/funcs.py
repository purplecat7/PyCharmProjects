def add (first, second):
    """
    add two numbers
    :param first: number
    :param second: number
    :return: added number
    """
    result = first + second

    return result

def open_file():
    try:
        open('file/missing.text')
    except FileNotFoundError as e:
        print ("woops!" + e.strerror)
        raise

def main():
    try:
        print(add(1,2))
        print(add(3,4))
        open_file()
    except Exception as e:
        print("main failed" + str(e))


if __name__ == "__main__":
    main()
    main()