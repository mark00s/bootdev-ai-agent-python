from functions.get_file_content import get_file_content


def tests():
    result = get_file_content("calculator", "main.py")
    print("\nResult for 'main.py' file:")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print("\nResult for 'pkg/calculator.py' file:")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print("\nResult for '/bin/cat' file:")
    print(result)


if __name__ == "__main__":
    tests()
