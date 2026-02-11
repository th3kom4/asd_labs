import numpy as np
import random
from plot_data import plot_data 
import matplotlib.pyplot as plt

def generate_data(n, gen_type="random"):
    if gen_type == "best":
        a = [i+1 for i in range(n)]
        return a
    elif gen_type == "worst":
        a = [i+1 for i in reversed(range(n))]
        return a
    else:
        a = [i+1 for i in range(n)]
        random.shuffle(a)
        return a

def bubble_sort(seq):
	op_count = 0
	swap_count = 0
	n = len(seq)
	for i in range(n - 1):
		for j in range(0, n - 1 - i):
			op_count += 1
			if (seq[j] > seq[j + 1]):
				temp = seq[j]
				seq[j] = seq[j + 1]
				seq[j + 1] = temp
				swap_count += 1
	return (op_count, swap_count)

def bubble_impr_sort(seq):
	op_count = 0
	swap_count = 0
	n = len(seq)
	for i in range(n - 1):
		swapped = False
		for j in range(0, n - 1 - i):
			op_count += 1
			if (seq[j] > seq[j + 1]):
				temp = seq[j]
				seq[j] = seq[j + 1]
				seq[j + 1] = temp
				swapped = True
				swap_count += 1
		if not swapped:
			break
	return (op_count, swap_count)

tokuda_gaps = [
    68178,
    30301,
    13467,
    5985,
    2660,
    1182,
    525,
    233,
    103,
    46,
    20,
    9,
    4,
    1,
]

def shellsort(seq, tokuda_gaps):
	n = len(seq)
	op_count = 0
	swap_count = 0
	for gap in tokuda_gaps:
		for i in range(gap, n):
			j = i
			temp = seq[j]
			while j >= gap:
				op_count += 1
				if seq[j - gap] > temp:
					seq[j] = seq[j - gap]
					j -= gap
					swap_count += 1
				else:
					break
			seq[j] = temp
	return (op_count, swap_count)

sizes = [10, 100, 1000]
types = ["random", "best", "worst"]

data_plot = {
    'random': {'bubble':{}, 'shellsort':{}, 'bubble_impr':{}},
    'best':   {'bubble':{}, 'shellsort':{}, 'bubble_impr':{}},
    'worst':  {'bubble':{}, 'shellsort':{}, 'bubble_impr':{}}
}

for n in sizes:
    print("\nDATA SIZE: ", n)
    
    for gen_type in types:
        print("\n\tDATA TYPE:", gen_type)
        
        data = generate_data(n, gen_type)
        
        data_bubble = np.copy(data)
        (bubble_op_count, bubble_swap_count) = bubble_sort(data_bubble)
        print("\tBubble sort operation count:", int(bubble_op_count))
        print("\tBubble sort swap count:", int(bubble_swap_count))
        data_plot[gen_type]['bubble'][n] = bubble_op_count

        data_bubble_impr = np.copy(data)
        (bubble_impr_op_count, bubble_impr_swap_count) = bubble_impr_sort(data_bubble_impr)
        print("\tImproved bubble sort operation count:", int(bubble_impr_op_count))
        print("\tImproved bubble sort swap count:", int(bubble_impr_swap_count))
        data_plot[gen_type]['bubble_impr'][n] = bubble_impr_op_count
		
        data_shellsort = np.copy(data)
        (shellsort_op_count, shellsort_swap_count) = shellsort(data_shellsort, tokuda_gaps)
        print("\tShellsort sort operation count:", int(shellsort_op_count))
        print("\tShellsort sort swap count:", int(shellsort_swap_count))
        data_plot[gen_type]['shellsort'][n] = shellsort_op_count
        
plot_data(data_plot['random'], logarithmic=True, oneplot=True, data_label="Random Data")
plot_data(data_plot['best'], logarithmic=True, oneplot=True, data_label="Best Case")
plot_data(data_plot['worst'], logarithmic=True, oneplot=True, data_label="Worst Case")

plt.show()