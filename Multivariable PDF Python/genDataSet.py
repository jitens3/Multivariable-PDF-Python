import numpy
import matplotlib.pyplot as plt

def randGen(sampleAmount):
    mean = 0
    std = 2 
    samples = numpy.random.normal(mean, std, size=num_samples)
    return samples

def writeFiles(fileName, dataType):
    f = open(fileName, "w")
    for i in range(num_samples):
        f.write("%lf\n" % dataType[i])
        i += 1
    f.close()

num_samples = 1000
std = 2
mean = 0

plt.plot(randGen(num_samples))
plt.show()
