# Smart Quote Request Assistant

Smart Quote Request Assistant is a Python program created to collect and organise the main information needed for a trade quote request.

The program asks for customer details, job information, surface condition, requested finish, visible damage, available photos and area measurements. It then classifies the job, recommends whether a site inspection may be needed, calculates an approximate price range and saves the completed request in a text file.

The calculated range is only an initial estimate. A formal quote may change after the business reviews the photos or inspects the job.

## Requirements

- Python 3
- Visual Studio Code or another code editor
- A terminal or command line
- No external Python packages are required

## How to run the program

1. Open the project folder in Visual Studio Code.
2. Open a new terminal.
3. Run:

```bash
python3 main.py
```

If this command does not work, try:

```bash
python main.py
```

4. Enter the requested customer and job information.
5. The completed request will be displayed in the terminal.
6. The request will also be saved locally in `quote_requests.txt`.

## Features

- Collects the customer name, email address and phone number
- Collects the job location
- Collects the service type and surface type
- Collects the current condition of the surface
- Collects the requested finish
- Records whether damage is present
- Records whether photos are available
- Collects the area in square metres
- Allows additional job notes
- Prevents required text fields from being empty
- Rejects numeric-only service and surface descriptions
- Performs basic email and phone validation
- Rejects zero, negative and non-numeric area values
- Classifies the job as Low, Medium or High complexity
- Recommends whether a site inspection may be required
- Calculates an approximate price range
- Generates a unique quote request ID
- Saves completed requests without deleting earlier records

## How the approximate price range works

The prototype uses a base rate of $150 per square metre.

The basic estimate is calculated using:

```text
Area × Base rate
```

When damage is present, the estimated amount is increased by 25%.

The program then calculates a range that is 10% below and 10% above the estimated amount.

For example, a 50 m² job with damage produces the following calculation:

```text
50 × $150 = $7,500
$7,500 + 25% = $9,375
Approximate range = $8,437.50 to $10,312.50
```

This calculation is intentionally simplified because the final price of a trade job may also depend on the material, condition, access, required finish, amount of repair work, products used and other site conditions.

## Job classification

The program uses the submitted information to give the job a basic complexity level.

A job may be classified as High when:

- damage is present;
- the condition includes words such as damaged or scratched;
- the requested work includes grinding.

A site inspection may also be recommended when:

- damage is present;
- photos are not available;
- the job appears to require more detailed professional assessment.

This classification is only an initial guide and does not replace professional judgement.

## Project files

- `main.py` contains the Python program
- `README.md` contains the project instructions and documentation
- `.gitignore` prevents local customer test records from being uploaded
- `quote_requests.txt` stores completed requests locally and is generated when the program runs

## Testing

The program was tested several times during development. Earlier tests were completed before all features had been added, while the final test used the current version of the program.

### Test 1: Initial price calculation

Input:

- Service type: Polish
- Surface type: Marble
- Area: 50 m²
- Additional notes: Honed finish

Result:

- The program calculated a price of $7,500.00
- The request was saved in the text file

This test confirmed that the original area-based calculation worked.

### Test 2: Quote ID and formatted price

Input:

- Service type: Polish
- Surface type: Granite
- Area: 50 m²
- Additional notes: Honed finish

Result:

- A unique quote ID was generated
- The price was displayed as `$7,500.00`
- The request was saved successfully

This test confirmed that the quote ID and currency formatting worked.

### Test 3: Numeric surface input

Input:

- Service type: Grinding
- Surface type: `50`

Result in the earlier version:

- The value was accepted

This showed that the original validation only checked whether the field was empty. The program was later updated to reject numeric-only service and surface values.

### Test 4: Job assessment without price range

Input:

- Service type: Polish
- Surface type: Marble
- Current condition: Scratches
- Requested finish: Honed
- Damage present: Yes
- Photos available: No
- Area: 50 m²

Result:

- Job complexity: High
- Site inspection recommended: Yes
- The request was saved for professional review

This test confirmed that job complexity and inspection recommendations were working.

### Test 5: Final version with approximate price range

Input:

- Service type: Polish
- Surface type: Marble
- Current condition: Damaged
- Requested finish: Polished
- Damage present: Yes
- Photos available: Yes
- Area: 50 m²
- Additional notes: Sealing

Expected and actual result:

- Job complexity: High
- Site inspection recommended: Yes
- Approximate price range: $8,437.50 to $10,312.50
- The request was saved successfully

This test confirmed that the final version could collect detailed job information, classify the job and calculate an approximate price range.

### Test 6: Empty required information

Input:

- Leave a required field empty

Expected result:

- The program displays `This field cannot be empty.`
- The user is asked to enter the information again

### Test 7: Invalid text value

Input:

- Enter `50` as the service type or surface type

Expected result:

- The program displays `Please enter a valid text value.`
- The user is asked to enter the information again

### Test 8: Invalid phone number

Input:

- `abc123`

Expected result:

- The program displays `Please enter a valid phone number using digits only.`

### Test 9: Invalid area

Input:

- `twenty`
- `-5`
- `0`

Expected result:

- Text input displays `Please enter a valid number.`
- Zero or negative values display `Area must be greater than zero.`

## Limitations

- The price calculation is simplified and does not represent every possible trade cost
- The same base rate is currently used for all services and materials
- The program cannot analyse uploaded photographs
- Photos can only be recorded as available or unavailable
- The email validation is basic
- An address such as `simona@gmail.con` may be accepted because the program only checks for `@` and `.`
- The phone validation only checks that the value contains digits and has at least eight characters
- The complexity classification depends partly on keywords entered by the user
- Spelling mistakes may prevent some condition keywords from being recognised
- The program saves data in a text file rather than a database
- The program runs only in the terminal
- The approximate price range is not a formal quotation

## Future improvements

- Use different base rates for different trades, materials and job types
- Allow staff to manually adjust the estimate
- Add more detailed questions about access, stairs, edges and site conditions
- Improve email validation
- Support Australian phone number formats
- Improve spelling and keyword recognition
- Create a web-based interface
- Allow customers to upload photos
- Save requests in a database
- Add customer consent and privacy information
- Send completed requests to the business by email
- Add secure staff login
- Allow a professional to approve or edit the final quote

## Privacy

The program collects customer information such as names, email addresses, phone numbers and job locations.

For this prototype, requests are stored only in a local text file. The file is excluded from GitHub through `.gitignore` so that customer and test information is not uploaded to the public repository.

A production version would require stronger security, access controls, consent information and a clear data-retention policy.