# Anexo 1: formatos por actividad

Fuente: `docs/Anexo 1. Herramientas_para_la_construccion_del_PETI.xlsx` (19 hojas). Columnas transcritas de la hoja. Cuando el PETI presente una tabla que corresponde a una hoja, debe contener estas columnas o explicar por qué omite alguna.

| Hoja | Formato | Columnas |
|---|---|---|
| Fases y Actividades | Índice | Fase, actividad (las 17 de la guía) |
| Actividad 1 | Equipo y stakeholders | Equipo: área, nombre, rol, correo, móvil, ¿existe el perfil en la entidad? (S/N). Stakeholders: área, nombre, aporte, correo, móvil |
| Actividad 3 | Cronograma | Fase, ID, actividad, fecha de inicio, responsable, salida o resultado, meses E-D |
| Actividad 4A | Ficha de la entidad | Nombre, municipio, orden, presupuesto ejecutado total y de TI en la última vigencia, naturaleza jurídica, nivel, fechas de actualización del plan estratégico institucional, del PETI y del plan sectorial; misión; visión; objetivos (ID, nombre) y metas (ID, nombre, medición actual) |
| Actividad 4B | Procesos de la cadena de valor | ID, proceso, una columna por SI con **T** (soporta totalmente) o **P** (parcialmente) |
| Actividad 4C | Servicios, trámites u OPAs | ID, nombre, descripción, tipo, registrado en SUIT, áreas, tipo de usuario, norma, procesos, usuarios del último año, costos, satisfacción, PQR, complejidad, criticidad, valor al ciudadano, tiempo de ciclo, riesgo de corrupción, nivel de automatización, canales 1-8 |
| Actividad 4D | Normatividad | ID, norma, descripción, tipo |
| Actividad 5 | Planes externos | ID, plan o CONPES, responsabilidad u obligación, fecha de plazo |
| Actividad 6 | **DOFA** | Fortalezas y debilidades (origen interno), oportunidades y amenazas (origen externo), con preguntas guía por cuadrante. La guía pide **una DOFA por dominio** |
| Actividad 7 | Tendencias | Tendencia, características, y cruce con servicios (S01…), trámites (C01…) y procesos (P01…). Lista base: cloud, IA/ML, IoT, big data, blockchain, microservicios/SOA, DevOps, plataformas de ciberseguridad, realidad aumentada, plataforma colaborativa, robótica y drones, impresión 3D, IA adaptativa, metaverso |
| Actividad 8 | **Estrategia de TI** | Misión de TI, visión de TI; objetivos: ID `OETI01…`, objetivo, ID de objetivos institucionales asociados; metas: ID `METI01…`, nombre, **medición actual o línea base, año 1, año 2, año 3** |
| Actividad 11 | **Catálogo de brechas** | ID `B001…`, ID del servicio, trámite o proceso afectado, nombre del elemento (capacidad, recurso, rol, proceso), **acción [crear, eliminar, modificar]**, descripción y justificación, **tiempo estimado total, costo estimado de inversión total**, proyecto en ejecución [SI, NO] |
| Actividad 12 | Iniciativas de otros planes | ID `IPGD001…`, nombre, plan asociado, servicios, descripción, área líder, metas estratégicas, áreas involucradas, tiempo, fecha de inicio, costo, brechas |
| Actividad 13 | **Catálogo de iniciativas y proyectos** | ID `IT001…`, nombre, descripción, subproyectos, **dominio de gestión de TI**, **objetivo estratégico institucional**, **objetivo estratégico de TI**, **meta a la que contribuye**, área líder, áreas involucradas, **tiempo total (meses)**, vigencia, fecha de inicio estimada, **costo o presupuesto estimado**, **brecha asociada** |
| Actividad 14A | Indicadores de gestión de TI | Código, dominio, categoría (eficacia, eficiencia…), tipo (estratégico…), nombre, descripción, fórmula. Rangos de ejemplo: bueno 0,9-1; intermedio 0,5-0,8; malo 0-0,5 |
| Actividad 14B | **Hoja de vida del indicador** | ID `IND.ES.01…`, nombre, objetivo, tipo, **fórmula, frecuencia, origen de los datos, responsable, meta, rangos** (tres niveles), observaciones |
| Actividad 17 | Plan de comunicación | Grupos de interés (descripción, características); plan: actividad, grupo de interés, canal, formato, responsable, frecuencia |
| Listas paramétricas | Nivel de automatización | Totalmente manual, automatizado parcial o totalmente, parcial o totalmente en línea, parcialmente automatizado y en línea |
| Calificaciones Sesión 4 | Escalas | Trámite en línea (sí 0, no 10), complejidad, criticidad (bajo, medio, alto) y satisfacción (0-5) |

## Ejemplos del Anexo que sirven de molde

Hoja de vida `IND.ES.01`: "Nivel de ejecución del PETI por vigencia"; fórmula EP = (IE / IP) × 100 %, donde IE son iniciativas ejecutadas e IP iniciativas planeadas; frecuencia semestral; origen: tablero de control de seguimiento al plan de proyectos del PETI; responsable: líder de estrategia de TI; meta 1; rangos ≥ 95 %, entre 94 % y 71 %, ≤ 70 %.

Brecha según la guía (Actividad 11): "El elemento aplicación móvil tendrá la acción crear, el tiempo estimado de diseño, desarrollo e implementación es de seis meses, el costo estimado de inversión es de $100.000.000." El nivel de detalle esperado es ese: elemento, acción, tiempo y costo.

Iniciativa según la guía (Actividad 13): se agrupan brechas similares; el tiempo total suma diseño, planeación, ejecución y cierre (y contratación si hay proveedor); el área de TI siempre figura como área líder o acompañante; el costo sale de la suma de las brechas que la componen o de valores de referencia de procesos similares. Las brechas asociadas a proyectos en curso no se consolidan: van directo a la hoja de ruta.

## Costos en un PETI académico

Normalmente no hay presupuesto real de la organización. Opciones aceptables, en este orden: (1) rango de orden de magnitud con el supuesto explícito (tarifas públicas de nube, precios de lista publicados de licencias, horas-persona por rol con tarifa de referencia citada); (2) costo relativo (bajo, medio, alto) con los umbrales definidos en el mismo documento y registrados como `INT-` (por ejemplo: bajo < USD 50.000; medio USD 50.000-250.000; alto > USD 250.000, o su equivalente en pesos); (3) "costo por estimar" con responsable y fecha. Lo que no es aceptable es dejar la columna vacía sin explicación o inventar una cifra exacta sin supuesto. Si la organización es pública y publica su presupuesto o sus contratos en SECOP, úsalos como fuente `PUB-`.
