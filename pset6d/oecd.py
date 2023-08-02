import csv
from matplotlib import pyplot as plt
import scipy


def correlation_plot(arr1, arr2, label1, label2, filename):
    r = scipy.stats.linregress(arr1, arr2)
    slope = r[0]
    intercept = r[1]
    correlation = r[2]
    plt.scatter(arr1, arr2)
    x1 = min(arr1)
    y1 = intercept + slope * x1
    x2 = max(arr1)
    y2 = intercept + slope * x2
    plt.plot([x1, x2], [y1, y2])
    plt.text(x1, y2, f"Correlation: {correlation:.3f}")
    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.savefig(filename)
    plt.clf()


def lr_no_us(healthex, lifeexp):
    us_index = healthex.index(max(healthex))
    healthex_no_us = healthex.copy()
    lifeexp_no_us = lifeexp.copy()
    del healthex_no_us[us_index]
    del lifeexp_no_us[us_index]
    correlation_plot(
        healthex, lifeexp, "Health expenditures", "Life expectancy", "lr_no_us.png"
    )


def lr_income_life(incomepc, lifeexp):
    correlation_plot(
        incomepc, lifeexp, "Income per capita", "Life expectancy", "lr_income_life.png"
    )


def lr_size_pop(worldarea, worldpop):
    correlation_plot(
        worldarea, worldpop, "Country Size", "Population", "lr_size_pop.png"
    )


def main():
    lifeexp = []
    healthex = []
    incomepc = []
    worldpop = []
    worldarea = []
    reader = csv.DictReader(open("oecd.csv"))
    for row in reader:
        lifeexp.append(float(row["Life expectancy"]))
        healthex.append(float(row["Health expenditures"]))
        incomepc.append(float(row["Per capita income"]))
    with open("worldpop.txt") as f:
        for line in f:
            worldpop.append(int(line.split()[-1].strip()))
    with open("worldarea.txt") as f:
        for line in f:
            worldarea.append(int(line.split()[-1].strip()))
    lr_no_us(healthex, lifeexp)
    lr_income_life(incomepc, lifeexp)
    lr_size_pop(worldarea, worldpop)


if __name__ == "__main__":
    main()
