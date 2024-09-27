import itertools

def all_variants(text):
    for r in range(1, len(text) + 1):
        for combination in itertools.combinations(text, r):
            yield ''.join(combination)

a = all_variants("abc")
for i in a:
    print(i)

