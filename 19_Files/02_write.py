file = open("new_file.txt", "w")  # Open in write mode (creates or overwrites)
string=''' Hello my name is john. I live in Nyc & i am a data engineer'''
file.write(string)
file.close()