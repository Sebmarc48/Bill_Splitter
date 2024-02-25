from random import uniform

names_and_prices = {}
name_list = []


def get_dividends_lucky(bill, names, name_list):
    for name_person in name_list:
        names[name_person] = round((bill / (len(name_list) - 1)), 2)
    return names


def get_dividends(bill, names, name_list):
    for name_person in name_list:
        names[name_person] = round((bill / (len(name_list))), 2)
    return names


def get_lucky_person(names):
    random_num = int(uniform(1, (len(names))))
    return names[random_num]


num = int(input("Enter the number of friends joining (including you):"))
if num < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(num):
        name = input()
        name_list.append(name)

    total_bill = int(input("Enter the total bill value:"))
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input()
    if (choice == "Yes"):
        lucky_person = get_lucky_person(name_list)
        names_and_prices = get_dividends_lucky(total_bill, names_and_prices, name_list)
        names_and_prices[lucky_person] = 0
        print(lucky_person, " is the lucky one!")
        print(names_and_prices)

    else:
        print("No one is going to be lucky")
        names_and_prices = get_dividends(total_bill, names_and_prices, name_list)
        print(names_and_prices)
