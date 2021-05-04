# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 17:18:25 2021

@author: lenovo
"""
from line import line
size=7
number=6
infinite=99999
graph_matrix=[[0]*size for row in range(size)]
distance=[0]*size
def build(path_cost):
    for i in range(1,size):
        for j in range(1,size):
            if i==j:
                graph_matrix[i][j]=0
            else:
                graph_matrix[i][j]=infinite
    i=0
    while i<size:
        start_point=path_cost[i][0]
        end_point=path_cost[i][1]
        graph_matrix[start_point][end_point]=path_cost[i][2]
        i+=1
def shortestpath(vertex1,vertex_total):
    shortest_vertex=1
    goal=[0]*size
    for i in range(1,vertex_total+1):
        goal[i]=0
        distance[i]=graph_matrix[vertex1][i]
    goal[vertex1]=1
    distance[vertex1]=0
    print()
    for i in range(1,vertex_total+1):
        shortest_distance=infinite
        for j in range(1,vertex_total+1):
            if goal[j]==0 and shortest_distance>distance[j]:
                shortest_distance=distance[j]
                shortest_vertex=j
        goal[shortest_vertex]=1
        for j in range(vertex_total+1):
            if goal[j]==0 and \
                distance[shortest_vertex]+graph_matrix[shortest_vertex][j] \
                    <distance[j]:
                distance[j]=distance[shortest_vertex] \
                    +graph_matrix[shortest_vertex][j]
global path_cost
path_cost=[[1,2,29],[2,3,30],[2,4,35], \
           [3,5,28],[3,6,87],[4,5,42], \
           [4,6,75],[5,6,97]]
build(path_cost)
shortestpath(1, number)
line()
print("顶点1到各顶点的最短距离的结果:")
line()
for j in range(1,size):
    print("顶点1到顶点%2d的最短距离=%3d"%(j,distance[j]))
line()
print()