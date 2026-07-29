"""Smart Quote Request Assistant.

This program collects the main details needed for a quote request,
checks that the information is valid, calculates an estimated price,
and saves the request in a text file.
"""

from datetime import datetime


def get_required_text(prompt):
    """Ask the user for information and prevent an empty answer."""
    value = input(prompt).strip()

    while value == "":
        print("This field cannot be empty.")
        value = input(prompt).strip()

    return value


def get_text_only(prompt):
    """Ask the user for text and reject empty or numeric-only answers."""
    value = input(prompt).strip()

    while value == "" or value.isdigit():
        print("Please enter a valid text value.")
        value = input(prompt).strip()

    return value


# Display the application title
print("Smart Quote Request Assistant")

# Collect and validate the customer's name
customer_name = get_required_text("Enter the customer name: ")

# Collect and perform basic validation on the customer's email address
email = input("Enter the customer email: ").strip()

while "@" not in email or "." not in email:
    print("Please enter a valid email address.")
    email = input("Enter the customer email: ").strip()

# Collect and validate the customer's phone number
phone = input("Enter the customer phone number: ").strip()

while not phone.isdigit() or len(phone) < 8:
    print("Please enter a valid phone number using digits only.")
    phone = input("Enter the customer phone number: ").strip()

# Collect and validate the job location
job_location = get_required_text("Enter the job location: ")

# Collect and validate the requested service type
service_type = get_text_only("Enter the service type: ")

# Collect and validate the surface type
surface_type = get_text_only("Enter the surface type: ")

# Collect optional information about the job
additional_notes = input("Enter any additional notes: ").strip()

if additional_notes == "":
    additional_notes = "No additional notes provided."

# Collect and validate the area as a positive numeric value
while True:
    try:
        area = float(input("Enter the area in square metres: "))

        if area > 0:
            break

        print("Area must be greater than zero.")

    except ValueError:
        print("Please enter a valid number.")

# Calculate the indicative price using a fixed rate per square metre
rate_per_square_metre = 150
estimated_price = area * rate_per_square_metre

# Generate a unique reference number using the current date and time
quote_id = datetime.now().strftime("QR-%Y%m%d-%H%M%S")

# Display a summary of the completed quote request
print("\n--- Quote Request Summary ---")
print("Quote ID:", quote_id)
print("Customer name:", customer_name)
print("Email:", email)
print("Phone:", phone)
print("Job location:", job_location)
print("Service type:", service_type)
print("Surface type:", surface_type)
print("Additional notes:", additional_notes)
print("Area:", area, "m²")
print(f"Estimated price: ${estimated_price:,.2f}")

# Explain that the calculated amount is not a final quotation
print("\nImportant: This is an indicative estimate only.")
print("A site inspection may be required before a final quote is provided.")

# Save the quote request to a text file without deleting previous records
with open("quote_requests.txt", "a", encoding="utf-8") as file:
    file.write("\n--- New Quote Request ---\n")
    file.write("Quote ID: " + quote_id + "\n")
    file.write("Date: " + str(datetime.now()) + "\n")
    file.write("Customer name: " + customer_name + "\n")
    file.write("Email: " + email + "\n")
    file.write("Phone: " + phone + "\n")
    file.write("Job location: " + job_location + "\n")
    file.write("Service type: " + service_type + "\n")
    file.write("Surface type: " + surface_type + "\n")
    file.write("Area: " + str(area) + " m²\n")
    file.write("Additional notes: " + additional_notes + "\n")
    file.write(f"Estimated price: ${estimated_price:,.2f}\n")

# Confirm that the record was saved
print("\nQuote request saved successfully.")