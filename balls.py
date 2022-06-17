import matplotlib.pyplot as plt

ball1 = plt.Circle ((1,0),0.2, color = 'red')
ball2 = plt.Circle ((0.5,0),0.2, color = 'blue')

fig, ax = plt.subplots ()

ax.add_patch(ball1)
ax.add_patch(ball2)

plt.show()