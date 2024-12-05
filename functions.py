import csv
from distutils.log import debug
from pickle import FALSE, TRUE
from types import new_class
import nz_deets_SA12018 as nz
import demographpics as dem
import aus_deets as aus
from os import listdir
from os.path import isfile, join
from datetime import date
import pandas as pd

def get_file_path(country):
    # print(country,' is country')
    if country == 'NZ':
        return nz.NZ_FILE_PATH
    elif country == 'AUS':
        return aus.AUS_FILE_PATH
    else:
        return ''

def write_to_csv(country, out_file, csv_cols, increment = ''):
    with open(country+'_demographics_'+str(date.today())+increment+'.csv', 'w') as out:
        writer = csv.DictWriter(out, fieldnames = csv_cols)
        writer.writeheader()
        for data in out_file:
            writer.writerow(data)
        # for key in out_file.keys():
        #     out.write("%s,%s\n"%(key,out_file[key]))
    pass

def return_ratio(numer, denom):
    try:
        return round(numer / denom,0)
    except:
        return 0

def isNaN(num):
    return num != num

def get_demographics(country, find_fields_only):
    population_of_area = [0.0,0]
    num_houses = [0.0,0]
    pplPerHousehold = []
    num_houses_dict = {}
    population_of_area_dict = {}
    

    filenames = get_file_names(country)
    # for i in filenames:
    #     print(i)
    all_demographics = {}
    for file in filenames:
        path_in_file = get_file_path(country) + file
        # print(in_file.split(NZ_FILE_PATH,1)[1])
        if country == 'NZ':
            demograph_list = nz.find_nz_fields(file)
            encoding = nz.ENCODING
            code = nz.CODE
        elif country == 'AUS':
            demograph_list = {}
            encoding = nz.ENCODING
            code = nz.CODE

        else:
            demograph_list = {}

        demoDict = {}
        listDat = {}
        with open(path_in_file, 'r', encoding = encoding) as f:
            data = csv.DictReader(f)
            listDat = list(data)
            f.close()
            # read_data = TRUE
        read_data = not bool(find_fields_only)
        find_fieldnames = bool(find_fields_only)
        
        # print(find_fields_only)
        # print(read_data)
        # print(find_fieldnames)
        

            
        if find_fieldnames:
            kkey = data.fieldnames
            print()
            print(file)
            for i in kkey:
                if '2018' in i:
                    print(i)
            print() 
        if read_data:
            for segment in demograph_list:
                # print("Segment is -->",segment)
                for tableName in segment:
                    # print('**************tblname',tableName)
                    # print('**************tblname',segment[tableName])
                    if tableName == '':
                        pass
                    for tblSegment in listDat:
                            # print()
                            # print('-------',tblSegment)

                            if tblSegment[code] not in demoDict.keys():
                                demoDict[tblSegment[code]] = {}
                            # print(tblSegment[code])
                            for tblRow in tblSegment:
                                # household numer = age househol = ttl households
                                if file == 'Households_totalNZ-wide_format_updated_16-7-20.csv':
                                    # num_houses[0] = float(tblSegment['Census_2018_total_households_in_occupied_private_dwellings'])
                                    num_houses_dict[tblSegment[code]] = float(tblSegment['Census_2018_total_households_in_occupied_private_dwellings'])
                                    num_houses[1] = 1
                                    # demoDict[tblSegment[code]].pop('total_households')
                                    # if population_of_area[1] == 1:
                                    #     demoDict[tblSegment[code]]['Agerage_people_per_house'] = return_ratio(population_of_area[0],num_houses[0])      

                                # # indiv prt 1 for denom = ttl pop
                                if file == 'Individual_part1_totalNZ-wide_format_updated_16-7-20.csv':
                                    # population_of_area[0] = float(tblSegment['Census_2018_usually_resident_population_count'])
                                    population_of_area_dict[tblSegment[code]] = float(tblSegment['Census_2018_usually_resident_population_count'])
                                    population_of_area[1] = 1
                                    # if num_houses[1] == 1:
                                    #     demoDict[tblSegment[code]]['Agerage_people_per_house'] = return_ratio(population_of_area[0],num_houses[0])      

                                if tblRow == tableName:
                                    if isNaN(tblSegment[tblRow]) or tblSegment[tblRow] == 'C' or tblSegment[tblRow] == '..':
                                        demoDict[tblSegment[code]][segment[tableName]] = '0'
                                    elif segment[tableName] != 'total_households':
                                        demoDict[tblSegment[code]][segment[tableName]] = tblSegment[tblRow]      
                                    if num_houses[1] == 1 and population_of_area[1] == 1:
                                        demoDict[tblSegment[code]]['Agerage_people_per_house'] = return_ratio(population_of_area_dict[tblSegment[code]],num_houses_dict[tblSegment[code]]) 
                                    # if file == 'Households_totalNZ-wide_format_updated_16-7-20.csv':
                                    #     demoDict[tblSegment[code]].pop('total_households')
                                        # pplPerHousehold = return_ratio(population_of_area[0],num_houses[0])
                                # population_of_area = [0.0,0]
                                # num_houses = [0.0,0]
        
        # if num_houses[1] == 1 and population_of_area[1] == 1:
        #     all_demographics
        all_demographics[file] = demoDict                       
        
    
    return all_demographics

def create_better_dict(readfile_vals):
    debug = 0
    dataframe = pd.read_csv(readfile_vals['filename'], skiprows = readfile_vals['skip'], usecols=[readfile_vals['from'],readfile_vals['to']])
    if debug == 1:
        if readfile_vals['to_header'] == 'MB':
            print('dataframe')
            print(dataframe)
    df_dict = dataframe.set_index(readfile_vals['from']).to_dict()[readfile_vals['to']]
    if debug == 1:
        if readfile_vals['to_header'] == 'MB':
            print('df_dict')
            print(df_dict)
        # for i in df_dict:
        #     if str(i) == '7000000':
        #         print(str(i),' df_dict[',i,'] = ',str(df_dict[i]))
    return df_dict


def match_area_unit2(code_to_match, dict_to_match_1, dict_to_match_2, dict_to_match_3 = None, dict_to_match_4 = None):
    entry = {}
    debug = 0
    try:
        try:
            if dict_to_match_3 is not None:
                if debug == 1:
                    print('code to match = ',code_to_match,' is ',type(code_to_match))
                    print(code_to_match,' -> ',dict_to_match_1[code_to_match])
                    print(code_to_match,' -> ',dict_to_match_1[code_to_match],' -->> ', dict_to_match_2[dict_to_match_1[code_to_match]])
                    print(code_to_match,' -> ',dict_to_match_1[code_to_match],' -->> ', dict_to_match_2[dict_to_match_1[code_to_match]],' --->>> ', dict_to_match_3[dict_to_match_2[dict_to_match_1[code_to_match]]])
                return [dict_to_match_2[dict_to_match_1[code_to_match]], dict_to_match_3[dict_to_match_2[dict_to_match_1[code_to_match]]] ]
                pass
            else:
                if debug == 1:
                    print(code_to_match)
                    print(code_to_match,' -> ',dict_to_match_1[code_to_match])
                    print(code_to_match,' -> ',dict_to_match_1[code_to_match],' -->> ', dict_to_match_2[dict_to_match_1[code_to_match]])
                return [dict_to_match_1[code_to_match], dict_to_match_2[dict_to_match_1[code_to_match]] ]
                pass
        except:
            code_to_match = int(code_to_match)
            if dict_to_match_3 is not None:
                if debug == 1:
                    print('code to match = ',code_to_match,' is ',type(code_to_match))
                    print(code_to_match,' -> ',dict_to_match_1[code_to_match])
                    print(code_to_match,' -> ',dict_to_match_1[code_to_match],' -->> ', dict_to_match_2[dict_to_match_1[code_to_match]])
                    print(code_to_match,' -> ',dict_to_match_1[code_to_match],' -->> ', dict_to_match_2[dict_to_match_1[code_to_match]],' --->>> ', dict_to_match_3[dict_to_match_2[dict_to_match_1[code_to_match]]])
                return [dict_to_match_2[dict_to_match_1[code_to_match]], dict_to_match_3[dict_to_match_2[dict_to_match_1[code_to_match]]] ]
                pass
            else:
                if debug == 1:
                    print(code_to_match)
                    print(code_to_match,' -> ',dict_to_match_1[code_to_match])
                    print(code_to_match,' -> ',dict_to_match_1[code_to_match],' -->> ', dict_to_match_2[dict_to_match_1[code_to_match]])
                return [dict_to_match_1[code_to_match], dict_to_match_2[dict_to_match_1[code_to_match]] ]
                pass
        pass
    except:
        try: 
            if debug == 2:
                print(str(code_to_match),' ---matched--->>>',str(dict_to_match_4[code_to_match]))
            return [dict_to_match_4[code_to_match], dict_to_match_3[dict_to_match_4[code_to_match]]]
            pass
        except:
            return ['no_match_','Unknown_Area']
        pass
    pass

def match_area_unit(code_to_match, file_to_match_1, file_to_match_2, file_to_match_3 = None, file_to_match_4 = None):
    entry = {}
    mapping_1 = {}
    mapping_2 = {}
    mapping_3 = {}

    with open(file_to_match_1['filename'],'r') as map1:
        for i in range(file_to_match_1['skip']):
            next(map1)
        map1_reader = csv.DictReader(map1)
        mapping_1 = list(map1_reader)
        map1.close
    with open(file_to_match_2['filename'],'r') as map2:
        for i in range(file_to_match_2['skip']):
            next(map2)
        map2_reader = csv.DictReader(map2)
        mapping_2 = list(map2_reader)
        map2.close
    if file_to_match_3 is not None:
        with open(file_to_match_3['filename'],'r') as map3:
            for i in range(file_to_match_3['skip']):
                next(map3)
            map3_reader = csv.DictReader(map3)
            mapping_3 = list(map3_reader)
            map3.close
    try:
        for map_1 in mapping_1:
            if code_to_match == map_1[file_to_match_1['from']]:
                print('1 ---> ',code_to_match,' matches ',map_1[file_to_match_1['from']])
                entry[file_to_match_1['to_header']+'_code'] = map_1[file_to_match_1['to']]
                if file_to_match_1['to_name'] == None:
                    entry[file_to_match_1['to_header']] = map_1[file_to_match_1['to_name']][0]
                    print('   ->',entry[file_to_match_1['to_header']],' -> ', map_1[file_to_match_1['to_name']][0],'    or --> ',map_1[file_to_match_1['to']])
                else:
                    entry[file_to_match_1['to_header']] = map_1[file_to_match_1['to_name']]
                    print('   ->',entry[file_to_match_1['to_header']],' -> ', map_1[file_to_match_1['to_name']],'    or --> ',map_1[file_to_match_1['to']])
        for map_2 in mapping_2:
            if entry[file_to_match_1['to_header']+'_code'] == map_2[file_to_match_2['from']]:
                print('2 ---> ',entry[file_to_match_1['to_header']+'_code'],' matches ',map_2[file_to_match_2['from']])
                entry[file_to_match_2['to_header']+'_code'] = map_2[file_to_match_2['to']]
                if map_2[file_to_match_2['to_name']] == None:
                    entry[file_to_match_2['to_header']] = map_2[file_to_match_2['to_name']][0]
                    print('   ->',entry[file_to_match_2['to_header']] ,' -> ', map_2[file_to_match_2['to_name']][0])
                else:
                    entry[file_to_match_2['to_header']] = map_2[file_to_match_2['to_name']]
                    print('   ->',entry[file_to_match_2['to_header']] ,' -> ', map_2[file_to_match_2['to_name']])
        print([entry[file_to_match_1['to_header']],entry[file_to_match_2['to_header']]])
        if file_to_match_3 is not None:
            print()
            print()
            print()
            print('In Zone 3====================================')
            for map_3 in mapping_3:
                print(entry[file_to_match_2['to_header']+'_code'], '  ==  ', map_3[file_to_match_3["from"]])
                if entry[file_to_match_2['to_header']+'_code'] == map_3[file_to_match_3["from"]]:
                    print('3 ---> ',entry[file_to_match_2['to_header']+'_code'],' matches ',map_3[file_to_match_3['from']])
                    entry[file_to_match_3['to_header']+'_code'] = map_3[file_to_match_3['to']]
                    if map_3[file_to_match_3['to_name']] == None:
                        entry[file_to_match_3['to_header']] = map_3[file_to_match_3['to_name']][0]
                        print('   ->',entry[file_to_match_3['to_header']],' -> ', map_3[file_to_match_3['to_name']][0])
                    else:
                        entry[file_to_match_3['to_header']] = map_3[file_to_match_3['to_name']]
                        print('   ->',entry[file_to_match_3['to_header']],' -> ', map_3[file_to_match_3['to_name']])
                    print([entry[file_to_match_1['to_header']], entry[file_to_match_2['to_header']], entry[file_to_match_3['to_header']]])
                    

    except:
        return ['SA1',code_to_match]
    if file_to_match_3 is not None:
        return [entry[file_to_match_2['to_header']], entry[file_to_match_3['to_header']]]
    return [entry[file_to_match_1['to_header']],entry[file_to_match_2['to_header']]]
    pass

def remove_key_from_dicts(og_list,target_key):
    for i in og_list:
        del i[target_key]
    return og_list
    pass

def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def prep_for_rows(all_demographics):
    all_demo = []
    csv_cols = [nz.AREA_UNIT]
    init_list = FALSE
    ttl_sa1 = 0
    ttl_mtchd = 0
    debug = 0
    # dict_to_match_1 = create_better_dict(nz.FILE_MAP_SA1_MB)
    dict_to_match_1 = create_better_dict(nz.FILE_MAP_SA1_MB_v3)
    # for j in dict_to_match_1:
    #     print(j)
    dict_to_match_2 = create_better_dict(nz.FILE_MAP_MB_LBURB_v4)
    dict_to_match_3 = create_better_dict(nz.FILE_MAP_LBURB_TA)
    dict_to_unmatched = create_better_dict(nz.FILE_MAP_UNMATCHED_SA1_LBURB)
    for i in all_demographics:
        # print(i)
        for unit_in in all_demographics[i]:
            if unit_in == 'total':
                break
            # print(all_demographics[i][unit_in])
            if init_list == FALSE:
                # print(unit_in,' ======----->>>>>>',match_area_unit(unit_in))
                # if unit_in =='7000000':
                #     print(unit_in,' ======----->>>>>>',dict_to_match_1[int(unit_in)])
                newkey = match_area_unit2(unit_in,dict_to_match_1, dict_to_match_2, dict_to_match_3,dict_to_unmatched)
                ttl_sa1 += 1

                if newkey[0] != 'no_match_':
                    ttl_mtchd += 1

                if newkey[0] != 'no_match':
                    all_demographics[i][unit_in][nz.KEY_PAIR] = newkey
                    # all_demographics[i][unit_in][nz.KEY_PAIR] = match_area_unit(unit_in,nz.FILE_MAP_SA1_MB,nz.FILE_MAP_MB_LBURB,nz.FILE_MAP_LBURB_TA)
                    # all_demographics[i][unit_in][nz.KEY_PAIR] = match_area_unit(unit_in,nz.FILE_MAP_SA1_SA2,nz.FILE_MAP_SA2_TA)
                    all_demographics[i][unit_in][nz.AREA_UNIT] = unit_in   
                    all_demo.append(all_demographics[i][unit_in])

            else:
                for entry in all_demo:
                    if entry[nz.AREA_UNIT] == unit_in:
                        if debug == 1:
                            print(entry[nz.AREA_UNIT],' --> ', str(unit_in))
                        entry.update(all_demographics[i][unit_in])
            for key in all_demographics[i][unit_in]:
                # print(str(unit_in),' --> ', str(key),' ---> ',str(all_demographics[i][unit_in][key]))
                if key not in csv_cols:
                    csv_cols.append(key)
        
        if init_list == FALSE:
            init_list = TRUE
    all_demo = remove_key_from_dicts(all_demo,nz.AREA_UNIT)
    csv_cols.remove(nz.AREA_UNIT)
    # print()
    # print(csv_cols)
    # print()
    
    while csv_cols.index(nz.KEY_PAIR) != 0:
        csv_cols = swapPositions(csv_cols,csv_cols.index(nz.KEY_PAIR)-1,csv_cols.index(nz.KEY_PAIR))
        # print()
        # print(csv_cols.index(nz.KEY_PAIR))
    return [all_demo, csv_cols,[ttl_mtchd,ttl_sa1,round((ttl_mtchd/ttl_sa1)*100,2)]]
    pass


def get_file_names(country):
    return [f for f in listdir(get_file_path(country)) if isfile(join(get_file_path(country), f))]

def squash_to_weighted_avg(dict_of_dicts, field_for_weight, field_for_key):
    debug = 0
    exclude_vals_for = 'total_households'
    squash = {}
    # print(squash[field_for_key] )
    # print(dict_of_dicts)
    # print(dict_of_dicts[0])
    # print(dict_of_dicts[0][field_for_key])
    squash[field_for_key] = dict_of_dicts[0][field_for_key]
    # dict_keys = dict_of_dicts[0].keys()
    dict_keys = dict_of_dicts[0].keys()
    for key in dict_keys:
        tmpNumer = 0
        tmpDenom = 0
        tmpTtlHouses = 0
        # print(key)

        if key != field_for_key and field_for_weight and key != exclude_vals_for:
            # print(key)
            # print(field_for_key)
            for i in dict_of_dicts:
                if i == exclude_vals_for:
                    i.pop(exclude_vals_for)
                # print(type(i[key]))
                # print(type(i[field_for_weight]))
                # print(type(i[field_for_weight]))
                tmpNumer += float(i[key])*float(i[field_for_weight])
                tmpDenom += float(i[field_for_weight])
                try:
                    tmpTtlHouses = float(i[exclude_vals_for])
                except:
                    pass
                # print(tmpDenom)
            try:
                squash[key] += round(tmpNumer/tmpDenom,0)
            except:
                if tmpDenom == 0:
                    squash[key] = 0
                else:
                    squash[key] = round(tmpNumer/tmpDenom,0)
            # Make median income weekly
            if key == 'median_household_income':
                squash[key] = squash[key]/52
        if key == field_for_weight:
            squash[key] = tmpDenom
        # if key == exclude_vals_for:
        #     squash[key] = tmpTtlHouses
    if debug == 1:
        for entry in squash:
            print(entry)
        # entry.pop(exclude_vals_for)
    return squash

def squash(country, csv_heads, increment=''):
    areaList = {}
    forSquash = {}
    test = []
    # with open('NZ_demographics_v01_'+str(date.today())+'.csv', 'r') as infile:
    with open(country+'_demographics_'+str(date.today())+increment+'.csv', 'r') as infile:
        reader = csv.DictReader(infile)
        areaList = list(reader)
        infile.close
    for entry in areaList:
        if entry[nz.KEY_PAIR] not in forSquash.keys():
            forSquash[entry[nz.KEY_PAIR]] = [entry]
        else:
            forSquash[entry[nz.KEY_PAIR]].append(entry)

    for key_pair in forSquash:
        # test = squash_to_weighted_avg(forSquash[key_pair],'population_count',key_pair)
        test.append(squash_to_weighted_avg(forSquash[key_pair],'population_count',nz.KEY_PAIR))
    # for j in test:
    #     print('test')
    #     print(j)
    write_to_csv(country, test, csv_heads, increment+'_weighted_average')
    pass