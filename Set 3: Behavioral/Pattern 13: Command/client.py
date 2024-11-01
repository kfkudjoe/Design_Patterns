"""
The Command Pattern Use Case Example.
A smart light switch.
"""

from light import Light
from switch import Switch
from switch_on_command import SwitchOnCommand
from switch_off_command import SwitchOffCommand

# Create a receiver
LIGHT = Light()

# Create Commands
SWITCH_ON = SwitchOnCommand(LIGHT)
SWITCH_OFF = SwitchOffCommand(LIGHT)

# Register the commands with the invoker
SWITCH = Switch()

SWITCH.register("ON", SWITCH_ON)
SWITCH.register("OFF", SWITCH_OFF)

# Execute the commands that are registered on the Invoker
SWITCH.execute("ON")
SWITCH.execute("OFF")
SWITCH.execute("ON")
SWITCH.execute("OFF")

# Show history
SWITCH.show_history()

# Replay last two execued commands
SWITCH.replay_last(2)