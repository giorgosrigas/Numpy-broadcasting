# Numpy-broadcasting
NumPy uses broadcasting to perform mathematical operations on pairs of arrays that do
not have the same size in each dimension or not the same number of dimensions. For a
detailed explanation on broadcasting, refer to the lecture slides and literature and click this
link to read the SciPy page on broadcasting. The limitation of broadcasting is: If none of the
arrays has size 1 in the mismatched dimension, NumPy’s broadcasting fails. Therefore, we
here want to extend the broadcasting capabilities of NumPy.

# Broadcast function:
takes two input arrays and performs element-wise
mathematical operations. If the arrays have different sizes, including
different dimensions, the function matches them and the output array has
the maximum shape. The function returns eturns output array which is the product of the executed
mathematical function between the two input arrays.
