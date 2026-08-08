import fastf1 as ff1

# Get a specific session from an event
# year: the championship year of the session (ie. 2025)
# gp: the event that the session was in (ie. "Silversone", 1)
# session: the specific session to get (ie. FP1, Q, R)
def getSession(year, gp, session):
    session = ff1.get_session(year, gp, session)
    session.load()
    return session