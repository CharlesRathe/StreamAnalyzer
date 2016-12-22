import pickle, collections
import re

dp = {}
frame_counts = {}

file = r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\putlockers_fi_sources.p'
output = open(r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\putlockers_output', 'w+')

try:
    dp = pickle.load( open(file, 'rb'))
except pickle.UnpicklingError as p:
    print("Unpickling Error :: " + p.__cause__)
except BaseException as e:
    print("Other error :: " + e.__cause__)

frames = dp["iframe"]
frames.extend(dp["video"])

output.write("Data :: %s\n" % frames.__len__())
output.write("----------------------------------------------\n")
for frame in frames:
    host = frame
    host = re.sub(re.compile(r'\.[a-z]+'), '', host) \
        .replace('.us', '').replace('.tv', '').replace('.com', '').replace('.co', '') \
        .replace('.to', '').replace('.net', '').replace('.me', '').replace('.eu', '').replace('embed.', '').replace(
        'hd', '').replace('.red', '').replace('.pro', '')
    host.lower()
    if host in frame_counts.keys():
        frame_counts[host] += 1
    else:
        frame_counts[host] = 1

ord_frames = collections.OrderedDict(sorted(frame_counts.items(), key=lambda x: x[1]))

for key in ord_frames:
    output.write('%s :: %s\n' % (key, frame_counts[key]))
output.write('----------------------------------------------\n')



