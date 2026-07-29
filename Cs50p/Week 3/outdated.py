months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date:").strip()

        if date[0].isalpha():
            parts = date.split()

            if len(parts) < 3:
                continue

            day_str = parts[1]
            if not day_str.endswith(","):
                continue

            day = int(day_str.replace(",", ""))
            if not (1 <= day <= 31):
                continue
            month = months.index(parts[0]) + 1
            year = int(parts[2])

            print(f"{year}-{month:02}-{day:02}")
            break

        elif date[0].isnumeric():
            numbers = date.split("/")

            if len(numbers) != 3:
                continue

            month = int(numbers[0])
            day = int(numbers[1])
            year = int(numbers[2])

            if not (1 <= month <= 12) or not (1 <= day <= 31):
                continue

            print(f"{year}-{month:02}-{day:02}")
            break

    except ValueError:
        continue
    except EOFError:
        break
