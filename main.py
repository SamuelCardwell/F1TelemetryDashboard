# main thingy

import datetime
import PySimpleGUI as sg
import fastf1 as ff1

from pages.session_select_pg import build_layout as session_layout, handle_events as session_events
from pages.race_dashboard_pg import build_layout as dashboard_layout, handle_events as dashboard_events, play_race

ff1.Cache.enable_cache('./cache')


def main():
    # tracks which page is the active (visible) page
    active_page = 'SESSION_SELECT'

    # holds the state of the program, stores important variables
    state = {
            "query_year": datetime.datetime.now().year,
            "query_event": None,
            "query_session": None,
            "new_session": False,
            "play": False,
            "session_started_at": 0.0,
            "prev_time": 0.0,
            "session_time": 0.0,
            "lead_lap": 0
        }
    
    layout = [
        [
            sg.Column(session_layout(state), key='SESSION_SELECT'),
            sg.Column(dashboard_layout(state), key='RACE_DASHBOARD', visible=False)
        ]
    ]

    window = sg.Window("F1TelemetryDashboard", layout, finalize=True)
    window.maximize()


    while True:
        event, values = window.read(timeout=100)

        if event == sg.WIN_CLOSED:
            break

        if event == 'GET_SESSION':
            active_page = 'RACE_DASHBOARD'
            window['SESSION_SELECT'].update(visible=False)
            window['RACE_DASHBOARD'].update(visible=True)

        # if active_page == 'SESSION_SELECT':
        session_events(window, event, values, state)
        # elif active_page == 'RACE_DASHBOARD':
        dashboard_events(window, event, values, state)

        if state.get('play', False) and 'session' in state:
            play_race(window, state)


    window.close()

main()