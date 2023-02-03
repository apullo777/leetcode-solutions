# https://leetcode.com/problems/find-duplicate-file-in-system/

# Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
# Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

# Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
# Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for line in paths:
            data = line.split()
            root = data[0]
            for file in data[1:]:
                name, _, content = file.partition('(')
                ans[content[:-1]].append(root + '/' + name)
                
        return [i for i in ans.values() if len(i) > 1]