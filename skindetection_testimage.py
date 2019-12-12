from PIL import Image

# change as per need
TEST_IMAGE_LOCATION = "07_WickedlyFastWifi_crop.jpg"
TRAINING_FILE_LOCATION = "training_sheet.txt"
OUTPUT_IMAGE_NAME = "output_image8.png"

OUTPUT_IMAGE=[]
MY_HASH_LIST = {}

im=Image.open(TEST_IMAGE_LOCATION, "r")
pix_val=list(im.getdata())

for line in open(TRAINING_FILE_LOCATION).readlines():
    MY_HASH_LIST[line.strip()] = ""

for rgb in pix_val:
    r_unmask, g_unmask, b_unmask = rgb
    key = str(255*255*r_unmask + 255*g_unmask + b_unmask)

    if key in MY_HASH_LIST:
        OUTPUT_IMAGE.append((r_unmask, g_unmask, b_unmask))
    else:
        OUTPUT_IMAGE.append((255, 255, 255))


im.putdata(OUTPUT_IMAGE)
im.save(OUTPUT_IMAGE_NAME)