import numpy as np


##### Input all the terms, mass,c,ro,area,g,initial velocity
ro=float(input("Enter the density of air: "))
c=float(input("Enter the drag coefficient: "))
area=float(input("Enter the area of the body:"))
mass=float(input("ENter he mass: "))
delt=float(input("Enter the time interval: "))      #time interval
g=float(9.8)
v0=float(input("Enter the initial velocity: "))
theta=float(input("Enter the angle"))#angle
i=1
N=5
t=0.0     #time ?????? 

v0y=v0*np.math.sin(theta)


vx=v0*np.math.cos(theta)    #velocity in x direction\
vy=v0y-(g*t)  #velocity in y direction

x=0#initial coordinates
y=0#initial y cordinate

t=0#initial t
tmax=N*delt


# functions
def D(ro,area,c):       
    DD=float((ro*area*c)/2)
    return DD

def v(vx,vy):
    vv=np.math.sqrt((vx**2)+(vy**2))
    return vv

def ax(D,m,v,vx):
    axx=-(D/m)*v*vx
    return axx

def ay(D,m,v,vy,g):
    ayy=-g-(D/m)*v*vy
    return ayy

def delx(vx,delt,ax): #
    delta_x=vx*delt+(0.5*ax*(delt**2))
    return delta_x

def dely(vy,delt,ay):
    delta_y=vy*delt+(0.5*ay*(delt**2))
    return delta_y


while t<tmax:
    velocity=v(vx,vy)
    D_val=D(ro,area,c)
    accel_x=ax(D_val,mass,v0,vx)
    accel_y=ay(D_val,mass,velocity,vy,g)

    print("Attempt number : ",i)
    print("\n")

    print("Acceleration in x direction = ",accel_x)
    print("Acceleration in y direction = ",accel_y)
    print("\n")


    new_x_v=vx+accel_x*delt # vx+del vx
    new_y_v=vy+accel_y*delt #  vy+del vy

    print("New x velocity = ",new_x_v)
    print("New y velocity = ",new_y_v)
    print("\n")

    new_x_co=x+delx(vx,delt,accel_x)
    new_y_co=y+dely(vy,delt,accel_y)

    print("New x coordinates = ",new_x_co)
    print("New y coordinates = ",new_y_co)
    print("\n")

    t=t+delt
    i=i+1
    print("\n")
