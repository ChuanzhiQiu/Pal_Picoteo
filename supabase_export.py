from supabase import create_client, Client

# Reemplaza con tus valores reales de Supabase
SUPABASE_URL = "https://vnyzlqzwpexpfbdstsvb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZueXpscXp3cGV4cGZiZHN0c3ZiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAxODU3MzAsImV4cCI6MjA2NTc2MTczMH0.dIWJwc5Ij2B5PiahMQyELYRfH4CexarlrgFQGN9uvJo"

# Crear cliente Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------------- CLIENTES ----------------------
def insertar_cliente(nombre, telefono, email, direccion, notas):
    data = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "notas": notas
    }
    respuesta = supabase.table("Clientes").insert(data).execute()
    print("[✔] Cliente agregado:", respuesta)

# ---------------------- VENTAS ----------------------
def insertar_venta(fecha, producto, cantidad, precio_unitario, metodo_pago, cliente_id=None):
    total = cantidad * precio_unitario
    data = {
        "fecha": fecha,
        "producto": producto,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total_venta": total,
        "metodo_pago": metodo_pago,
        "cliente_id": cliente_id
    }
    respuesta = supabase.table("Ventas").insert(data).execute()
    print("[✔] Venta agregada:", respuesta)

# ---------------------- STOCK ----------------------
def insertar_stock(fecha_ingreso, producto, cantidad, precio_compra_unit, proveedor, observaciones):
    data = {
        "fecha_ingreso": fecha_ingreso,
        "producto": producto,
        "cantidad": cantidad,
        "precio_compra_unit": precio_compra_unit,
        "proveedor": proveedor,
        "observaciones": observaciones
    }
    respuesta = supabase.table("Stock").insert(data).execute()
    print("[✔] Stock agregado:", respuesta)

# ---------------------- GASTOS ----------------------
def insertar_gasto(fecha, categoria, monto, descripcion):
    data = {
        "fecha": fecha,
        "categoria": categoria,
        "monto": monto,
        "descripcion": descripcion
    }
    respuesta = supabase.table("Gastos").insert(data).execute()
    print("[✔] Gasto agregado:", respuesta)

# ---------------------- MERMAS ----------------------
def insertar_merma(fecha, producto, cantidad, motivo, observaciones):
    data = {
        "fecha": fecha,
        "producto": producto,
        "cantidad": cantidad,
        "motivo": motivo,
        "observaciones": observaciones
    }
    respuesta = supabase.table("Mermas").insert(data).execute()
    print("[✔] Merma registrada:", respuesta)

# ---------------------- ENCARGOS ----------------------
def insertar_encargo(cliente_id, producto, cantidad, fecha_entrega, estado, notas):
    data = {
        "cliente_id": cliente_id,
        "producto": producto,
        "cantidad": cantidad,
        "fecha_entrega": fecha_entrega,
        "estado": estado,
        "notas": notas
    }
    respuesta = supabase.table("Encargos").insert(data).execute()
    print("[✔] Encargo ingresado:", respuesta)

# ---------------------- PROMOCIONES ----------------------
def insertar_promocion(nombre, descripcion, fecha_inicio, fecha_fin, descuento_aplicado):
    data = {
        "nombre": nombre,
        "descripcion": descripcion,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "descuento_aplicado": descuento_aplicado
    }
    respuesta = supabase.table("Promociones").insert(data).execute()
    print("[✔] Promoción registrada:", respuesta)

# ---------------------- EJEMPLOS DE USO ----------------------
# insertar_cliente("Luis Torres", "+56911112222", "luis@correo.com", "Calle 8", "Sin notas")
# insertar_venta("2025-06-17", "Queso Gouda", 2, 6500, "Transferencia", 1)
# insertar_stock("2025-06-17", "Queso Azul", 10, 4500, "Proveedor X", "Lote nuevo")
# insertar_gasto("2025-06-16", "Transporte", 8000, "Flete desde Quilpué")
# insertar_merma("2025-06-15", "Brie", 2, "Vencido", "Temperatura mal controlada")
# insertar_encargo(1, "Queso Brie", 3, "2025-06-20", "Pendiente", "Entrega sábado")
# insertar_promocion("Pack 3 Quesos", "Mix gourmet", "2025-06-10", "2025-06-30", 15.0)
