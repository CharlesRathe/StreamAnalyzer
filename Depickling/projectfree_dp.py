import pickle, collections
from urllib.parse import urlsplit

dp = {}
video_counts = {}
frame_counts = {}

file = r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\projectfreetv_us_sources.p'
output = open(r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\projectfreetv_output', 'w+')

try:
    dp = pickle.load( open(file, 'rb'))
except pickle.UnpicklingError as p:
    print("Unpickling Error :: " + p.__cause__)
except BaseException as e:
    print("Other error :: " + e.__cause__)

frames = dp["iframe"]
videos = dp["video"]

output.write("IFrame Data :: %s\n" % frames.__len__())
output.write("----------------------------------------------\n")
for frame in frames:
    host = urlsplit(frame).hostname.replace('http://', '')

    if host in frame_counts.keys():
        frame_counts[host] += 1
    else:
        frame_counts[host] = 1

ord_frames = collections.OrderedDict(sorted(frame_counts.items()))

for key in ord_frames:
    output.write('%s :: %s\n' % (key, frame_counts[key]))
output.write('----------------------------------------------\n')



