from urllib.request import urlopen

response = urlopen('http://books.toscrape.com/')

source_code = response.read().decode('utf-8', 'ignore')

output_source_code = "C:\\Users\\irem3\\Documents\\test.txt"

with open(output_source_code, "w") as f:
    f.write(source_code)