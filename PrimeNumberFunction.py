def checkprime(n):
  flag=0
  for i in range(2,n):
    if n%i==0:
      flag=flag+1
      break
  return(flag==0)
def primeproduct(m):
  mum=m
  #print("taken number as=",number)
  for j in range(2,m):
      if m%j==0 and m!=j: 
          p=m//j
          if checkprime(p)==True:
            break
          else:
            m=p
            continue
      else:
          p=m//j
  q=mum//p
  return(checkprime(p)==checkprime(q))
