# main thingy

import datetime
import PySimpleGUI as sg
import fastf1 as ff1

from pages.session_select_pg import build_layout as session_layout, handle_event as session_event
from pages.race_dashboard_pg import build_layout as dashboard_layout

ff1.Cache.enable_cache('./cache')


def main():

    layout = [
        [
            sg.Column(session_layout(), key='SESSION_SELECT'),
            sg.Column(dashboard_layout(), key='RACE_DASHBOARD', visible=False)
        ]
    ]

    window = sg.Window("F1TelemetryDashboard", layout, finalize=True)
    window.maximize()

    state = {
        "query_year": datetime.datetime.now().year,
        "query_event": None,
        "query_session": None
    }

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'GET_SESSION':
            window['SESSION_SELECT'].update(visible=False)
            window['RACE_DASHBOARD'].update(visible=True)

        session_event(window, event, values, state)


    window.close()

main()