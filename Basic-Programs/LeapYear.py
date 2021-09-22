"""
   * Author - Satyam Vaishnav
   * Date -  16-SEP-2021
   * Time -  22:10 PM
   * Title - Leap Year 
"""

try:
    year= int(input("Enter a year:"))
        
    if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("{0} is a leap year".format(year))
                else:
                    print("{0} is not a leap year".format(year))
            else:
                print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
except Exception as e:
    print("Enter Correct Value:" ,e)  


try:
    def is_leap(year):
    
        year = int(input("Enter year:"))
        return year%4 ==0 and (year%100 != 0 or year%400==0)
        print(is_leap(year))
except Exception as e:
    print("Enter Integer Value",e)



                
                
