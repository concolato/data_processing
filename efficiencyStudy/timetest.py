import time

Xmin = -270.0       # default value
Xmax = 0.0          # default value

numberOfTerms = 14
coefficients = [
    0.000000000000E+00,
    0.586655087080E-01,
    0.454109771240E-04,
    -0.779980486860E-06,
    -0.258001608430E-07,
    -0.594525830570E-09,
    -0.932140586670E-11,
    -0.102876055340E-12,
    -0.803701236210E-15,
    -0.439794973910E-17,
    -0.164147763550E-19,
    -0.396736195160E-22,
    -0.558273287210E-25,
    -0.346578420130E-28] 

def compute(coefficients, x) :
    y = 0.0

    # Do sum in reverse order
    for index in range(numberOfTerms-1, -1, -1) :
        y = coefficients[index] + y * x
    return y

def checkTime(samplePoints, logFilename) :
    # same as default values
    Xmin = -270.0
    Xmax = 0.0

    saveLog = 1 if logFilename  else  0

    print('Time test of pure computation in Python' + (' with log' if saveLog else ' without log') )

    startTime = time.time() * 1000

    if saveLog :
        fLog = open(logFilename, 'w')

    delta = (Xmax-Xmin) / (samplePoints-1)  
    for point in range (0, samplePoints) :       
        X = Xmin + point*delta
        Y = compute(coefficients, X)

        if (saveLog) : 
            fLog.write('{} {}\n'.format(X, Y))

    if (saveLog) :
        fLog.close()

    endTime = time.time() * 1000
    timeUse = endTime - startTime

    print('time for {} computations is {} msec'.format(samplePoints, timeUse))
#end

def main() :
    checkTime(1000, None)
    checkTime(100000, None)
    checkTime(10000000, None)
    
    checkTime(1000, "plog-1000.txt")
    checkTime(100000, "plog-100000.txt")
    checkTime(10000000, "plog-10000000.txt")
#end main

if __name__ == "__main__" :
    startTime = time.time() * 1000
    #Observing optimization after modifications
    main()
    endTime = time.time() * 1000
    timeUse = endTime - startTime

    print('****Time for main function execution is {} msec'.format(timeUse))
