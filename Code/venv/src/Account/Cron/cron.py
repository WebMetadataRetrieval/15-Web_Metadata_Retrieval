from models import UserAccount
from Metadata.models import Metadata
from django.utils import timezone
import datetime

def reset_daily_limit():
    print("Daily Limit Reset")
    UserAccount.objects.all().update(daily_limit=1000)

def manage_cache():
    seven_days_ago = timezone.now() - datetime.timedelta(days=7)
    old_data = Metadata.objects.filter(timestamp__lt=seven_days_ago)
    print(old_data.count()," records removed!")
    old_data.delete()

def cache_health():
    cnt = Metadata.objects.all().count()
    print(cnt," totel records.")
    if cnt >= 100000:
        older = Metadata.objects.raw('SELECT * FROM metadata_metadata ORDER BY timestamp ASC LIMIT 10000')
        for metadata in older:
            metadata.delete()