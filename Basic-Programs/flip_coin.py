"""
   * Author - Satyam Vaishnav
   * Date -  16-SEP-2021
   * Time -  19.10 PM
   * Title - flip coin 
"""

import random

coin_heads, coin_tails, times_flipped = 0, 0, 0

timesflipped = 0  
while timesflipped < 100:
	coin_flips = random.randrange( 2 )
	if coin_flips == 0:
		coin_heads += 1
	else:
		coin_tails += 1
	timesflipped += 1
	

print ("Out of 100 flips, " + str(coin_heads) + " were heads and " + str(coin_tails) + " were tails.")

            
        
        

