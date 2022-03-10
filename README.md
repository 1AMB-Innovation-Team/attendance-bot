# attendance-bot
Telegram bot to simplify attendance taking

## Commands
- `/in` - Say user will be present at morning roll call
- `/out` - Say user will be absent at morning roll call
- `/set_in_for {user}` - Set another user to be present
- `/set_out_for {user}` - Set another user to be absent
- `/attendance` - Show attendance for morning roll call

## Usage
Users in the telegram chat can use `/in` or `/out`.
Users can provide their reasons from a preset list.

Each response to the bot will print the attendance.

## Technologies
- Python 3
- mySQL