import PySimpleGUI as ps

from ingest.session import getSession


def build_layout(state):

    return [
        [
            ps.T("Dashboard!\n"),
            ps.T("some session information:\n"),
            ps.T("", key='SESSION_INFO')
        ]
    ]

def handle_events(window, events, values, state):

    if state['new_session']:
        state['new_session'] = False
        session = getSession(state['query_year'], state['query_event'], state['query_session'])

        window['SESSION_INFO'].update(f"Session Name: {session.name}\nDate: {session.date}\nDrivers: {len(session.drivers)}")

    return
