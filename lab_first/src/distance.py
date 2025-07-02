import numpy as np

def eucledian(array1, array2):
    array = []
    sum = 0
    for i in range(len(array1)):
        print(i)
        array.append((array1[i] - array2[i]) ** 2)

    for i in range(len(array)):
        sum = sum + array[i]

    return np.sqrt(sum)

def manhattan(array1, array2):
    array =  abs(np.subtract(array1, array2))
    return np.sum(array)

def cosine_similarity(array1, array2):
    dot_product = np.dot(array1, array2)
    mag_a = np.sqrt(np.sum(np.square(array1)))
    print(mag_a)
    mag_b = np.sqrt(np.sum(np.square(array2)))
    result = dot_product / (mag_a * mag_b)
    return result

def jaggard_sim(array1, array2):
    m00 = np.sum((array1 == 0) & (array2 == 0))
    m01 = np.sum((array1 == 0) & (array2 == 1))
    m11 = np.sum((array1 == 1) & (array2 == 1))
    m10 = np.sum((array1 == 1) & (array2 == 0))
    print(m00, m01, m10, m11)
    jag_res = (m11) / (m01 + m10 + m11)
    return jag_res

def minmax_normalization(array):
    return np.array((np.subtract(array, np.min(array)))/ (np.max(array) - np.min(array)))

def zscore(array):
    return np.array(np.subtract(array, np.mean(array))/ np.std(array))

def decimal_scaling(array):
    j = len(str(np.max(array)))
    return (np.divide(array, 10 ** j))

def main():
    a = [2, 3, 7, 8, 7]
    b = [4, 7, 8, 2, 1]
    result_euc = eucledian(a, b)
    result_man = manhattan(a, b)
    result_cosine = cosine_similarity(a, b)
    x = [1, 0, 1, 0, 0, 0]
    y = [1, 0, 1, 1, 0, 1]
    result_jaggard = jaggard_sim(x, y)
    print(result_euc)
    print(result_man)
    print(result_cosine)
    print(result_jaggard)

    new_array = [35000, 42000, 39000, 45000]
    norm_minmax = minmax_normalization(new_array)
    print(norm_minmax)

    z_score = zscore(new_array)

    dec_scaling = decimal_scaling(new_array)
    print(dec_scaling)
    print(z_score)


if __name__ == '__main__':
    main()

