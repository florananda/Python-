class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
         if A==0 or B==0:
             if A==0:
                 return B
             else:
                 if B==0:
                     return A
         if   A==B:
            return A
         while B!=0:
             r = A % B;
             A = B;
             B = r;
         return A
    
