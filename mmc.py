# -----------
# mmc.py - Queueing models for M/M/c queueing systems
#
# Jeff Smith - 2016-12-20
#
# -----------
import sys
from math import factorial

#
# mmc() - solves the m/m/c queue and returns a dictionary
# with the following keys (and associated values):
#		lambda, mu, c, p0, Lq, L, Wq, W
#	Based on the formulae from Askin and Standridge (1993)
# 
def mmc(l, m, c):
	# save the original values
	sol = {'lambda':l, 'mu':m, 'c':c}
	# switch types to facilitate calculations
	l = float(l)
	m = float(m)
	c = int(c)
	util = l/(c*m)
	sol['rho'] = util
	if util < 1.0:
		if c == 1:
			sol['p0'] = 1 - util
			sol['Lq'] = (util**2)/(1 - util)
			sol['L']  = util/(1-util)
			sol['Wq'] = util/(m*(1-util))
			sol['W']  = 1/(m*(1-util))
		else:
			p0 = (c*util)**c/(factorial(c)*(1-util))
			for n in range(c):
				p0 = p0 + ((c*util)**n)/factorial(n)
			p0 = p0**(-1)
			sol['p0'] = p0
			sol['Lq'] = util*((c*util)**c)*p0/(factorial(c)*(1-util)**2)
			sol['L']  = sol['Lq'] + l/m
			sol['Wq'] = ((c*util)**c)*p0/(factorial(c)*c*m*(1-util)**2)
			sol['W']  = sol['Wq'] + (m**(-1))
	return sol

#
# show() - shows the solution
#
def show(sol, title = "Solution"):
	print ("{:}:".format(title))
	print ("\tLambda:\t{:8.4f}".format(sol['lambda']))
	print ("\tMu:\t{:8.4f}".format(sol['mu']))
	print ("\tC:\t{:8.4f}".format(sol['c']))
	print ("\tUtil:\t{:8.4f}".format(sol['rho']))
	if sol['rho'] < 1.0:
		print ("\tSystem stable")
		print ("\tp(0):\t{:8.4f}".format(sol['p0']))
		print ("\tLq:\t{:8.4f}".format(sol['Lq']))
		print ("\tL:\t{:8.4f}".format(sol['L']))
		print ("\tWq:\t{:8.4f}".format(sol['Wq']))
		print ("\tW:\t{:8.4f}".format(sol['W']))
	else:
		print ("\tSystem unstable")

#
# main()
#
def main():
	c = 1
	if len(sys.argv) > 2:
		l = float(sys.argv[1])
		m = float(sys.argv[2])
		if len(sys.argv) > 3:
			c = int(sys.argv[3])
	else :
		print ("Syntax: mmc.py lambda mu [c]")
		exit()
	sol = mmc(l, m, c)
	show(sol)

# This line causes main() to be executed if this module
# is executed without an import (i.e., from the command line).
if __name__ == "__main__": main()
