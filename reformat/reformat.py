# coding=utf-8


"""
Task: https://www.upwork.com/jobs/~0153ce71f8ed11d3eb

Convert some format
"""

# Change the INPUT to give different file names,
# or loop files in the main part
INPUT = 'input.txt'
header = """<h5><strong><a name="{c}">{c}</a></strong></h5>"""


def runner(inputfile):
    data = [x.strip() for x in open(inputfile) if x.strip() != '']
    key_poses = []
    for pos, item in enumerate(data):
        if item.endswith('AL CNA programs:'):
            key_poses.append(pos)

    for i in range(len(key_poses)-1):
        num_of_address = int((key_poses[i+1] - key_poses[i] - 1) / 3)
        club_name = data[key_poses[i]].split(',')[0]
        if num_of_address == 1:
            print(header.format(c=club_name))
            print("")
            print(data[key_poses[i]+1])
            print("Address: "+data[key_poses[i]+2])
            print(data[key_poses[i]+3])
        elif num_of_address > 1:
            print(header.format(c=club_name))
            for address in range(num_of_address):
                print("")
                print(data[key_poses[i]+1+num_of_address*3])
                print("Address: "+data[key_poses[i]+2+num_of_address*3])
                print(data[key_poses[i]+3+num_of_address*3])


if __name__ == '__main__':
    runner(INPUT)
