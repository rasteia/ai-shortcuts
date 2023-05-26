import cProfile
import pstats
import io
## PerformanceProfiling.py - a general-purpose Performance Profiling script 
  # that you can use to profile the performance of other Python scripts:
  
def profile_script(script_path):
    # Create a profiler object
    profiler = cProfile.Profile()

    # Run the script with profiling enabled
    profiler.enable()
    exec(open(script_path).read())
    profiler.disable()

    # Create a stream to save profiling results
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)

    # Sort the profiling results by the desired metric (e.g., 'cumulative', 'time', 'calls')
    stats.sort_stats('cumulative')

    # Print the profiling results
    stats.print_stats()

    # Save the profiling results to a file
    with open('profiling_results.txt', 'w') as file:
        file.write(stream.getvalue())

if __name__ == '__main__':
    # Replace 'path_to_script.py' with the actual path of the script you want to profile
    profile_script('path_to_script.py')
