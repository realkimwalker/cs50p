def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Must be 2 to 6 characters in length
    if 2 <= len(s) <= 6 and s.isalnum():
        # No periods, spaces, or punctuation marks are allowed
        if s.isalpha():
            return True
        elif s[:2].isalpha() and s[-2:].isdigit():
            # Numbers must be placed at the end
            for i in range(len(s)):
                if s[i].isdigit():
                    if s[i].startswith("0") or s[i:].isalpha():
                        return False
                else:
                    return True


main()
