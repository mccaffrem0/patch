from math import *
import scipy.integrate
import json

antenna = {
	"substrate" : {},
	"patch" : {}
}

def populate(f, h, epsilon, a):
	h = h/100
	f = float(f*10**9)
	v=float(3*10**8)
	epsilon_0 = 8.85e-12

	W=(v/(2*f))*(sqrt(2/(epsilon+1)))

	epsilon_eff=((epsilon+1.0)/2.0)+((epsilon-1.0)/2.0)*(1.0+12.0*h/W)**(-0.5)
	
	lamda=v/f
	L_e = (v/(2*f*sqrt(epsilon_eff)))
	L = L_e - 0.824*h*(((epsilon_eff+0.3)*(0.264+W/h))/((epsilon_eff-0.258)*(0.8+W/h)))

	k0=(2*pi)/lamda
	X=k0*W
	I1=-2+cos(X)+X*S_i(X)+sin(X)/X
	G1=I1/(120*pi**2)

	temp=scipy.integrate.quad(lambda x:(((sin(k0*W*cos(x)/2)/cos(x))**2)*J0(k0*L*sin(x))*sin(x)**3),0,pi)
	G12=(1/(120*pi**2))*temp[0]

	Rin=1/(2*(G1+G12))

	R=50.0
	y0=(L/pi)*(acos(sqrt(R/Rin)))
	W_f = .2
	g = W_f / 40

	lamda *= 100
	h *= 100
	W *= 100
	L *= 100
	
	y0 *= 100
	
	a["frequency"] = f
	a["quarter_wave"] = lamda/4
	a["substrate"]["height"] = float(h)
	a["substrate"]["epsilon"] = float(epsilon)
	a["substrate"]["width"] = float(W+6*h)
	a["substrate"]["length"] = float(L+6*h)
	
	a["patch"]["width"] = W
	a["patch"]["length"] = L
	a["patch"]["inset_depth"] = y0
	a["patch"]["notch_width"] = g
	a["patch"]["feed_width"] = W_f
	
def S_i(a):
	s = scipy.integrate.quad(lambda x: sin(x) / x, 0, a, limit=200)
	return s[0]


def J0(s):
	temp = scipy.integrate.quad(lambda x: cos(s * sin(x)), 0, pi, limit=200)
	temp = (1 / pi) * temp[0]
	return temp
	

file = open('patch.json','w')
populate(float(input('frequency (ghz): ')),float(input('\nh (cm): ')), float(input('\ne_r: ')), antenna)
file.write(json.dumps(antenna))
print(antenna)