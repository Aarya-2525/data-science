import numpy as np

user_input = input("Enter a list of values: ")
user_arr = user_input.split()
for i in range(len(user_arr)):
    user_arr[i]=int(user_arr[i])

num_arr = np.array(user_arr, dtype=float)
print(num_arr)
mean = np.mean(num_arr)            # mean (average)
pop_var = np.var(num_arr, ddof=0)     # variance (population, divide by n)
sample_var = np.var(num_arr, ddof=1)    # variance (sample, divide by n-1)
pop_sd = np.std(num_arr, ddof=0)     # std deviation (population)
sample_sd = np.std(num_arr, ddof=1)     # std deviation (sample)

r = int(input("Enter 'r' for moment: "))
pow_nums = num_arr**2
raw = np.mean(num_arr**r) # raw moment
central = np.mean((num_arr-mean)**r) #central moment
print(mean,pop_var,pop_sd,sample_var,sample_sd,raw,central)
