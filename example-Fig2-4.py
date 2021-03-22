# -----------------
# Example-Fig2-4.py - Queueing network from SASMAA (Figure 2.4)
#
# Jeff Smith - 2021-03-22
#
# -----------------
import sys
import mmc


# lambda - arrival rate
# station service rates (mu) and capacities (c)
lambdas = [100.00, 50.00, 44.44, 82.00, 30.00, 140.00]
mus     = [110.00, 60.00, 50.00, 95.00, 35.00, 150.00]

# solve
sol = []
for i in range(len(lambdas)):
	sol.append(mmc.mmc(lambdas[i], mus[i], 1))
	if sol[i]['rho'] >= 1.0:
		print ("System unstable (station {:})".format(i+1))
		sys.exit()
	else:
		mmc.show(sol[i], "Station {:}".format(i+1))

L = sum([s['L'] for s in sol])
W = sum([s['W'] for s in sol])
print ("\nNIS: {:.3f}, TIS: {:.3f}".format(L, W))
