import requests
from requests import Response

cookie_string = '_ga=GA1.1.1870671157.1724723224; intercom-device-id-yvpndjps=3b5c689b-8d0d-4806-b5d0-f3c8183fea59; __experiment_uuid=7488d17f-b099-4332-9427-dd3024414dca; GCP_IAP_UID=104700612389542383733; _fbp=fb.2.1726721459704.745976873131738412; _gcl_au=1.1.1411064912.1748225124; _ga_FXL9Y382GM=GS2.1.s1754269972$o135$g1$t1754269990$j42$l0$h0; _ga_0QGMXT9H3T=GS2.1.s1754270197$o66$g0$t1754270197$j60$l0$h0; intercom-session-yvpndjps=cms3L01iUitaK0ovR0JOVHREdjhFWStjRWVQY1ZQZi9xRDd2V0V4MnduYm5seWwvQXBpVnZScFJGaWJwOEREYno5b2t0Y1kwV2NzN0RVK3VmTklSZ2gwdWMrRHZzdHVLUjdEQzBTQUtBZEU9LS1NcFpIRGUrZ0MwUFhIN1o2UE16Z2l3PT0=--4a4e755f65b3a05cf99f7956fccab4f2a3796587; remember-me=Q1hFQ0ZDQkNMcWRsMnF6bkVIeXhQdyUzRCUzRDpYOTFCcVRzcE5Kb3pMOFZpNVFtUUd3JTNEJTNE; SESSION=YzI4MTRmNWYtYTk0NS00YjUyLTkwZjUtMTEyMTZkZDA1YjNh; _ga_B0D5TWJLTF=GS2.1.s1754284574$o10$g1$t1754284597$j37$l0$h0'
base_url = 'https://home-testing.raywhite.co.nz/'

with open("kieran-try.csv", "rb") as f:
    files = {
        "file": ("kieran-try.csv", f, "text/csv")
    }

# print(payload)

    response: Response = requests.post(
        f"{base_url}api/v2/bootstrap/demographics/nz",
        files=files,
        headers={
            "cookie": cookie_string,
            "accept": "application/json, text/plain, */*",
            "content-type": "text/csv"
        }
    )

    if response.status_code != 200:
        print(response.content)
        raise Exception("Shits fucked")

    print(response.status_code)
    print(response.text)