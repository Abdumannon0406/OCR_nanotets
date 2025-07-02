import csv

# Example OCR text result
result = """<img>A Philippine ID card.</img>
**REPUBLIC OF THE PHILIPPINES**
DEPARTMENT OF TRANSPORTATION
LAND TRANSPORTATION OFFICE

**DRIVER'S LICENSE**

Last Name, First Name, Middle Name
PERLO, JUVEN

Nationality
Phil.

Sex
M

Date of Birth
1996/07/07

Weight (kg)
79

Height (m)
1.73

Address
1, JAN LINO ST. TALAMPAS, QUEZON CITY,
QUEZON SECOND DISTRICT, 1110

Issuance Date
NO 1-20-000002

Expiration Date
2024/07/07

Agency Code
NO 1

Blood Type
A

Eye Color
BLACK

DL Codes
A,B

Conditions
NONE

<signature>Juven Perlo</signature>
Signature of Licensee

<signature>Tose Arturo Tugade</signature>
ATTY. JOSE ARTURO M. TUGADE
Assistant Secretary
"""

# Simple parser: extract key-value lines
lines = result.splitlines()
parsed_data = []
for i in range(len(lines)-1):
    key = lines[i].strip()
    value = lines[i+1].strip()
    if key and value and not key.startswith("<") and not key.startswith("**"):
        parsed_data.append((key, value))

# Save to CSV
csv_file = "ocr_output.csv"
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Field", "Value"])
    writer.writerows(parsed_data)

print(f"✅ Saved to {csv_file}")
