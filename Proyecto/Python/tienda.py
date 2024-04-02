import sqlite3

conn = sqlite3.connect('Stock_ropa.db')
cursor = conn.cursor()
#* Ropa para hombres
cursor.execute('''CREATE TABLE IF NOT EXISTS productos_hombre
                (id INTEGER PRIMARY KEY, descripcion TEXT, valor_unitario INTEGER, unidades INTEGER, tallas_disponibles TEXT, colores_disponibles TEXT)''')
conn.commit()

productos_hombre = [
    ('Camiseta basica manga corta cuello redondo', 26000, 80000, 'XS, S, M, L, XL', 'Azul, Negro, Rojo, Blanco, Gris claro'),
    ('Sobrecamisa a cuadros manga larga', 120000, 13000, 'S, M, XL', 'Azul-Negro, Negro-Blanco, Rojo-Blanco, Negro-Gris, Gris-blanco'),
    ('Camiseta basica con estampado', 37500, 8000, 'XS, S, M', 'Azul, Negro, Gris oscuro, Blanco'),
    ('Jean cargo azul claro', 80000, 5000, '28, 30', 'Azul, Negro, Beige, Blanco'),
    ('Camiseta oversize manga corta con estamp ado al frente', 48000, 500, 'S, M', 'Azul oscuro, Negro, Blanco con lineas Negras, Rojo con diseño amarillo en las mangas'),
    ('Chaqueta bomber manga larga', 150000, 7000, 'XS, S, M, L, XL', 'Negro, verde oscuro, Azul oscuro, Camuflaje'),
    ('Chaqueta acolchada ', 165000, 2000, 'XS, S, M, L, XL', 'Azul, Negro, Camuflaje'),
    ('Camisa sport manga corta', 60000, 800, 'XS, S, M, L, XL', 'Verde Menta, Blanco, Azul cielo'),
    ('Buzo basico sin capota', 60000, 1000, 'XS, S, M', 'Gris claro, Blanco, Negro'),
    ('Buzo oversize con estampado en frente y capota', 80000, 5000, 'M, L', 'Azul, Negro, Blanco')
]

cursor.executemany('INSERT INTO productos_hombre (descripcion, valor_unitario, unidades, tallas_disponibles, colores_disponibles) VALUES (?,?,?,?,?)', productos_hombre)
conn.commit()
#* Ropa para mujeres
cursor.execute('''CREATE TABLE IF NOT EXISTS productos_mujer
                (id INTEGER PRIMARY KEY, descripcion TEXT, valor_unitario INTEGER, unidades INTEGER, tallas_disponibles TEXT, colores_disponibles TEXT)''')
conn.commit()

productos_mujer = [
    ('Blusa manga corta', 50000, 1000, 'XS, S, M, L', 'Azul Oscuro, Negro, Blanco, Gris claro, Azul claro'),
    ('Blusa camisera manga larga', 70000, 200, 'XS, S, M', 'Salmón, Blanco, Verde menta, Verde oscuro, Azul oscuro'),
    ('Blusa manga corta con cuello', 72000, 400, 'XS, S, M', 'Blanco, Verde oscuro, Azul oscuro'),
    ('Blusa manga corta con cuello', 72000, 400, 'XS, S, M', 'Blanco, Verde oscuro, Azul oscuro'),
    ('Camiseta crop top manga corta oversize', 26000, 1400, 'S, M, XL', 'Blanco, Verde Poscuro, Azul oscuro, Negro, Gris claro, Gris oscuro'),
    ('Camiseta manga corta con cuello redondo', 20000, 2600, 'XS, S, L', 'Blanco, Negro, Gris claro'),
    ('Camiseta oversize manga corta con diseño en el frente', 22000, 600, 'XS, S', 'Salmón, Blanco, Negro, Azul'),
    ('Chaqueta de jean oversize con bolsillos', 100000, 2100, 'S, M, L', 'Negro'),
    ('Jean con rotos delanteros', 80000, 2500, '14, 16, 18', 'Azul claro'),
    ('Pantalón jogger con bolsillos', 80000, 420, '8, 10, 12', 'Negro, Beige')
]

cursor.executemany('INSERT INTO productos_mujer (descripcion, valor_unitario, unidades, tallas_disponibles, colores_disponibles) VALUES (?,?,?,?,?)', productos_mujer)
conn.commit()

conn.close()