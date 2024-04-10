from game_constants import DIVIDER
import phase.phase_constants as phase_constants
from phase.intro import intro_phase
from phase.name import name_phase
from phase.abilities import abilities_update

current_phase = phase_constants.INTRO

while True:
    if current_phase == phase_constants.INTRO:
        current_phase = intro_phase()
    elif current_phase == phase_constants.END:
        print(DIVIDER)
        print("Goodbye")
        break
    elif current_phase == phase_constants.NAME:
        print(DIVIDER)
        current_phase = name_phase()
    elif current_phase == phase_constants.INTRO_ABILITIES:
        print(DIVIDER)
        abilities_update()
        print(DIVIDER)
        print("Are you ready for your first fight?")
        break
