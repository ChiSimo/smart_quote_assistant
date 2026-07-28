# Smart Quote Request Assistant

This is a small Python program that collects customer and job information for a quote request.

The program checks that the main information is valid, calculates an indicative price, displays a summary, and saves the request in a text file.

## Requirements

- Python 3
- Visual Studio Code or another code editor

## How to run the program

1. Open the project folder in Visual Studio Code.
2. Open a new terminal.
3. Run the following command:

```bash
python3 main.py

## Features

- Collects the customer name, email address and phone number
- Collects the job location, service type and surface type
- Checks that required fields are not empty
- Performs basic validation of email addresses and phone numbers
- Checks that the area is a positive number
- Calculates an indicative price using a fixed rate per square metre
- Creates a unique quote reference number
- Displays a summary of the quote request
- Saves each request in `quote_requests.txt`

## Project files

- `main.py` contains the program code
- `quote_requests.txt` stores the completed quote requests
- `README.md` explains how to run and use the project

## Limitations

- The program uses one fixed rate of $150 per square metre
- It does not calculate different prices for different services
- The email and phone validation is basic
- The data is saved in a text file instead of a database
- The program only runs in the terminal
- The estimate is not a final quotation

## Future improvements

- Add different rates for different services and surface types
- Create a web-based interface
- Save requests in a database
- Allow customers to upload photos
- Add stronger email and phone validation
- Send completed quote requests by email
- Add a login area for the business owner