from models import UserAccount


def reset_daily_limit():
    print("Daily Limit Reset")
    UserAccount.objects.all().update(daily_limit=1000)