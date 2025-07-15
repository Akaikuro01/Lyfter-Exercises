def copy_song_list_txt_to_list(path):
	try:
		list_songs = []
		with open(path) as file:
			for song in file.readlines():
				if (song.endswith('\n')):
					list_songs.append(song)
				else:
					list_songs.append(song + '\n')
		return list_songs
	except FileNotFoundError as ex:
		print(ex)
	except PermissionError as ex:
		print(ex)
	except IsADirectoryError as ex:
		print(ex)
	except TypeError as ex:
		print(ex)
	except OSError as ex:
		print(ex)
	except Exception as ex:
		print(ex)

#def copy_list_songs_to_txt(list_songs):

def order_list_alphabetically(list_songs):
	try:
		ordered_list = []
		lowest_alphabetically = 0
		lowest_word_index = 0
		counter = 1

		while (True):
			if(len(list_songs) == 0):
				break
			else:
				for index, word in enumerate(list_songs):
					counter = 0
					while (counter <= len(word)):
						current_word_order = ord(word[0])
						if (current_word_order < lowest_alphabetically or lowest_alphabetically == 0):
							lowest_alphabetically = current_word_order
							lowest_word_index = index
							break
						elif (current_word_order == lowest_alphabetically):
							current_lowest_word_other_letter = ord(list_songs[lowest_word_index][counter + 1])
							current_word_other_letter = ord(word[counter + 1])
							if (current_word_other_letter < current_lowest_word_other_letter):
								lowest_alphabetically = current_word_order
								lowest_word_index = index
								break
							else:
								if (current_word_other_letter == current_lowest_word_other_letter):
									counter += 1
								else:
									break
						else:
							break

			ordered_list.append(list_songs.pop(lowest_word_index))
			lowest_alphabetically = 0
		return ordered_list
	except ValueError as ex:
		print(ex)
	except IndexError as ex:
		print(ex)
	except TypeError as ex:
		print(ex)
	except Exception as ex:
		print(ex)
	except Exception as ex:
		print(ex)

def write_song_list_ordered_alphabetically(path, list_ordered_songs):
	try:
		with open(path, 'w') as file:
			for song in list_ordered_songs:
				file.write(song)
	except FileNotFoundError as ex:
		print(ex)
	except PermissionError as ex:
		print(ex)
	except IsADirectoryError as ex:
		print(ex)
	except TypeError as ex:
		print(ex)
	except OSError as ex:
		print(ex)
	except Exception as ex:
		print(ex)


list_songs = copy_song_list_txt_to_list("D:\Documents\Lyfter\Week 8 Python exercises\one_ok_rock_detox_tracklist.txt")
List_in_order = order_list_alphabetically(list_songs)
write_song_list_ordered_alphabetically("D:\Documents\Lyfter\Week 8 Python exercises\one_ok_rock_detox_tracklist_alphabetically.txt", List_in_order)
