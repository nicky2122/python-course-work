import my_programs

def show_menu():
    print("\n* FUNCTION MENU *")
    print("1. Find the median of a list")
    print("2. Print even-indexed characters from string")
    print("3. Generate a random number between 1 to 100")
    print("4. Display calendar for a given month and year")
    print("5. Check if a triangle is equilateral, isosceles or scalene")
    print("6. Calculate BMI (Body Mass Index)")
    print("7. Find all factors of a number")
    print("8. Convert a string to title case without using title()")
    print("9. Count total number of spaces in a string")
    print("10. Convert hours and minutes into seconds")
    print("0. Exit")
    print("*")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        my_programs.median_of_list()
    elif choice == "2":
        my_programs.even_indexed_chars()
    elif choice == "3":
        my_programs.random_number()
    elif choice == "4":
        my_programs.display_calendar()
    elif choice == "5":
        my_programs.triangle_type()
    elif choice == "6":
        my_programs.bmi_calc()
    elif choice == "7":
        my_programs.factors()
    elif choice == "8":
        my_programs.title_case()
    elif choice == "9":
        my_programs.count_spaces()
    elif choice == "10":
        my_programs.time_to_seconds()
    elif choice == "0":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.\n")
