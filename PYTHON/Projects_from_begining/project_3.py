# Bill Split Calculator

print("Bill Split Calculator")

bill_amount =float(input())
tip_precentage =float(input())
number =int(input())

tip_amount =(tip_precentage / 100)* bill_amount

total_amount =bill_amount + tip_amount

per_person =total_amount / number

print(f"Total (including tip): ${total_amount}")
print(f"Each person pays: ${per_person}")