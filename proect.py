import numpy as np
import math
import matplotlib.pyplot as plt


##### Input all the terms, mass,c,ro,area,g,initial velocity
ro=float(input("Enter the density of air: "))
c=float(input("Enter the drag coefficient: "))
area=float(input("Enter the area of the body:"))
mass=float(input("ENter he mass: "))
delt=float(input("Enter the time interval: "))      #time interval
g=float(9.8)
v0=float(input("Enter the initial velocity: "))
theta_d=float(input("Enter the angle"))#angle
i=1
N=5
t=0  #time ?????? 

theta=np.radians(theta_d)

v0y=v0*math.sin(theta)

vx=v0*math.cos(theta)

x=0.0#initial coordinates
y=0.0#initial y cordinate

ar_x=[]
ar_y=[]

tmax=10


# functions


def velocity_y(v0y,g,t):
    vy=v0y-(g*t)  #velocity in y direction
    return vy


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
    vy=velocity_y(v0y,g,t)
    velocity=v(vx,vy)
    D_val=D(ro,area,c)
    accel_x=ax(D_val,mass,v0,vx)
    accel_y=ay(D_val,mass,velocity,vy,g)
    
    print("Attempt number : ",i)
    print("\n")
    print("Initial value of X cordinate :",x)
    print("Initial value of y cordinate :",y)
    print("\n")


    print("New x velocity = ",vx)
    print("New y velocity = ",vy)
    print("\n")


    print("Acceleration in x direction = ",accel_x)
    print("Acceleration in y direction = ",accel_y)
    print("\n")


    vx=vx+accel_x*delt # vx+del vx
    vy=vy+accel_y*delt #  vy+del vy


    x=x+delx(vx,delt,accel_x)
    y=y+dely(vy,delt,accel_y)

    t=t+delt
    i=i+1
    print("\n")



