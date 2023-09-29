CODES = ('+7', '8')

def check_phone(phone: str) -> bool:
    local_lens = 10
    for code in CODES:
        if phone.startswith(code):
            rest = phone[len(code):]
            return len(rest) == local_lens and rest.isdigit()
    return False

def get_regions_from_file(file:str = 'regions.txt'):
    with open(file, 'r') as file:
        data = [line.split('|') for line in file.readlines()]
    return {code: region.rstrip() for code, region in data}

def check_region(phone: str, region_codes:dict) -> str: 

print(check_phone('19282037102'))