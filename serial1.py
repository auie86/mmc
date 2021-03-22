# -----------------
# serial1.py - Serial line with M/M/c stations
#
# Jeff Smith - 2016-12-20
#
# -----------------
import mmc

# lambda - arrival rate
l = 15
# station service rates (mu) and capacities (c)
mus = [6, 18, 10, 4]
cs  = [3,  1,  2, 4]

# solve
sol = []
for i in range(len(mus)):
	sol.append(mmc.mmc(l, mus[i], cs[i]))
	if sol[i]['rho'] > 1.0:
		print ("System unstable (station {:})".format(i+1))
		exit()
	else:
		mmc.show(sol[i], "Station {:}".format(i+1))
L = sum([s['L'] for s in sol])
W = sum([s['W'] for s in sol])
print ("\nNIS: {:.3f}, TIS: {:.3f}".format(L, W))
