# Sistema de Contabilidad para PYMEs

Este proyecto es una aplicación de contabilidad diseñada para pequeñas y medianas empresas (PYMEs). Simplifica el proceso de registro de ingresos y gastos, lo que permite a las PYMEs mantener un control financiero eficiente y tomar decisiones informadas.

## Cómo funciona

El sistema de contabilidad ofrece las siguientes funcionalidades:

1. **Registro de Ingresos:** Puede ingresar los detalles de un ingreso, incluyendo el monto y una breve descripción.

2. **Registro de Gastos:** Permite registrar los gastos de su empresa, junto con el monto y una descripción.

3. **Cálculo del Saldo:** El sistema calcula automáticamente el saldo actual basado en los ingresos y gastos registrados.

## Beneficios

- **Simplicidad:** Facilita el seguimiento de las finanzas de su PYME sin complicaciones innecesarias.

- **Toma de Decisiones Informadas:** Al conocer su saldo actual, puede tomar decisiones financieras más informadas.

- **Registro Eficiente:** Utiliza un archivo CSV para almacenar datos contables, lo que facilita la gestión y el acceso a los registros.

## Ejemplo de Uso

```python
# Registrar un ingreso de $100
registrar_ingreso(100, "Venta de productos")

# Registrar un gasto de $50
registrar_gasto(50, "Compra de suministros")

# Calcular el saldo actual
saldo = calcular_saldo()
print(f"El saldo actual es: {saldo}")
```

## Requisitos

- Python 3.x
- Módulo CSV (incluido en la biblioteca estándar de Python)

## Uso

1. Clone el repositorio.

2. Ejecute el archivo `main.py` en su entorno de Python.

3. Siga las instrucciones en la consola para registrar ingresos, gastos y calcular el saldo.

Espero que esta herramienta simplifique la contabilidad y mejore la gestión financiera de las PYMEs.
