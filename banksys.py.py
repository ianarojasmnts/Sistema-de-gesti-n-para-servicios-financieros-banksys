import tkinter as tk
from tkinter import ttk

# Crear ventana principal
root = tk.Tk()
root.geometry("900x500")
root.title("BankSys - Sistema Financiero")

# Crear pestañas
notebook = ttk.Notebook(root)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)

notebook.add(tab1, text="Clientes")
notebook.add(tab2, text="Cuentas")
notebook.add(tab3, text="Créditos")
notebook.add(tab4, text="Transacciones")

notebook.pack(expand=True, fill="both")


# PESTAÑA 1 CLIENTES


titulo = tk.Label(tab1, text="FORMULARIO CLIENTES",
                  font=("Arial", 16, "bold"), fg="blue")
titulo.pack(pady=20)

form_frame = tk.Frame(tab1)
form_frame.pack(pady=10, padx=50, anchor="w")

tk.Label(form_frame, text="Código Cliente:").grid(row=0, column=0, pady=5)
codigo = tk.Entry(form_frame)
codigo.grid(row=0, column=1)

tk.Label(form_frame, text="Tipo Cliente:").grid(row=1, column=0, pady=5)
tipo = tk.Entry(form_frame)
tipo.grid(row=1, column=1)

tk.Label(form_frame, text="Nombre / Razón Social:").grid(row=2, column=0, pady=5)
nombre = tk.Entry(form_frame)
nombre.grid(row=2, column=1)

tk.Label(form_frame, text="Documento:").grid(row=3, column=0, pady=5)
documento = tk.Entry(form_frame)
documento.grid(row=3, column=1)

tk.Label(form_frame, text="Teléfono:").grid(row=4, column=0, pady=5)
telefono = tk.Entry(form_frame)
telefono.grid(row=4, column=1)

tk.Label(form_frame, text="Correo:").grid(row=5, column=0, pady=5)
correo = tk.Entry(form_frame)
correo.grid(row=5, column=1)

# Botones
btn_frame = tk.Frame(tab1)
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Guardar", bg="green", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Actualizar", bg="blue", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Eliminar", bg="red", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Limpiar", bg="orange").pack(side=tk.LEFT, padx=5)



# PESTAÑA 2 CUENTAS


titulo2 = tk.Label(tab2, text="FORMULARIO CUENTAS BANCARIAS",
                   font=("Arial", 16, "bold"), fg="green")
titulo2.pack(pady=20)

form_frame = tk.Frame(tab2)
form_frame.pack(pady=10, padx=50, anchor="w")

tk.Label(form_frame, text="Número Cuenta:").grid(row=0, column=0, pady=5)
cuenta = tk.Entry(form_frame)
cuenta.grid(row=0, column=1)

tk.Label(form_frame, text="Tipo Cuenta:").grid(row=1, column=0, pady=5)
tipo_cuenta = tk.Entry(form_frame)
tipo_cuenta.grid(row=1, column=1)

tk.Label(form_frame, text="Moneda:").grid(row=2, column=0, pady=5)
moneda = tk.Entry(form_frame)
moneda.grid(row=2, column=1)

tk.Label(form_frame, text="Sucursal:").grid(row=3, column=0, pady=5)
sucursal = tk.Entry(form_frame)
sucursal.grid(row=3, column=1)

tk.Label(form_frame, text="Saldo Actual:").grid(row=4, column=0, pady=5)
saldo = tk.Entry(form_frame)
saldo.grid(row=4, column=1)

tk.Label(form_frame, text="Estado:").grid(row=5, column=0, pady=5)
estado = tk.Entry(form_frame)
estado.grid(row=5, column=1)



# PESTAÑA 3 CRÉDITOS


titulo3 = tk.Label(tab3, text="GESTIÓN DE CRÉDITOS",
                   font=("Arial", 16, "bold"), fg="red")
titulo3.pack(pady=20)

form_frame = tk.Frame(tab3)
form_frame.pack(pady=10, padx=50, anchor="w")

tk.Label(form_frame, text="Número Operación:").grid(row=0, column=0, pady=5)
operacion = tk.Entry(form_frame)
operacion.grid(row=0, column=1)

tk.Label(form_frame, text="Monto Aprobado:").grid(row=1, column=0, pady=5)
monto = tk.Entry(form_frame)
monto.grid(row=1, column=1)

tk.Label(form_frame, text="Plazo (meses):").grid(row=2, column=0, pady=5)
plazo = tk.Entry(form_frame)
plazo.grid(row=2, column=1)

tk.Label(form_frame, text="Tasa Interés:").grid(row=3, column=0, pady=5)
interes = tk.Entry(form_frame)
interes.grid(row=3, column=1)

tk.Label(form_frame, text="Estado Crédito:").grid(row=4, column=0, pady=5)
estado_credito = tk.Entry(form_frame)
estado_credito.grid(row=4, column=1)



# PESTAÑA 4 TRANSACCIONES


titulo4 = tk.Label(tab4, text="TRANSACCIONES FINANCIERAS",
                   font=("Arial", 16, "bold"), fg="purple")
titulo4.pack(pady=20)

form_frame = tk.Frame(tab4)
form_frame.pack(pady=10, padx=50, anchor="w")

tk.Label(form_frame, text="Código Transacción:").grid(row=0, column=0, pady=5)
codigo_t = tk.Entry(form_frame)
codigo_t.grid(row=0, column=1)

tk.Label(form_frame, text="Tipo Transacción:").grid(row=1, column=0, pady=5)
tipo_t = tk.Entry(form_frame)
tipo_t.grid(row=1, column=1)

tk.Label(form_frame, text="Cuenta Origen:").grid(row=2, column=0, pady=5)
origen = tk.Entry(form_frame)
origen.grid(row=2, column=1)

tk.Label(form_frame, text="Cuenta Destino:").grid(row=3, column=0, pady=5)
destino = tk.Entry(form_frame)
destino.grid(row=3, column=1)

tk.Label(form_frame, text="Monto:").grid(row=4, column=0, pady=5)
monto_t = tk.Entry(form_frame)
monto_t.grid(row=4, column=1)

tk.Label(form_frame, text="Canal:").grid(row=5, column=0, pady=5)
canal = tk.Entry(form_frame)
canal.grid(row=5, column=1)


root.mainloop()