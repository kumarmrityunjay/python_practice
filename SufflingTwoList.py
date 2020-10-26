def shuffle(l1,l2):
  n=max(len(l1),len(l2))
  newlist=[]
  for i in range(n):
      try:
          newlist.append(int(l1[i]))
      except:
          pass
      try:
          newlist.append(int(l2[i]))
      except:
          pass
  return(newlist)
