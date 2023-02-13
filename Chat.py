name = input("Whats Your Name?")
age = int(input("How old are you?"))
department = input("What is your department?")

#print("hi %s, how are you ? I can see that you are from %s department. You are %i years old" %(name,department, age))
print(f"hi {name}, how are you? I see that you are from {department} department. You are {age} year old")