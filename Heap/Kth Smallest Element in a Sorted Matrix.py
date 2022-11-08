# whenever you see a 'k' problem, recall thy H E A P
# Inside nested for loops just simply append all the elements which is a O( 1 ) operation. 
# Rather than using heappush which is a O( logn ) operation. 
# your time complexity in worst case is going to O( (n ^ 2) * logn ). Just slight adjustments.

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        size = len( matrix )

        # store all the elements in the minHeap
        for i in range( size ) :
            for j in range( size ) :
                minHeap.append( matrix[ i ][ j ] )
                
        # heapify
        heapq.heapify( minHeap ) # time O( n )

        while k > 1 :
            heapq.heappop( minHeap )
            k -= 1
        return minHeap[ 0 ]
