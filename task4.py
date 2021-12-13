import requests

for municipality_name in ['Ylitornio','Merikarvia','Parikkala']:
    ceased_url = 'https://avoindata.prh.fi/tr/v1?totalResults=true&registeredOffice={}&companyForm=OY&companyRegistrationFrom=1978-03-14'.format(municipality_name)
    response = requests.get(ceased_url)
    json_data_ceased_url = response.json()
    length_of_companies = json_data_ceased_url['totalResults']

    print('Number of comapnies in ',municipality_name,':',length_of_companies)

    company_list = []
    for company_info in json_data_ceased_url['results']:
        company_list.append(company_info['bisDetailsUri'])


    for uri in company_list:
        bis_url = uri
        response = requests.get(uri)
        json_data_bis_url = response.json()

    json_data_bis_url_results = json_data_bis_url['results']
    counter = 0

    for i in range(0,len(json_data_bis_url_results)):
        register_entry = json_data_bis_url_results[i]['registeredEntries']
        for i in range(0,len(register_entry)):
            if register_entry[i]['endDate'] is not None:
                counter += 1

        print('Number of ceased companies in ',municipality_name,':',counter)
    