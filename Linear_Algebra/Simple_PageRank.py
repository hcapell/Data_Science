#############################################################################
# INSTRUCTIONS
#
# The dataset is located here:
# https://toreopsahl.com/datasets/#southernwomen
#
# Please navigate to "Network 13: Davis' Southern Women Club"
#
# Download "Binary static one-mode network: tnet-format (3kb)"
#
# Save the file as a txt file in the directory in which you are running python
#
# Leave the filename as the default given
#
# The output of the code will be the pagerank vectors for M^k up to k = 25
#
# The indexes of the top 10 and bottom 10 nodes will also be outputted
#############################################################################
import numpy as np

f = open('Davis_Southern_club_women-binary.txt')
data = f.readlines()
f.close()
data = [line.split(" ") for line in data]
data = np.array(data, dtype=int)

# Find the number of nodes
n = 0
for i in range(len(data)):
    if data[i,0]>n:
        n = data[i,0]

n = int(n)

# Create nxn matrix of zeros
A = np.zeros([n,n])

# Populate A with ones where nodes are connected to one another
for i in range(len(data)):
    x = data[i][0] - 1
    y = data[i][1] - 1
    A[x][y] = 1

# Calculate the sum of each column and store each sum in a list
colSums = []
for i in range(n):
    colSum = 0
    for j in range(n):
        colSum = colSum + A[j][i]
    colSums.append(colSum)

# Make all columns stochastic by dividing by the sum of the column
for i in range(n):
    for j in range (n):
        A[j][i] = (float(1)/float(colSums[i]))*A[j][i]

# Create starting vector v
v = np.ones([n,1])
v = (float(1)/float(n)) * v

# Create matrix of ones B
B = np.ones_like(A)

# Create matrix M
M = .85 * A + (.15/float(n)) * B

# Raise M to the power i+1
Mi = M
for i in range(1,25):
    Mi = np.matmul(Mi, M)
    pageRank = np.matmul(Mi, v)
    print "M^", i+1
    print pageRank


# Add an index to pageRank in order to find top 10 and bottom 10 nodes
index = np.zeros([len(pageRank),1])
for i in range (len(pageRank)):
    index[i] = i
pageRank = np.hstack((pageRank, index))

# Create a list of pageRank elements in order
pageRank_list = pageRank.tolist()

pageRank_sorted = sorted(pageRank_list)


print "bottom 10: ", pageRank_sorted [0:10]
print "top 10: ", pageRank_sorted [-11:-1]

