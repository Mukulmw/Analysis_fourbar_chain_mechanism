import math
print('Displacement analysis of fourbar mechanism')
a=input('Enter the length of crank "a":')
print('Crank=',float(a))
b=input('Enter the length of link "b" coupler')
print('Coupler=',float(b))
c=input('Enter the length of Rocker "c"')
print('Rocker=',float(c))
d=input('Enter the length of fixed link "d":')
print('fixed link "d"=',float(d))
theta=input('Enter the input angle in degrees:')
print('Theta=',float(theta),'Degrees')
a=float(a)
b=float(b)
c=float(c)
d=float(d)
theta=float(theta)
rad=float(theta)*math.pi/180
#print(type(rad)
k=((a**2)-(b**2)+(c**2)+(d**2))/2
A=k-(a*(d-c)*(math.cos(rad)))-(c*d)
B=-2*a*c*(math.sin(rad))
C=k-(a*(d+c)*math.cos(rad))+(c*d)
#print("Value of  K A B C are",k,a,b,c)
posq=(-B+((B**2)-(4*A*C))**0.5)/(2*A)#positive discriminant / 2a
negq=(-B-((B**2)-(4*A*C))**0.5)/(2*A)#negative discriminant / 2a
phi1=2*math.atan(posq)#value phi wiill be in rad and has to be converted into degree on later stage
posiphi=phi1*180/math.pi#convert radians to degrees
phi2=2*math.atan(negq)
negphi=phi2*180/math.pi#convert radians to degrees
print('The values of output angle in degrees are:',posiphi,negphi)

beta1=math.asin(((c*math.sin(phi1))-(a*math.sin(rad)))/b)
beta2=math.asin(((c*math.sin(phi2))-(a*math.sin(rad)))/b)
posbeta=beta1*180/math.pi
negbeta=beta2*180/math.pi
print('The coupler link position Beta are',posbeta, negbeta)
print('Displacement analysis is done, Thankyou!')
w=input('Do you want to proceed for velocity analysis? y/n')

if w=="y":
    wa=input('Enter the ang. velocity of input link in rad/sec')
    wa=float(wa)
    wb1=-(a*wa*math.sin(phi1-rad))/(b*math.sin(phi1-beta1))
    wb2=-(a*wa*math.sin(phi2-rad))/(b*math.sin(phi2-beta2))
    wc1=(a*wa*math.sin(beta1-rad))/(c*math.sin(beta1-phi1))
    wc2=(a*wa*math.sin(beta2-rad))/(c*math.sin(beta2-phi2))
    print('The value of angular velocity of "b" coupler are',wb1,'and',wb2,'rad/sec')
    print('The value of angular velocity of "c" rocker are',wc1,'and',wc2,'rad/sec')
elif w=="n":
    print('Done, Good luck!')

del w
w=input('Do you want to proceed for acceleration analysis? y/n')

if w=="y":
    aa=input('Enter the value of ang. acceleration of input link in rad/sec2')
    aa=float(aa)
    ab1=((a*aa*math.sin(phi1-rad))-(a*wa*wa*math.cos(phi1-rad))-(b*wb1*wb1*math.cos(phi1-beta1))+(c*wc1*wc1))/(b*math.sin(beta1-phi1))
    ab2=((a*aa*math.sin(phi2-rad))-(a*wa*wa*math.cos(phi2-rad))-(b*wb2*wb2*math.cos(phi2-beta2))+(c*wc2*wc2))/(b*math.sin(beta2-phi2))
    ac1=((a*aa*math.sin(beta1-rad))-(a*wa*wa*math.cos(beta1-rad))-(b*wb1*wb1)+(c*wc1*wc1*math.cos(beta1-phi1)))/(c*math.sin(beta1-phi1))
    ac2=((a*aa*math.sin(beta2-rad))-(a*wa*wa*math.cos(beta2-rad))-(b*wb2*wb2)+(c*wc2*wc2*math.cos(beta2-phi2)))/(c*math.sin(beta2-phi2))
    print('The value of angular acceleration of "b" coupler are',ab1,'and',ab2,'rad/sec2')
    print('The value of angular acceleration of "C" rocker are',ac1,'and',ac2,'rad/sec2')
elif w=="n":
    print('Done, Good luck!')

input('Press press "ENTER" to exit')
