try:
  print("pyhon")
  try:
    print(5/0)
  except:
    print("inner handler")
    print("done")
except:
  print("outer handler")
