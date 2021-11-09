bill = float(input("Enter your bill, please: ").replace("$", ""))
twenty = bill / 100 * 20
fifty = bill / 100 * 50
eighty = bill / 100 * 80
print(f"""Here is your bill: {bill:.2f}$
And here is your options for the tips: 
20% - {twenty:.2f}$
50% - {fifty:.2f}$
80% - {eighty:.2f}$""")
