import pandas as pd
import csv
f = open("clean_output.txt", "r")
file_contents = []
group=-1
guard_dict={}
for line in f:
  line_out = line.split(",")
  a=line_out[0][0]
  if line_out[0][0] == "G":
      group += 1
  line_out[0] = str(line_out[0]).split(" ")[1][1:]
  line_out[1] = int(line_out[1])
  line_out.append(group)
  line_out.append(a)
  file_contents.append(line_out)
clean_data = []
for line in file_contents:
    if line[3] == "G":
        guard = line[0]
    if line[3] == "f":
        sleep_minute = line[1]
    if line[3] == "w":
        wake_minute = line[1]
        data_point=[guard, sleep_minute, wake_minute, wake_minute - sleep_minute]
        clean_data.append(data_point)

with open("out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerows(clean_data)




# data = pd.read_csv('input_day_4.txt', header = None)
# print(data)