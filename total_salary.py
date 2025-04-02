def total_salary(path):
   
  with open(path, mode='r', encoding='utf-8') as file:
    lines = file.readlines()
    total = 0

    for line in lines:
     line = line.split(',')[1]
     line = int(line.strip())
     total += line
     
  return total, total / len(lines)

total, average = total_salary("salary_file.txt")
print (f"Общая сумма заработной платы: {total}, Средняя заработная плата: {average}")
