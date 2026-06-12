app = input("File name: ").lower().strip()

if app.endswith(".gif"):
    print("image/gif")
elif app.endswith(".jpg") or app.endswith(".jpeg"):
    print("image/jpeg")
elif app.endswith(".png"):
    print("image/png")
elif app.endswith(".pdf"):
    print("application/pdf")
elif app.endswith(".txt"):
    print("text/plain")
elif app.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

