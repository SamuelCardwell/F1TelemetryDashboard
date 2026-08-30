import datetime
import PySimpleGUI as sg

# import the api ingesters from the other file
from ingest.events import getEventsList, getEventSessions

# this function creates and returns the layout for the session select page
def build_layout(state):
    current_year = datetime.datetime.now().year             # gets the current year
    years = list(range(2024, current_year + 1))             # creates a list of years from 2024 to the current year (not sure how far back the data goes)

    # this is the list within a list that determines the page layout
    # note the dropdown menus (denoted with sg.Drop) are technically sg.Combo s but they are aliased to Drop. keep in mind when researching
    return [
        [
            sg.Text("Year:"),           # creates a piece of text
            sg.Drop(years, default_value=current_year, key='DROP_YEAR', readonly=True, enable_events=True),         # creates a dropdown menu with the list of years, the parameters (or inputs) are mostly self explanatory
            sg.Text("Event:"),
            sg.Drop(getEventsList(current_year), default_value="", key='DROP_EVENT', readonly=True, enable_events=True),        # this dropdown menu is for the events in a year
            sg.Text("Session:"),
            sg.Drop([], default_value="", key='DROP_SESSION', readonly=True, enable_events=True),
            sg.Button("Go", key='GET_SESSION', disabled=True, bind_return_key=True)             # this is a button with the key 'GET_SESSION'. when is is clicked it will create an event with the same name
        ]
    ]

# this function handles the events that occur on the session select page
def handle_events(window, event, values, state):
    # when the year dropdown menu is changed
    if event == 'DROP_YEAR':
        state['query_year'] = values['DROP_YEAR']       # update the query_year in the state dictionary
        
        window['DROP_EVENT'].update(values=getEventsList(state['query_year']))      # update the events in the event dropdown
        window['DROP_SESSION'].update(values=[])                                    # clear the session dropdown
        window['GET_SESSION'].update(disabled=True)                                 # diable the search button

    # when the event dropdown menu is changed. does the same as above but for the sessions dropdown
    if event == 'DROP_EVENT':
        state['query_event'] = values['DROP_EVENT']

        window['DROP_SESSION'].update(values=getEventSessions(state['query_year'], state['query_event']))
        window['GET_SESSION'].update(disabled=True)

    # when the session dropdown menu is changes
    if event == 'DROP_SESSION':
        window['GET_SESSION'].update(disabled=False)    # enables the search button

    # the search button is clicked
    if event == 'GET_SESSION':
        # updates the state dictionary with all of the search values
        state.update({
            'query_year': values['DROP_YEAR'],
            'query_event': values['DROP_EVENT'],
            'query_session': values['DROP_SESSION'],
            'new_session': True
        })
