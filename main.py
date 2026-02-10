import numpy as np
import random
from plot_data import plot_data 

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
		n = len(seq)

		for i in range(n):
				for j in range(0, n - 1 - i):
						op_count += 1
						if (seq[j] > seq[j + 1]):
								temp = seq[j]
								seq[j] = seq[j + 1]
								seq[j + 1] = temp

		return op_count

def bubble_impr_sort(seq):
		op_count = 0
		n = len(seq)

		for i in range(n):
				swapped = False
				for j in range(0, n - 1 - i):
						op_count += 1
						if (seq[j] > seq[j + 1]):
								temp = seq[j]
								seq[j] = seq[j + 1]
								seq[j + 1] = temp

								swapped = True

				if not swapped:
					break

		return op_count

sizes = [10, 100, 1000]
types = ["random", "best", "worst"]

data_plot = {
    'random': {'bubble':{}, 'insertion':{}, 'bubble_impr':{}},
    'best':   {'bubble':{}, 'insertion':{}, 'bubble_impr':{}},
    'worst':  {'bubble':{}, 'insertion':{}, 'bubble_impr':{}}
}

for n in sizes:
    print("\nDATA SIZE: ", n)
    
    for gen_type in types:
        print("\n\tDATA TYPE:", gen_type)
        
        data = generate_data(n, gen_type)
        
        data_bubble = np.copy(data)
        bubble_op_count = bubble_sort(data_bubble)
        print("\tBubble sort operation count:", int(bubble_op_count))
        data_plot[gen_type]['bubble'][n] = bubble_op_count
        
        data_bubble_impr = np.copy(data)
        bubble_impr_op_count = bubble_impr_sort(data_bubble_impr)
        print("\tImproved bubble sort operation count:", int(bubble_impr_op_count))
        data_plot[gen_type]['bubble_impr'][n] = bubble_impr_op_count
        
plot_data(data_plot["best"], logarithmic=True, oneplot=True)
