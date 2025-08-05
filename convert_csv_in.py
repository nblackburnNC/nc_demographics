import functions as fnct
import csv

# IN_FILE = 'nz_data/to_process/census_2023_final_with_dwellings - data.csv'
IN_FILE = 'nz_data/to_process/census_2023_final_with_dwellings_02 - data.csv'

def convert_given_NZ_data():
    head_done = False
    return_values = {}
    all_data = {}
    headers = []
    with open(IN_FILE, 'r', encoding = 'UTF-8') as f:
        data = csv.DictReader(f)
        listDat = list(data)
        f.close()
    for i in listDat:
        # print(i)
        if head_done == False:
            head_done = True
            for head in i.keys():
                if head != 'SA1_Code':
                    headers.append(head)
            print()
            print(headers)
            # input('Press Enter to continue... headers')
        # print(i['Area_code'])
        # print(i['Area_name'])
        # print(i['Total_dwellings'])
        # print(i['Total_persons'])

        # input('Press Enter to continue...1')
        all_data[i['SA1_Code']] = {}
        for key in i:
            if key != 'SA1_Code':
                all_data[i['SA1_Code']][key] = i[key]
        # print(all_data[i['SA1_Code']])
        # input('Press Enter to continue...2')
    # print(all_data) 
    # 20250804_census_2023_final_with_dwellings
    # fnct.write_to_csv('NZ', all_data, headers, '__census_2023_final_with_dwellings')
    return_values['all_nadya_data'] = all_data
    return return_values

def main():
    convert_given_NZ_data()
    pass

if __name__ == "__main__":
    main()
    pass