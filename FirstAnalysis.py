import numpy as np
import matplotlib.pyplot as plt

location = './'

dict_in = {}
dict_out = {}
file = open(location + "events.ascii")

line = file.readline() #ignore first line of avgflux
line = file.readline().split()
while line:
	ni = int(line[0])
	nf = int(line[1])
	for x in range(ni):
		data = file.readline().split()
		PDG = data[0]
		if PDG in dict_in:
			dict_in[PDG] = dict_in[PDG] + 1
		else:
			dict_in[PDG] = 1
	for x in range(nf):
		data = file.readline().split()
		PDG = data[0]
		if PDG in dict_out:
			dict_out[PDG] = dict_out[PDG] + 1
		else:
			dict_out[PDG] = 1
	line = file.readline().split()	
	
print(dict_in)

plt.figure("in")
plt.bar(dict_in.keys(), dict_in.values())
plt.title("Incoming Particles")
plt.xlabel("Type of Particle (PDG)")
plt.ylabel("Number of Particles")
plt.savefig("plt_in.png")


plt.figure("out")
plt.bar(dict_out.keys(), dict_out.values())
plt.title("Outgoing Particles")
plt.xlabel("Type of Particle (PDG)")
plt.ylabel("Number of Particles")
plt.savefig("plt_out.png")

 
# Analyze the following:
#     1. Counts of interacting particles (different plots for incoming and outgoing particles)
#     2. Energy distribution of initial particles, separated by particle type
#     3. Energy distribution of produced particles, separated by particle type
#     4. Angular distribution of produced particles (total, and separated by particle type)

