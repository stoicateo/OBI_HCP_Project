import os

male = [121416,122620,123117,125222,129028,130013,130114,130417,131823,133625]
female = [114217,117021,118023,118528,119833,120010,120111,120414,120515,122418]

for s in female:
    print 'downloading ' +str(s)
    cmd = 'python HCP_download/download_HCP_1200.py --subject=' +str(s) +' --out_dir=/imaging/jerez/obi/hcp/data/'
    os.system(cmd)

