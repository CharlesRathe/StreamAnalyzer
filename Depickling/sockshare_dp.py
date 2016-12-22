import pickle
import re, collections

dp = {}
frame_counts = {}

file = r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\sockshare_net_sources.p'
output = open(r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\sockshare_output', 'w+')

try:
    dp = pickle.load( open(file, 'rb'))
except pickle.UnpicklingError as p:
    print("Unpickling Error :: " + p.__cause__)
except BaseException as e:
    print("Other error :: " + e.__cause__)

frames = dp["iframe"]

output.write("IFrame Data :: %s\n" % frames.__len__())
output.write("----------------------------------------------\n")
for frame in frames:
    host = frame.replace('Server', ''). replace('Link ', '').replace(' ', '')
    host = re.sub('[0-9]+\Z', '', host).lower()

    if host in frame_counts.keys():
        frame_counts[host] += 1
    else:
        frame_counts[host] = 1

ord_frames = collections.OrderedDict(sorted(frame_counts.items(), key=lambda x: x[1]))

for key in ord_frames:
    output.write('%s :: %s\n' % (key, frame_counts[key]))

output.write("----------------------------------------------\n")


