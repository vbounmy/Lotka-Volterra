import matplotlib.pyplot as plt
import numpy
import pandas

time = [0]
lapin = [1]
renard = [2]

alpha, beta, delta, gamma = 2/3, 4/3, 1, 1

step = 0.001

for _ in range(0, 100_000):
    new_value_time = time[-1] + step
    new_value_lapin = (lapin[-1] * (alpha - beta * renard[-1])) * step + lapin[-1]
    new_value_renard = (renard[-1] * (delta * lapin[-1] - gamma)) * step + renard[-1]

    time.append(new_value_time)
    lapin.append(new_value_lapin)
    renard.append(new_value_renard)

lapin = numpy.array(lapin)
lapin *= 1000

renard = numpy.array(renard)
renard *= 1000



populations_lapins_renards = pandas.read_csv("populations_lapins_renards.csv", sep=',')


plt.figure(figsize=(15, 6))
plt.plot(time, lapin, "b-", label='Lapins')
plt.plot(time, renard, "r-", label='Renards')
plt.xlabel('Temps (Mois)')
plt.ylabel('Population')
plt.title('Dynamique des populations Proie-Prédateur')
plt.legend()
plt.show()    