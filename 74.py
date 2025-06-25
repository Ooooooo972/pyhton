def generateTable(n):
  table=""
  for i in range (1,11):
    table+=f"{n}*{i}={n*i}\n"
    with open(f"tables/table_{n}","w") as f:
      f.write(table)

for i in range(2,22):
  generateTable(i)     