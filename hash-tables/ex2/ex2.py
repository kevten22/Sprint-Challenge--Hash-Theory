def reconstruct_trip(tickets):
  table = {}
  for i in tickets:
    table[i[0]] = i[1]
  
  result = []
  
  try:
    link = table[None]
    result.append(link)
    complete = False

    print(link)
    while(complete == False):
      try:
        link = table[link]
        if(link):
          result.append(link)
        if(link == None):
          complete = True
      except:
        return []
      
    return result

  except:
    return []

  

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print(reconstruct_trip([
      ('PIT', 'ORD'),
      ('XNA', 'CID'),
      ('SFO', 'BHM'),
      ('FLG', 'XNA'),
      (None, 'LAX'), 
      ('LAX', 'SFO'),
      ('CID', 'SLC'),
      ('ORD', None),
      ('SLC', 'PIT'),
      ('BHM', 'FLG'),
    ]))
  pass
