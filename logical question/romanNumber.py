def int_to_roman(x):
    numbers=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CD","D","CM","M"]
    i=12
    roman_numbera1=""
    while x != 0:
        if numbers[i]<=x:
            roman_numbera1 +=roman[i]
            x=x-numbers[i]
        else:
            i-=1
    return roman_numbera1
x=int(input("enter the number"))
print(int_to_roman(x)) 



