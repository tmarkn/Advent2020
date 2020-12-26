import re

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

# possible eye colors
eyeColors = {
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth'
}

# hair color regex pattern
hclPattern = re.compile(r'^#(?:[0-9a-f]{6})$')

# passport extends dictionary with a custom isValid function
class Passport(dict):
    def isValid(self):
        # check if all fields exist
        for field in fields:
            if field not in self:
                return False
        
        # byr (Birth Year)
        if int(self['byr']) < 1920 or int(self['byr']) > 2002:
            return False
        # iyr (Issue Year)
        if int(self['iyr']) < 2010 or int(self['iyr']) > 2020:
            return False
        # eyr (Expiration Year)
        if int(self['eyr']) < 2020 or int(self['eyr']) > 2030:
            return False
        
        # hgt (Height)
        # cm
        if self['hgt'].endswith('cm'):
            if int(self['hgt'][:-2]) < 150 or int(self['hgt'][:-2]) > 193:
                return False
        # in
        elif self['hgt'].endswith('in'):
            if int(self['hgt'][:-2]) < 59 or int(self['hgt'][:-2]) > 76:
                return False
        # neither cm nor in
        else:
            return False

        # hcl (Hair Color)
        if not hclPattern.match(self['hcl']):
            return False
        # ecl (Eye Color)
        if self['ecl'] not in eyeColors:
            return False
        # pid (Passport ID)
        if len(self['pid']) != 9 or not self['pid'].isdigit():
            return False
        return True

# get input
with open('Day04/input.txt', 'r') as f:
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
numValidPassports = sum(passport.isValid() for passport in passports)
print(f'The number of valid passports is {numValidPassports}')