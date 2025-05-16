import validators

def main():
    print(validator(input("What's your email address? ")))


def validator(s):
    if response := validators.email(s):
        response = "Valid"
    else:
        response = "Invalid"
    return(response)


if __name__ == "__main__":
    main()
