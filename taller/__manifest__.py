{
    'name': "Taller",
    'version': '1.0',
    'depends': ['base'],
    'author': "Juuxn",
    'category': 'Category',
    'description': """
    Description text
    """,
    'depends': ['sale'],
    "data": [
        "security/ir.model.access.csv",
        "views/taller_vehiculo_views.xml",
        "views/taller_marca_vehiculo_views.xml",
        "views/taller_pasajero_views.xml",
        "views/taller_vehiculo_hijo_views.xml"
    ],
    # data files containing optionally loaded demonstration data
    'demo': [

    ],
}
