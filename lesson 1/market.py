print("now we calculate your marketing:\n\nprices:\n------------\ntomato=3 NIS\ncucamber=2 NIS\ncola=5 NIS\nchicken=20 NIS\n")
tomatos=int(input("enter how many tomato?""))
cucmabers=int(input("enter how many cucambers?"))
colas=int(input("enter how many colas?"))
chickens=int(input("enter how many chickens?"))

print("\nsummary of your order:\n---------------\ntomatos: " + str(tomatos) + "\ncucambers: " + str(cucambers) + "\ncolas: " + str(colas) + "\nchickens: " + str(chickens))

sum1=tomatos*3
sum2=cucambers*2
sum3=colas*5
sum4=chickens*20

summary=(tomatos*3)+(cucambers*2)+(colas*5)+(chickens*20)
print("\nyou have to pay: " + str(summary) + " NIS without tax")
print("\nyou have to pay: " + str("%.2f" % (summary*1.17) + " NIS without tax")

