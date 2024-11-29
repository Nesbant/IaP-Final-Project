import streamlit as st
from products import register_product, get_products
from sales import register_sale, get_sales, modify_sale_quantity, get_highest_sale
from algorithms import bubble_sort, quicksort, binary_search
from charts import sales_by_product_chart
from persistence import read_file

# Título principal
st.title("Productos Electrónicos")

# Sidebar para opciones
selected_option = st.sidebar.radio(
    "Opciones",
    [
        "Registrar Producto",
        "Registrar Venta",
        "Ver Productos",
        "Ver Ventas",
        "Modificar Venta",
        "Ordenar Ventas",
        "Buscar Venta",
        "Ventas por Producto (Gráficos)",
        "Venta Más Alta",
    ]
)

# Mostrar la vista seleccionada
if selected_option == "Registrar Producto":
    st.subheader("Registrar Producto")
    with st.form("product_form"):
        description = st.text_input("Descripción")
        product_type = st.selectbox("Tipo de Producto", ["computadora", "celular", "accesorio"])
        tax_benefit = st.radio("IGV", ["YES", "NO"])
        submitted = st.form_submit_button("Registrar Producto")
        if submitted:
            product = register_product(description, product_type, tax_benefit)
            st.success(f"Producto Registrado: {product}")

elif selected_option == "Registrar Venta":
    st.subheader("Registrar Venta")
    with st.form("sales_form"):
        product_code = st.text_input("Código de Producto")
        description = st.text_input("Descripción del Producto")
        quantity = st.number_input("Cantidad", min_value=1, max_value=10, step=1)
        price = st.number_input("Precio", min_value=0.0, format="%.2f")
        tax_benefit = st.radio("IGV", ["YES", "NO"])
        submitted_sale = st.form_submit_button("Registrar Venta")
        if submitted_sale:
            sale = register_sale(product_code, description, quantity, price, tax_benefit)
            st.success(f"Venta Registrada: {sale}")

elif selected_option == "Ver Productos":
    st.subheader("Productos Registrados")
    products = get_products()
    if products:
        st.table([product.split("|") for product in products])
    else:
        st.write("No hay productos registrados.")

elif selected_option == "Ver Ventas":
    st.subheader("Ventas Registradas")
    sales = get_sales()
    if sales:
        st.table([sale.split("|") for sale in sales])
    else:
        st.write("No hay ventas registradas.")

elif selected_option == "Modificar Venta":
    st.subheader("Modificar Venta")
    sale_number_to_modify = st.number_input("Número de Venta", min_value=100, step=1)
    new_quantity = st.number_input("Nueva Cantidad", min_value=1, max_value=10, step=1)
    if st.button("Actualizar Venta"):
        if modify_sale_quantity(sale_number_to_modify, new_quantity):
            st.success(f"Venta {sale_number_to_modify} actualizada correctamente.")
        else:
            st.error("Venta no encontrada.")

elif selected_option == "Ordenar Ventas":
    st.subheader("Ordenar Ventas por Total")
    sales = read_file("data/sales.txt")
    sorted_sales = bubble_sort(sales)
    st.table([sale.split("|") for sale in sorted_sales])

elif selected_option == "Buscar Venta":
    st.subheader("Buscar Venta")
    sales_sorted = quicksort(get_sales())
    sale_number_to_search = st.number_input("Número de Venta a Buscar", min_value=100, step=1)
    if st.button("Buscar"):
        result = binary_search(sales_sorted, sale_number_to_search)
        if result:
            st.success(f"Venta Encontrada: {result}")
        else:
            st.error("Venta no encontrada.")

elif selected_option == "Ventas por Producto (Gráficos)":
    st.subheader("Gráficos de Ventas por Producto")
    sales = get_sales()
    if sales:
        chart = sales_by_product_chart(sales)
        st.pyplot(chart)
    else:
        st.write("No hay datos de ventas para generar gráficos.")

elif selected_option == "Venta Más Alta":
    st.subheader("Venta Más Alta")
    highest_sale = get_highest_sale()
    if highest_sale:
        st.success(f"Venta Más Alta: {highest_sale}")
    else:
        st.error("No hay ventas registradas.")
