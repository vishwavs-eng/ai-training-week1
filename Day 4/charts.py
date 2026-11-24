import matplotlib.pyplot as plt

days = ["Day 1", "Day 2", "Day 3", "Day 4"]
scores = [70, 80, 85, 95]

plt.bar(days, scores)
plt.title("My AI Training Progress")
plt.ylabel("Score")
plt.savefig("progress_chart.png")
plt.show()
