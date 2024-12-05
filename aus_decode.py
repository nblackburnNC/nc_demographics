

def decode_pcode_medians():
    return {
        '1' : 'Median_Age',
        '4' : 'Median_Household_Income',
        '5' : 'Median_mortgage_repayments',
        '6' : 'Median_rent',
        '8' : 'Median_household_size',
    }

def decode_pcode_industry():
    return {
        'A' : 'agricultureForestryAndFishing',
        'B' : 'mining',
        'C' : 'manufacturing',
        'D' : 'electricityGasWaterAndWaste',
        'E' : 'construction',
        'F' : 'wholesaleTrade',
        'G' : 'retailTrade',
        'H' : 'accommodationAndFoodServices',
        'I' : 'transportPostalAndWarehousing',
        'J' : 'informationMediaAndTelecommunications',
        'K' : 'financeAndInsurance',
        'L' : 'rentalHiringAndRealEstateServices',
        'M' : 'professionalScientificAndTechnical',
        'N' : 'administrativeAndSupportServices',
        'O' : 'publicAdministrationAndSafety',
        'P' : 'educationAndTraining',
        'Q' : 'healthCareAndSocialAssistance',
        'R' : 'artAndRecreationServices',
        'S' : 'otherServices',
    }

def decode_pcode_transport_2_work():
    return {
        "1" : "train",
        "2" : "bus",
        "3" : "ferry",
        "4" : "tramLight rail",
        "5" : "taxi",
        "6" : "car",
        "7" : "car", # car_passangerwill need to merge with car
        "8" : "truck",
        "9" : "motorbike",
        "10" : "bicycle",
        "11" : "other",
        "232" : "walking",
        "233" : "workFromHome",
    }

def decode_pcode_dwelling_type():
    return {
        "11" : "house",
        "2" : "semiDetachedOrTerrace",
        "3" : "flatOrApartment",
        "9" : "otherDwelling",
        "_N" : "dwellingStructureNotSpecified",
    }

def decode_pcode_dwelling_tenure():
    return {
        "1" : "ownedOutright",
        "2" : "ownedMortgage",
        "R_T" : "rented_total",
        "3" : "rentedRegular", # Rented: Real estate agent
        "4" : "rentedStateHousingAuthority", # Rented: State or territory housing authority
        "5" : "rentedStateHousingAuthority", # Rented: Community housing provider
        "6" : "rentedRegular", # Rented: Person not in same household
        "7" : "rentedRegular", # Rented: Other landlord type
        "R_N" : "rentedRegular", # Rented: Landlord type not stated
        "9" : "otherTenureType",
        "_N" : "tenureTypeNotSpecified",
    }

def decode_pcode_ancestry():
    return {
        "1101" : "australian",
        "1102" : "indigenousAustralian",
        "6101" : "chinese",
        "3204" : "croatian",
        "2303" : "dutch",
        "2101" : "english",
        "5201" : "filipino",
        "2305" : "french",
        "2306" : "german",
        "3205" : "greek",
        "3304" : "hungarian",
        "7106" : "indian",
        "2201" : "irish",
        "3103" : "italian",
        "6902" : "korean",
        "4106" : "lebanese",
        "3206" : "macedonian",
        "3104" : "maltese",
        "1201" : "maori",
        "1202" : "newZealand",
        "3307" : "polish",
        "3308" : "russian",
        "2102" : "scottish",
        "3213" : "serbian",
        "9215" : "southAfrican",
        "3106" : "spanish",
        "7126" : "sriLankan",
        "5107" : "vietnamese",
        "2103" : "welsh",
        "_O" : "other",
        "_N" : "ancestryNotStated",
    }

def decode_population():
    return {}