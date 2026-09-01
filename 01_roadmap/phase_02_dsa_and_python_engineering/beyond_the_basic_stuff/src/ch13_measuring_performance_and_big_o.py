"""
Python Performance Tools Reference
- timeit: Used for micro-benchmarking small snippets.
- cProfile: Used for macro-profiling complete functions or programs.
"""

import cProfile
import timeit


# ==============================================================================
# 1. TIMEIT (Micro-benchmarking Snippets)
# ==============================================================================
# Use case: Compare execution speed of small logic options
xor_time = timeit.timeit(
    "a, b = 42, 101; a = a ^ b; b = a ^ b; a = a ^ b", number=1_000_000
)
temp_time = timeit.timeit("a, b = 42, 101; temp = a; a = b; b = temp", number=1_000_000)
unpack_time = timeit.timeit("a, b = 42, 101; a, b = b, a", number=1_000_000)

print(f"XOR Time:       {xor_time:.5f} seconds")
print(f"Temp Var Time:  {temp_time:.5f} seconds")
print(f"Unpack Time:    {unpack_time:.5f} seconds")


# ==============================================================================
# 2. CPROFILE (Macro-profiling Full Workflows)
# ==============================================================================
# Use case: Find bottlenecks in whole functions or scripts
def main():
    print("Starting profiling...")

    # Prepare inputs
    # input_data = "sample data"

    profiler = cProfile.Profile()
    profiler.enable()

    # Call your target function
    # target_function(input_data)

    profiler.disable()
    profiler.print_stats(sort="cumulative")

    print("Profiling finished!")


if __name__ == "__main__":
    main()
