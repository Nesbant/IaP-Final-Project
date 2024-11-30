# Sistema de Gestión de Ventas de Productos Electrónicos
Este proyecto es una aplicación de gestión de ventas diseñada para registrar, modificar, consultar y analizar ventas de productos electrónicos. Fue desarrollado en Python usando Streamlit como framework de interfaz gráfica.

## Características
- Registrar productos: Registra productos con sus detalles como descripción, tipo y si aplican a beneficios tributarios.
- Registrar ventas: Gestiona ventas relacionadas con productos específicos.
- Consultar productos y ventas: Visualiza productos y ventas registradas en tablas.
- Modificar ventas: Actualiza la cantidad de productos en ventas existentes.
- Ordenar ventas: Ordena las ventas por el total usando el algoritmo de burbuja.
- Buscar ventas: Encuentra una venta específica mediante búsqueda binaria.
- Generar gráficos: Visualiza las ventas por producto mediante gráficos generados con Matplotlib.
- Venta más alta: Muestra la venta con el total más alto.


## Requisitos
Asegúrese de tener instaladas las siguientes dependencias:

Python 3.9 o superior
- Streamlit: pip install streamlit
- Matplotlib: pip install matplotlib

Streamlit instalará automaticamente otras dependencias necesarias. Las podrá ver en el archivo `requirements.txt`.

## Configuración del entorno
1. Crea un entorno virtual:
```
python -m venv env
```


2. Activa el entorno virtual:
```
.\env\Scripts\activate
```

3. Instala las dependencias:
```
pip install -r requirements.txt
```

## Cómo Usar
1. Ejecutar la Aplicación
Ejecute el siguiente comando desde la raíz del proyecto para iniciar la aplicación:

```
streamlit run view.py
```


