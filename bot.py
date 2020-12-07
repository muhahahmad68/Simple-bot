print('''Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.''')
name = input()
print(f"""What a great name you have, {name}!\nLet me guess your age.""")
print("Enter the remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Yor age is {age}; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
num = int(input())
count = 0
for _ in range(num + 1):
    print(count, '!')
    count += 1

print("""Let's test your programming knowledge.
Why do we use methods?""")

print("""1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
while True:
    ans = int(input())
    if ans == 2:
        break
    else:
        print("Please, try again.")
print("Completed, have a nice day!")
print("Congratulations, have a nice day!")
