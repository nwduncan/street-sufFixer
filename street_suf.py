## Street suffix restorer
## Nathan Duncan
## Converts the abbreviated suffix in a string to the full name.
## e.g. 'Example Ln' = 'Example Lane'
## Returns False if no match found.
## Append entries to the dictionary to suit your needs.
## import street_suf and run with street_suf.Fixer("input string")

def Fixer(testString):
    testString = testString.strip()
    testString = testString.lower()
    # Abbreviation key dictionary. Edit as required.
    keyDict = { 'av': 'avenue',
                'rd': 'road',
                'ct': 'court',
                'crt': 'court',
                'st': 'street',
                'tce': 'terrace',
                'cr': 'crescent',
                'pl': 'place',
                'hwy': 'highway',
                'dr': 'drive',
                'crct': 'circuit',
                'cct': 'circuit',
                'ln': 'lane',
                'cov': 'cove',
                'gr': 'grove',
                'cl': 'close',
                'grn': 'green',
                'wy': 'way',
                'wlk': 'walk',
                'tc': 'terrace',
                'cnr': 'corner',
                'pde': 'parade',
                'cres': 'crescent',
                'avenue': 'avenue',
                'road': 'road',
                'court': 'court',
                'street': 'street',
                'crescent': 'crescent',
                'place': 'place',
                'highway': 'highway',
                'drive': 'drive',
                'circuit': 'circuit',
                'lane': 'lane',
                'cove': 'cove',
                'grove': 'grove',
                'close': 'close',
                'green': 'green',
                'way': 'way',
                'walk': 'walk',
                'terrace': 'terrace',
                'corner': 'corner',
                'parade': 'parade',
                'pines': 'pines',
                'copse': 'copse',
                'cross': 'cross',
                'meadow': 'meadow',
                'fell': 'fell',
                'rest': 'rest',
                'mews': 'mews',
                'view': 'view',
                'rise': 'rise',
                'ridge': 'ridge',
                'dale': 'dale',
                'bend': 'bend',
                'hill': 'hill',
                'end': 'end',
                'nook': 'nook',
                'dam': 'dam',
                'vista': 'vista' }

    attempt_items = 0
    # Iterate over the keys to find a match
    for key in keyDict:
        attempt_items += 1
        keyTest = " " + key
        lenTest = -len(keyTest)
        inpTest = testString[lenTest:]
        # If a match is found return the fixed string
        if keyTest == inpTest:
            newName = testString[:lenTest] + " " + keyDict[key]
            return newName.title()
        # If no matc is found return False
        else:
            if attempt_items == len(keyDict):
                return False
            else: pass
