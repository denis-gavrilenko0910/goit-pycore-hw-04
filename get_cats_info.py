def get_cats_info(path):
  result = []


  with open(path, mode='r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
      line = line.split(',')
      id = line[0]
      name = line[1]
      age = int(line[2].strip())
      result.append({"id": id, "name": name, "age": age})   

  return result    


cats_info = get_cats_info("cats_file.txt")
print(cats_info)


