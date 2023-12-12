n = int(input())
scores = list(map(int, input().split))

ranked_score = sorted(scores, reverse = True)
ranks = [ranked_score.index(score) + 1 for score in scores]

for i in range(n):
  print(scores[i],ranks)
