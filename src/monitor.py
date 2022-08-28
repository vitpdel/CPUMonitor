import  os, psutil  as  ps
from    time   import  sleep

def clear():
    # To not show multiple monitors under each other
    os.system("clear")

def monitor(cpuUsage,   memoryUsage,    bars=50):
    clear()
    
    cpuPercent  =   (cpuUsage   /   100.0)  #To show the percentage of usage
    cpuBar =   "#" *   int(cpuPercent  *   bars)+"-"*(bars -   int(cpuPercent*bars))
    
    # Represent how many percent CPU or Memory being use with bars 

    memoryPercent   =   (memoryUsage    /   100.0)
    memoryBar   =   "#" *   int(memoryPercent   *   bars)+"-"*(bars -   int(memoryPercent*bars))
    

    print(f"\rCPU Usage:    |{cpuBar}| {cpuUsage:.2f}%  ",    end="\n")
    
    # To show the percentage and the bar of usage
    # :.2f == formating in 2 decimal places
    
    print(f"\nMemory Usage: |{memoryBar}| {memoryUsage:.2f}%  ",   end="\r")


while   True:
    # To update the monitor

    monitor(ps.cpu_percent(),    ps.virtual_memory().percent,   30)
    sleep(0.5)


