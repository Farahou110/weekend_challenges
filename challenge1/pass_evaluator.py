import re

def check_password(password):  
    for x in password: 
     sp = bool(re.search(r"[!,@,#,$,%^&*(),]", password))
    for x in  password:
         
     
    length = len(password) > 6   
    for x in password: {
     num_check ==str(x) in password}

        
    
        # num_check =bool(type(x))= int
 
    # print("password length is less than required")
    return sp,length,num_check

password = input(f"enter password  ")
sp,length,num_check = check_password(password)



# if length :
#  if sp :
if (num_check == int):
   print ("✅✅ ✅Strong✅✅✅")
else:
     print("❌❌❌weak❌❌❌")    

