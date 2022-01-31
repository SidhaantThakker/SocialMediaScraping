from serpapi import GoogleSearch


def search_google(data):

    socials = ['Twitter','Instagram','Facebook']
    organic_results = []

    for social in socials:
        params = {
            "engine": "google",
            "q": data+' '+social,
            "api_key": "12fc1521ed880bbc4fb159bb2c0b45c951b8c5e08a43df5699bfe2e8dc1842ef"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results.append({'social': social, 'title': results['organic_results'][0]['title'], 'link': results['organic_results'][0]['link']})
    return organic_results

# print(search_google('Sidhaant Thakker Mumbai India'))
