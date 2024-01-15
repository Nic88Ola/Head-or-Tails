		#|--------------------|
		#|		 RULES		    	|
		#|						        |
		#|head = testa        |
    #|tails = croce       |
		#|                    |
		#|                    |
		#|--------------------|

import random

head_or_tails = random.randint(1,2)
choice = len(str(input('HEAD OR TAILS\n\n')))


if head_or_tails == 1:
	  print(""" 
					HEAD
				 __________
				 |		    |
				 |   👨🏻   |
				 |		    |
				 ----------""")
else:
	  		 
	  print("""
				   TAILS
				 __________
				 |		    |
				 |   ❌   |
				 |		    |
				 ----------""")
					
if choice == 4 and head_or_tails == 1:
		print("			   ⭐️ YOU WIN ⭐️")
elif choice == 4 and head_or_tails == 2:
		print("			   ❌ YOU LOSE ❌")
elif choice == 5 and head_or_tails == 2:
		print("			   ⭐️ YOU WIN ⭐️")
elif choice == 5 and head_or_tails == 1:
		print("			   ❌ YOU LOSE ❌")
