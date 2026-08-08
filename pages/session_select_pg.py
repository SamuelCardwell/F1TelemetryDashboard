import datetime
import PySimpleGUI as sg
from ingest.events import getEventsList, getEventSessions

def build_layout(state):
    current_year = datetime.datetime.now().year
    years = list(range(2024, current_year + 1))
    
    return [
        [
            sg.T("Year:"),
            sg.Drop(years, default_value=current_year, key='DROP_YEAR', readonly=True, enable_events=True),
            sg.T("Event:"),
            sg.Drop(getEventsList(current_year), default_value="", key='DROP_EVENT', readonly=True, enable_events=True),
            sg.T("Session:"),
            sg.Drop([], default_value="", key='DROP_SESSION', readonly=True, enable_events=True),
            sg.Button("Go", key='GET_SESSION', disabled=True, bind_return_key=True)
        ]
    ]

def handle_events(window, event, values, state):
    if event == 'DROP_YEAR':
        state['query_year'] = values['DROP_YEAR']
        
        window['DROP_EVENT'].update(values=getEventsList(state['query_year']))
        window['DROP_SESSION'].update(values=[])
        window['GET_SESSION'].update(disabled=True)
    
    if event == 'DROP_EVENT':
        state['query_event'] = values['DROP_EVENT']

        window['DROP_SESSION'].update(values=getEventSessions(state['query_year'], state['query_event']))
        window['GET_SESSION'].update(disabled=True)

    if event == 'DROP_SESSION':
        window['GET_SESSION'].update(disabled=False)

    if event == 'GET_SESSION':
        state.update({
            'query_year': values['DROP_YEAR'],
            'query_event': values['DROP_EVENT'],
            'query_session': values['DROP_SESSION'],
            'new_session': True
        })