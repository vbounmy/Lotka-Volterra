import matplotlib.pyplot as plt
import numpy
import pandas

def get_true_value():
    populations_lapins_renards = pandas.read_csv("populations_lapins_renards.csv", sep=',')

    true_value_lapin = populations_lapins_renards['lapin'].tolist()
    true_value_renard = populations_lapins_renards['renard'].tolist()

    return true_value_lapin, true_value_renard

def get_pred_value():
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

    return lapin, renard

def objectif(true_value, pred_value):
    mse = numpy.square(numpy.subtract(true_value, pred_value)).mean()
    return mse


pred_lapin, pred_renard = get_pred_value()
true_value_lapin, true_value_renard = get_true_value()

mse_lapin = objectif(true_value_lapin, pred_lapin[:len(true_value_lapin)])
mse_renard = objectif(true_value_lapin, pred_lapin[:len(true_value_renard)])

print(f"MSE lapin : {mse_lapin}")
print(f"MSE renard : {mse_renard}")

# plt.figure(figsize=(15, 6))
# plt.plot(time, lapin, "b-", label='Lapins')
# plt.plot(time, renard, "r-", label='Renards')
# plt.xlabel('Temps (Mois)')
# plt.ylabel('Population')
# plt.title('Dynamique des populations Proie-Prédateur')
# plt.legend()
# plt.show()    