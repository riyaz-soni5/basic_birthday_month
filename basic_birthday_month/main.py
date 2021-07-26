while True:
    month_list = ("1","January", "February", "March","April","May","June","July","August","September","October","November","December")

    user_birthday = input("enter your birthday in dd-mm-year : ")
    a = int(user_birthday[3:5])
    print("you were born in {}".format(month_list[a]))



