from django import forms
from .models import Booking
from datetime import datetime, timedelta

active_fields = ('sauna', 'entry_date', 'entry_time', 'quantity', 'hours')


class NewBooking(forms.ModelForm):
    class Meta:
        min_date = datetime.now()
        max_date = datetime.now() + timedelta(days=21)
        min_time = datetime.now() + timedelta(minutes=5)

        min_date_month = "0" + str(min_date.month) if len(str(min_date.month)) == 1 else str(min_date.month)
        max_date_month = "0" + str(max_date.month) if len(str(max_date.month)) == 1 else str(max_date.month)
        min_day_month = "0" + str(min_date.day) if len(str(min_date.day)) == 1 else str(min_date.day)
        max_day_month = "0" + str(max_date.day) if len(str(max_date.day)) == 1 else str(max_date.day)
        min_date_str = str(min_date.year) + "-" + min_date_month + "-" + min_day_month
        max_date_str = str(max_date.year) + "-" + max_date_month + "-" + max_day_month

        time_now_hour = "0" + str(min_time.hour) if len(str(min_time.hour)) == 1 else str(min_time.hour)
        time_now_minute = "0" + str(min_time.minute) if len(str(min_time.minute)) == 1 else str(min_time.minute)
        time_now = str(time_now_hour) + ":" + str(time_now_minute)

        model = Booking
        widgets = {
            "sauna": forms.Select(attrs={'class': 'form-control rounded 3'}),
            "entry_date": forms.TextInput(attrs={'class': 'rounded 3', 'type': 'date', "min": min_date_str, "max": max_date_str, "value": min_date_str}),
            "entry_time": forms.TextInput(attrs={'class': 'rounded 3', 'type': 'time', "min": "00:00", "max": "23:59", "value": time_now})
        }
        fields = active_fields


class EditBooking(forms.ModelForm):
    class Meta:
        model = Booking
        fields = active_fields
        widgets = {
            "user": forms.Select(attrs={'class': 'form-control rounded 3'}),
            "sauna": forms.Select(attrs={'class': 'form-control rounded 3'}),
            "entry_date": forms.TextInput(attrs={'class': 'rounded 3', 'type': 'date'}),
            "entry_time": forms.TextInput(attrs={'class': 'rounded 3', 'type': 'time'})
        }