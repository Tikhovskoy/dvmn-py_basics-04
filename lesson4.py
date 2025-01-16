from PIL import Image

image = Image.open("image.jpg")
red_channel, green_channel, blue_channel = image.split()

red_crop_left = 50
red_crop_sides = 25
red_left = red_channel.crop((red_crop_left, 0, red_channel.width, red_channel.height))
red_center = red_channel.crop((red_crop_sides, 0, red_channel.width - red_crop_sides, red_channel.height))
blended_red = Image.blend(red_left, red_center, alpha=0.5)

blue_crop_right = 50
blue_crop_sides = 25
blue_right = blue_channel.crop((0, 0, blue_channel.width - blue_crop_right, blue_channel.height))
blue_center = blue_channel.crop((blue_crop_sides, 0, blue_channel.width - blue_crop_sides, blue_channel.height))
blended_blue = Image.blend(blue_right, blue_center, alpha=0.5)

green_crop_sides = 25
green_cropped = green_channel.crop((green_crop_sides, 0, green_channel.width - green_crop_sides, green_channel.height))

final_image = Image.merge("RGB", (blended_red, green_cropped, blended_blue))
final_image.save("final_image.jpg")

final_image.thumbnail((80, 80))
final_image.save("final_image_thumbnail.jpg")
