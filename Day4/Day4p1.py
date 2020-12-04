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

class Passport(dict):
    def isValid(self):
        for field in fields:
            if field not in self:
                return False
        return True

# get input
with open('Day4/input.txt', 'r') as f:
    inp = f.read()

items = [x.split() for x in inp.split('\n\n')]

passports = []
for item in items:
    passport = Passport()
    passports.append(passport)

    for field in item:
        key, value = field.split(':')
        passport[key] = value

validPassports = 0
for passport in passports:
    if passport.isValid():
        validPassports += 1

print(validPassports)