NZ_FILE_PATH = 'nz_data/2013_mb_dataset_Total_New_Zealand_CSV/'
CODE = 'Code'
ENCODING = 'cp1252'
AREA_UNIT = 'Meshblock'

def find_nz_fields(fnSwitch):
    # print(fnSwitch)
    
    if fnSwitch == '2013-mb-dataset-Total-New-Zealand-Household.csv':
        return [
            get_median_rent(), 
            get_median_household_income(), 
            get_tenure_type(), 
            get_average_household_size()
            ]
    elif fnSwitch == '2013-mb-dataset-Total-New-Zealand-Individual-Part-1.csv':
        return [
            get_median_age(),
            get_ethnicity(),
            get_total_population()
            ]
    elif fnSwitch == '2013-mb-dataset-Total-New-Zealand-Dwelling.csv':
        return [
            get_dwelling_types()
            ]
    elif fnSwitch == '2013-mb-dataset-Total-New-Zealand-Individual-Part-3b.csv':
        return [
            get_transport_to_work()
            ]
    elif fnSwitch == '2013-mb-dataset-Total-New-Zealand-Individual-Part-3a.csv':
        return [
            get_industry()
            ]
    else:
        return [{''}]
# Need to get:
    # 2013-mb-dataset-Total-New-Zealand-Household.csv
def get_median_rent():
    return {'2013_Census_weekly_rent_paid_for_households_in_rented_occupied_private_dwellings(14)_Median_Weekly_Rent_Paid_($)(16)(18)' : 'median_rent'}
def get_median_household_income():
    return {'2013_Census_total_household_income_(grouped)(2)(3)(4)_for_households_in_occupied_private_dwellings_Median_household_income_($)(18)(23)' : 'median_household_income'}
def get_tenure_type():
    return {
        '2013_Census_sector_of_landlord_for_households_in_rented_occupied_private_dwellings(14)_Private_Person_Trust_or_Business' : 'Private_Person_Trust_or_Business',
        '2013_Census_sector_of_landlord_for_households_in_rented_occupied_private_dwellings(14)_Local_Authority_or_City_Council' : 'Local_Authority_or_City_Council',
        '2013_Census_sector_of_landlord_for_households_in_rented_occupied_private_dwellings(14)_Housing_New_Zealand_Corporation' : 'Housing_New_Zealand_Corporation',
        '2013_Census_sector_of_landlord_for_households_in_rented_occupied_private_dwellings(14)_Other_State-Owned_Corporation_or_State-Owned_Enterprise_or_Government_Department_or_Ministry' : 'Other_State-Owned_Corporation',
        '2013_Census_tenure_of_household(10)_for_households_in_occupied_private_dwellings_Dwelling_Owned_or_Partly_Owned' : 'Owned_or_Partly_Owned',
        '2013_Census_tenure_of_household(10)_for_households_in_occupied_private_dwellings_Dwelling_Not_Owned_and_Not_Held_in_a_Family_Trust(12)' : 'Not_Owned_and_Not_Held_in_a_Family_Trust',
        '2013_Census_tenure_of_household(10)_for_households_in_occupied_private_dwellings_Dwelling_Held_in_a_Family_Trust(13)' : 'Held_in_a_Family_Trust'
        }
def get_average_household_size():
    return {'2013_Census_number_of_usual_residents_in_household(1)_for_households_in_occupied_private_dwellings_Mean_Number_of_Usual_Household_Members' : 'Mean_Number_of_Usual_Household_Members'}


#     2013-mb-dataset-Total-New-Zealand-Individual-Part-1.csv
def get_median_age():
    return {'2013_Census_age_in_five-year_groups_for_the_census_usually_resident_population_count(1)_Median_Age(3)' : 'Median_Age'}
def get_ethnicity():
    return {
        '2013_Census_ethnic_group_(grouped_total_responses)(7)(8)_for_the_census_usually_resident_population_count(1)_European' : 'European',
        '2013_Census_ethnic_group_(grouped_total_responses)(7)(8)_for_the_census_usually_resident_population_count(1)_Maori' : 'Maori',
        '2013_Census_ethnic_group_(grouped_total_responses)(7)(8)_for_the_census_usually_resident_population_count(1)_Pacific_Peoples' : 'Pacific_Peoples',
        '2013_Census_ethnic_group_(grouped_total_responses)(7)(8)_for_the_census_usually_resident_population_count(1)_Asian' : 'Asian',
        '2013_Census_ethnic_group_(grouped_total_responses)(7)(8)_for_the_census_usually_resident_population_count(1)_MELAA(9)' : 'MELAA',
        '2013_Census_ethnic_group_(grouped_total_responses)(7)(8)_for_the_census_usually_resident_population_count(1)_Other(10)' : 'Other',
        }
def get_total_population():
    return {'2013_Census_sex_for_the_census_usually_resident_population_count(1)_Total_people' : 'Total_people'}

#     2013-mb-dataset-Total-New-Zealand-Dwelling.csv
def get_dwelling_types():
    return {
        '2013_Census_occupied_private_dwelling_type_Separate_House' : 'Separate_House',
        '2013_Census_occupied_private_dwelling_type_Two_or_More_Flats/Units/Townhouses/_Apartments/Houses_Joined_Together' : 'Tow_or_More_Dwellings_Joined_together',
        '2013_Census_occupied_private_dwelling_type_Other_Occupied_Private_Dwellings(1)' : 'Occupied_Private_Dwellings',
        '2013_Census_occupied_private_dwelling_type_Occupied_Private_Dwelling_Not_Further_Defined' : 'Occupied_Private_Dwelling_Not_Further_Defined'
        }

# 2013-mb-dataset-Total-New-Zealand-Individual-Part-3b.csv
def get_transport_to_work():
    return {
        '2013_Census_main_means_of_travel_to_work_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Worked_at_Home' : 'Worked_at_Home',
        '2013_Census_main_means_of_travel_to_work_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Did_Not_Go_to_Work_Today' : 'Did_Not_Go_to_Work_Today',
        '2013_Census_main_means_of_travel_to_work_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Drove_a_Private_Car_Truck_or_Van' : 'Drove_a_Private_Car_Truck_or_Van',
        '2013_Census_main_means_of_travel_to_work_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Drove_a_Company_Car_Truck_or_Van' : 'Drove_a_Company_Car_Truck_or_Van',
        '2013_Census_main_means_of_travel_to_work_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Passenger_in_a_Car_Truck_Van_or_Company_Bus' : 'Passenger_in_a_Car_Truck_Van_or_Company_Bus',
        '2013_Census_main_means_of_travel_to_work_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Public_Bus' : 'Public_Bus',
        '2013_Census_main_means_of_travel_to_work_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Train' : 'Train',
        '2013_Census_main_means_of_travel_to_work_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Motor_Cycle_or_Power_Cycle' : 'Motor_Cycle_or_Power_Cycle',
        '2013_Census_main_means_of_travel_to_work_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Bicycle' : 'Bicycle',
        '2013_Census_main_means_of_travel_to_work_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Walked_or_Jogged' : 'Walked_or_Jogged',
        '2013_Census_main_means_of_travel_to_work_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Other' : 'Other'
}

# 2013-mb-dataset-Total-New-Zealand-Individual-Part-3a.csv
def get_industry():
      return {
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Agriculture_Forestry_and_Fishing' : 'Agriculture_Forestry_and_Fishing',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Mining' : 'Mining',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Manufacturing' : 'Manufacturing',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Electricity_Gas_Water_and_Waste_Services' : 'Electricity_Gas_Water_and_Waste_Services',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Construction' : 'Construction',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Wholesale_Trade' : 'Wholesale_Trade',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Retail_Trade' : 'Retail_Trade',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Accommodation_and_Food_Services' : 'Accommodation_and_Food_Services',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Transport_Postal_and_Warehousing' : 'Transport_Postal_and_Warehousing',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Information_Media_and_Telecommunications' : 'Information_Media_and_Telecommunications',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Financial_and_Insurance_Services' : 'Financial_and_Insurance_Services',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Rental_Hiring_and_Real_Estate_Services' : 'Rental_Hiring_and_Real_Estate_Services',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Professional_Scientific_and_Technical_Services' : 'Professional_Scientific_and_Technical_Services',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Administrative_and_Support_Services' : 'Administrative_and_Support_Services',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Public_Administration_and_Safety' : 'Public_Administration_and_Safety',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Education_and_Training' : 'Education_and_Training',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Health_Care_and_Social_Assistance' : 'Health_Care_and_Social_Assistance',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Arts_and_Recreation_Services' : 'Arts_and_Recreation_Services',
        '2013_Census_industry_(ANZSIC06_division)(15)(16)_for_the_employed_census_usually_resident_population_count_aged_15_years_and_over(1)_Other_Services' : 'Other_Services'
      }