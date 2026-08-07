# main thingy

import sys
import datetime
import PySimpleGUI as sg
import fastf1 as ff1

from ingest.events import getEventsList

ff1.Cache.enable_cache('./cache')


def main():
    currentYear = datetime.datetime.now().year
    years = list(range(2024, currentYear + 1))

    layout = [
        [
            sg.T("Year:"),
            sg.Drop(years, default_value=currentYear, key='DROP_YEAR', readonly=True, enable_events=True),
            sg.T("Event:"),
            sg.Drop(getEventsList(currentYear), default_value="", key='DROP_EVENT', readonly=True)
        ]
    ]

    window = sg.Window("F1TelemetryDashboard", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'DROP_YEAR':
            query_year = values['DROP_YEAR']
            
            window['DROP_EVENT'].update(values=getEventsList(query_year))

        

    window.close()

main()