
def main():
    name = input("Enter file name: ").lower().strip()

    if ".gif" in name:
        print("image/gif", end="")
    elif ".jpg" in name:
        print("image/jpeg", end="")
    elif ".jpeg" in name:
        print("image/jpeg", end="")
    elif ".png" in name:
        print("image/png", end="")
    elif ".pdf" in name:
        print("application/pdf", end="")
    elif ".txt" in name:
        print("text/plain", end="")
    elif ".zip" in name:
        print("application/zip", end="")
    else:
        print("application/octet-stream")

main()
