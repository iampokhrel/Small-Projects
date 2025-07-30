'''
This project was taken from "Coding with Sagar" YouTube channel with link https://www.youtube.com/watch?v=iCwkuJOxvRI
'''

rent  = float(input("Enter your hostel/flat rent: "))
food = float(input("Enter your total food ordered amount: "))
elect = float(input("Enter total electricity units used: "))
elect_charge = float(input("Enter electricity charges per unit: "))
persons = float(input("Total number of persons in hostel/flat: "))

total_amt = rent + food + (elect*elect_charge)
rent_per_person = total_amt/persons

print(f"The total rent is {total_amt:.2f}")
print(f"The rent payable per person is {rent_per_person:.2f}")


