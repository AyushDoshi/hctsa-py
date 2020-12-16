import warnings

# import numba

# @numba.jit(nopython=True,parallel=True)
import numpy


def EN_SampEn(x, m=2, r=.2, scale=True):
    """
    """
    warnings.filterwarnings('ignore')

    if scale:
        r = numpy.std(x, ddof=1) * r

    templates = make_templates(x, m)
    # print(templates)
    A = 0
    B = 0

    for i in range(templates.shape[0]):
        template = templates[i, :]

        A = A + numpy.sum(numpy.amax(numpy.absolute(templates - template), axis=1) < r) - 1

        B = B + numpy.sum(numpy.amax(numpy.absolute(templates[:, 0:m] - template[0:m]), axis=1) < r) - 1

    if B == 0:
        return {'Sample Entropy': numpy.nan, "Quadratic Entropy": numpy.nan}

    return {'Sample Entropy': - numpy.log(A / B), "Quadratic Entropy": - numpy.log(A / B) + numpy.log(2 * r)}


# @numba.jit(nopython=True,parallel=True)
def make_templates(x, m):
    """
    """
    N = int(len(x) - m)

    templates = numpy.zeros((N, m + 1))

    for i in range(N):
        templates[i, :] = x[i:i + m + 1]

    return templates

# def SampEn(U, m = 2, r = .2):
#
#     r = r * numpy.log(U)
#
#     def _maxdist(x_i, x_j):
#
#         result = max([abs(ua - va) for ua, va in zip(x_i, x_j)])
#
#         return result
#
#
#     def _phi(m):
#
#         x = [[U[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]
#
#         C = 0
#
#         for i in range(len(x)):
#
#             for j in range(len(x)):
#
#                 if i == j:
#
#                     continue
#
#                 C += (_maxdist(x[i], x[j]) <= r)
#
#         return C
#
#
#     N = len(U)
#
#     return -numpy.log(_phi(m+1) / _phi(m))

# def EN_SampEn(y,M = 2,r = 0,pre = ''):
#     if r == 0:
#         r = .1*numpy.std(y)
#     else:
#         r = r*numpy.std(y)
#     M = M + 1
#     N = len(y)
#     print('hi')
#     lastrun = numpy.zeros(N)
#     run = numpy.zeros(N)
#     A = numpy.zeros(M)
#     B = numpy.zeros(M)
#     p = numpy.zeros(M)
#     e = numpy.zeros(M)
#
#     for i in range(1,N):
#         y1 = y[i-1]
#
#         for jj in range(1,N-i + 1):
#
#             j = i + jj - 1
#
#             if numpy.absolute(y[j] - y1) < r:
#
#                 run[jj] = lastrun[jj] + 1
#                 M1 = min(M,run[jj])
#                 for m in range(int(M1)):
#                     A[m] = A[m] + 1
#                     if j < N:
#                         B[m] = B[m] + 1
#             else:
#                 run[jj] = 0
#         for j in range(N-1):
#             lastrun[j] = run[j]
#
#     NN = N * (N - 1) / 2
#     p[0] = A[0] / NN
#     e[0] = - numpy.log(p[0])
#     for m in range(1,int(M)):
#         p[m] = A[m] / B[m-1]
#         e[m] = -numpy.log(p[m])
#     i = 0
#     # out = {'sampen':numpy.zeros(len(e)),'quadSampEn':numpy.zeros(len(e))}
#     # for ent in e:
#     #     quaden1 = ent + numpy.log(2*r)
#     #     out['sampen'][i] = ent
#     #     out['quadSampEn'][i] = quaden1
#     #     i = i + 1
#     out = {'Sample Entropy':e[1],'Quadratic Entropy':e[1] + numpy.log(2*r)}
#     return out
