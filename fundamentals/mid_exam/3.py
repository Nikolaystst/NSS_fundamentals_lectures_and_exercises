from math import floor

bisc_of_worker_per_day = int(input())
workers = int(input())
other_factory = int(input())
total_buiscuits = 0
diff_in_percent = 0

for i in range(1, 31):
    if i % 3 == 0:
        total_buiscuits += floor(bisc_of_worker_per_day * workers * 0.75)
    else:
        total_buiscuits += (bisc_of_worker_per_day * workers)

diff_in_percent = abs(total_buiscuits - other_factory) / other_factory * 100

print(f"You have produced {total_buiscuits} biscuits for the past month.")

if total_buiscuits > other_factory:
    print(f"You produce {diff_in_percent:.2f} percent more biscuits.")
else:
    print(f"You produce {diff_in_percent:.2f} percent less biscuits.")
