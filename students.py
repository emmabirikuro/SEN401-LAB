
"""
Hostel Waste Management System
Student waste collection records.
"""

students = [
    {
        "name": "Emmanuel",
        "hostel": "Block A",
        "room": "A12",
        "waste_type": "Plastic",
        "quantity": 3
    },
    {
        "name": "David",
        "hostel": "Block B",
        "room": "B08",
        "waste_type": "Organic",
        "quantity": 5
    },
    {
        "name": "Sarah",
        "hostel": "Block A",
        "room": "A15",
        "waste_type": "Paper",
        "quantity": 2
    },
    {
        "name": "Michael",
        "hostel": "Block C",
        "room": "C04",
        "waste_type": "Plastic",
        "quantity": 4
    },
    {
        "name": "Grace",
        "hostel": "Block B",
        "room": "B11",
        "waste_type": "Organic",
        "quantity": 6
    }
]


def calculate_total_waste():
    """Calculate the total quantity of waste collected."""
    total = 0

    for student in students:
        total += student["quantity"]
    return total


def get_highest_waste_record():
    """Find the student record with the highest waste quantity."""
    if not students:
        return None
    
    return max(students, key=lambda student: student["quantity"])
