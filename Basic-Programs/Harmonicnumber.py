"""
   * Author - Satyam Vaishnav
   * Date -  16-SEP-2021
   * Time -  18:03 PM
   * Title - Harmonic Series Check
"""

# Use try except block.
try:

	n=int(input("Enter nth number:"))
	def harmonic_sum(n):
		
		if n < 2:
			return 1
		else:
	    		return 1 / n + (harmonic_sum(n - 1))
	    
	print(harmonic_sum(n))
	
except Exception as e: 
	print("Enter Numeric Value" ,e) 
