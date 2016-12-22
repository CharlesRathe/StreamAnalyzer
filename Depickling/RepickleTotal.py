import collections, csv

filtered_files = [r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\123movie_output', r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\housemovie_output',
                  r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\hugemoveDB_output', r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\movie4k_output',
                  r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\movierill_output', r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\m2watch_output',
                  r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\projectfreetv_output', r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\putlockers_output',
                  r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\sockshare_output', r'C:\Users\crrat\PycharmProjects\StreamCrawler\FilteredResults\watchfree_output']

filtered_edge = ['123Movies', 'HouseMovies', 'HugeMovieDB', 'Movie4k', 'MovieRill', 'MovieToWatch','ProjectFreeTV', 'Putlockers', 'Sockshare', 'WatchFree']
f = 0

edges = 'Edges.csv'
nodes = 'Nodes.csv'

total = 0
total_counts = {}
with open(edges, 'w', newline='') as b:
    d = csv.writer(b, delimiter=',')
    d.writerow(["Source", "Target", "Weight"])
    for s in filtered_files:
        temp_counts = {}
        file = open(s, 'r+')
        not_done = 1
        line = file.readline()
        l = line.replace('\n', '').split(' :: ')
        total += int(l[1])
        line = file.readline()

        while not_done:
            line = file.readline()
            l = line.replace('\n', '').split(' :: ')
            if l == [''] or '------' in l:
                not_done = 0
            else:
                if l[0] in total_counts.keys():
                    total_counts[l[0]] += int(l[1])
                else:
                    total_counts[l[0]] = int(l[1])
                if l[0] in temp_counts.keys():
                    temp_counts[l[0]] += int(l[1])
                else:
                    temp_counts[l[0]] = int(l[1])


        for t in temp_counts:
            d.writerow([filtered_edge[f], t, temp_counts[t]])

        f += 1


ord = collections.OrderedDict(sorted(total_counts.items(), key=lambda x: x[1]))

with open(nodes, 'w', newline='') as c:
    a = csv.writer(c, delimiter=',')
    a.writerow(["ID"])
    for o in ord:
        a.writerow([o])

# newfile = (r"C:\Users\crrat\PycharmProjects\Analyzer\SourceAnalysis\total.txt")
# of = open(newfile, "w+")
# for o in ord:
#     of.write("%s :: %s\n" % (o, ord[o]))
# pickle.dump(total_counts, of)



print(total)

