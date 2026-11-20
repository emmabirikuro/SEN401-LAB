
#Utility functions for Hostel Waste Management System.


from students import students


def display_waste_records():
    #Display all recorded waste collection activities.

    print("\n========== WASTE RECORDS ==========")

    for student in students:
        print(
            f"Student: {student['name']} | "
            f"Hostel: {student['hostel']} | "
            f"Room: {student['room']} | "
            f"Category: {student['waste_type']} | "
            f"Quantity: {student['quantity']} kg"
        )


def calculate_category_totals():
    #Calculate the total quantity collected per waste category.

    category_totals = {}

    for student in students:
        category = student["waste_type"]
        quantity = student["quantity"]

        if category in category_totals:
            category_totals[category] += quantity
        else:
            category_totals[category] = quantity

    return category_totals


def display_category_statistics():
    #Display waste quantities grouped by category.

    totals = calculate_category_totals()

    print("\n========== WASTE STATISTICS ==========")

    for category, quantity in totals.items():
        print(f"{category}: {quantity} kg")


def display_hostel_summary():
    """Display waste quantities grouped by hostel."""

    hostel_totals = {}

    for student in students:
        hostel = student["hostel"]
        quantity = student["quantity"]

        if hostel in hostel_totals:
            hostel_totals[hostel] += quantity
        else:
            hostel_totals[hostel] = quantity

    print("\n========== HOSTEL SUMMARY ==========")

    for hostel, quantity in hostel_totals.items():
        print(f"{hostel}: {quantity} kg")
