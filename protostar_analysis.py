import numpy as np
import matplotlib.pyplot as plt

location = './'


#PROBLEM 1

dict_in = {}
dict_out = {}
file = open(location + "proneutr_star.ascii")

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

dict_symbols = {"11":r"$e^-$", "12":r"$v_e$", "13":r"$μ^-$", "14":r"$v_μ$", 
		"15":r"$τ^-$", "16":r"$v_τ$", "22":r"$γ$", "2112":r"n", "2212":r"p", 
		"1000010020":r"d", "1000010030":r"t", "1000020030":r"h", 
		"1000020040":r"$α$", "1000180400":r"$^{40} Ar$", 
		"1000190400":"$^{40} K$", 
		"1000170350":"$^{35} Cl$", "1000190390":"$^{39} K$", 
		"1000180380":r"$^{38} Ar$", "1000170360":r"$^{36} Cl$",
		"1000180390":r"$^{39} Ar$", "1000160350":r"$^{35} S$",
		"1000170380":r"$^{38} Cl$", "1000160340":r"$^{34} S$",
		"1000190380":r"$^{38} K$", "1000180370":r"$^{37} Ar$"}
#$ means math mode, r is for correct formatting

x_vals_in = list(dict_symbols[x] for x in dict_in.keys()) #mapping symbols to keys
x_vals_out = list(dict_symbols[x] for x in dict_out.keys()) #mapping symbols to keys
#sub these in the graphs to replace 'dict_in.keys()' and out for x values

plt.figure("in")
plt.bar(x_vals_in, dict_in.values())
plt.title("Incoming Particles")
plt.xlabel("Type of Particle (PDG)")
plt.ylabel("Number of Particles")
plt.savefig("plt_in.png")


plt.figure("out")
plt.bar(x_vals_out, dict_out.values())
plt.title("Outgoing Particles")
plt.xlabel("Type of Particle (PDG)")
plt.ylabel("Number of Particles")
plt.tick_params(labelsize=6)
plt.savefig("plt_out.png")

 

#PROBLEM 2 & 3 #diff histogram for each diff particle

dict_initial = {} #dictionary mapping PDG's to a list of energies
dict_final = {}
file = open(location + "proneutr_star.ascii")

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
			dict_initial[PDG].append(Etot)
		else:
			dict_initial[PDG] = [Etot]
	for x in range(nf):
		data = file.readline().split()
		PDG = data[0]
		Etot = float(data[1])
		if PDG in dict_final:
			dict_final[PDG].append(Etot)
		else:
			dict_final[PDG] = [Etot]
	line = file.readline().split()

#mapping symbols to keys
symbols_set_in = list(dict_symbols[x] for x in dict_initial.keys()) 
symbols_set_out = list(dict_symbols[x] for x in dict_final.keys())
#replace x axis below for graphing with this set

for pdg_code, energies in dict_initial.items():
	plt.figure("initial"+ pdg_code)
	plt.hist(energies, bins = 20)
	symbol = dict_symbols.get(pdg_code)
	plt.title("Initial Energy Distribution of " + symbol)
	plt.xlabel("Energies (MeV)")
	plt.ylabel("Number of Particles")
	plt.savefig("initial_" + pdg_code + ".png")

for pdg_code, energies in dict_final.items():
	plt.figure("final"+ pdg_code)
	plt.hist(energies, bins = 20)
	symbol = dict_symbols.get(pdg_code)
	plt.title("Final Energy Distribution of " + symbol)
	plt.xlabel("Energies (MeV)")
	plt.ylabel("Number of Particles")
	plt.savefig("final_" + pdg_code + ".png")



# Analyze the following:
#     1. Counts of interacting particles (different plots for incoming and outgoing particles)
#     2. Energy distribution (Etot) of initial particles, separated by particle type
#     3. Energy distribution of produced particles, separated by particle type

