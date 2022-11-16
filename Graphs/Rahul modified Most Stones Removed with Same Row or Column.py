	# class Solution:
	# 	def removeStones(self, stones: List[List[int]]) -> int:
			
	# 		def remove_point(a,b):                           # Function to remove connected points from the ongoing graph. 
	# 			points.discard((a,b))
	# 			for y in x_dic[a]:
	# 				if (a,y) in points:
	# 					remove_point(a,y)

	# 			for x in y_dic[b]:
	# 				if (x,b) in points:
	# 					remove_point(x,b)

	# 		x_dic = defaultdict(list)
	# 		y_dic = defaultdict(list)
	# 		points= {(i,j) for i,j in stones}
			
	# 		for i,j in stones:                                # Construction of graph by x_coordinates and y_coordinates.
	# 			x_dic[i].append(j)
	# 			y_dic[j].append(i)

	# 		cnt = 0
	# 		for a,b in stones:                                # counting of distinct connected graph.
	# 			if (a,b) in points:
	# 				remove_point(a,b)
	# 				cnt+=1

	# 		return len(stones)-cnt



class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        points={(i,j) for i,j in stones}
        x_dict,y_dict=defaultdict(list),defaultdict(list)
        
        for i,j in stones:
            x_dict[i].append(j)
            y_dict[j].append(i)
        
        def remove_point(a,b):
            points.discard((a,b))
            for y in x_dict[a]:
                if (a,y) in points:
                    remove_point(a,y)
            for x in y_dict[b]:
                if (x,b) in points:
                    remove_point(x,b)
        cnt=0
        for a,b in stones:
            if (a,b) in points:
                remove_point(a,b)
                cnt+=1
        return len(stones)-cnt
        