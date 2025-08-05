import csv
# from email.policy import default
import json
from os import listdir
from os.path import isfile, join
# from pickle import FALSE, TRUE
import sys
import functions as fnct
import nz_deets_SA12018 as nz
import aus_deets as aus
import get_mb_from_lburb as getSubLst
import convert_csv_in as convert

# NOTES:
# Aus by {suburb, postcode}
# NZ by {suburb, postcode} possibly weighted average population for suburb

DEBUG = 0

def main(argv):
    country = argv[0].upper()
    
    if country == 'NZ':
        find_fields_only = False
        # filenames = fnct.get_file_names(country)
        # all_demographics = fnct.get_demographics(country, find_fields_only)
        # for i in all_demographics:
        #     # for unit_in in all_demographics[i]:
        #     #     print(all_demographics[i][unit_in])#[nz.KEY_PAIR]
        #     #     print(i, '->', unit_in)
        #     #     input('Press Enter to continue... unit_in')
        #     print(i)
        #  from nads data
        all_demographics = convert.convert_given_NZ_data()
        # print()
        if DEBUG ==1:
            full_burb_list = [
                # ['Hamilton Central'],
                # ['Kamo'],
                # ['Waipoua Forest'],
                # ['Whau Valley'],
                # ['Whangarei'],
                # ['Kumeu'],
                # ['Waiheke Island'],
                # ['Ponsonby'],
                # ['Papanui'],
                # ['Wanaka'],
                ['Greenhithe'],
                ]
            for burb_list in full_burb_list:
                target_area = getSubLst.build_sublist(burb_list)
                # print('target_area')
                # print(target_area)
                # print()
                # print(type(target_area[0]))
                target_dict = {}
                target_lst = []
                csv_cols = ['',]
                new = 1
                for j in all_demographics:
                    # print('file is -> ',j)
                    # print(type(j))
                    for l in all_demographics[j]:
                        # print(type(l))
                    #     print(all_demographics[j][l])
                        if l in target_area:
                            # print(l)
                            # print(all_demographics[j][l])

                            if new ==1:
                                target_dict[l] = {'':''}
                                target_dict[l].update(all_demographics[j][l])
                            else:
                                # target_dict[l].update({'':''})
                                target_dict[l].update(all_demographics[j][l])
                            for key in all_demographics[j][l]:
                                if key not in csv_cols:
                                    csv_cols.append(key)
                                # csv_cols.append('')
                    if new == 1:
                        new = 0
                        
                for entry in target_dict:
                    target_lst.append(target_dict[entry])
                # for k in target_lst:
                #     print(k)
                    
                fnct.write_to_csv(country,target_lst, csv_cols,'_'+str(burb_list)+'')
        else:
            if find_fields_only == False:
            # if find_fields_only == False:
                # ---------------------------------------------
                # for row in all_demographics:
                #     print('Row: ', row)
                #     # print(all_demographics[row])
                #     # input('Press Enter to continue... (all_demographics[row])')
                #     for k in all_demographics[row]:
                #         print(k, '->', all_demographics[row][k])
                #         input('Press Enter to continue... row row your boat')
                #     print('Row: ', row)
                #     print(all_demographics[row])
                #     input('Press Enter to continue... (all_demographics[row])')
                # ---------------------------------------------
                
                # # og code 
                all_dem_by_mb = fnct.prep_for_rows(all_demographics)
                

                # for h in all_dem_by_mb[0]:
                # for h in all_dem_by_mb:
                #     for k in all_dem_by_mb[h]:
                #         print(k, '->', all_dem_by_mb[h][k])
                #         input('Press Enter to continue...')
                #     # print(h)
                #     input('Press Enter to continue...')
                # print(all_dem_by_mb[1])
                # if DEBUG == 1:
                #     for h in all_dem_by_mb:
                #         if 'Hamilton Central' in all_dem_by_mb[h][nz.KEY_PAIR]:
                #             print('in')
                #         print(all_dem_by_mb[h][nz.KEY_PAIR])
                filename_increment = '_v07'
                fnct.write_to_csv(country, all_dem_by_mb[0], all_dem_by_mb[1],filename_increment)
                # ---------------------------------------------
                fnct.squash(country, all_dem_by_mb[1],filename_increment)

                print('ttl_matched = ', all_dem_by_mb[2][0])
                print('ttl = ', all_dem_by_mb[2][1])
                print('percentage_matched = ', all_dem_by_mb[2][2],'%')
    elif country == 'AUS':
        # aus.sort_csv(country)
        # aus.api_call(aus.INDUSTRY_API_URL_xml)
        cnt = 0
        for i in aus.all_endPts():
            print()
            print(i['API'])
            print()
            aus.api_call(i['API'],str(cnt))
            cnt += 1
        # aus.api_call(aus.MEDIANS,'medians')
    pass

if __name__ == "__main__":
    main(sys.argv[1:])
    pass