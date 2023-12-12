def hanoi(n,a,b,c):
  if n==1:
    print(f"Disk {n}: {a} to {c} ")
  else:
    hanoi(n-1, a, c, b)
    print(f"Disk {n}: {a} to {c} ")
    hanoi(n-1, b, a, c)
#n-1을 하는 건 한 칸 아래의 원반을 지정하려고.
if __name__ == "__main__":
  n = int(input())
  hanoi(n, "A", "B", "C")