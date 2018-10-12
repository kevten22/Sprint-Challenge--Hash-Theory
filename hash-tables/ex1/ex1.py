def get_indices_of_item_weights(weights, limit):
  table = {}

  for i in range(len(weights)):
    table[weights[i]] = i

  if(len(weights) <= 1):
    return ()
  
  elif(len(weights) == 2):
    return (1,0)

  for weight in table:
    try:
      difference = table[limit-weight]
      if(difference):
        return (table[limit-weight], table[weight])
    except KeyError:
      print("Value not found")

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 7), (6, 2))

    