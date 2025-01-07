from collections import defaultdict

test_list = ["gfg is best for geeks", "geeks love gfg", "gfg is best"]

print("The original list is : " + str(test_list))

temp = defaultdict(int)

for sub in test_list:
	for wrd in sub.split():
		temp[wrd] += 1

res = max(temp, key=temp.get)

print("Word with maximum frequency : " + str(res))
