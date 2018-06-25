class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        #len=(len.A)
        count=0
        cand=""
        for i in A:
            if count==0:
                count=count+1
                cand=i
            else:
                if cand==i:
                    count=count+1
                else:
                    count=count-1
        if count==0:
            return null
        else:
            if A.count(cand)>math.floor(len(A)/2):
                return cand
            else:
                return null
