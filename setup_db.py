import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect("pal_picoteo.db")
cursor = conn.cursor()

# Activar claves foráneas
cursor.execute("PRAGMA foreign_keys = ON")

# Crear tabla Clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT,
    email TEXT,
    direccion TEXT,
    notas TEXT
)
''')

# Crear tabla Ventas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Ventas (
    id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    producto TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    total_venta REAL NOT NULL,
    metodo_pago TEXT,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id_cliente)
)
''')

# Crear tabla Stock
cursor.execute('''
CREATE TABLE IF NOT EXISTS Stock (
    id_stock INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_ingreso TEXT NOT NULL,
    producto TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_compra_unit REAL,
    proveedor TEXT,
    observaciones TEXT
)
''')

# Crear tabla Gastos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Gastos (
    id_gasto INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    categoria TEXT NOT NULL,
    monto REAL NOT NULL,
    descripcion TEXT
)
''')

# Crear tabla Mermas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Mermas (
    id_merma INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    producto TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    motivo TEXT,
    observaciones TEXT
)
''')

# Crear tabla Encargos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Encargos (
    id_encargo INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    producto TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha_entrega TEXT NOT NULL,
    estado TEXT,
    notas TEXT,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id_cliente)
)
''')

# Crear tabla Promociones
cursor.execute('''
CREATE TABLE IF NOT EXISTS Promociones (
    id_promocion INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    fecha_inicio TEXT NOT NULL,
    fecha_fin TEXT NOT NULL,
    descuento_aplicado REAL
)
''')

# Guardar y cerrar conexión
conn.commit()
conn.close()
