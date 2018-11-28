import io 

f = open("/sys/class/thermal/thermal_zone0/temp", "r")
t = f.readline ()

cputemp = "CPU temp: "+t

print (cputemp)
