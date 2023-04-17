def calculate_sum(file_name):
  with open(file_name, "r") as file:
    contents= file.readlines()
    total = 0
    for line in contents:
      line = line.strip()
      total+= int(line)
  return total



def readFile(fileName):
    f=open(fileName)
    line=f.readline()
    for i in range(int(line)):
      print(line)
      line=f.readline()
      line = int(line)
    f.close()


try:
  fileName = input("Введите имя файла: ")
  file_name = "poem.txt"
  result=calculate_sum(file_name)
  print("Сумма цифр",result)


except EOFError:
    print("Дошли до конца файла")


except ValueError:
  print("передан аргумент с неподдерживаемым значением, убедитесь что в файле все строки состоят из цифр, или то что все пустые строки удалены")
except IOError:
  print("Файл не найден")
except:
  print("В файле есть строка с буквами")