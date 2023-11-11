from datetime import date, datetime, timedelta
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")


def get_birthdays_per_week(users):
    if not users:
      return {}
    # Реалізуйте тут домашнє завдання
    now = date.today()
    current_week_day = now.weekday()
    user_birthday = []
    res = {day: [] for day in WEEKDAYS}
    end_date = now + timedelta(days=7)
    for user in users:
        birthday = user.get('birthday').replace(year=now.year)
        if birthday < now:
            birthday = birthday.replace(year=now.year + 1)
        if now <= birthday <= end_date:
            user_birthday.append(user)
    for user in user_birthday:
        result = user.get('birthday').replace(year=now.year).weekday()
        try:
                user_happy_day = WEEKDAYS[result]
        except IndexError:
                user_happy_day = WEEKDAYS[0]
        res[user_happy_day].append(user.get('name'))
    filtered_res = {day: value for day, value in res.items() if value}
    return filtered_res



if __name__ == "__main__":
    users = [{"name": "Jan Koum", "birthday": datetime(1976, 11, 11).date()}, {"name": "Julia", "birthday": datetime(1986, 11, 10).date()}]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
