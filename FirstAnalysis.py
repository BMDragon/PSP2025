import numpy as np
import matplotlib.pyplot as plt

location = './'


#PROBLEM 1

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

#dict_symbols = {"11":r"$e^-$", "12":r"$v_e$", 
#finish mapping values to symbols, $ means math mode, r is for correct formatting

#x_vals_in = (dict_symbols[x] for x in dict_in.keys()) #mapping symbols to keys
#x_vals_out = (dict_symbols[x] for x in dict_out.keys()) #mapping symbols to keys
#sub these in the graphs to replace 'dict_in.keys()' and out for x values

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

 

#PROBLEM 2 & 3 #diff histogram for each diff particle

dict_initial = {} #dictionary mapping PDG's to a list of energies
dict_final = {}
file = open(location + "events.ascii")

line = file.readline() #ignore first line of avgflux
line = file.readline().split()
while line:
	ni = int(line[0])
	nf = int(line[1])
	for x in range(ni):
		data = file.readline().split()
		PDG = data[0]
		Etot = float(data[1])
		if PDG in dict_initial:
			dict_initial[PDG] = dict_initial[PDG].append(Etot)
		else:
			dict_initial[PDG] = [Etot]
	for x in range(nf):
		data = file.readline().split()
		PDG = data[0]
		Etot = float(data[1])
		if PDG in dict_final:
			dict_final[PDG] = dict_final[PDG].append(Etot)
		else:
			dict_final[PDG] = [Etot]
	line = file.readline().split()

#symbols_set_in = (dict_symbols[x] for x in dict_initial.keys()) #mapping symbols to keys
#symbols_set_out = (dict_symbols[x] for x in dict_final.keys()) #mapping symbols to keys
#replace x axis below for graphing with this set

for x in range(len(dict_initial)):
	plt.figure(str(dict_inital.keys()[x]))
	plt.hist(dict_initial[x], bins = 20)
	plt.title("Initial Energy Distribution of " + str(dict_inital.keys()[x]))
	plt.xlabel("Energies (MeV)")
	plt.ylabel("Number of Particles")
	plt.savefig(str(dict_inital.keys()[x]) + ".png")

for x in range(len(dict_final)):
	plt.figure(str(dict_final.keys()[x]))
	plt.hist(dict_final[0], bins = 20)
	plt.title("Initial Energy Distribution of " + str(dict_final.keys()[x]))
	plt.xlabel("Energies (MeV)")
	plt.ylabel("Number of Particles")
	plt.savefig(str(dict_final.keys()[x]) + ".png")



# Analyze the following:
#     1. Counts of interacting particles (different plots for incoming and outgoing particles)
#     2. Energy distribution (Etot) of initial particles, separated by particle type
#     3. Energy distribution of produced particles, separated by particle type
#     4. Angular distribution of produced particles (total, and separated by particle type)

