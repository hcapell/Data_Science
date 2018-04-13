import numpy as np
import matplotlib.pyplot as plt

# Change filepath to your local directory
fr = open('/Users/hollycapell/MSAN502/Homework 3/education_wages.txt')

lines = fr.readlines()
fr.close()

header = lines[0]
data = lines[1:]
data2 = [line.split(',') for line in data]
data2 = np.array(data2)

# Set m equal to the number of rows in the data
m = data2.shape[0]

# Create empty matrix A and vector b
A = np.zeros(shape = (m, 2))
b = np.zeros(shape = (m, 1))

# Create matrix A and vector b
for i in range(m):
    A[i][0] = 1
    A[i][1] = data2[i][-2]
    b[i][0] = data2[i][-1]

# Create A transpose
A_T = A.T

# Multiply A transpose and A
ATA = np.matmul(A_T, A)

# Take the inverse of A_T_A
ATA_inv = np.linalg.inv(ATA)

# Multiply ATA_inv and A_T
ATA_inv_AT = np.matmul(ATA_inv,A_T)

# Multiply by b
x_hat = np.matmul(ATA_inv_AT,b)

print "x_hat values:"
print x_hat

# Define function to create the best fit line
def line(x):
    y = x_hat[0][0] + (x_hat[1][0] * x)
    return y


# Create vector of x's and y's to plot
x = []
y = []

# Create vector y_hat which represents the y's of the best fit line, and diff which represents difference
# between observed y and y_hat
y_hat = []
diff = []

for i in range(m):
    x.append(A[i][1])
    y.append(b[i][0])
    y_hat.append(line(x[i]))
    diff.append(y[i] - y_hat[i])

# Calculate sum of squared errors
SSE = 0
for i in diff:
    SSE = SSE + i**2

print "Sum of squared errors:"
print SSE

plt.scatter(x, y, s = 0.7, color = 'k')
plt.plot(x, y_hat)
plt.show()






