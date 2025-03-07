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


<<<<<<< HEAD
=======
#### **2. Almacenamiento de opciones de diamantes**
- **Actor:** Comprador de anillo de compromiso.
- **Requerimiento:** El usuario debe poder almacenar y visualizar opciones de diamantes con sus características y precios.
- **Funcionalidad esperada:** Guardado de diamantes en una lista accesible.

#### **3. Cálculo de precio personalizado de diamantes**
- **Actor:** Comprador de anillo de compromiso
- **Requerimiento:** El sistema debe calcular el precio de un diamante basado en sus características.
- **Funcionalidad esperada:** Algoritmo de cálculo según valores ingresados por el usuario.

#### **4. Comparación de precios de diversas joyas**
- **Actor:** Inversionista en joyas
- **Requerimiento:** El usuario debe poder comparar distintas joyas y sus precios en una interfaz visual.
- **Funcionalidad esperada:** Mostrar una tabla con varias joyas y sus precios.

#### **5. Generación de archivo con lista de joyas y precios**
- **Actor:** Coleccionista de joyas
- **Requerimiento:** El sistema debe permitir exportar la lista de joyas a un archivo descargable.
- **Funcionalidad esperada:** Exportación a CSV o PDF.

#### **6. Eliminación de joyas de la lista**
- **Actor:** Usuario general
- **Requerimiento:** El usuario debe poder eliminar una joya ingresada en caso de error.
- **Funcionalidad esperada:** Opción para eliminar elementos de la lista.

#### **7. Almacenamiento y ajuste de precios para negocio**
- **Actor:** Dueño de joyería
- **Requerimiento:** El usuario debe poder asignar nombres a las joyas, registrar su precio y ajustarlo.
- **Funcionalidad esperada:** Campo de personalización de nombres y ajuste de precios según margen de ganancia.

### **Media Prioridad**

#### **8. Análisis de precios en años anteriores**
- **Actor:** Inversionista en joyas
- **Requerimiento:** El usuario debe poder consultar precios de joyas en años anteriores.
- **Funcionalidad esperada:** Base de datos con precios históricos.

#### **9. Comparación entre precios actuales y pasados**
- **Actor:** Heredero de joyas
- **Requerimiento:** El sistema debe permitir comparar precios actuales con pasados.
- **Funcionalidad esperada:** Mostrar una tabla con precios de diferentes años.

#### **10. Comparación de precios por degradación de las joyas**
- **Actor:** Coleccionista de joyas
- **Requerimiento:** El sistema debe permitir modificar características de una joya y recalcular su precio según degradación.
- **Funcionalidad esperada:** Modificación y recálculo de precios.

#### **11. Cálculo de precios de piedras preciosas en relojes de lujo**
- **Actor:** Inversionista en relojes de lujo
- **Requerimiento:** El sistema debe calcular el valor de piedras preciosas en relojes.
- **Funcionalidad esperada:** Algoritmo de cálculo específico para relojes de lujo.

#### **12. Actualización de valores estándar**
- **Actor:** Usuario general
- **Requerimiento:** El usuario debe poder modificar los valores base de cálculo de precios.
- **Funcionalidad esperada:** Formulario editable con valores base.

#### **13. Simulación de precios de joyas en diferentes épocas**
- **Actor:** Usuario curioso
- **Requerimiento:** El sistema debe permitir cambiar precios base según diferentes años.
- **Funcionalidad esperada:** Ajuste de cálculo según años seleccionados.

## **3. Requerimientos No Funcionales**

1. **Interfaz de usuario intuitiva:** Diseño atractivo y fácil de usar.
2. **Almacenamiento persistente:** Uso de base de datos para guardar información.
4. **Visualización de datos:** Implementar gráficas para tendencias de precios y datos guardados.

## **4. Tecnologías Recomendadas**
- **Backend:** Estrcutura bascia e importancion de algunas librerias de Python (tabulate).
- **Base de Datos:** Esctructura basica de manejo de diccionarios JASON.
- **Exportación:** Librería para generar archivos CSV (en caso de que no se use JASON, esta desicion depende de la comodidad de los desarrolladores).

**TENER EN CUENTA LA CERACION DE RAMAS PARA MEJOR ORGANIZACION DEL EQUIPO EN EL DESARROLLO DEL PROGRAMA**

## **5. Consideraciones Finales**
Este documento proporciona las funciones claras y precisas para cumplir a cabalidad con los requerimientos que se rezliaron teniendo en cuenta las diversas historias de usuario que se ueron presentadas para el desarrollo del sistema. Se recomienda priorizar las historias de usuario **de alta prioridad** y luego avanzar en las de **media prioridad**. La flexibilidad en los cálculos y la integración de datos actualizados serán clave para el éxito del proyecto (esto se puede comprobar en el espacio de trbajo de ClickUp). 

>>>>>>> 487b186b2b22c3fbe0aaa129ccd71081291388a7
