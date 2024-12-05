import pandas as pd
import nz_deets_SA12018 as nz
import functions as fnct

LOOKIN_FOR = ['Hamilton Central']

def build_list(file_to_open,src_lst,src_key, target_key):
    target_list = []
    count = 0
    df = pd.read_csv(file_to_open)
    df_dict = df.to_dict()

    for i in df_dict[src_key]:
        if df_dict[src_key][i] in src_lst:
            print('Row: ',i,' -> ' ,df_dict[src_key][i],': ',df_dict[target_key][i])
            target_list.append(df_dict[target_key][i])
            count += 1
    print('total ',src_key,' -> ',target_key,': ',str(count))
    print(target_list)
    print()
    return target_list
    pass

# def main():
def build_sublist(looking_for = LOOKIN_FOR):
    built_lst = build_list(nz.FILE_MAP_SA1_MB_v3['filename'],build_list(nz.FILE_MAP_MB_LBURB_v4['filename'], looking_for, 'suburb_locality_ascii', 'meshblock_id'),'MB2018 V1.0.0','SA12018 V1.0.0')
    strlst = [str(x) for x in built_lst]
    return strlst

def main():
    country = 'NZ'
# def build_sublist(looking_for = LOOKIN_FOR):
    # built_lst = build_list(nz.FILE_MAP_SA1_MB_v3['filename'],build_list(nz.FILE_MAP_MB_LBURB_v4['filename'], looking_for, 'suburb_locality_ascii', 'meshblock_id'),'MB2018 V1.0.0','SA12018 V1.0.0')
    # strlst = [str(x) for x in built_lst]
    # return strlst
    filenames = fnct.get_file_names(country)
    path = fnct.get_file_path(country)
    finding_area = build_sublist()

    data_extract = {}
    for i in finding_area:
        data_extract[i] = {}

    for file in filenames:
        df = pd.read_csv(path+file)
        df_dict = df.to_dict()

        fields = nz.find_nz_fields(file)

        for i in df_dict:
            # print(i)
            print()
            print('Area_code')
            # print(df_dict['Area_code'])
            print(i)
            # print(df_dict[i])
            # print()
            if '2018' in i:
                print('2018 here ----')
                for j in df_dict[i]:
                    print(j)
                    # print(df_dict[i])
                    if df_dict['Area_code'][j] in finding_area:
                        print(i,' -> ',df_dict[i][j])
                        print('Area_code ---->',df_dict['Area_code'][j])
                        data_extract[df_dict['Area_code'][j]].append({i : df_dict[i][j]})
                    for dictionary in fields:
                        for key in dictionary:
                            if i == key:
                                # print(i,':-> ',df_dict[i])
                                pass

            # print(df_dict[i])
            # print(type(i))
            # if i in finding_area:
            #     print(i)
    # return build_list(nz.FILE_MAP_SA1_MB_v3['filename'],build_list(nz.FILE_MAP_MB_LBURB_v4['filename'], looking_for, 'suburb_locality_ascii', 'meshblock_id'),'MB2018 V1.0.0','SA12018 V1.0.0')
    pass



if __name__ == "__main__":
    main()
    pass