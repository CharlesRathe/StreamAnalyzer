import pickle, collections
from urllib.parse import urlsplit

dp = {}
frame_counts = {}
video_counts = {}

file = r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\movierill_sources.p'
output = open(r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\movierill_output', 'w+')

try:
    dp = pickle.load( open(file, 'rb'))
except pickle.UnpicklingError as p:
    print("Unpickling Error :: " + p.__cause__)
except BaseException as e:
    print("Other error :: " + e.__cause__)

frames = dp["iframe"]
videos = dp["video"]

output.write("Video Data :: %s\n" % videos.__len__())
output.write("----------------------------------------------\n")
for video in videos:
    host = urlsplit(video).hostname.replace('www.', '').replace('https://', ''). replace('http://', '')
    if host in video_counts.keys():
        video_counts[host] += 1
    else:
        video_counts[host] = 1

ord_video = collections.OrderedDict(sorted(video_counts.items()))

for key in ord_video:
    output.write('%s :: %s\n' % (key, ord_video[key]))

output.write("----------------------------------------------\n")

output.write("IFrame Data :: %s\n" % frames.__len__())
output.write("----------------------------------------------\n")
for frame in frames:
    host = urlsplit(frame).hostname.replace('www.', '').replace('https://', ''). replace('http://', '')

    if host in frame_counts.keys():
        frame_counts[host] += 1
    else:
        frame_counts[host] = 1

ord_frames = collections.OrderedDict(sorted(frame_counts.items()))

for key in ord_frames:
    output.write('%s :: %s\n' % (key, frame_counts[key]))
output.write('----------------------------------------------\n')




