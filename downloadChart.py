#! python3
# downloadChart.py - Downloads Stock chart

import requests, os, bs4, sys

query = sys.argv[1]
print(query)

url = 'http://bigcharts.marketwatch.com/advchart/frames/frames.asp?show=&insttype=Stock&symb='+query+'&time=8&startdate=1%2F4%2F1999&enddate=4%2F22%2F2019&freq=1&compidx=aaaaa%3A0&comptemptext=&comp=none&ma=6&maval=20%2C50%2C200&uf=0&lf=268435456&lf2=0&lf3=0&type=4&style=320&size=4&x=47&y=15&timeFrameToggle=false&compareToToggle=false&indicatorsToggle=false&chartStyleToggle=false&state=11'
#url = 'http://bigcharts.marketwatch.com/advchart/frames/frames.asp?show=&insttype=&symb='+query+'&x=32&y=17&time=8&startdate=1%2F4%2F1999&enddate=4%2F27%2F2019&freq=1&compidx=aaaaa%3A0&comptemptext=&comp=none&ma=6&maval=20%2C50%2C200&uf=0&lf=268435456&lf2=4&lf3=1024&type=4&style=320&size=4&timeFrameToggle=false&compareToToggle=false&indicatorsToggle=false&chartStyleToggle=false&state=11'
os.makedirs('/Users/emilolbinado/Downloads/stockcharts/', exist_ok=True)

# Download the page.
print('Downloading page %s...' %url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")

print('Done')

chartElem = soup.select('.chart-cont img')

if (chartElem == []):
    print('Could not find the chart image.')
    sys.exit()
else:
    chartUrl = chartElem[0].get('src')
    # Download the image.
    print('Downloading the image %s...' %(chartUrl))
    res = requests.get(chartUrl)
    res.raise_for_status()

# Save the image to ./stockcharts
imageFile = open(os.path.join('/Users/emilolbinado/Downloads/stockcharts/',query+'.gif'),'wb')
for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close
print('Done')