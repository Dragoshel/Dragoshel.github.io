import sys
from PIL import Image

def hide(image_data, pixel_index, color_index, msg_array, msg_index, bit_index):
	msg = msg_array[msg_index]
	msg &= 1 << bit_index
	msg >>= bit_index
	
	image_data_pixel_list = list(image_data[pixel_index])
	image_data_pixel_list[color_index] &= ~1
	image_data_pixel_list[color_index] |= msg
	image_data[pixel_index] = tuple(image_data_pixel_list)

def reveal(image_data, pixel_index, color_index, char, bit_index):
	byte = image_data[pixel_index][color_index]
	byte &= 1
	char[0] |= byte << bit_index

def encode(image_path, message):
	image = None
	
	try:
		image = Image.open(image_path, 'r')
	except FileNotFoundError:
		print('The file doesn\'t exist.')
		return -1

	image_data = list(image.getdata())
	
	if len(image_data) * 3 < len(message) * 8:
		print('Can\'t fit the msessage in this file. The message is too big.')
	else:
		msg_array = bytearray(message, 'utf8')
		color_index = 3
		pixel_index = 0
	
		for msg_index in range(len(msg_array)):
			for bit_index in range(8):
				hide(image_data, pixel_index, color_index % 3, msg_array, msg_index, bit_index)	
				
				if color_index % 3 >= 2:
					pixel_index += 1
				color_index += 1

		new_image = Image.new('RGB', image.size)
		new_image.putdata(image_data)
		new_image.save('./encoded.png', format='PNG')
		new_image.close()
		
	image.close()
def decode(image_path):
	image = None

	try:
		image = Image.open(image_path, 'r')
	except FileNotFoundError:
		print('The file doesn\'t exist.')
		return -1

	image_data = list(image.getdata())
	decoded_msg = ''

	char = bytearray('\0', 'utf8')
	color_index = 3
	pixel_index = 0

	while pixel_index < 500:
		for bit_index in range(8):
			reveal(image_data, pixel_index, color_index % 3, char, bit_index)

			if color_index % 3 >= 2:
				pixel_index += 1
			color_index += 1

		try:
			decoded_msg += char.decode('utf8')
		except UnicodeDecodeError:
			pass
		char[0] &= 0

	return decoded_msg
if __name__ == '__main__':
	option = sys.argv[1]

	if option == 'encode':
		image_path = sys.argv[2]
		message = sys.argv[3]
		encode(image_path, message)

	elif option == 'decode':
		image_path = sys.argv[2]
		decoded = decode(image_path)
		print(decoded)
	
	else:
		print('Invalid first option.')
