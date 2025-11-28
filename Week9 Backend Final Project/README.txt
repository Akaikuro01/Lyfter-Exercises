––––––––––––––––––––––––––––––––––––
README (texto simple)
––––––––––––––––––––––––––––––––––––
Nombre del proyecto
PetShop API (Flask + SQLAlchemy Core + PostgreSQL + Redis opcional)

Requisitos
• Python 3.11+
• PostgreSQL (base de datos “petshop” o el nombre que defina)
• Redis opcional (si desea usar el caché real)

Configuración rápida

Crear base de datos en PostgreSQL: crear una BD llamada petshop.

Variables de entorno (ejemplos):
– DATABASE_URL=postgresql://usuario:password@localhost:5432/petshop
– JWT_SECRET o claves RS256 ya incluidas en el contenedor IoC
– (Opcional) configuración de Redis si lo usa realmente.

Instalar dependencias con pip (Flask, SQLAlchemy, psycopg2-binary, pytest, pytest-cov y redis si aplica).

La app crea tablas al iniciar si no existen (según db.py).

Ejecución del servidor
• Desde la carpeta raíz del proyecto, ejecutar main.py con Python o configurar FLASK_APP y usar flask run.
• La API quedará disponible en http://127.0.0.1:5000/
 por defecto.

Autenticación
• Registro y login devuelven un JWT.
• Use el token en el header: Authorization: Bearer <token>.
• Roles esperados: 1 = admin, 2 = user.

Endpoints principales (resumen)
• Productos: CRUD y listado paginado.
• Métodos de pago: alta, consulta, edición y borrado del método del usuario autenticado.
• Carrito: ver, agregar/actualizar ítems, limpiar.
• Checkout: crea factura (header + lines), descuenta stock, limpia carrito.
• Facturas: listado paginado del usuario autenticado; responde lista vacía cuando no hay datos.

Caché
• Se usa cache manager con Redis para respuestas de lectura (listados).
• No hay TTL configurado; la invalidación se realiza borrando claves por patrón tras escrituras (por ejemplo, cambios en productos o nuevas facturas).

Pruebas
• Ejecutar “pytest” en la carpeta raíz del proyecto.
• Las pruebas incluyen casos de éxito y error para endpoints y lógica de negocio.
• Se genera un reporte breve en consola (pytest-cov).

Notas operativas
• Para producción, almacenar contraseñas hasheadas.
• Proteger JWT y variables sensibles fuera del repositorio.
• Si el esquema ya existe y requiere cascadas adicionales, aplicar ALTER TABLE o migraciones.

Archivos clave
• db.py: definición del esquema y engine a petshop. 
• ioc_container.py: inyección de dependencias (repos, JWT, cache). 
• JWT_Manager.py: encode/decode de tokens con RS256. 
• cache_manager.py: wrapper de Redis (set/get/exists/delete, patrón). 
Si quieres, te lo dejo en dos archivos separados (Architecture.md y README.txt) tal cual este contenido.