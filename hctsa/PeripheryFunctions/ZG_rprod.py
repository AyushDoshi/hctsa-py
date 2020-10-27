import numpy


def ZG_rprod(X, Y):
    """
    """
    if len(X.shape) < 2:
        X = X[:, None]

    n, m = X.shape

    if Y.shape[0] != n or len(Y.shape) != 1:
        print('rprod error')
        return None

    Y = Y[:, None]

    Z = numpy.multiply(X, numpy.matmul(Y, numpy.ones((1, m))))

    return Z
