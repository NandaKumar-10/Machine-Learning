import matplotlib.pyplot as plt

time_slots = ['T1', 'T2', 'T3', 'T4', 'T5']
demands = [100, 400, 200, 300, 50]

print("--- Demand Analysis ---")
print(f"{'Time Slot':<10} | {'Demand':<10}")
print("-" * 25)
for t, d in zip(time_slots, demands):
    print(f"{t:<10} | {d:<10}")

plt.bar(time_slots, demands, color='skyblue')
plt.xlabel('Time Slots (2 min duration)')
plt.ylabel('Number of Requests')
plt.title('Demand Request Pattern Analysis')
plt.show()