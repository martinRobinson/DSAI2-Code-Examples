import matplotlib.pyplot as plt
import csv

with open("./iris.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    petal_lengths = []
    petal_widths = []
    for row in reader_variable:
        if 'setosa' in row:
            petal_lengths.append(row[2])
            petal_widths.append(row[3])

petal_lengths_floats = [float(i) for i in petal_lengths]
petal_widths_floats = [float(i) for i in petal_widths]

plt.style.use("seaborn-v0_8")

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))
axes[0].set_title("Setosa - Petal Length")
axes[0].set_ylabel("Petal Length", fontsize=10)
axes[0].scatter(range(len(petal_lengths)),petal_lengths, marker='o', c=petal_lengths_floats, cmap=plt.cm.Reds, s=25)
axes[1].set_title("Setosa - Petal Width")
axes[1].set_ylabel("Petal Width", fontsize=10)
axes[1].scatter(range(len(petal_widths)),petal_widths, marker='o', c=petal_widths_floats, cmap=plt.cm.Greens, s=25)
fig.tight_layout()

plt.show()