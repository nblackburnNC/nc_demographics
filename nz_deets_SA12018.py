NZ_FILE_PATH = 'nz_data/Statistical Area 1 dataset for Census 2018 - total New Zealand - CSV_updated_16-7-20/'
CODE = 'Area_code'
ENCODING = 'UTF-8'
AREA_UNIT = 'SA1'
# KEY_PAIR = 'SA2-TA'
KEY_PAIR = 'LBURB-TA'
# FILE_MAP_SA1_SA2 = {'filename' : 'nz_data/SA1-2018_SA2-2018.csv','from' : 'SA12018 V1.0.0', 'to' : 'SA22018 V1.0.0', 'to_name' : None, 'skip' : 6, 'to_header' : 'SA2'}
# FILE_MAP_SA2_TA = {'filename' : 'nz_data/sa2-2018_TA-2018.csv','from' : 'SA22018 V1.0.0', 'to' : 'TA2018 V1.0.0', 'to_name' : None, 'skip' : 6, 'to_header' : 'TA'}
# FILE_MAP_SA1_MB = {'filename' : 'nz_data/MB-2018_SA1-2018.csv','from' : 'SA12018 V1.0.0', 'to' : 'MB2018 V1.0.0', 'to_name' : 'MB2018 V1.0.0', 'skip' : 6, 'to_header' : 'MB'}
FILE_MAP_SA1_MB_v3 = {'filename' : 'nz_data/MB-2018_SA1-2018_v03.csv','from' : 'SA12018 V1.0.0', 'to' : 'MB2018 V1.0.0', 'to_name' : 'MB2018 V1.0.0', 'skip' : 0, 'to_header' : 'MB'}
# FILE_MAP_MB_LBURB = {'filename' : 'nz_data/meshblock_linz_suburbs.csv','from' : 'meshblock_id', 'to' : 'linzSuburb', 'to_name' : 'linzSuburb', 'skip' : 0, 'to_header' : 'LBURB'}
FILE_MAP_MB_LBURB_v2 = {'filename' : 'nz_data/MB_LBURB_v02.csv','from' : 'meshblock_id', 'to' : 'suburb_locality_ascii', 'to_name' : 'suburb_locality_ascii', 'skip' : 0, 'to_header' : 'LBURB'}
FILE_MAP_MB_LBURB_v3 = {'filename' : 'nz_data/MB_LBURB_v03_100m.csv','from' : 'meshblock_id', 'to' : 'suburb_locality_ascii', 'to_name' : 'suburb_locality_ascii', 'skip' : 0, 'to_header' : 'LBURB'}
FILE_MAP_MB_LBURB_v4 = {'filename' : 'nz_data/MB_LBURB_v04_150m.csv','from' : 'meshblock_id', 'to' : 'suburb_locality_ascii', 'to_name' : 'suburb_locality_ascii', 'skip' : 0, 'to_header' : 'LBURB'}
FILE_MAP_LBURB_TA = {'filename' : 'nz_data/linz_suburb_ta.csv','from' : 'suburb_locality_ascii', 'to' : 'territorial_authority', 'to_name' : 'territorial_authority', 'skip' : 0, 'to_header' : 'TA'}
FILE_MAP_UNMATCHED_SA1_LBURB = {'filename' : 'nz_data/unmatched_SA1_LBURB.csv','from' : 'SA1', 'to' : 'Linz Suburb', 'to_name' : 'Linz Suburb', 'skip' : 0, 'to_header' : 'LBURB'}

EX_SA1 = ['7012238',
    "7012239",
    "7012240",
    "7012241",
    "7012242",
    ]
EX_MB = ["910400",
"910500",
"910600",
"910700",
    "910900",
"911000",
"911101",
"911102",
"911200",
"911300",
    "911401",
"911402",
    "911600",
"911700",
"911800"
"931000",
    "911500",
    "911900",
"912000",
"912100",
"912200",
"912300",
"912500",
"912600",
"4011742"
]
LBURB = ['Hamilton Central']
EX_TA = []

def find_nz_fields(fnSwitch):
    # print(fnSwitch)
    
    if fnSwitch == 'Households_totalNZ-wide_format_updated_16-7-20.csv':
        return [
            get_median_rent(), 
            get_tenure_type(), 
            get_average_household_size()
            ]
    elif fnSwitch == 'Individual_part1_totalNZ-wide_format_updated_16-7-20.csv':
        return [
            get_median_age(),
            get_ethnicity(),
            get_total_population()
            ]
    elif fnSwitch == 'Dwellings_totalNZ-wide_format_updated_16-7-20.csv':
        return [
            get_dwelling_types()
            ]
    elif fnSwitch == 'Individual_part3b_totalNZ-wide_format_updated_16-7-20.csv':
        return [
            get_transport_to_work()
            ]
    elif fnSwitch == 'Individual_part3a_totalNZ-wide_format_updated_16-7-20.csv':
        return [
            get_industry()
            ]
    elif fnSwitch =='Individual_part2_totalNZ-wide_format_updated_16-7-20.csv':
        return [
            get_median_personal_income(), 
        ]
    else:
        return [{''}]
# Need to get:
    # Households_totalNZ-wide_format_updated_16-7-20.csv
def get_median_rent():
    return {'Census_2018_Weekly_rent_Median_households_in_rented_occupied_private_dwellings' : 'median_rent'}

def get_tenure_type():
    return {
        'Census_2018_Sector_of_landlord_1_Private_person_trust_or_business_households_in_rented_occupied_private_dwellings' : 'Private_Person_Trust_or_Business',
        'Census_2018_Sector_of_landlord_2_Local_authority_or_city_council_households_in_rented_occupied_private_dwellings' : 'Local_Authority_or_City_Council',
        'Census_2018_Sector_of_landlord_3_Housing_New_Zealand_Corporation_households_in_rented_occupied_private_dwellings' : 'Housing_New_Zealand_Corporation',
        'Census_2018_Sector_of_landlord_4_Iwi_hapū_or_Māori_land_trust_households_in_rented_occupied_private_dwellings' : 'Iwi_hapū_or_Māori_land_trust_households',
        'Census_2018_Sector_of_landlord_5_Other_community_housing_provider_households_in_rented_occupied_private_dwellings' : 'Other_community_housing_provider',
        'Census_2018_Sector_of_landlord_6_Other_state_owned_corporation_or_state_owned_enterprise_or_government_department_or_ministry_households_in_rented_occupied_private_dwellings' : 'Other_State-Owned_Corporation',
        'Census_2018_Tenure_of_household_001_Dwelling_owned_or_partly_owned_households_in_occupied_private_dwellings' : 'Owned_or_Partly_Owned',
        'Census_2018_Tenure_of_household_002_Dwelling_not_owned_and_not_held_in_a_family_trust_households_in_occupied_private_dwellings' : 'Not_Owned_and_Not_Held_in_a_Family_Trust',
        'Census_2018_Tenure_of_household_003_Dwelling_held_in_a_family_trust_households_in_occupied_private_dwellings' : 'Held_in_a_Family_Trust'
        }

def get_average_household_size():
    return {'Census_2018_total_households_in_occupied_private_dwellings' : 'total_households'}
    # return {'Census_2018_total_households_in_occupied_private_dwellings' : 'Mean_Number_of_Usual_Household_Members'}

# Individual_part2_totalNZ-wide_format_updated_16-7-20.csv
def get_median_personal_income():
    return {'Census_2018_Total_personal_income_Median_CURP_15years_and_over' : 'median_household_income'}

#     2013-mb-dataset-Total-New-Zealand-Individual-Part-1.csv
def get_median_age():
    return {'Census_2018_median_age_CURP' : 'Median_Age'}
def get_ethnicity():
    return {
        'Census_2018_Ethnicity_grouped_total_responses_level_1_1_European_CURP' : 'European',
        'Census_2018_Ethnicity_grouped_total_responses_level_1_2_Māori_CURP' : 'Maori',
        'Census_2018_Ethnicity_grouped_total_responses_level_1_3_Pacific_Peoples_CURP' : 'Pacific_Peoples',
        'Census_2018_Ethnicity_grouped_total_responses_level_1_4_Asian_CURP' : 'Asian',
        'Census_2018_Ethnicity_grouped_total_responses_level_1_5_Middle_Eastern_Latin_American_African_CURP' : 'MELAA',
        'Census_2018_Ethnicity_grouped_total_responses_level_1_6_Other_Ethnicity_CURP' : 'Other',
        'Census_2018_Ethnicity_grouped_total_responses_level_2_61_New_Zealander_CURP' : 'New_Zealander',
        'Census_2018_Ethnicity_grouped_total_responses_level_2_69_Other_Ethnicity_nec_CURP' : 'Other_Ethnicity_nec',
        }
def get_total_population():
    return {'Census_2018_usually_resident_population_count' : 'population_count'}

#     Dwellings_totalNZ-wide_format_updated_16-7-20.csv
def get_dwelling_types():
    return {
        'Census_2018_Occupied_private_dwelling_type_11_Separate_house' : 'Separate_House',
        'Census_2018_Occupied_private_dwelling_type_12_Joined_dwelling' : 'Dwellings_Joined_together',
        'Census_2018_Occupied_private_dwelling_type_13_Other_private_dwelling' : 'Occupied_Private_Dwellings',
        'Census_2018_Occupied_private_dwelling_type_10_Private_dwelling_not_further_defined' : 'Occupied_Private_Dwelling_Not_Further_Defined'
        }

# Individual_part3b_totalNZ-wide_format_updated_16-7-20.csv
def get_transport_to_work():
    return {
        'Census_2018_Travel_to_work_by_usual_residence_address_Counts_001_Work_at_home_CURP_employed_15years_and_over' : 'Worked_at_Home',
        'Census_2018_Travel_to_work_by_usual_residence_address_Counts_002_Did_not_go_to_work_today_CURP_employed_15years_and_over' : 'Did_Not_Go_to_Work_Today',
        'Census_2018_Travel_to_work_by_usual_residence_address_Counts_003_Drive_a_private_car_truck_or_van_CURP_employed_15years_and_over' : 'Drove_a_Private_Car_Truck_or_Van',
        'Census_2018_Travel_to_work_by_usual_residence_address_Counts_004_Drive_a_company_car_truck_or_van_CURP_employed_15years_and_over' : 'Drove_a_Company_Car_Truck_or_Van',
        'Census_2018_Travel_to_work_by_usual_residence_address_Counts_005_Passenger_in_a_car_truck_van_or_company_bus_CURP_employed_15years_and_over' : 'Passenger_in_a_Car_Truck_Van_or_Company_Bus',
        'Census_2018_Travel_to_work_by_usual_residence_address_Counts_006_Public_bus_CURP_employed_15years_and_over' : 'Public_Bus',
        'Census_2018_Travel_to_work_by_usual_residence_address_Counts_007_Train_CURP_employed_15years_and_over' : 'Train',
        'Census_2018_Travel_to_work_by_usual_residence_address_Counts_009_Bicycle_CURP_employed_15years_and_over' : 'Bicycle',
        'Census_2018_Travel_to_work_by_usual_residence_address_Counts_010_Walk_or_jog_CURP_employed_15years_and_over' : 'Walked_or_Jogged',
        'Census_2018_Travel_to_work_by_usual_residence_address_Counts_012_Ferry_CURP_employed_15years_and_over' : 'Ferry',
        'Census_2018_Travel_to_work_by_usual_residence_address_Counts_016_Other_CURP_employed_15years_and_over' : 'Other_travel_to_Work',
}

# Individual_part3a_totalNZ-wide_format_updated_16-7-20.csv
def get_industry():
      return {
        'Census_2018_Industry_by_usual_residence_address_A_Agriculture_Forestry_and_Fishing_CURP_employed_15years_and_over' : 'Agriculture_Forestry_and_Fishing',
        'Census_2018_Industry_by_usual_residence_address_B_Mining_CURP_employed_15years_and_over' : 'Mining',
        'Census_2018_Industry_by_usual_residence_address_C_Manufacturing_CURP_employed_15years_and_over' : 'Manufacturing',
        'Census_2018_Industry_by_usual_residence_address_D_Electricity_Gas_Water_and_Waste_Services_CURP_employed_15years_and_over' : 'Electricity_Gas_Water_and_Waste_Services',
        'Census_2018_Industry_by_usual_residence_address_E_Construction_CURP_employed_15years_and_over' : 'Construction',
        'Census_2018_Industry_by_usual_residence_address_F_Wholesale_Trade_CURP_employed_15years_and_over' : 'Wholesale_Trade',
        'Census_2018_Industry_by_usual_residence_address_G_Retail_Trade_CURP_employed_15years_and_over' : 'Retail_Trade',
        'Census_2018_Industry_by_usual_residence_address_H_Accommodation_and_Food_Services_CURP_employed_15years_and_over' : 'Accommodation_and_Food_Services',
        'Census_2018_Industry_by_usual_residence_address_I_Transport_Postal_and_Warehousing_CURP_employed_15years_and_over' : 'Transport_Postal_and_Warehousing',
        'Census_2018_Industry_by_usual_residence_address_J_Information_Media_and_Telecommunications_CURP_employed_15years_and_over' : 'Information_Media_and_Telecommunications',
        'Census_2018_Industry_by_usual_residence_address_K_Financial_and_Insurance_Services_CURP_employed_15years_and_over' : 'Financial_and_Insurance_Services',
        'Census_2018_Industry_by_usual_residence_address_L_Rental_Hiring_and_Real_Estate_Services_CURP_employed_15years_and_over' : 'Rental_Hiring_and_Real_Estate_Services',
        'Census_2018_Industry_by_usual_residence_address_M_Professional_Scientific_and_Technical_Services_CURP_employed_15years_and_over' : 'Professional_Scientific_and_Technical_Services',
        'Census_2018_Industry_by_usual_residence_address_N_Administrative_and_Support_Services_CURP_employed_15years_and_over' : 'Administrative_and_Support_Services',
        'Census_2018_Industry_by_usual_residence_address_O_Public_Administration_and_Safety_CURP_employed_15years_and_over' : 'Public_Administration_and_Safety',
        'Census_2018_Industry_by_usual_residence_address_P_Education_and_Training_CURP_employed_15years_and_over' : 'Education_and_Training',
        'Census_2018_Industry_by_usual_residence_address_Q_Health_Care_and_Social_Assistance_CURP_employed_15years_and_over' : 'Health_Care_and_Social_Assistance',
        'Census_2018_Industry_by_usual_residence_address_R_Arts_and_Recreation_Services_CURP_employed_15years_and_over' : 'Arts_and_Recreation_Services',
        'Census_2018_Industry_by_usual_residence_address_S_Other_Services_CURP_employed_15years_and_over' : 'Other_Services',
      }