import numpy as np
import matplotlib.pyplot as plt

location = './'

file = open(location + "events.ascii")
line = file.readline()
line = file.readline()

# Analyze the following:
#     1. Counts of interacting particles (different plots for incoming and outgoing particles)
#     2. Energy distribution of initial particles, separated by particle type
#     3. Energy distribution of produced particles, separated by particle type
#     4. Angular distribution of produced particles (total, and separated by particle type)