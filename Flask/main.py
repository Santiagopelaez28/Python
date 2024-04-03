from flask import Flask, render_template


app = Flask(__name__)

class ropa_hombre:
    def __init__(self, descripcion, precio_unitario, en_stock, tallas_disponibles, colores_disponibles, imagen):
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.en_stock = en_stock
        self.tallas_disponibles = tallas_disponibles
        self.colores_disponibles = colores_disponibles
        self.imagen = imagen
    
    def mostrar_ps(self):
        return f"Descripción: {self.descripcion}, Precio: {self.precio_unitario}, En Stock: {self.en_stock}, Tallas Disponibles: {self.tallas_disponibles}, Colores Disponibles: {self.colores_disponibles}"


ph1 = ropa_hombre('Camiseta basica manga corta cuello redondo', 26000, 80000, 'XS, S, M, L, XL', 'Azul, Negro, Rojo, Blanco, Gris claro', 'https://http2.mlstatic.com/D_NQ_NP_666578-MCO75312676396_032024-O.webp')
ph2 = ropa_hombre('Sobrecamisa a cuadros manga larga', 120000, 13000, 'S, M, XL', 'Azul-Negro, Negro-Blanco, Rojo-Blanco, Negro-Gris, Gris-blanco', 'https://static.bershka.net/4/photos2/2024/V/0/2/p/1631/228/060//01/f51f82f83486ada4a00586a45efa3363-1631228060_1_1_0.jpg?imwidth=850&impolicy=bershka-itxmediumhigh&imformat=chrome')
ph3 = ropa_hombre('Camiseta basica con estampado', 37500, 8000, 'XS, S, M', 'Azul, Negro, Gris oscuro, Blanco', 'https://m.media-amazon.com/images/I/61FuG5X6PCL._AC_UY1000_.jpg')
ph4 = ropa_hombre('Jean cargo', 80000, 5000, '28, 30', 'Azul, Negro, Beige, Blanco', 'https://colombia.bioweb.co/cdn/shop/products/azul.jpg?v=1553787125')
ph5 = ropa_hombre('Camiseta oversize manga corta con estampado al frente', 48000, 500, 'S, M', 'Azul oscuro, Negro, Beige, Blanco con lineas Negras, Rojo con diseño amarillo en las mangas', 'https://cdn.koaj.co/194504-big_default/camiseta-oversize-para-hombre-con-estampado-frente-y-espalda-urbana.jpg')
ph6 = ropa_hombre('Chaqueta bomber manga larga', 150000, 7000, 'XS, S, M, L, XL', 'Negro, verde oscuro, Azul oscuro, Camuflaje', 'https://cdn.koaj.co/214405-big_default/chaqueta-bomber-tipo-college-unicolor-para-hombre-manga-larga-cuello-punos-y-bajos-con-rectilineo-bolsillos-de-ribete-por-costa.jpg')
ph7 = ropa_hombre('Chaqueta acolchada ', 165000, 2000, 'XS, S, M, L, XL', 'Azul, Negro, Camuflaje', 'https://http2.mlstatic.com/D_NQ_NP_936156-CBT50428573501_062022-O.webp')
ph8 = ropa_hombre('Camisa tipo sport manga corta', 60000, 800, 'XS, S, M, L, XL', 'Verde Menta, Blanco, Azul cielo', 'https://camiseriainglesa.vteximg.com.br/arquivos/ids/197264-435-528/13173-camisa-sport-hombre-unicolor-verde-1.jpg?v=638350680822270000')
ph9 = ropa_hombre('Buzo basico sin capota', 60000, 1000, 'XS, S, M', 'Gris claro, Blanco, Negro, Verde oscuro','https://tienda.utp.edu.co/wp-content/uploads/2022/09/buzo-verde-unisex-somos-uno-4-1.jpg')
ph10 = ropa_hombre('Buzo oversize con estampado en frente y capota', 80000, 5000, 'M, L', 'Azul, Negro, Blanco', 'https://cdn.koaj.co/188269-big_default/buzo-capota-blanco-con-estampado-en-frente-estilo-college.jpg')


ph1.mostrar_ps()
ph2.mostrar_ps()
ph3.mostrar_ps()
ph4.mostrar_ps()
ph5.mostrar_ps()
ph6.mostrar_ps()
ph7.mostrar_ps()
ph8.mostrar_ps()
ph9.mostrar_ps()
ph10.mostrar_ps()

class ropa_mujer:
    def __init__(self, descripcion, precio_unitario, en_stock, tallas_disponibles, colores_disponibles, imagen):
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.en_stock = en_stock
        self.tallas_disponibles = tallas_disponibles
        self.colores_disponibles = colores_disponibles
        self.imagen = imagen
    
    def mostrar_ps(self):
        return f"Descripción: {self.descripcion}, Precio: {self.precio_unitario}, En Stock: {self.en_stock}, Tallas Disponibles: {self.tallas_disponibles}, Colores Disponibles: {self.colores_disponibles}"


pm1 = ropa_mujer('Blusa manga corta', 50000, 1000, 'XS, S, M, L', 'Azul Oscuro, Negro, Blanco, Gris claro, Azul claro', 'https://quest.vtexassets.com/arquivos/ids/442485-800-auto?v=638370499439030000&width=800&height=auto&aspect=true')
pm2 = ropa_mujer('Blusa camisera manga larga', 70000, 200, 'XS, S, M', 'Salmón, Blanco, Verde menta, Verde oscuro, Azul oscuro', 'https://leclee.com.co/cdn/shop/products/209B_1.webp?v=1672854805')
pm3 = ropa_mujer('Blusa manga corta con cuello', 72000, 400, 'XS, S, M', 'Blanco, Verde oscuro, Azul oscuro','https://cdn.koaj.co/125737-big_default/blusa-en-tela-fluida-unicolor-manga-corta-cuello-camisero-silueta-oversize.jpg')
pm4 = ropa_mujer('Camiseta crop top manga corta oversize', 26000, 1400, 'S, M, XL', 'Blanco, Verde Poscuro, Azul oscuro, Negro, Gris claro, Gris oscuro', 'https://oneillco.vtexassets.com/arquivos/ids/164992/camiseta-mujer-blanco-1N00118-0002-2.jpg?v=638005077216870000')
pm5 = ropa_mujer('Camiseta manga corta con cuello redondo', 20000, 2600, 'XS, S, L', 'Blanco, Negro, Gris claro', 'https://cdn.koaj.co/176615-thickbox_default/camiseta-manga-corta-cuello-redondo-para-mujer-estampada-en-frente-estilo-college.jpg')
pm6 = ropa_mujer('Camiseta oversize manga corta con diseño en el frente', 22000, 600, 'XS, S', 'Salmón, Blanco, Negro, Azul', 'https://cdn.koaj.co/193637-big_default/camiseta-femenina-hombro-rodado-manga-corta-con-estampado-en-frente-de-la-pantera-rosa.jpg')
pm7 = ropa_mujer('Chaqueta de jean oversize con bolsillos', 100000, 2100, 'S, M, L', 'Negro', 'https://cdn.koaj.co/202783-big_default/chaqueta-jean-oversize.jpg')
pm8 = ropa_mujer('Jean con rotos delanteros', 80000, 2500, '14, 16, 18', 'Azul claro', 'https://i0.wp.com/img.ltwebstatic.com/images3_pi/2021/12/07/1638855961b38d33d41548d2340e4f37e6a4f951a9.webp?fit=1340%2C1785&ssl=1')
pm9 = ropa_mujer('Pantalón jogger con bolsillos', 80000, 420, '8, 10, 12', 'Negro, Beige', 'https://dyaboo.com/cdn/shop/files/JCCARO_1024x1024.webp?v=1692802070')


pm1.mostrar_ps()
pm2.mostrar_ps()
pm3.mostrar_ps()
pm4.mostrar_ps()
pm5.mostrar_ps()
pm6.mostrar_ps()
pm7.mostrar_ps()
pm8.mostrar_ps()
pm9.mostrar_ps()


@app.route('/')

def index():
    prendas_hombre = [ph1, ph2, ph3, ph4, ph5, ph6, ph7, ph8, ph9, ph10]
    prendas_mujer = [ph1, ph2, ph3, ph4, ph5, ph6, ph7, ph8, ph9]
    return render_template('index.html', prendas_hombre = prendas_hombre, 
                                        prendas_mujer = prendas_mujer)

if __name__ == '__main__':
    app.run()
