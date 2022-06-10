num = int(input('How many numbers: '))
total_sum = 0
for n in range(num):
    try:
        numbers = float(input('Enter number : '))
    except:
        print("no number, please try again.")
    total_sum += numbers
avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)




