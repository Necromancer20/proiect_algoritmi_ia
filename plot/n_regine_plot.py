import matplotlib.pyplot as plt  # Changed from 'plot' to 'plt'

def plot_chart(table_sizes, solving_times, solving_times_at, algo_labels):
    plt.plot(table_sizes, solving_times, label=algo_labels[0])
    plt.plot(table_sizes, solving_times_at, label=algo_labels[1], linestyle='--')
    plt.xlabel('Complexitate')
    plt.ylabel('Timp(s)')
    plt.xticks(range(len(table_sizes)), table_sizes)
    plt.grid()
    plt.legend()
    plt.show()