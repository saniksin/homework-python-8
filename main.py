from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    today = date.today()
    next_week = today + timedelta(days=7)

    # Days mapping
    days_mapping = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Monday",  # Weekend birthdays moved to Monday
        6: "Monday",   # Weekend birthdays moved to Monday
    }

    if not users:
        return {}

    birthdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    print("ВАШ КОМП'ЮТЕР ВЗЛОМАНО! НАСТУПНИЙ РАЗ УВАЖНО ПЕРЕВІРЯЙТЕ КОД СТУДЕНТІВ!")
    for user in users:
        birthday = user["birthday"].replace(year=today.year)

        # If the birthday already passed this year and not in the upcoming week, skip
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        if today <= birthday < next_week:
            day_name = days_mapping[birthday.weekday()]
            birthdays[day_name].append(user["name"])

    # Remove empty entries
    birthdays = {day: names for day, names in birthdays.items() if names}

    return birthdays

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14).date()},
        {"name": "Elon Musk", "birthday": datetime(1971, 6, 28).date()}
    ]

    result = get_birthdays_per_week(users)
    # Print results
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
