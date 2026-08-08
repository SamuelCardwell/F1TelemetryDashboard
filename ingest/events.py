import datetime
import fastf1 as ff1

# Returns a list of the events in a championship
# year: the championship year of the events to get (ie. 2025)
def getEventsList(year):
    schedule = ff1.get_event_schedule(year)

    today = datetime.date.today()

    event_names = [f"{row.EventName} (upcoming)" if row.EventDate.date() > today else f"{row.EventName}"
                   for _, row in schedule.drop_duplicates(subset='EventName').iterrows()]

    return event_names



# Returns event type (ie. "Race", "Sprint", "Testing")
# year: the championship year of the event (ie. 2025)
# gp: the event of (ie. "Silversone", 1)
def getEventSessions(year, gp):
    if gp == 'Pre-Season Testing':
        event = ff1.get_testing_event(year, 1)
        print("weird stuff might happen, will check and fix later")
    else:
        event = ff1.get_event(year, gp)

    # print(event.EventFormat)

    if event.EventFormat == 'conventional':
        return ['FP1', 'FP2', 'FP3', 'Q', 'R']
    elif event.EventFormat == 'sprint' or event.EventFormat == 'sprint_qualifying':
        return ['FP', 'SQ', 'S', 'Q', 'R']         # not sure if ids are right
    else:
        print("error: unknown event format")
        return []




# Get a specific session from an event
# year: the championship year of the session (ie. 2025)
# gp: the event that the session was in (ie. "Silversone", 1)
# session: the specific session to get (ie. FP1, Q, R)
def getSession(year, gp, session):
    schedule = ff1.get_session(year, gp, session)