import time
import PySimpleGUI as ps
import pandas as pd

# import the api ingesters from the other file
from ingest.session import getSession

# this function creates and returns the layout for the dashboard page
def build_layout(state):
    # this is the same as the layout for the session select page but only text for now. the keys allow us to get the elements later and update them
    return [
        [
            ps.Text("Dashboard!\n"),
            ps.Text("some session information:\n"),
            ps.Text("", key='SESSION_INFO'),
            ps.Button("Start Race", key="PLAY_RACE"),
            ps.Text("Current lead lap: 00", key="LEAD_LAP"),
            display_the_driver_and_their_position
        ]
    ]

# this function handles the events that occur on the session select page
def handle_events(window, event, values, state):
    # if the new_session variable in the state dictionary is true (only done when clicking the search button)
    if state['new_session']:
        state['new_session'] = False        # reset the value back to false
        
        session = getSession(state['query_year'], state['query_event'], state['query_session'])     # use the imported function to get the session dataframe

        state['session'] = session      # put the dataframe in the state dictionary so it can be accessed anywhere

        window['SESSION_INFO'].update(f"Session Name: {session.name}\nDate: {session.date}\nDrivers: {len(session.drivers)}")       # update the text on the page


    # if the play race button is clicked
    if event == "PLAY_RACE":        # 'pausing' currently just resets to the beginning

        state['play'] = not state.get('play', False)            # flips the value of the play variable (used for pausing and unpausing), if the play variable isn't found then default to false

        if state.get('play', False):            # if play is true (default to false if no play)
                state['session_started_at'] = time.perf_counter()               # when play was clicked
                state['prev_time'] = time.perf_counter()                        # used to track the previous update time
                state['session_time'] = state['session'].session_start_time     # gets the session start time
                state['lead_lap'] = 0                                           # tracks the lead lap
        
        window['PLAY_RACE'].update("Pause Race")        # updates the button text
        print("starting/stopping race")                 # outputs to terminal for debugging purposes

    return


# this function tracks the 'current' race time and counts the laps that go by
def play_race(window, state):

    time_speedup = 10       # allows for fast forward

    # update session time
    now = time.perf_counter()                                                           # gets the current time
    delta_time = now - state.get('prev_time')                                           # gets the amount of time passed
    state['prev_time'] = now                                                            # stores the current time
    state['session_time'] += pd.Timedelta(seconds=(delta_time * time_speedup))          # adds the amount of time passed to the session time

    # creates a list of laps
    driver_laps = state['session'].laps[
        (state['session'].laps["LapStartTime"] <= state['session_time']) &          # filters the laps for laps that started before the 'current' session time
        (state['session'].laps["Position"] == 1)                                    # filters the laps for laps done by the driver in position 1
    ].sort_values("LapStartTime")                                   # sorts the laps by the start time (mot recent at the back)

    if not driver_laps.empty:                                           # checks if the list of laps is empty

        current_lead_lap = int(driver_laps.iloc[-1]["LapNumber"])       # gets the lap number of the last lap in the list (the most recent)
        
        if current_lead_lap > state['lead_lap']:                        # checks if it is a new lap
            state['lead_lap'] = current_lead_lap                        # if it is then update the variable in the state dictionary and the text on the page
            window['LEAD_LAP'].update(f"Current lead lap: {current_lead_lap:02d}")


        # for each driver check the if their postion has changed
        add_check_here_and_update_text

    return
