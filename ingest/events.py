import datetime
import fastf1 as ff1

def getEventsList(year):
    schedule = ff1.get_event_schedule(year)

    today = datetime.date.today()

    event_names = [f"{row.EventName} (upcoming)" if row.EventDate.date() > today else f"{row.EventName}"
                   for _, row in schedule.drop_duplicates(subset='EventName').iterrows()]

    return event_names