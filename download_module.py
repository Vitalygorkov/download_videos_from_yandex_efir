import csv
import requests
import re

tsv_file = open("list.tsv", encoding='utf-8')
read_tsv = csv.reader(tsv_file, delimiter="\t")
list_video = []
for row in read_tsv:
  list_video.append(row)
print(list_video)
tsv_file.close()
for i in list_video:
  url = i[1]
  name = i[0]
  print(name)
  reg = re.compile('[^a-zA-Zа-яА-Я0-9,() ]')
  name_clean = reg.sub('', name)
  print(name_clean)
  print(url)
  # print(f'{name_clean}.mp4')
  r = requests.get(url, allow_redirects=True)
  open(f'{name_clean}.mp4', 'wb').write(r.content)
