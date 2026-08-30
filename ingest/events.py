import datetime
import fastf1 as ff1

# Returns a list of the events in a championship
# year: the championship year of the events to get (ie. 2025)
def getEventsList(year):
    # calls the fastf1 library, aliased as ff1, to get the events in a year
    schedule = ff1.get_event_schedule(year)

    # defines when today is
    today = datetime.date.today()

    # creates a list of the events, is the event is after today then it has (upcoming) tagged to it, otherwise it is just its name
    event_names = [f"{row.EventName} (upcoming)" if row.EventDate.date() > today else f"{row.EventName}"
                   for _, row in schedule.drop_duplicates(subset='EventName').iterrows()]

    # this returns the list of event names
    return event_names



# Returns event session types (ie. "Race", "Sprint", "Quali")
# year: the championship year of the event (ie. 2025)
# gp: the event of (ie. "Silversone", 1)
def getEventSessions(year, gp):
    # checks if the event is pre-season testing, if so then warn the user that is hasn't been implemented yet
    if gp == 'Pre-Season Testing':
        event = ff1.get_testing_event(year, 1)
        print("weird stuff might happen, will check and fix later")
    # otherwise get the event
    else:
        event = ff1.get_event(year, gp)

    # is the event format is a regular race weekend
    if event.EventFormat == 'conventional':
        # return a list of the regular weekend sessions
        return ['FP1', 'FP2', 'FP3', 'Q', 'R']
    # if the event format is a sprint race weekend
    elif event.EventFormat == 'sprint' or event.EventFormat == 'sprint_qualifying':
        # return a list of the sprint race weekend sessions
        return ['FP', 'SQ', 'S', 'Q', 'R']         # not sure if id values are right
    # otherwise its a weird weekend and i don't know what to do
    else:
        print("error: unknown event format")
        return []
