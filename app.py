 
"""
Hostel Waste Management System
Main application entry point.
"""

from students import (
    students,
    calculate_total_waste,
    get_highest_waste_record
)

from utils.helpers import (
    display_waste_records,
    display_category_statistics,
    display_hostel_summary
)


def add_waste_record():
    """Add a new student waste collection record."""

    print("\n========== ADD WASTE RECORD ==========")

    name = input("Student name: ")
    hostel = input("Hostel block: ")
    room = input("Room number: ")
    waste_type = input("Waste category: ")
    quantity = float(input("Waste quantity (kg): "))

    new_record = {
        "name": name,
        "hostel": hostel,
        "room": room,
        "waste_type": waste_type,
        "quantity": quantity
    }

    students.append(new_record)

    print("\nWaste record added successfully!")


def show_total_waste():
    """Display the total quantity of waste collected."""

    total = calculate_total_waste()

    print("\n========== TOTAL WASTE ==========")
    print(f"Total waste collected: {total} kg")


def show_highest_waste():
    """Display the student record with the highest waste quantity."""

    record = get_highest_waste_record()

    print("\n========== HIGHEST WASTE RECORD ==========")

    if record is None:
        print("No waste records available.")
        return

    print(f"Student: {record['name']}")
    print(f"Hostel: {record['hostel']}")
    print(f"Quantity: {record['quantity']} kg")



def main():
    while True:
        print("\n========== HOSTEL WASTE MANAGER ==========")
        print("1. View Waste Records")
        print("2. Add Waste Record")
        print("3. View Total Waste Collected")
        print("4. View Waste Category Statistics")
        print("5. View Hostel Waste Summary")
        print("6. View Highest Waste Record")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_waste_records()
        elif choice == "2":
            add_waste_record()
        elif choice == "3":
            show_total_waste()
        elif choice == "4":
            display_category_statistics()
        elif choice == "5":
            display_hostel_summary()
        elif choice == "6":
            show_highest_waste()
        elif choice == "0":
            print("Thank you for using Hostel Waste Manager!")
            break
        else:
            print("Invalid choice.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
