import requests

def check_carrier(phone_number, api_key):
    base_url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=US&format=1"
    response = requests.get(base_url)
    data = response.json()

    if "valid" in data and data["valid"]:
        return data.get("carrier", "Carrier information not available")
    else:
        return "Invalid Number"

def save_numbers_by_carrier(phone_numbers, api_key):
    carriers = {}
    for number in phone_numbers:
        carrier = check_carrier(number, api_key)
        if carrier not in carriers:
            carriers[carrier] = []
        carriers[carrier].append(number)

    for carrier, numbers_list in carriers.items():
        # Remove any characters that are not letters, numbers, or underscores from the carrier name
        clean_carrier = ''.join(c for c in carrier if c.isalnum() or c == '_')
        filename = f"{clean_carrier}_numbers.txt"
        with open(filename, "w") as file:
            file.write("\n".join(numbers_list))

if __name__ == "__main__":
    file_name = input("List number: ")
    with open(file_name, "r") as file:
        phone_numbers = file.read().splitlines()

    api_key =""  # change with your numverify apikey

    save_numbers_by_carrier(phone_numbers, api_key)
