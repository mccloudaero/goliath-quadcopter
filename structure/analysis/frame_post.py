#!/usr/bin/python
import numpy as np

# Read input file
input_data = list() 
input_file = open('template.3dd','r')
for line in input_file:
 if (line[0] != '#'):
  line_clean = line.strip()
  if len(line_clean) != 0:
   input_data.append(line_clean)
input_file.close()

# Process input file
# Nodes
nodes = list()
num_nodes = int(input_data[0].split()[0])
print 'Number of Nodes:',num_nodes
for i in range(1,num_nodes+1):
 node_data = input_data[i].split()[:5]
 nodes.append([int(node_data[0]),float(node_data[1]),float(node_data[2]),float(node_data[3]),float(node_data[4])])
# Note:
# Nodes are sorted since they don't have to be sorted in input
nodes = sorted(nodes)

# Node Reactions
node_reactions = list()
num_node_reactions = int(input_data[num_nodes+1].split()[0])
print 'Number of Node Reactions:',num_node_reactions 
for i in range(num_nodes+2,num_nodes+num_node_reactions+2):
 node_reactions.append(input_data[i].split()[:7])
#print node_reactions

# Elements
elements = list()
num_elements = int(input_data[num_nodes+num_node_reactions+2].split()[0])
print 'Number of Elements:',num_elements
for i in range(num_nodes+num_node_reactions+3,num_nodes+num_node_reactions+num_elements+3):
 elements.append(input_data[i].split()[:13])
#print elements

# Compute element lengths
wide_length = 0
wide_area = 0.1261
narrow_length = 0

for i in range(num_elements):
 elem = elements[i]
 start_node = int(elem[1])-1
 end_node = int(elem[2])-1
 area = float(elem[3])
 start_xyz = nodes[start_node][1:4]
 end_xyz = nodes[end_node][1:4]
 delta_xyz = [end_xyz[0]-start_xyz[0],end_xyz[1]-start_xyz[1],end_xyz[2]-start_xyz[2]]
 length = np.linalg.norm(delta_xyz)
 print i,start_node,delta_xyz,length
 if area == wide_area:
  wide_length += length 
 else:
  narrow_length += length

print 'Total Length of Wide Tubing:',wide_length,'in',wide_length/12.0,'ft'
print 'Total Length of Narrow Tubing:',narrow_length,'in',narrow_length/12.0,'ft'
