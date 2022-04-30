import models

# Generación de modelos de malla
#Mesh 30
g    = models.mesh(10,3)
dot  = g.create_graphviz('Mesh_10x3')
g2 = g.bfs(0)
dot2 = g2.create_graphviz('Mesh_bfs_30')
dot2.render('Mesh_bfs_30','bfs', view=True)
g3 = g.dfs(0)
dot3 = g3.create_graphviz('Mesh_dfs_30')
dot3.render('Mesh_dfs_30','dfs', view=True)
g4 = g.dfs_r(0)
dot4 = g4.create_graphviz('Mesh_dfs_r_30')
dot4.render('Mesh_dfs_r_30','dfs_r',view=True)

#Mesh 100
g    = models.mesh(10,10)
dot  = g.create_graphviz('Mesh_10x10')
g2 = g.bfs(0)
dot = g2.create_graphviz('Mesh_bfs_100')
dot.render('Mesh_bfs_100','bfs', view=True)
g3 = g.dfs(0)
dot3 = g3.create_graphviz('Mesh_dfs_100')
dot3.render('Mesh_dfs_100','dfs', view=True)
g4 = g.dfs_r(0)
dot4 = g4.create_graphviz('Mesh_dfs_r_100')
dot4.render('Mesh_dfs_r_100','dfs_r', view=True)

# #Mesh 500
g    = models.mesh(50,10)
dot  = g.create_graphviz('Mesh_50x10')
g2 = g.bfs(0)
dot = g2.create_graphviz('Mesh_bfs_500')
dot.render('Mesh_bfs_500', view=True)
g3 = g.dfs(0)
dot3 = g3.create_graphviz('Mesh_dfs_500')
dot3.render('Mesh_dfs_500','dfs', view=True)
g4 = g.dfs_r(0)
dot4 = g4.create_graphviz('Mesh_dfs_r_500')
dot4.render('Mesh_dfs_r_500','dfs_r', view=True)


# # Generación de modelos de Erdos y Rengy
# Erdos 30
g    = models.erdos_rengy(30,45)
dot  = g.create_graphviz( 'Erdos_Rengy_30x45' )
g2 = g.bfs(0)
dot2 = g2.create_graphviz('Erdos_Rengy_bfs_30')
dot2.render('Erdos_Rengy_bfs_30','bfs', view=True)
g3 = g.dfs(0)
dot3 = g3.create_graphviz('Erdos_Rengy_dfs_30')
dot3.render('Erdos_Rengy_dfs_30','dfs', view=True)
g4 = g.dfs_r(0)
dot4 = g4.create_graphviz('Erdos_Rengy_dfs_r_30')
dot4.render('Erdos_Rengy_dfs_r_30','dfs_r',view=True)

# Erdos 100
g    = models.erdos_rengy(100,200)
dot  = g.create_graphviz('Erdos_Rengy_100x200')
g2 = g.bfs(0)
dot2 = g2.create_graphviz('Erdos_Rengy_bfs_100')
dot2.render('Erdos_Rengy_bfs_100','bfs', view=True)
g3 = g.dfs(0)
dot3 = g3.create_graphviz('Erdos_Rengy_dfs_100')
dot3.render('Erdos_Rengy_dfs_100','dfs', view=True)
g4 = g.dfs_r(0)
dot4 = g4.create_graphviz('Erdos_Rengy_dfs_r_100')
dot4.render('Erdos_Rengy_dfs_r_100','dfs_r',view=True)

# Erdos 500
g    = models.erdos_rengy(500,700)
dot  = g.create_graphviz('Erdos_Rengy_500x700')
g2 = g.bfs(0)
dot2 = g2.create_graphviz('Erdos_Rengy_bfs_500')
dot2.render('Erdos_Rengy_bfs_500','bfs', view=True)
g3 = g.dfs(0)
dot3 = g3.create_graphviz('Erdos_Rengy_dfs_500')
dot3.render('Erdos_Rengy_dfs_500','dfs', view=True)
g4 = g.dfs_r(0)
dot4 = g4.create_graphviz('Erdos_Rengy_dfs_r_500')
dot4.render('Erdos_Rengy_dfs_r_500','dfs_r',view=True)

# # Generación de modelos de Gilbert
# g    = models.gilbert(30,0.4,False,False)
# dot  = g.create_graphviz('Gilbert_30x0.4')
# g    = models.gilbert(100,0.3,False,False)
# dot  = g.create_graphviz('Gilbert_100x0.3')
# g    = models.gilbert(500,0.2,False,False)
# dot  = g.create_graphviz('Gilbert_500x0.2')

# # Generación de modelos de geográficos simples
# g    = models.geo_simple(30,0.3,False,False)
# dot  = g.create_graphviz('Geografico_Simple_30x0.8')
# g    = models.geo_simple(100,0.3,False,False)
# dot  = g.create_graphviz('Geografico_Simple_100x0.8')
# g    = models.geo_simple(500,0.3,False,False)
# dot  = g.create_graphviz('Geografico_Simple_500x0.8')

# # Generación de modelos de Barabasi
# g    = models.barabasi(30,20,False,False)
# dot  = g.create_graphviz('Barabasi_30x60')
# g    = models.barabasi(100,50,False,False)
# dot  = g.create_graphviz('Barabasi_100x50')
# g    = models.barabasi(500,20,False,False)
# dot  = g.create_graphviz('Barabasi_500x20')

# # Generación de modelos de Dorogovtsev-Mendes
# g    = models.dorogovtsev_mendes(30,False)
# dot  = g.create_graphviz('Dorogovtsev_Mendes_30')
# g    = models.dorogovtsev_mendes(100,False)
# dot  = g.create_graphviz('Dorogovtsev_Mendes_100')
# g    = models.dorogovtsev_mendes(500,False)
# dot  = g.create_graphviz('Dorogovtsev_Mendes_500')