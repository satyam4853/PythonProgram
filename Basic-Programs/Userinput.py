"""
   * Author - Satyam Vaishnav
   * Date -  16-SEP-2021
   * Time -  18:03 PM
   * Title - User Input and Replace String Template
"""



text=input("User Name:")
text=str(text)
text_length=len(text)
   
if text_length >= 3:
    print(text_length)
    print("Hello", text,"How are you?")
else:
    print("Inalid Name")






