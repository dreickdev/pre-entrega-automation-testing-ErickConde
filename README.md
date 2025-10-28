# Pre-Entrega de Proyecto: Automation Testing (Erick Conde)

Este proyecto es la pre-entrega del curso de Automation Testing. El objetivo es automatizar los flujos básicos (Login, Catálogo y Carrito) del sitio web `saucedemo.com`.


* **Python**: Lenguaje principal de programación.
* **Selenium WebDriver**: Para la automatización e interacción con el navegador.
* **Pytest**: Framework para la estructura y ejecución de las pruebas.
* **pytest-html**: Plugin para generar reportes de prueba en formato HTML.
* **webdriver-manager**: Para manejar automáticamente el `chromedriver`.
* **Git y GitHub**: Para el control de versiones.

## Cómo Instalar y Ejecutar

Sigue estos pasos para configurar el entorno y correr las pruebas.

### 1. Prerrequisitos

* Tener Python 3.x instalado.
* Tener Git instalado.
* Tener Google Chrome instalado.

### 2. Instalación de Dependencias

1.  Clona este repositorio:
    ```bash
    git clone [https://github.com/dreickdev/pre-entrega-automation-testing-ErickConde.git](https://github.com/dreickdev/pre-entrega-automation-testing-ErickConde.git)
    ```
2.  Navega a la carpeta del proyecto:
    ```bash
    cd pre-entrega-automation-testing-ErickConde
    ```
3.  (Recomendado) Crea un entorno virtual:
    ```bash
    python -m venv venv
    # En Windows: venv\Scripts\activate
    # En Mac/Linux: source venv/bin/activate
    ```
4.  Instala las librerías necesarias:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Cómo Ejecutar las Pruebas

Para ejecutar todas las pruebas y **generar el reporte HTML** en la carpeta `reports/`, usa el siguiente comando:

```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html
```
* `-v`: Modo "verbose" (muestra más detalles).
* `--html=reports/reporte.html`: Crea el reporte en la carpeta `reports`.