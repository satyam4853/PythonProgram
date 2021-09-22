"""
   * Author - Satyam Vaishnav
   * Date -  21-SEP-2021
   * Time -  10:48 AM
   * Title - WindChill
"""
import math

try:
    #initlize the tempreture and speed of windchill.
    t_tempreture =int(input("Enter the Tempreture in Fahranheit: "))
    v_windspeed =int(input("Enter the Wind Speed in miles per hours: "))
    
    #formula for calculating the effective temp.
    effective_tempreture = (35.74+0.6215*t_tempreture+(0.4275*t_tempreture-35.75)*v_windspeed**0.16)

    # Condition for temp and speed.
    if(t_tempreture < 50 and(v_windspeed <120 or v_windspeed>3)):
        print(effective_tempreture)   
    else:
        print("Follow instructions while giving input of tempreture and speed ")  
except Exception as e:
    print("Enter int value" ,e)     


