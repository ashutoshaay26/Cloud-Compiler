def getMonitorIP(monitorData):
    ip, maximum = monitorData[0][0], int(monitorData[0][1]) 
    for i in range(1, len(monitorData)):
        if int(monitorData[i][1])>maximum:
            ip = monitorData[i][0]
    return ip

if __name__=="__main__":
    d = [['10.20.24.62',1726528],\
         ['10.20.24.15',1824538]]
    print getMonitorIP(d)