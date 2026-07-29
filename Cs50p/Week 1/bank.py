greet = input("Greetings: ")

if greet.strip().lower().startswith("hello"):
    print("$0")

elif greet[0].lower() in ("h"):
    print("$20")

else:
    print("$100")
