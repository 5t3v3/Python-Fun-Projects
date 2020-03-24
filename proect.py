import math
import matplotlib.pyplot as plt


##### Input all the terms, mass,c,ro,area,g,initial velocity
ro=float(input("Enter the density of air: "))
c=float(input("Enter the drag coefficient: "))
area=float(input("Enter the area of the body:"))
mass=float(input("ENter he mass: "))
dt=float(input("Enter the time interval: "))      #time interval
v0=float(input("Enter the initial velocity: "))
angle=float(input("Enter the angle"))#angle

g=9.8
t=0  #time ?????? 
tmax=10

theta=(3.14*angle)/180   #angle in radians


vy=[v0*math.sin(theta)] 

vx=[v0*math.cos(theta)]


x=[0]#initial coordinates
y=[0]#initial y cordinate



# functions

def DE(ro,area,c):       # drag 
    DD=float((ro*area*c)/2)
    return DD

p=0

accel_x=[]
accel_y=[]

while y[p]>=0:
    
    D=DE(ro,area,c)  # D in eqn
    
    vxx=float(vx[p]) # x coponent of velocity at pth position in list
    vyy=float(vy[p]) # y component of velocity at pth position in list
  
    ayy=-g-((D/mass)*vyy) #acceleration y component
    axx=-(D/mass)*vxx   #acceleration x component

    accel_x.append(axx) #acceleration in x direction
    accel_y.append(ayy)    #acceleration in y direction

    delta_x=(vxx*dt)+(accel_x[p]*(dt**2)/2)  # dx
    delta_y=(vyy*dt)+(accel_y[p]*(dt**2)/2)   #dy
    

    accelxx=accel_x[p]
    accelyy=accel_y[p]
    
    
    vx.append(vxx+(accelxx*dt) )# vx + delta vx
    vy.append(vyy+(accelyy*dt)) #  vy + delta vy


    x.append(x[p]+delta_x) #adding the value of x to list
    y.append(y[p]+delta_y) #adding the value of y to list

    t=t+dt
    p=p+1

####### Graph

plt.plot(x,y)
plt.grid()
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.show()
