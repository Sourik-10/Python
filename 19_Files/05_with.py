with open ("read.txt","r") as f:
  content =f.read()
  print(content) #no neeed to write f.close() file is already closed by default when we use with syntax