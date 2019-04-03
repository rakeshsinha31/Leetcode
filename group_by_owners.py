def group_by_owners(files):
    req_dict = {}
    for i in files:
        print req_dict
        if files[i] in req_dict:
            print ('---in if---')
            print req_dict[files[i]]
            print files[i]
            req_dict[files[i]] = req_dict[files[i]].append(i)
        else:
            print ('---in else--', i)
            req_dict[files[i]] = [i]
    return req_dict
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))