def delchar(s,c):
  new=[]
  for i in s:
      if c!=i:
          new.append(i)
  if len(new)>1:
      answer=""
      for r in new:
          answer+=r
      return(answer)
    
      
  else:
      return(s)
