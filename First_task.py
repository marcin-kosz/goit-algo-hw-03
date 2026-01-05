from datetime import datetime, date

def get_days_from_today(date_string):
    try:
        nonstring_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        today = date.today()
        days_from_today = nonstring_date - today
        return days_from_today.days
    except ValueError:
        print("Error: type your date as YYYY-MM-DD")
    except TypeError:
        print("Error: type your date as string")
