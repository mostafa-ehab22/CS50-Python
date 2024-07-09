def main():
    filename = input("File name: ").strip().lower()
    extension = get_media_type(filename)
    print(extension)


def get_media_type(filename):
    if filename.endswith(".gif"):
        return "image/gif"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        return "image/jpeg"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".pdf"):
        return "application/pdf"
    elif filename.endswith(".txt"):
        return "text/plain"
    elif filename.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()
