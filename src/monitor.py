import  os, psutil  as  ps
from    time   import  sleep

def clear():
    # To not show multiple monitors under each other
    os.system("clear")


def cpuMonitor(cpuUsage, bars=50):
    # Represent how many percent CPU or Memory being use with bars 

    #CPU Informations
    print("="*30,"CPU Info", "="*30)

    # Cores informations
    print(f"Physical cores:       {ps.cpu_count(logical=False)}")
    print(f"Total cores:          {ps.cpu_count(logical=True)}")
            #                          #
    # CPU frequencies
    cpufreq =   ps.cpu_freq()
    print(f"Max frequency:        {cpufreq.max:.2f}Mhz")
    print(f"Min frequency:        {cpufreq.min:.2f}Mhz")
    print(f"Current frequency:    {cpufreq.current:.2f}Mhz")



    cpuPercent  =   (cpuUsage   /   100.0)  #To show the percentage of usage
    cpuBar =   "#" *   int(cpuPercent  *   bars)+"-"*(bars -   int(cpuPercent*bars))
    
    # To show the percentage and the bar of usage
    # :.2f == formating in 2 decimal place

    print(f"\rTotal CPU Usage:     |{cpuBar}| {cpuUsage:.2f}%  ",    end="\n")
    

def memMonitor(memoryUsage,    bars=50):
    #Memory Informations
    print("="*30, "Memory Info", "="*30)

    #Memory Details

    mem =   ps.virtual_memory()
    print(f"Memory Total: {ps.get_size(mem.total)}")

    memoryPercent   =   (memoryUsage    /   100.0)
    memoryBar   =   "#" *   int(memoryPercent   *   bars)+"-"*(bars -   int(memoryPercent*bars))
    
    print(f"\nMemory Usage: |{memoryBar}| {memoryUsage:.2f}%  ",   end="\r")


def monitor():
    clear()

    cpuMonitor(ps.cpu_percent(), 30)
    memMonitor(ps.virtual_memory().percent, 30)

#def cpu(cpuUsage,   bars=50):
    #clear()

#    cpuPercent  =   (cpuUsage   /   100.0)  #To show the percentage of usage
#    cpuBar =   "#" *   int(cpuPercent  *   bars)+"-"*(bars -   int(cpuPercent*   bars))
#
#    print("="*40,   "CPU Info", "="*40)
#    
#    # Cores informations
#    print(f"Physical cores: {ps.cpu_count(logical=False)}")
#    print(f"Total cores: {ps.cpu_count(logical=True)}")
#
#    # CPU frequencies
#    cpufreq =   ps.cpu_freq()
#    print(f"Max frequency:     {cpufreq.max:.2f}Mhz")
#    print(f"Min frequency:     {cpufreq.min:.2f}Mhz")
#    print(f"Current frequency: {cpufreq.current:.2f}Mhz")
#
#    print(f"\rCPU Usage:    |{cpuBar}| {cpuUsage:.2f}%  ",    end="\n")

while   True:
    # To update the monitor
    #cpu(ps.cpu_percent)
    #monitor(ps.cpu_percent(),    ps.virtual_memory().percent,   30)
    monitor()
    sleep(0.5)


