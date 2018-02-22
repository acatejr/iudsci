from bs4 import BeautifulSoup
import requests

RAINGAGE_URL = r"https://www.tucson.ars.ag.gov/dap/gage_locations.asp"
RAINGAGE_DATA_FILE = "raingages.csv"
PRECIP_EVENT_BASE_URL = r"https://www.tucson.ars.ag.gov/dap/eventh.asp"
PRECIP_FORM = {
    'hiddenStartYear': '1953',
    'hiddenEndYear': '1999',
    'Watershed': '63',
    'gages': '1',
    'StartMonth': '1',
    'StartDay': '1',
    'StartYear': '1953',
    'EndMonth': '12',
    'EndDay': '31',
    'EndYear': '1999',
    'all': 'ON',
    'type': 'summary',
    'format': 'text',
    'sortby': 'sortby_gage',
    'units': 'inches',
    'MinDepth': '',
    'MaxDepth': '',
    'MinDuration': '',
    'MaxDuration': '',
    'submit': 'Submit'
}
RAW_PRECIP_DATA_HEADER = "Gage|Date|Time|Duration|Depth|Time_Est"

def get_raingage_info():
    raingages = []

    result = requests.get(RAINGAGE_URL)
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "lxml")
        body_content = soup.select("#bodyContent")[0]
        raingage_table = body_content.select("table")[0]
        raingage_table_rows = raingage_table.select("tr")[4:]
        with open(RAINGAGE_DATA_FILE, 'w') as f:
            f.write("watershed_id|gage_id|east|north|elevation|err\n")
            for r in raingage_table_rows:
                row_data = r.select("td")
                watershed_id = str(row_data[0].text.strip())
                gage_id = str(row_data[1].text.strip())
                east = str(row_data[2].text.strip())
                north = str(row_data[3].text.strip())
                elevation = str(row_data[4].text.strip())
                err = str(row_data[5].text.strip())

                rg = {
                    'watershed_id': watershed_id,
                    'gage_id': gage_id,
                    'east': east,
                    'north': north,
                    'elevation': elevation,
                    'err': err
                }

                raingages.append(rg)

                f.write("{}|{}|{}|{}|{}|{}\n".format(watershed_id, gage_id, east, north, elevation, err))

    return raingages
    

def get_precip_data(raingages):
    
    if raingages:
        with open('raw_precip_data.txt', 'w') as f:
            for rg in raingages:
                url = PRECIP_EVENT_BASE_URL
                PRECIP_FORM['gages'] = rg['gage_id']
                resp = requests.post(url, data=PRECIP_FORM)
                
                if resp.status_code == 200:
                    # Save the raw precip data locally                    
                    f.write(resp.text)

def post_process_raw_precip_data():

    with open('precip.csv', 'w') as pf:
        pf.write(RAW_PRECIP_DATA_HEADER + "\n")
        with open('raw_precip_data.txt', 'r') as f:
            data = f.readlines()
            for r in data:
                l = r.strip()
                if len(l) > 0:
                    if l.startswith("SELECT") != True and l.startswith("#") != True and l.startswith("there was some error") != True:
                        # values = l.split(',')
                        # gage = values[0]
                        # dt = values[1]
                        # tm = values[2]
                        # duration = values[3]
                        # depth = values[4]
                        # time_est = values[5]
                        # pf.write("{}|{}|{}|{}|{}|{}\n".format(gage, dt, tm, duration, depth, time_est))
                        l = l.replace(',', '|')
                        # l = l.replace('/', '-')
                        pf.write(l[0:-1] + "\n")

if __name__ == '__main__':
    # print("Scraping watershed info.")
    # raingages = get_raingage_info()    
    # print("Done scraping raingage information.\n")

    # print("Scraping precipitation info.")
    # get_precip_data(raingages)
    # print("Done scraping precipitation info.\n")

    post_process_raw_precip_data()
