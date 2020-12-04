# required fields
fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
    # 'cid'
]

# passport extends dictionary with a custom isValid function
class Passport(dict):
    def isValid(self):
        for field in fields:
            if field not in self:
                return False
        return True

# get input
with open('Day4/input.txt', 'r') as f:
    inp = f.read()

# split by two newline characters
items = [x.split() for x in inp.split('\n\n')]

# create passport dictionaries
passports = []
for item in items:
    passport = Passport()
    passports.append(passport)

    # split key:value pairs with colon
    for field in item:
        key, value = field.split(':')
        passport[key] = value

# count valid passports
validPassports = 0
for passport in passports:
    if passport.isValid():
        validPassports += 1

print(f'The number of valid passports is {validPassports}')