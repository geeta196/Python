products = ["mobile", "laptop", "tablet"]

search = input("Enter product name: ")

for item in products:
    if item == search:
        print("Product found")
        break
else:
    print("Product not found")
