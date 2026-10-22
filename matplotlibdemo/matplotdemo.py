import matplotlib.pyplot as plt
import numpy_demo as np

xpoints = np.array([2022, 2023, 2024, 2025])
ypoints = np.array([6.6, 7, 8.7, 6.8])

#plt.title('GDP')
#plt.xlabel('Year')
#plt.ylabel('GDP')
#plt.grid(color = 'brown', linestyle = '--', linewidth = 1) # add axis = 'y' to add lines only on y axis
#plt.plot(xpoints, ypoints, color='red', alpha = .2, linewidth = 2)
#plt.scatter(xpoints, ypoints, color = 'red')
#plt.bar(xpoints, ypoints, color = 'orange', alpha = .3)
#student_scores = np.array([80, 90, 88, 22, 34, 90, 80, 70, 66])
#plt.hist(student_scores, rwidth=0.7)

fix, ax = plt.subplots(nrows=1, ncols=2)
ax[0].plot(xpoints, ypoints, color='red')

xpoints = np.array([2022, 2023, 2024, 2025])
ypoints = np.array([-4,3.7, -2.6, 4.2])
ax[1].plot(xpoints, ypoints, color='green')
plt.show()