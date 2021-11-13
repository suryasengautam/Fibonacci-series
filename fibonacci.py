#1st method
##logic:- a swaped by a+b,b swaped by a
a=0
b=1
i = 1
while i<=10:
    print(a)
    # c=a+b
    # a=b
    # b=c
    a,b=a+b,a
    i+=1
#######################################################################
##2nd method
#####logic:-third variable in c assign a+b and swap a,b,c
# a=0
# b=1
# i = 1
# while i<=10:
#     print(a)   
#     c=a+b
#     # a,b,c=c,a,b
#     # a,b,c=b,c,a
#     tem = a
#     a = b
#     b= c
#     c= tem
#     i+=1