import pickle

total = 0

file = r"C:\Users\crrat\PycharmProjects\Analyzer\SourceAnalysis\total.p"

try:
    dp = pickle.load( open(file, 'rb'))
except pickle.UnpicklingError as p:
    print("Unpickling Error :: " + p.__cause__)
except BaseException as e:
    print("Other error :: " + e.__cause__)

for t in dp:
    total += dp[t]

print(total)