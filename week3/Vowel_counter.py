x=input("write your text")
vowels = list('a''e''i''o''u''A''E''I''O''U')
count=0

for char in x:
    if char in vowels:
        count+=1

print(f"the text '{x}' has {count} vowels" )