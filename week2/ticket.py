# data = { 
#     "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40 
# }

# global age
# def discount(age):
    
#      if age == 25:
#         return age
#      elif age== 2:
#         return "Tuesday"
#      elif age== 3:
#         return "Wednesday"
#      elif age== 4:
#         return "Thursday"
#      elif age== 5:
#         return "Friday"
#      elif age== 6:
#         return "Saturday"
#      elif age== 7:
#         return "Sunday"
#      else:
#         return "Invalid day"





# # adults= sum(x*20 for x in data.values() if x > 15)
# # child = sum(x*5 for x in data.values() if x <= 18)
# # total = adults + child
# # print(get_day_name(3))  # Output: Wednesday

# #     match discount:
# #         case 25:
# #             return(x*20)
# #         case (48):
# #             return(total)
# #         case (12):
# #             return(total)
# #         case (71):
# #             return(total)
# #         case (18):
# #             return(total)
# #         case (19):
# #             return(total)
# #         case (33):
# #             return(total)
# #         case (64):
# #             return(total)
# #         case (80):
# #             return(total)
# #         case (11):
# #             return(total)
# #         case (5):
# #             return(total)
# #         case (72):
# #             return(total)
# #         case (27):
# #             return(total)
# #         case (27):
# #             return(total)
# adults= sum(age*20 for x in data.values() if x > 15)
# child = sum(age*5 for x in data.values() if x <= 18)
# total = adults + child
        
# # indexes = list(data.values())
# # print(indexes.index(40)) 



# # child = (sum(1 for v in data.values() if v <= 18))
# # adult = (sum(1 for v in data.values() if v > 18))
# # count = child+adult
# # print(count) 

# # adults= sum(x*20 for x in data.values() if x > 15)
# # child = sum(x*5 for x in data.values() if x <= 18)
# # total = adults + child
# # print (discount)





#Ticket Challenge

'''
Ticket Office

You are analyzing sales data from a ticket office. 
The ticket for an adult is $20, while the ticket for a child under 18 is $5.
The data you are given is in a dictionary format, where the keys are the sold ticket numbers, and the values are the customer ages.
For example, "123-08": 24 means that the ticket was bought a 24 year old.
Your goal is to calculate how much more money the office would make if it would change the ticket discount age to the given input.
So, your program needs to take an integer as input and output the percentage of revenue growth, if the discount was given to people under that age.

For example, if the office made $15000 with the original discount age, and would make $18000 with 14 as the discount age, then the growth would be ((18000-15000)/15000)*100 = 20%

Test data
data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}
'''



# data = {
#     "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
# }

# discount_age = 18
# new_discount_age = int(input("WHAT IS THE NEW DISCOUNT AGE?\n"))

# def revenue_calc(data, disc_age):
#     count_adult = 0
#     count_child = 0
#     for i in data.values():
#         if (i >= disc_age):
#             count_adult += 1
#         else:
#             count_child += 1

#     rev_adult = count_adult * 20
#     rev_child = count_child * 5

#     total_rev = rev_adult + rev_child

#     return total_rev

# current_rev = revenue_calc(data, discount_age)
# new_rev = revenue_calc(data, new_discount_age)

# rev_percent_increase = ((new_rev - current_rev)/ current_rev) * 100

# print(round(rev_percent_increase),"%")


# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 08:41:03 2025

@author: Ayobami Adeyemo
"""

data = {"100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54":19, "097-32": 33, "065-135": 64, "99-043": 80,\
        "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44,\
        "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15,  "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21,\
        "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40}

q = int(input("Enter desired discount age:"))
y = data.values()
z = len(y)
# print(z)
# print (y)

def count(integer, chars=[]):
    count = 0
    for i in integer:
        if i in chars:
            count += 1
    return count

special = list(range(1,q+1))
x = count(y,special)
#print(x)


#Standard Revenue 
if q == 18:
    x = 15
    Total_revenue = (z - 15) * 20 +  15 * 5
    print(Total_revenue)
#Discounted Revenue
elif q == q:
    Discount_revenue = (z - x) * 20 + x * 5
    print ("Total Revenue at discount age", q ,"is:", Discount_revenue)

Total_revenue = (z - 15) * 20 +  15 * 5
Percentange_Change = abs((Discount_revenue - Total_revenue)/Discount_revenue * 100)
print("Percentage Change in Revenue with Discount Age", q, "is", round(Percentange_Change),"%")