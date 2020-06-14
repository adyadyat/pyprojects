import sys

votes = sys.argv[1:]

# Преобразуем каждый элемент в целое число.
# Элемент функционального программирования, 
# будем изучать в отдельном курсе.
votes = list(map(int, votes))

votes.sort(reverse=True)
votes_copy = votes[1:-1]

print(votes_copy)