import sqlite3
import supabase_export
from supabase import create_client, Client

# Reemplaza con tus valores reales de Supabase
SUPABASE_URL = "https://vnyzlqzwpexpfbdstsvb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZueXpscXp3cGV4cGZiZHN0c3ZiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAxODU3MzAsImV4cCI6MjA2NTc2MTczMH0.dIWJwc5Ij2B5PiahMQyELYRfH4CexarlrgFQGN9uvJo"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def menu():
    while True:
        print("\n¿Qué deseas ingresar?")
        print("1. Cliente")
        print("2. Venta")
        print("3. Stock")
        print("4. Gasto")
        print("5. Merma")
        print("6. Encargo")
        print("7. Promoción")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ingresar_cliente()
        elif opcion == "2":
            ingresar_venta()
        elif opcion == "3":
            ingresar_stock()
        elif opcion == "4":
            ingresar_gasto()
        elif opcion == "5":
            ingresar_merma()
        elif opcion == "6":
            ingresar_encargo()
        elif opcion == "7":
            ingresar_promocion()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

def ingresar_cliente():
    print("\n--- Ingreso de Cliente ---")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    direccion = input("Dirección: ")
    notas = input("Notas (opcional): ")
    data = {"nombre": nombre, "telefono": telefono, "email": email, "direccion": direccion, "notas": notas}
    supabase.table("clientes").insert(data).execute()
    print("Cliente ingresado correctamente.")

def ingresar_venta():
    print("\n--- Ingreso de Venta ---")
    fecha = input("Fecha (YYYY-MM-DD): ")
    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))
    precio_unitario = float(input("Precio unitario: "))
    metodo_pago = input("Método de pago: ")
    cliente_id = input("ID Cliente (opcional): ")
    cliente_id = int(cliente_id) if cliente_id else None
    total_venta = cantidad * precio_unitario
    data = {"fecha": fecha, "producto": producto, "cantidad": cantidad, "precio_unitario": precio_unitario, "total_venta": total_venta, "metodo_pago": metodo_pago, "cliente_id": cliente_id}
    supabase.table("ventas").insert(data).execute()
    print("Venta ingresada correctamente.")

def ingresar_stock():
    print("\n--- Ingreso de Stock ---")
    fecha_ingreso = input("Fecha ingreso (YYYY-MM-DD): ")
    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio compra unitario: "))
    proveedor = input("Proveedor: ")
    observaciones = input("Observaciones: ")
    data = {"fecha_ingreso": fecha_ingreso, "producto": producto, "cantidad": cantidad, "precio_compra_unit": precio, "proveedor": proveedor, "observaciones": observaciones}
    supabase.table("stock").insert(data).execute()
    print("Stock ingresado correctamente.")

def ingresar_gasto():
    print("\n--- Ingreso de Gasto ---")
    fecha = input("Fecha (YYYY-MM-DD): ")
    categoria = input("Categoría: ")
    monto = float(input("Monto: "))
    descripcion = input("Descripción: ")
    data = {"fecha": fecha, "categoria": categoria, "monto": monto, "descripcion": descripcion}
    supabase.table("gastos").insert(data).execute()
    print("Gasto ingresado correctamente.")

def ingresar_merma():
    print("\n--- Ingreso de Merma ---")
    fecha = input("Fecha (YYYY-MM-DD): ")
    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))
    motivo = input("Motivo: ")
    observaciones = input("Observaciones: ")
    data = {"fecha": fecha, "producto": producto, "cantidad": cantidad, "motivo": motivo, "observaciones": observaciones}
    supabase.table("mermas").insert(data).execute()
    print("Merma ingresada correctamente.")

def ingresar_encargo():
    print("\n--- Ingreso de Encargo ---")
    cliente_id = int(input("ID Cliente: "))
    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))
    fecha_entrega = input("Fecha entrega (YYYY-MM-DD): ")
    estado = input("Estado (Pendiente/Confirmado/Entregado): ")
    notas = input("Notas: ")
    data = {"cliente_id": cliente_id, "producto": producto, "cantidad": cantidad, "fecha_entrega": fecha_entrega, "estado": estado, "notas": notas}
    supabase.table("encargos").insert(data).execute()
    print("Encargo ingresado correctamente.")

def ingresar_promocion():
    print("\n--- Ingreso de Promoción ---")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
    descuento = float(input("Descuento aplicado: "))
    data = {"nombre": nombre, "descripcion": descripcion, "fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin, "descuento_aplicado": descuento}
    supabase.table("promociones").insert(data).execute()
    print("Promoción ingresada correctamente.")

menu()
