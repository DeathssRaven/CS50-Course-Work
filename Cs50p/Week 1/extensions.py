name = input("FILE name: ").strip().lower()

if "." in name:
    ext = name.rsplit(".", 1)[1]
else:
    ext = ""

if ext in ("gif",):
    print("image/gif")
elif ext in ("jpg", "jpeg"):
    print("image/jpeg")
elif ext in ("png",):
    print("image/png")
elif ext in ("pdf",):
    print("application/pdf")
elif ext in ("txt",):
    print("text/plain")
elif ext in ("zip",):
    print("application/zip")
else:
    print("application/octet-stream")
