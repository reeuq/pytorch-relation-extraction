import matplotlib.pyplot as plt

x = []
y = []

with open('./PCNN_ONE_DEF_16_PR.txt', 'r') as f:
    lines = f.readlines()
    for temp in lines:
        temp_x, temp_y = temp.split()
        x.append(float(temp_x))
        y.append(float(temp_y))

plt.plot(y, x)
plt.show()
