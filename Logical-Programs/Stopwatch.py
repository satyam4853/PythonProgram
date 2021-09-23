"""
   * Author - Satyam Vaishnav
   * Date -  21-SEP-2021
   * Time -  11:10 AM
   * Title - Stopwatch
"""

import time
input("Press enter to start time")
start_time = time.time()
input("Press enter to end time")
end_time = time.time()
elapsed_time = end_time - start_time
print("The time elapsed is : ",elapsed_time)