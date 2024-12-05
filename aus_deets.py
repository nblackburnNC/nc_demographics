import functions as fnct
import csv
import requests
from dotenv import load_dotenv
import json
import xmltodict
import aus_decode as decoder

AUS_FILE_PATH = 'aus_data/'
CODE = 'Area_code'
ENCODING = 'UTF-8'

# All mapping contains Meshblocks
PCODE_MAP = 'aus_data/mapping/POA_2021_AUST.csv'
SAL_MAP = 'aus_data/mapping/SAL_2021_AUST.csv'

# INDUSTRY_API_URL_json = "https://api.data.abs.gov.au/data/ABS,C21_G56_SAL,1.0.0/D+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+_N+E+C+B+A._T...?startPeriod=2021&dimensionAtObservation=AllDimensions&format=jsondata"
# INDUSTRY_API_URL_xml = "https://api.data.abs.gov.au/data/ABS,C21_G56_SAL,1.0.0/D+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+_N+E+C+B+A._T...?startPeriod=2021&dimensionAtObservation=AllDimensions"
# INDUSTRY_API_URL_xml = "https://api.data.abs.gov.au/data/ABS,C21_G56_SAL,1.0.0/A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+_N+_T....?startPeriod=2021"
# INDUSTRY_API_URL = "https://api.data.abs.gov.au/dataflow/ABS/C21_G56_SAL/1.0.0"
PCODE_MEDIANS = 'https://api.data.abs.gov.au/data/ABS,C21_G02_POA,1.0.0/5+1+8+6+4...?startPeriod=2021&dimensionAtObservation=AllDimensions'
PCODE_INDUSTRY = 'https://api.data.abs.gov.au/data/ABS,C21_G56_POA,1.0.0/._T...?startPeriod=2021&dimensionAtObservation=AllDimensions'
PCODE_TRANSPORT_2_WORK = 'https://api.data.abs.gov.au/data/ABS,C21_G62_POA,1.0.0/9+10+11+232+1+2+3+4+5+6+7+8+_N+234+T_1+233+_T.3...?startPeriod=2021&dimensionAtObservation=AllDimensions'
PCODE_DWELLING_TYPE = 'https://api.data.abs.gov.au/data/ABS,C21_G36_POA,1.0.0/_N+9+3+2+11.D...?startPeriod=2021&dimensionAtObservation=AllDimensions'
PCODE_DWELLING_TENURE = 'https://api.data.abs.gov.au/data/ABS,C21_G37_POA,1.0.0/R_N+5+6+7+3+4+R_T+_N+9+2+1+_T._T...?startPeriod=2021&dimensionAtObservation=AllDimensions'
PCODE_ANCESTRY = 'https://api.data.abs.gov.au/data/ABS,C21_G08_POA,1.0.0/1101+1102+6101+3204+2303+2101+5201+2305+2306+3205+3304+7106+2201+3103+6902+4106+3206+3104+1201+1202+3307+3308+1504+2102+3213+9215+3106+7126+5107+2103+_O+_N._T...?startPeriod=2021&dimensionAtObservation=AllDimensions'
PCODE_POPULATION = 'https://api.data.abs.gov.au/data/ABS,C21_G27_POA,1.0.0/3._T._T...?startPeriod=2021&dimensionAtObservation=AllDimensions'

BURB_MEDIANS = 'https://api.data.abs.gov.au/data/ABS,C21_G02_SAL,1.0.0/8+5+4+1+6...?startPeriod=2021&dimensionAtObservation=AllDimensions'
BURB_INDUSTRY = 'https://api.data.abs.gov.au/data/ABS,C21_G56_SAL,1.0.0/H+I+J+K+L+M+N+O+P+Q+R+S+_N+G+F+E+D+C+B+A._T...?startPeriod=2021&dimensionAtObservation=AllDimensions'
BURB_TRANSPORT_2_WORK = 'https://api.data.abs.gov.au/data/ABS,C21_G62_SAL,1.0.0/7+8+9+10+11+232+6+5+4+3+2+1+233+_N+234+_T.3...?startPeriod=2021&dimensionAtObservation=AllDimensions'
BURB_DWELLING_TYPE = 'https://api.data.abs.gov.au/data/ABS,C21_G37_SAL,1.0.0/._N+9+3+2+11...?startPeriod=2021&dimensionAtObservation=AllDimensions'
BURB_DWELLING_TENURE = 'https://api.data.abs.gov.au/data/ABS,C21_G37_SAL,1.0.0/3+4+5+6+7+R_N+R_T+1+2+9+_N+_T....?startPeriod=2021&dimensionAtObservation=AllDimensions'
BURB_ANCESTRY = 'https://api.data.abs.gov.au/data/ABS,C21_G08_SAL,1.0.0/6902+4106+3206+3104+1201+1202+3307+3213+9215+3106+7126+5107+2103+_O+_N+3308+1504+2102+3103+2201+7106+3304+2306+3205+2305+5201+2101+2303+3204+6101+1102+1101+_T._T...?startPeriod=2021&dimensionAtObservation=AllDimensions'
PCODE_POPULATION = 'https://api.data.abs.gov.au/data/ABS,C21_G04_SAL,1.0.0/_T.3...?startPeriod=2021&dimensionAtObservation=AllDimensions'

def all_endPts():
    return [
        {'API' : BURB_MEDIANS, 'decoder' : decoder.decode_pcode_medians()},
        {'API' : BURB_INDUSTRY, 'decoder' : decoder.decode_pcode_industry()},
        {'API' : BURB_TRANSPORT_2_WORK, 'decoder' : decoder.decode_pcode_transport_2_work()},
        {'API' : BURB_DWELLING_TYPE, 'decoder' : decoder.decode_pcode_dwelling_type()},
        {'API' : BURB_DWELLING_TENURE, 'decoder' : decoder.decode_pcode_dwelling_tenure()},
        {'API' : BURB_ANCESTRY, 'decoder' : decoder.decode_pcode_ancestry()},
        {'API' : PCODE_POPULATION, 'decoder' : decoder.decode_population()},
    ]

def sort_csv(country):
    filenames = fnct.get_file_names(country)
    all_demographics = {}
    for file in filenames:
        path_in_file = fnct.get_file_path(country) + file
        demoDict = {}
        demoHeads = ["postcode"]
        init = True
        with open(path_in_file, 'r', encoding = 'cp1252') as f:
            data = csv.DictReader(f)
            listDat = list(data)
            keys = listDat[0].keys()
            for row in listDat:
                postcode = str(row["REGION: Region"].split(":",1)[0])
                tmp = {}
                if "Total" in row["AGEP: Age"]:
                    if init == True:
                        tmpCountry = row["BPLP: Country of birth of person"].split(": ",1)[1] + ' Population'
                    else:
                        tmpCountry = row["BPLP: Country of birth of person"].split(": ",1)[1]
                    
                    if tmpCountry not in demoHeads:    
                        demoHeads.append(tmpCountry)
                    tmp[tmpCountry] = row["OBS_VALUE"]
                    if postcode in demoDict:
                            init = False
                    if init == True:
                        tmp["postcode"] = postcode
                        demoDict[postcode] = tmp
                    else:
                        demoDict[postcode].update(tmp)                            
    demoList = []
    for entry in demoDict:
        demoList.append(demoDict[entry])
    fnct.write_to_csv(country,demoList,demoHeads)

def find_aus_fields():
    pass

def create_json_rspnse(response, naming='w_xml'):
    with open(AUS_FILE_PATH + 'response_'+ str(naming) +'.json', 'w') as f:
        try:
            json.dump(response.json(), f, indent=2)
        except:
            json.dump(response, f, indent=2)

        print("The json file is created for " + naming)

def api_call(url,naming):
    load_dotenv()
    # headers = {
    #     'accept': 'application/vnd.sdmx.structure+json'
    # #     'Accept': 'application/json'
    # }
    response = requests.get(url)
    # response = requests.get(INDUSTRY_API_URL, headers)
    try:
        print('json try')

        print(response.json())
        infile = response.json()
        for i in infile:
            print('---->',i,' : ',infile[i])
    except:
        print('no json')
        print('response is:', response)
        data_dict = xmltodict.parse(response._content)
        json_data = json.dumps(data_dict)
        # print(data_dict)
        create_json_rspnse(data_dict,naming)

        medians_decode = {
            '1' : 'Median_Age',
            '4' : 'Median_Household_Income',
            '5' : 'Median_mortgage_repayments',
            '6' : 'Median_rent',
            '8' : 'Median_household_size',
        }

        better_dict = {}
        for i in data_dict["message:GenericData"]['message:DataSet']["generic:Obs"]:
            try:
                print(i)
                print(i['generic:ObsKey']["generic:Value"][2]["@value"])
                print(medians_decode[i['generic:ObsKey']["generic:Value"][1]["@value"]])
                print(i['generic:ObsValue']["@value"])
                print(i['generic:ObsKey']["generic:Value"][2]["@value"],' --->>>' , medians_decode[i['generic:ObsKey']["generic:Value"][1]["@value"]] , ' ====>>>>>' , i['generic:ObsValue']["@value"])
                better_dict[i['generic:ObsKey']["generic:Value"][2]["@value"]] = { medians_decode[i['generic:ObsKey']["generic:Value"][1]["@value"]] : i['generic:ObsValue']["@value"] }
            except:
                print('error')

        # create_json_rspnse(json_data,3)
        # for i in json_data:
        #     print(i)
    # fnct.write_to_csv(response)
    pass