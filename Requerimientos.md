**Especificación Técnica: Sistema de Cálculo y Comparación de Precios de Joyas**
1. Funcionalidades Principales (MVP)

Consulta y Almacenamiento de Precios
✅ Mostrar tablas de referencia con precios de diamantes u otras piedras preciosas (diamantes safiro, esmeralda, rubi u otra joya) o metales (oro, metal u otros metales)según características (quilates, claridad, color, talla).
✅ Permitir almacenar y visualizar opciones de diamantes con características y precios a traves de una tabla (tabulate y JSON).
✅ Calcular precio de un diamante según parámetros ingresados por el usuario y las caracteristicas que tiene el programa (quilates, claridad, color, talla).

Comparación y Gestión de Datos
✅ Exportar listas de joyas y precios en CSV o JSON(tabulate).
✅ Eliminar, editar, mostrar, agregar y joyas de la lista.
2. Funcionalidades Adicionales (Mejoras Futuras)
Análisis Histórico y Proyecciones

✅ Comparar precios de diversas joyas en una interfaz visual (mostrar las caracteristicas de todas las joyas o de una joya o caracteristica en especifico).
✅ Calcular valor de piedras preciosas en relojes de lujo, collares u otras joyas, haciendo que el usuario calcula una joya y defina la cantidad de la piedras preciosas que posee (por ejemplo, un collar de diamantes que tiene 15 diamantes, calcular primero el precio por diamante y luego multiplicarlo por la cantidad de diamantes).
✅ Crear una función para que una persona pueda agregar otro metal u joya y que el usuario pueda definir sus caracteristicas y precios.
✅ Agregar opciones de ordenar y buscar datos.
3. Requerimientos No Funcionales

    Interfaz intuitiva y responsiva.
    Almacenamiento persistente con JSON (con tabulate).
    Visualización de datos con tablas para facilitar la parte visual del usuario.

4. Tecnologías Recomendadas

    Backend: Python (uso de tabulate y otras librerías según necesidad).
    Base de Datos: JSON (con tabulate) o alternativa según requerimientos.
    Exportación: CSV si se requiere compatibilidad fuera de JSON (preferiblemente usar JSON).

5. Consideraciones para el Desarrollo

    Uso de control de versiones con ramas organizadas por función (Git y GitHub).
    Priorización de funcionalidades en fases de desarrollo.
    Validación de cálculos con referencias externas (Ejemplo: Simulador de precios https://www.diamantes-infos.com/diamante-bruto/precio-diamante-bruto.html#simulador-precio-diamante-bruto).


