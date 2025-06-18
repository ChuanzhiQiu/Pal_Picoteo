import streamlit as st
from supabase import create_client, Client

# Configuración de Supabase
SUPABASE_URL = "https://vnyzlqzwpexpfbdstsvb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZueXpscXp3cGV4cGZiZHN0c3ZiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAxODU3MzAsImV4cCI6MjA2NTc2MTczMH0.dIWJwc5Ij2B5PiahMQyELYRfH4CexarlrgFQGN9uvJo"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("Pal Picoteo - Ingreso de Datos")

menu = ["Cliente", "Venta", "Stock", "Gasto", "Merma", "Encargo", "Promoción"]
opcion = st.sidebar.selectbox("Selecciona la operación:", menu)

if opcion == "Cliente":
    st.subheader("Formulario de Ingreso de Cliente")
    nombre = st.text_input("Nombre")
    telefono = st.text_input("Teléfono")
    email = st.text_input("Email")
    direccion = st.text_input("Dirección")
    notas = st.text_area("Notas (opcional)")
    if st.button("Guardar Cliente"):
        if nombre != "":
            data = {"nombre": nombre, "telefono": telefono, "email": email, "direccion": direccion, "notas": notas}
            supabase.table("clientes").insert(data).execute()
            st.success("Cliente ingresado correctamente ✅")
        else:
            st.warning("El campo Nombre es obligatorio.")

elif opcion == "Venta":
    st.subheader("Formulario de Ingreso de Venta")
    fecha = st.date_input("Fecha")
    producto = st.text_input("Producto")
    cantidad = st.number_input("Cantidad", min_value=1, step=1)
    precio_unitario = st.number_input("Precio unitario", min_value=0.0)
    metodo_pago = st.text_input("Método de pago")
    cliente_id = st.text_input("ID Cliente (opcional)")
    if st.button("Guardar Venta"):
        total_venta = cantidad * precio_unitario
        data = {"fecha": fecha.strftime("%Y-%m-%d"), "producto": producto, "cantidad": cantidad, "precio_unitario": precio_unitario, "total_venta": total_venta, "metodo_pago": metodo_pago, "cliente_id": int(cliente_id) if cliente_id else None}
        supabase.table("ventas").insert(data).execute()
        st.success("Venta ingresada correctamente ✅")

elif opcion == "Stock":
    st.subheader("Formulario de Ingreso de Stock")
    fecha_ingreso = st.date_input("Fecha ingreso")
    producto = st.text_input("Producto")
    cantidad = st.number_input("Cantidad", min_value=1, step=1)
    precio_compra_unit = st.number_input("Precio compra unitario", min_value=0.0)
    proveedor = st.text_input("Proveedor")
    observaciones = st.text_area("Observaciones")
    if st.button("Guardar Stock"):
        data = {"fecha_ingreso": fecha_ingreso.strftime("%Y-%m-%d"), "producto": producto, "cantidad": cantidad, "precio_compra_unit": precio_compra_unit, "proveedor": proveedor, "observaciones": observaciones}
        supabase.table("stock").insert(data).execute()
        st.success("Stock ingresado correctamente ✅")

elif opcion == "Gasto":
    st.subheader("Formulario de Ingreso de Gasto")
    fecha = st.date_input("Fecha")
    categoria = st.text_input("Categoría")
    monto = st.number_input("Monto", min_value=0.0)
    descripcion = st.text_area("Descripción")
    if st.button("Guardar Gasto"):
        data = {"fecha": fecha.strftime("%Y-%m-%d"), "categoria": categoria, "monto": monto, "descripcion": descripcion}
        supabase.table("gastos").insert(data).execute()
        st.success("Gasto ingresado correctamente ✅")

elif opcion == "Merma":
    st.subheader("Formulario de Ingreso de Merma")
    fecha = st.date_input("Fecha")
    producto = st.text_input("Producto")
    cantidad = st.number_input("Cantidad", min_value=1, step=1)
    motivo = st.text_input("Motivo")
    observaciones = st.text_area("Observaciones")
    if st.button("Guardar Merma"):
        data = {"fecha": fecha.strftime("%Y-%m-%d"), "producto": producto, "cantidad": cantidad, "motivo": motivo, "observaciones": observaciones}
        supabase.table("mermas").insert(data).execute()
        st.success("Merma ingresada correctamente ✅")

elif opcion == "Encargo":
    st.subheader("Formulario de Ingreso de Encargo")
    cliente_id = st.number_input("ID Cliente", min_value=1, step=1)
    producto = st.text_input("Producto")
    cantidad = st.number_input("Cantidad", min_value=1, step=1)
    fecha_entrega = st.date_input("Fecha entrega")
    estado = st.selectbox("Estado", ["Pendiente", "Confirmado", "Entregado"])
    notas = st.text_area("Notas")
    if st.button("Guardar Encargo"):
        data = {"cliente_id": cliente_id, "producto": producto, "cantidad": cantidad, "fecha_entrega": fecha_entrega.strftime("%Y-%m-%d"), "estado": estado, "notas": notas}
        supabase.table("encargos").insert(data).execute()
        st.success("Encargo ingresado correctamente ✅")

elif opcion == "Promoción":
    st.subheader("Formulario de Ingreso de Promoción")
    nombre = st.text_input("Nombre")
    descripcion = st.text_area("Descripción")
    fecha_inicio = st.date_input("Fecha inicio")
    fecha_fin = st.date_input("Fecha fin")
    descuento_aplicado = st.number_input("Descuento aplicado (%)", min_value=0.0)
    if st.button("Guardar Promoción"):
        data = {"nombre": nombre, "descripcion": descripcion, "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d"), "fecha_fin": fecha_fin.strftime("%Y-%m-%d"), "descuento_aplicado": descuento_aplicado}
        supabase.table("promociones").insert(data).execute()
        st.success("Promoción ingresada correctamente ✅")