import time
import PySimpleGUI as ps
import pandas as pd

from ingest.session import getSession


def build_layout(state):

    return [
        [
            ps.Text("Dashboard!\n"),
            ps.Text("some session information:\n"),
            ps.Text("", key='SESSION_INFO'),
            ps.Button("Start Race", key="PLAY_RACE"),
            ps.Text("Current lead lap: 00", key="LEAD_LAP")
        ]
    ]

def handle_events(window, event, values, state):

    if state['new_session']:
        state['new_session'] = False
        
        session = getSession(state['query_year'], state['query_event'], state['query_session'])

        state['session'] = session

        window['SESSION_INFO'].update(f"Session Name: {session.name}\nDate: {session.date}\nDrivers: {len(session.drivers)}")

        # play_race(window, state, session)

    # 'pausing' currently just resets to the beginning
    if event == "PLAY_RACE":
        state['play'] = not state.get('play', False)

        if state.get('play', False):
                state['session_started_at'] = time.perf_counter()
                state['prev_time'] = time.perf_counter()
                state['session_time'] = state['session'].session_start_time
                state['lead_lap'] = 0
        
        window['PLAY_RACE'].update("Pause Race")
        print("starting/stopping race")

    return


def play_race(window, state):

    time_speedup = 10

    # update session time
    now = time.perf_counter()
    delta_time = now - state.get('prev_time')
    state['prev_time'] = now
    state['session_time'] += pd.Timedelta(seconds=(delta_time * time_speedup))

    driver_laps = state['session'].laps[
        (state['session'].laps["LapStartTime"] <= state['session_time']) &
        (state['session'].laps["Position"] == 1)
    ].sort_values("LapStartTime")

    if not driver_laps.empty:
        current_lead_lap = int(driver_laps.iloc[-1]["LapNumber"])
            
        if current_lead_lap > state['lead_lap']:
            state['lead_lap'] = current_lead_lap
            window['LEAD_LAP'].update(f"Current lead lap: {current_lead_lap:02d}")

    return