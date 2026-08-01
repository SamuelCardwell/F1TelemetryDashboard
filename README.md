# F1TelemetryDashboard
A dashboard showing telemetry from F1 races.

# Pages

## Start Up Page
Mostly blank screen with two options:
- View the current championship
- Pick a race
  - Either have to type in name accurately
  - Or API call to generate a drop down list

## Championship Page
One side of the screen will contain the Driver's Championship. The drivers will be listed in order of position with the number of points displayed.

The other side of the screen will contain the Constructor's Championship. Again each constructor will be listed in order with points displayed. The percent of points coming from the lead driver will also be shown.

There will also be an option to display the F1.5 championship points.

## Main Telemetry Page
After the users has selected the race they would like to receive telemetry for they will reach this page.

The left side of the screen will have a track map with each of the driver's position represented by a dot. The dot will be in the driver's team's colour and display the driver number to identify which driver.

Below the track map will be the pole lap time, the current fastest lap, the expected time lost for a pit stop, a pit stop under VSC, and a pit stop under SC.

The rest of the screen will be taken up by a list of the drivers. There will be two rows of drivers with the right row being offset vertically. The drivers will be arranged like a starting grid, with P1 at the top left, P2 at the top right, P3 below P1, P4 below P2, and so on.

Each driver will have their:
- 3 letter driver ID (HAM, MAX, LAN)
- Current tire
- Tire age
- Number of pit stops
- Rolling average lap time
- Previous lap time delta to their average
- Positions gained/lost (if space)

Clicking on a driver will provide more information about them.

In the top corner there will be two buttons. One will take the user back to the start screen. The other will take the user to the live championship points.

## Driver Telemetry Page
The page will contain information about the driver and their race weekend.
- Driver name and number
- Current position
- Starting positions (gained/lost)
- Current tire
- Tire age
- Number of pit stops
  - Team's average pit stop time this race (expected time if no stops)
- Rolling average lap time
  - Average lap time by tire
- Previous lap time
  - Delta to their average
  - Delta to driver in front and behind average
- Championship position
  - Forecasted position
  - Team position and forecasted position

## Live Championship
This will be very similar to the Championship Page with a couple differences.
It will display the forecasted championship points assuming that drivers will finish where they are currently. This will include there forecasted points as well as how many points they are forecasted to score (in parentheses).
There will also be the forecasted F1.5 championship as an option.
