# Fix the code below so that the it runs as expected

def getNameandAge():

    # 1. Variable was called nam not name
    # 2. Mix of single and double quotes
    name = input("Please enter your name:")
    age = int(input('Please enter your age:'))
    # 3. Comma missing from print statement
    print(name, age)

    # 4. Age should be greater than 17 to be an adult
    if age > 17:
        # 5. Missing a '+' symbol after name
        print("Hi " + name + " you are an adult")
    else:
        print("Hi " + name + " you are a minor")

while True:
    getNameandAge()
