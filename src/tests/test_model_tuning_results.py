from src.tools.sampling import k_fold_sample_data_set
import numpy as np
x = [[i, i, i] for i in range(1, 11, 1)]
y = [i for i in range(11, 21, 1)]
x_train_list, y_train_list, x_test_list, y_test_list = k_fold_sample_data_set(x, np.array(y), 10)

for j in range(0, 10, 1):
    print x_test_list[j]
