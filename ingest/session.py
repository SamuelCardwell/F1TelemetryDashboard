import fastf1 as ff1

# Get a specific session from an event
# year: the championship year of the session (ie. 2025)
# gp: the event that the session was in (ie. "Silversone", 1)
# session: the specific session to get (ie. FP1, Q, R)
def getSession(year, gp, session):
    session = ff1.get_session(year, gp, session)
    session.load()
    return session



# session dataframe format and sample data
# Index(['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint',
#        'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time',
#        'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime',
#        'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest',
#        'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime',
#        'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason',
#        'FastF1Generated', 'IsAccurate'],
#       dtype='object')
#                     Time Driver DriverNumber                LapTime  LapNumber  Stint  ... TrackStatus Position Deleted DeletedReason FastF1Generated IsAccurate
# 0 0 days 01:03:56.437000    NOR            1 0 days 00:01:36.458000        1.0    1.0  ...           1      6.0   False                         False      False
# 1 0 days 01:05:23.781000    NOR            1 0 days 00:01:27.344000        2.0    1.0  ...           1      6.0   False                         False       True
# 2 0 days 01:06:50.644000    NOR            1 0 days 00:01:26.863000        3.0    1.0  ...           1      7.0   False                         False       True
# 3 0 days 01:08:16.501000    NOR            1 0 days 00:01:25.857000        4.0    1.0  ...           1      7.0   False                         False       True
# 4 0 days 01:09:42.074000    NOR            1 0 days 00:01:25.573000        5.0    1.0  ...           1      7.0   False                         False       True
# 
# [5 rows x 31 columns]