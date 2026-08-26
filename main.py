# main program loop

# these import external libraries that allow you to use certain functions
import datetime
import PySimpleGUI as sg
import fastf1 as ff1

# these import our funnctions from other files, and give them a unquie name
from pages.session_select_pg import build_layout as session_layout, handle_events as session_events
from pages.race_dashboard_pg import build_layout as dashboard_layout, handle_events as dashboard_events, play_race

# creates a folder name cache that stores all looked up data so it doesn't have to be looked up in the future
ff1.Cache.enable_cache('./cache')

# this is the main function for the app, it is called at the bottom of this file and is always called 
def main():

    # this is a data structure called a dictionary, basically a table where each row has a label and a value. dictionaries are denoted with { }
    # this one is being used to hold the state of important variables. the first value in " " is the 'label', the second is the value
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

    # this is a data structure called a list, pretty self explanatory. to access a certain value in a list use the index > list_name[0] 0 is the index which points to the first value of the list. think of it as the list[plus how many], so the first item is list[plus 0]
    # this list is being used by the Graphical User Interfact system we are using, it is actually a list within a list (denoted by the [ within [ ] ] structure)
    layout = [
        [
            # each of these list items represents something to display for the GUI, these ones are functions that return the other page layouts for the rest of the app. check their files for info on the other layouts
            sg.Column(session_layout(state), key='SESSION_SELECT'),                         # this is the first page that lets users pick a session, it is automatically shown when the app starts
            sg.Column(dashboard_layout(state), key='RACE_DASHBOARD', visible=False),        # this is the dashboard page, it is automatically hidden when the app starts
            create_a_new_drive_info_page        # add a new page for the driver info
        ]
    ]

    # this sets up and maximizes the window for the app's GUI to use 
    window = sg.Window("F1TelemetryDashboard", layout, finalize=True)
    window.maximize()


    # this is the main loop for the app, it will run continuously until the app is closed
    while True:
        # this sets up two variables, event and values, that allow users to interact with the GUI, it rereads the GUI interactions every 100 ms
        event, values = window.read(timeout=100)

        # this stops the program when the close window button (red x) is clicked
        if event == sg.WIN_CLOSED:
            break

        # this checks if the button with the 'GET_SESSION' key has been clicked
        # if it has then in hids the first page and displays the dashboard page
        if event == 'GET_SESSION':
            window['SESSION_SELECT'].update(visible=False)
            window['RACE_DASHBOARD'].update(visible=True)

        # this function checks for any events occuring in the first, session select, page
        session_events(window, event, values, state)

        # this function checks for any events occuring in the dashboard page
        dashboard_events(window, event, values, state)

        # this checks if the play variable in the dictionary is set to true and if there is a session variable in the dictionary
        # if so then it runs the function, which starts replaying the race
        if state.get('play', False) and 'session' in state:
            play_race(window, state)

    # this closes the window, it only runs when the above loop is broken, when the window close button is clicked
    window.close()


# the program starts here
main()
