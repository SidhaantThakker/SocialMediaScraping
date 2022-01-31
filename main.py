import csv
import requests
from google_search import search_google

api_key = 'ee3a9d9d-da8a-4c1e-aedf-1ba3f3f2722d'


def contact_api(email):

    api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/resolve/email'
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'work_email': email,
    }
    response = requests.get(api_endpoint, params=params, headers=header_dic)
    print(response.json()['url'])
    return response.json()['url']

def profile_api(url):

    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'url': url,
        'use_cache': 'if-present',
    }
    response = requests.get(api_endpoint, params=params, headers=header_dic)
    return response.json()

def email_to_linkedin(name, email):
    url = contact_api(email)
    json_data = profile_api(url)
    # print(json_data)
    education_array = []
    for education in json_data['education']:
        education_array.append({'Degree': education['degree_name'], 'School':education['school']})
    search_object = {
        'name': name,
        'country': json_data['country_full_name'],
        'city': json_data['city'],
        'current_company': json_data['experiences'][0]['company'],
        'education': education_array
    }
    return search_object

def search_for_links(search_object):
    query = search_object['name']+' '+search_object['current_company']+' '+search_object['city']+' '+search_object['country']
    return search_google(query)


def email_profiler(name, email):
    search_object = email_to_linkedin(name, email)
    organic_results = search_for_links(search_object)
    search_object['socials'] = organic_results
    return search_object

def main():
    fieldnames = ['name', 'country', 'city', 'current_company', 'education', 'socials']
    with open('output.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        with open('input_data.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['Name'],', ', row['Email'])
                json_data = email_profiler(row['Name'], row['Email'])
                print(json_data)
                writer.writerow({'name': json_data['name'], 'country': json_data['country'], 'city': json_data['city'], 'current_company': json_data['current_company'], 'education': json_data['education'], 'socials': json_data['socials']})

main()


