# Project 1 - Graph generation and management library.
Project made by Omar Alejandro Linares Escobar for the subject "Design and Analysis of Algorithms".
## Objective of the project. 
Generate random graphs through 6 different methods, which are:
* Merge Method.
* Erdös & Rény Method.
* Gilbert Method.
* Simple Geographic Method.
* Barabási-Albert Method.
* Dorogovtsev-Mendes Method.

For each method, 3 different graphs were generated, which had 30, 100 and 500 nodes.  
Each graph generates a **.gv** file, which allowed to generate through Gephi, its corresponding **.png** image.

## How to test the project?
In order to correctly replicate the results obtained with this project, the following steps must be followed:
1. Download the files and store them in the same folder.
2. Run the code *graph* which will store the 18 graph files in a folder called *gv*.
3. Open each of the generated files in the *Gephi* software and export them in **.png** format.

## Functioning
* *vertex.py:* Code that generates the vertex class, which requires its identifier (id) as a parameter.
* *edge.py:* Code that generates the edge class, which requires the source vertex and the target vertex as parameters.
* *models.py:* In this code all the functions of the different six graph generation methods mentioned above are defined.
* *graph.py:* Code that generates the graph class, which requires the list of vertices and their corresponding edges.
* *main.py:* Finally, the code that allows generating at the user's will, the number of graphs with the model he chooses and their respective parameters.

## Results
The results obtained, which are the 18 **.png** images corresponding to the 18 **.gv** files obtained by 3 different tests for each of the 6 models, can be found at *gv/images/*.

# Project 2 - BFS and DFS algorithms.
Project made by Omar Alejandro Linares Escobar for the subject "Design and Analysis of Algorithms".
## Objective of the project. 
This second project improves the previous one by adding the opportunity to execute the BFS and DFS algorithms in any of the six graph generation methods, thus generating its .gv file and converting it into an image in a .pdf file.

# Project 3 - Dijkstra algorithm.
Project made by Omar Alejandro Linares Escobar for the subject "Design and Analysis of Algorithms".
## Objective of the project. 
This third project improves the previous one by adding the opportunity to execute the Dijkstra algorithm in any of the six graph generation methods, thus generating its .gv file and converting it into an image in a .jpg file by the use of Gephi software, restoring them in a new folder called dijkstra_graph.
