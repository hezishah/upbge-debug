import bge
from bge import logic as GameLogic
import ptvsd
print("Start remote debugger")
ptvsd.enable_attach()
ptvsd.wait_for_attach()

import loop

loop.loop()