def getArtisticPhotographCount(N, C, X, Y):
  # Write your code here
  a = 0
  for i, item in enumerate(C):
    if item in ("P", "B"):
      for j in range(X,Y+1):
        if (i+j) >= N:
            break
        if C[i+j] == "A":
          for k in range(X,Y+1):
            if (i + j + k) >= N:
              break
            if ''.join([item, C[i + j], C[i + j + k]]) in ('PAB', 'BAP'):
              a+=1
  return a


if __name__ == "__main__":
    a = getArtisticPhotographCount(5, "APABA", 1, 2)
    print(a)