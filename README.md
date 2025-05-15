app_recurrencia
Visualización interactiva de un modelo de recurrencia basado en 7 variables, desarrollado con Streamlit.

Descripción
Esta aplicación permite explorar y visualizar un modelo de recurrencia que utiliza siete variables predictoras. Proporciona una interfaz sencilla para ingresar valores y obtener predicciones, facilitando el análisis y la comprensión del modelo.

Características
Interfaz interactiva: Permite al usuario ingresar valores para las variables y obtener predicciones en tiempo real.

Visualización de resultados: Muestra las predicciones de manera clara y concisa.

Desplegada en la nube: Accesible desde cualquier dispositivo con conexión a internet.

Acceso a la aplicación
Puedes acceder a la aplicación en el siguiente enlace:

👉 https://recurrencia7.streamlit.app/

Instalación y ejecución local
Para ejecutar la aplicación en tu entorno local, sigue estos pasos:

Clona el repositorio:

bash
Copiar
Editar
git clone https://github.com/dfp25/app_recurrencia.git
cd app_recurrencia
Crea un entorno virtual (opcional pero recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecuta la aplicación:

bash
Copiar
Editar
streamlit run app_recurrencia.py
Estructura del repositorio
app_recurrencia.py: Código principal de la aplicación Streamlit.

modelo_recurrencia_7.joblib: Archivo del modelo de recurrencia entrenado.

requirements.txt: Lista de dependencias necesarias para ejecutar la aplicación.

Requisitos
Python 3.7 o superior

Las dependencias listadas en requirements.txt

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Autor
Desarrollado por dfp25.
