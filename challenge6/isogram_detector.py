def is_isogram(text):
   for i in range(len(text)):
      for j in  range(i+1, len(text)):
         
         if text[i]==text[j]:
            return False
   return True
prompt=input("Enter text please")
text=prompt
print(is_isogram(text))

        


    