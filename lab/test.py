# def charStuf(flagbyte, escbyte, payload):
#     x=payload.replace(escbyte,escbyte*2)
#     y=x.replace(flagbyte, escbyte+flagbyte)
#     return flagbyte+y+flagbyte

# def destuff(flagbyte,escbyte,payload):
#     x=payload.replace(escbyte+flagbyte,flagbyte)
#     y=x.replace(escbyte*2,escbyte)
#     return y[1:-1]

# payload=input("payload : ")
# flagbyte=input("flagbyte : ")
# escbyte=input("escbyte : ")
# stuff=charStuf(flagbyte,escbyte,payload)
# print("stuff : ",stuff)
# print("destuff : ",destuff(flagbyte,escbyte,stuff))



# def bitStuff(pattern):
#     one_count=0
#     stuffed_pattern=[]
    
#     for bit in pattern:
#         stuffed_pattern.append(bit)
#         if bit=='1':
#             one_count+=1
#             if one_count == 5:
#                 stuffed_pattern.append('0')
#                 one_count=0
#         else:
#             one_count=0
#     return "".join(stuffed_pattern)

# def bitDestuff(stuffed_pattern):
#     one_count=0
#     destuffed_pattern=[]
    
#     i=0
#     while i<len(stuffed_pattern):
#         bit =stuffed_pattern[i]
#         destuffed_pattern.append(bit)
        
#         if bit=='1':
#             one_count+=1
#             if one_count==5:
#                 i+=1
#                 one_count=0
#         else:
#             one_count=0
#         i+=1
#     return "".join(destuffed_pattern)

# pattern=input("enter pattern : ")
# stuffed_pattern=bitStuff(pattern)
# destuffed_pattern = bitDestuff(stuffed_pattern)
# print("stuff : ",stuffed_pattern)
# print("destuff : ",destuffed_pattern)
        
        
import sys
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for col in range(self.V)] for row in range(self.V)]
        
    def printGraph(self,dist):
        print("Vertex \t Distance from Source")
        for i in range(self.V):
            print(f'{i}\t {dist[i]}')
            
    def minDistance(self,dist,setSpl):
        min=sys.maxsize
        min_index=-1
        
        for i in range(self.V):
            if dist[i]<min and not setSpl[i]:
                min=dist[i]
                min_index=i
                
        return min_index
    
    def dijskthra(self,src):
        dist=[sys.maxsize]*self.V
        dist[src]=0
        setSpl=[False]*self.V
        
        for count in range(self.V):
            u=self.minDistance(dist,setSpl)
            setSpl[u]=True
            
            for v in range(self.V):
                if(self.graph[u][v]>0 and not setSpl[v] and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
        
        self.printGraph(dist)
        
g=Graph(4)
g.graph=[
    [0, 1, 4, 0],
    [1, 0, 2, 6],
    [4, 2, 0, 3],
    [0, 6, 3, 0]
]

g.dijskthra(0)
