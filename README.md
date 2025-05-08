ORGANIZACION DEL REPOSITORIO DE GITHUB:
    1- Enlace compartido con el docente
    2- Ramas separadas por integrantes (rama_brian , rama_ivana)
    3- commits con mensajes descriptivos sobre el cambio realizado
    4- evidencia de merges o pull requests

ESTRUCTURA DE DJANGO:
    1- Mostrar arbol de carpetas. Apps bien nombradas y ordenadas
    2- Explicacón del archivo setting.py con las apps registradas
    3- Uso del archivo urls.py central y por app, , con rutas correctamente definidas y usando name= para los redirect() y reverse().

CRUD FUNCIONAL:
    1- Mostrar en el navegador un CRUD completo de una tabla (ej. Producto, Cliente, Reserva, etc.).
    2- El CRUD debe incluir:
        <> Listado con DataTables: búsqueda, ordenamiento, paginación.
        <> Botones de acción para editar y eliminar (Bootstrap).
        <> Formularios de alta y modificación con validación (mínima en frontend).
        <> Eliminación con confirmación mediante JS (confirm() o SweetAlert2 si usaron).
        <> Al menos un formulario que se envíe por AJAX (crear o modificar).


ESTETICA Y USABILIDAD
    1- Interfaz amigable usando Bootstrap (formularios, tablas, botones, layout).
    2- Código limpio y organizado (nombres claros, indentación).
    3- Uso correcto de plantillas (base.html con {% block %} y herencia).

PREPARACION PARA LA AUTENTIFICACIÓN:
    1-Comentario o muestra del archivo settings.py con AUTHENTICATION_BACKENDS (si lo modificaron).
    2- Comentarios sobre cómo planean implementar login, logout y permisos en las próximas semanas.
