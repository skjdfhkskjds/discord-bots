import requests  # to get image from the web
import shutil  # to save it locally


path = 'rock images/'
file_type = '.png'

def genesis_images():
    with open('rockImages.txt', 'r') as file:
        lst = file.readlines()

    lines = []
    for line in lst:
        lines.append(line.replace("\n", ""))

    for i in range(31):
        image_url = lines[i]
        filename = path + lines[i + 31] + file_type

        r = requests.get(image_url, stream=True)
        # Open a local file with wb ( write binary ) permission.
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', filename)
        return


def new_image(name, image_url):
    filename = path + name + file_type
    r = requests.get(image_url, stream=True)
    # Open a local file with wb ( write binary ) permission.
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    success_message = ('Image sucessfully downloaded: ', name + file_type)
    print(success_message)
    return success_message
