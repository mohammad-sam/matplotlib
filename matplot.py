# import matplotlib.pyplot as plt
# plt.plot(range(-1000, 1000), [pow(x, 2) for x in range(-1000, 1000)])
# plt.show()
#
# import matplotlib.pyplot as plt
# plt.scatter(range(-10, 11), [pow(x, 2) for x in range(-10, 11)])
# plt.show()
#
# import matplotlib.pyplot as plt
# plt.boxplot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# plt.show()
#
# from matplotlib import pyplot as plt
# movies = ["a", "b", "c", "d", "e"]
# num_oscars = [2, 1, 3, 2, 3]
# xs = range(len(movies))
# plt.bar(xs, num_oscars)
# plt.ylabel("# of Academy Awards")
# plt.xlabel("some label")
# plt.title("Best Movies")
# plt.xticks(xs, movies)
# plt.show()
#
# from matplotlib import pyplot as plt
# variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]#y
# bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
# total_error = [x + y for x, y in zip(variance, bias_squared)]
# xs = list(range(len(variance)))
# plt.plot(xs, variance, 'g-', label='variance')
# plt.plot(xs, bias_squared, 'r-.', label='bias^2')
# plt.plot(xs, total_error, 'b:', label='total error')
# plt.xlabel("model complexity")
# plt.ylabel("value")
# plt.legend()
# plt.title("The Bias-Variance Trade-off")
# plt.show()
#
# import matplotlib.pyplot as plt
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" 'Hogs'
# plt.pie(sizes, explode=explode, labels=labels, autopct='%0.0f%%', shadow=True, startangle=90)
# plt.show()
#
# import matplotlib.pyplot as plt
# plt.hist([20, 25, 28, 30, 32, 33, 34, 35, 40, 60])
# plt.show()
#
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.random.rand(40)
# y = np.random.rand(40)
# z = np.random.rand(40)
# plt.scatter(x, y, s=z*1000, alpha=0.5)
# plt.show()

# from sklearn.datasets import load_iris
# import matplotlib.pyplot as plt
# 
# fig = plt.figure()
# data = load_iris().data
# for i in range(data.shape[1]):
#     sub = fig.add_subplot(2, 2, i+1)#2 row
#     sub.boxplot(data[:,i])
# plt.show()
# 
# import matplotlib.pyplot as plt
# circle1 = plt.Circle((0.5,0.5), .2, color='r')
# plt.gca().add_artist(circle1)
# plt.show()#gca() means Get Current Axis

