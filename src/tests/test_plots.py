from src.plots.stability import create_box_plots

A = [0.877098818079, 0.87749100808, 0.877883198081, 0.878372746008, 0.878862293934]
B = [0.876511091101, 0.877250880484, 0.877990669867, 0.878343997022, 0.878697324176]
C = [0.3, 0.4, 0.5, 0.7]
D = [0.3, 0.6, 0.5, 0.7]
E = [0.3, 0.8, 0.22, 0.7]
data = list()
data.append(A)
data.append(B)
data.append(C)
data.append(D)
data.append(E)
create_box_plots(data, 5)
