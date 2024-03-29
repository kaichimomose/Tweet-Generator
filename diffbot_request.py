import requests

DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = '9249e70e00b35e27c545eefc0cda2887'

def get_article(article_url):
    # set request params for API request
    params = {'token': DIFFBOT_DEV_TOKEN,
              'url': article_url,
              'discussion': 'false'}

    res = requests.get(DIFFBOT_API_URL, params)  # hit the Diffbot API
    res_obj = res.json()['objects'][0]           # parse the response object

    return res_obj['text']                       # pull out the text

if __name__ == '__main__':
    import sys
    urls_file = open(sys.argv[1])
    output_file = open('corpus.txt', 'w')

    corpus = ''

    for line in urls_file:
        url = line.strip() # remove leading/trailing whitespace
        article = get_article(url)
        corpus += article
        print("this is url: {}".format(url))

    output_file.write(corpus)
    print('Corpus saved to {}'.format(output_file.name))
