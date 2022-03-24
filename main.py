import models

# Generación de modelos de malla
g    = models.mesh(10,3)
dot  = g.create_graphviz('Mesh_10x3')
g    = models.mesh(10,10)
dot  = g.create_graphviz('Mesh_10x10')
g    = models.mesh(50,10)
dot  = g.create_graphviz('Mesh_50x10')

# Generación de modelos de Erdos y Rengy
g    = models.erdos_rengy(30,45)
dot  = g.create_graphviz( 'Erdos_Rengy_30x45' )
g    = models.erdos_rengy(100,200)
dot  = g.create_graphviz('Erdos_Rengy_100x200')
g    = models.erdos_rengy(500,700)
dot  = g.create_graphviz('Erdos_Rengy_500x700')

# Generación de modelos de Gilbert
g    = models.gilbert(30,0.4,False,False)
dot  = g.create_graphviz('Gilbert_30x0.4')
g    = models.gilbert(100,0.3,False,False)
dot  = g.create_graphviz('Gilbert_100x0.3')
g    = models.gilbert(500,0.2,False,False)
dot  = g.create_graphviz('Gilbert_500x0.2')

# Generación de modelos de geográficos simples
g    = models.geo_simple(30,0.3,False,False)
dot  = g.create_graphviz('Geografico_Simple_30x0.8')
g    = models.geo_simple(100,0.3,False,False)
dot  = g.create_graphviz('Geografico_Simple_100x0.8')
g    = models.geo_simple(500,0.3,False,False)
dot  = g.create_graphviz('Geografico_Simple_500x0.8')

# Generación de modelos de Barabasi
g    = models.barabasi(30,20,False,False)
dot  = g.create_graphviz('Barabasi_30x60')
g    = models.barabasi(100,50,False,False)
dot  = g.create_graphviz('Barabasi_100x50')
g    = models.barabasi(500,20,False,False)
dot  = g.create_graphviz('Barabasi_500x20')

# Generación de modelos de Dorogovtsev-Mendes
g    = models.dorogovtsev_mendes(30,False)
dot  = g.create_graphviz('Dorogovtsev_Mendes_30')
g    = models.dorogovtsev_mendes(100,False)
dot  = g.create_graphviz('Dorogovtsev_Mendes_100')
g    = models.dorogovtsev_mendes(500,False)
dot  = g.create_graphviz('Dorogovtsev_Mendes_500')