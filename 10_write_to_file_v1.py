file_name = "test_filename.txt"
heading = "calc test heading !!!!"
data = "calc history here"
date = "todays date here"

text_file = open(file_name, "w+")
text_file.write("Generated: {}".format(heading))
text_file.write("\n\n")
text_file.write(date)
text_file.write("\n\n")
text_file.write(data)
text_file.close()
