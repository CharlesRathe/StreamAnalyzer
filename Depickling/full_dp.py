import pickle, re, collections

source_files = [r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\123movies_net_sources.p', r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\housemovie_to_sources.p',
         r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\movie4k_sources.p', r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\movierill_sources.p',
         r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\moviestowatch_sources.p', r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\projectfreetv_us_sources.p',
         r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\putlockers_fi_sources.p', r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\sockshare_net_sources.p',
         r'C:\Users\crrat\PycharmProjects\StreamCrawler\logs\watchfree_to_sources.p']
filtered_files = [r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\123movie_output', r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\housemovie_output',
                  r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\hugemoveDB_output', r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\movie4k_output',
                  r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\movierill_output', r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\m2watch_output',
                  r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\projectfreetv_output', r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\putlockers_output',
                  r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\sockshare_output', r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\watchfree_output']

output = open(r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\total_output', 'w+')

video = 1
frame_counts = {}
video_counts = {}

for file in filtered_files:
    input = open(file, 'r+')

    firstLine = input.readline()

    if "Video Data" in firstLine:
        not_done = 1
        input.readline()

        while not_done:
            line = input.readline()
            if "----" in line:
                not_done = 0
            else:
                l = line.replace('\n', '').split(' :: ')
                print("%s :: %s" % (l[0], l[1]))
                if l[0] in video_counts.keys():
                    video_counts[l[0]] += int(l[1])
                else:
                    video_counts[l[0]] = int(l[1])
    else:
        video = 0

    if video:
        # Go to Iframe data
        not_done = 1
        while not_done:
            line = input.readline()
            if "IFrame" in line:
                not_done = 0

    # Get rid of first line
    line = input.readline()

    not_done = 1
    while not_done:
        line = input.readline()
        if "---" in line:
            not_done = 0
        else:
            l = line.replace('\n', '').split(' :: ')
            if l[0] in frame_counts.keys():
                frame_counts[l[0]] += int(l[1])
            else:
                frame_counts[l[0]] = int(l[1])

# Write Data to File
ord_video = collections.OrderedDict(sorted(video_counts.items(), key=lambda x: x[1]))

for key in ord_video:
    output.write('%s :: %s\n' % (key, ord_video[key]))

output.write('----------------------------------------------\n')

ord_frames = collections.OrderedDict(sorted(frame_counts.items(), key=lambda x: x[1]))

for key in ord_frames:
    output.write('%s :: %s\n' % (key, frame_counts[key]))
output.write('----------------------------------------------\n')
