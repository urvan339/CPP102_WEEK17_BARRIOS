"""Simulated Device Monitoring and Alert System (CPP102 Week 17)."""


def get_initial_readings():
    """Return the starting list of simulated temperature readings in Celsius."""
    return [28, 31, 35, 37, 29]


def display_menu():
    """Print the main menu."""
    print()
    print("SIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")
    print()


def is_whole_number(text):
    """Return True if text is a whole number such as 33 or -5."""
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":  # a minus sign is allowed only at the front
        start = 1
    if start == len(text):  # the text is only "-"
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True


def display_readings(readings):
    """Print every reading with its position number."""
    print()
    print("CURRENT READINGS")
    print("----------------")
    position = 1
    for reading in readings:
        print(f"Reading {position}: {reading} °C")
        position = position + 1


def add_reading(readings, lowest, highest):
    """Ask for one reading and add it to the list only if it is valid."""
    text = input("Enter new reading: ")
    print()
    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
    elif int(text) < lowest or int(text) > highest:
        print(f"Invalid reading. Enter a value from {lowest} to {highest}.")
    else:
        readings.append(int(text))
        print("Reading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return NORMAL, WARNING, or CRITICAL for one reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:  # boundary: 35 is still WARNING
        return "WARNING"
    else:
        return "CRITICAL"


def display_classification(readings, warning_limit, critical_limit):
    """Print every reading with its classification."""
    print()
    print("READING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        category = classify_reading(reading, warning_limit, critical_limit)
        print(f"{reading} °C -> {category}")


def compute_total(readings):
    """Return the total of all readings (computed with a loop)."""
    total = 0
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    """Return the average of all readings."""
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Return the smallest reading (computed with a loop)."""
    minimum = readings[0]  # start with the first reading, not 0
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    """Return the largest reading (computed with a loop)."""
    maximum = readings[0]  # start with the first reading, not 0
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Return how many readings belong to the given category."""
    count = 0
    for reading in readings:
        if classify_reading(reading, warning_limit, critical_limit) == category:
            count = count + 1
    return count


def compute_percentage(count, whole):
    """Return count as a percentage of whole."""
    return count / whole * 100


def determine_overall_status(warning_count, critical_count):
    """Return the overall monitoring status."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings, warning_limit, critical_limit):
    """Print the full numerical summary and the overall status."""
    number = len(readings)
    normal_count = count_category(readings, warning_limit, critical_limit, "NORMAL")
    warning_count = count_category(readings, warning_limit, critical_limit, "WARNING")
    critical_count = count_category(readings, warning_limit, critical_limit, "CRITICAL")

    print()
    print("MONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {number}")
    print(f"Total of readings   : {compute_total(readings)}")
    print(f"Average temperature : {compute_average(readings):.2f} °C")
    print(f"Minimum temperature : {find_minimum(readings)} °C")
    print(f"Maximum temperature : {find_maximum(readings)} °C")
    print()
    print(f"NORMAL   : {normal_count} ({compute_percentage(normal_count, number):.2f}%)")
    print(f"WARNING  : {warning_count} ({compute_percentage(warning_count, number):.2f}%)")
    print(f"CRITICAL : {critical_count} ({compute_percentage(critical_count, number):.2f}%)")
    print()
    print("Overall Status:", determine_overall_status(warning_count, critical_count))


def main():
    """Control the order of the program: show the menu until the user exits."""
    lowest = 0
    highest = 100
    warning_limit = 30    # 30 and above is WARNING
    critical_limit = 35   # above 35 is CRITICAL
    readings = get_initial_readings()

    running = True
    while running:
        display_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            print()
            add_reading(readings, lowest, highest)
        elif choice == "3":
            display_classification(readings, warning_limit, critical_limit)
        elif choice == "4":
            display_summary(readings, warning_limit, critical_limit)
        elif choice == "5":
            print()
            print("Thank you for using the Device Monitoring System.")
            running = False
        else:
            print()
            print("Invalid choice. Please enter a number from 1 to 5.")


main()