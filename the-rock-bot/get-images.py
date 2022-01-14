import requests # to get image from the web
import shutil # to save it locally

with open('rockImages.txt','r') as file:
    lst = file.readlines()

lines = []
for line in lst:
    lines.append(line.replace("\n",""))


for i in range(31):
    image_url = lines[i]
    filename = lines[i + 31] + '.png'

    r = requests.get(image_url, stream = True)
    # Open a local file with wb ( write binary ) permission.
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)

    print('Image sucessfully Downloaded: ',filename)
