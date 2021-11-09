bill = float(input("Enter your bill, please: ").replace("$", ""))
# float(input("Enter your bill, please: ").strip("$"))
small = bill / 100 * 15
medium = bill / 100 * 18
big = bill / 100 * 20
print(f"""Here is your bill: {bill:.2f}$
-------------------------------------
And here is your options for the tips: 
-------------------------------------
15% - {small:.2f}$
18% - {medium:.2f}$
20% - {big:.2f}$""")
