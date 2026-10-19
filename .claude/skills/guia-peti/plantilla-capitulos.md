# Plantilla PETI (Anexo 2): capítulos y contenido mínimo

Fuente: `docs/Anexo 2. Plantilla PETI.docx` (cartilla MinTIC, versión 3.0, noviembre de 2023). La plantilla trae textos base, recuadros guía y tablas de ejemplo de una alcaldía o ministerio; los recuadros se eliminan en la versión final. Donde la plantilla dice "entidad", en este proyecto se lee la organización de "Datos del proyecto" (`.claude/CLAUDE.md`).

La columna **Numeral del PETI** indica dónde va cada contenido en la estructura de 16 numerales de `docs/peti_2026_2028.md`. Esa estructura es la que el profesor aceptó en otro grupo; no la cambies sin razón. Indica dónde debería estar el contenido, no si está bien hecho.

## Capítulos

| # | Capítulo de la plantilla | Contenido mínimo que pide | Herramienta | Numeral del PETI |
|---|---|---|---|---|
| 1 | Introducción | Marco (Política de Gobierno Digital, Decreto 767 de 2022, MRAE v3.0), periodo del PETI, qué contiene (situación actual, arquitectura actual y destino, brechas, marco normativo, iniciativas, portafolio y hoja de ruta, indicadores) y beneficios esperados | — | §1 |
| 2 | Objetivo y alcance | Objetivo del documento con periodo; alcance: fases de la guía y dominios del modelo de gestión (Estrategia, Gobierno, Información, SI, Infraestructura, Uso y Apropiación, Seguridad) | — | §2 (2.1 objetivo, 2.2 alcance, 2.3 alcance de la evidencia) |
| 3 | Normatividad (marco normativo) | Tabla norma → descripción, revisando su aplicación real al entorno | Act. 4D | §3 |
| 4 | Metodología | Metodología usada para construir el PETI; en empresa privada, las adaptaciones | Guía completa | §4 |
| 5 | Contexto y modelo operativo | **Motivadores estratégicos** con fuente (estrategia nacional, sectorial, institucional, lineamientos); compromisos externos con plazo; rupturas | Act. 5 | §5.1 |
| 5 | | **Contexto institucional**: misión, visión, objetivos estratégicos (ID, objetivo, fuente), metas con línea base | Act. 4A | §5.2 |
| 5 | | **Estructura organizacional**: organigrama, número de áreas, empleados y contratistas | — | §5.3 |
| 5 | | **Modelo operativo**: mapa de procesos; 5.1.1-5.1.4 procesos estratégicos, misionales, de apoyo, de evaluación y control (ID, nombre, objetivo) | Act. 4B | §5.4.1 |
| 5 | | 5.1.5 **Alineación de TI con los procesos**: proceso, categoría, SI que lo soporta, cubrimiento (total, parcial, sin cobertura), oportunidad de mejora | Act. 4B | §5.4.2 |
| 5 | | 5.1.6 Servicios institucionales o de negocio; 5.1.7 Trámites; 5.1.8 OPAs (ficha: usuario, horario, canales, oportunidades de mejora con TI) | Act. 4C | §5.4.3. En empresa privada, trámites y OPAs **no aplican**: declararlo y caracterizar los servicios al cliente |
| 6 | **Situación actual** | 6.1 Estrategia de TI: lienzo estratégico, misión y visión de TI vigentes, servicios de TI (catálogo con ANS), capacidades de TI, indicadores y tablero de TI | Act. 6 | §6.1 (6.1.1 a 6.1.4) |
| 6 | | 6.2 Gobierno de TI: instancia de decisión y periodicidad, **matriz de riesgos de TI**, gestión del presupuesto de TI, políticas y estándares, procesos de gestión de TI adoptados, estructura humana de TI y **matriz RACI**, esquema de toma de decisiones, gestión de proyectos | Act. 6 | §6.2 |
| 6 | | 6.3 Gestión de información: planeación y gobierno, arquitectura de información, componentes de información (catálogo), análisis y aprovechamiento, calidad y seguridad | Act. 6 | §6.3 |
| 6 | | 6.4 Sistemas de información: catálogo de SI, capacidades funcionales, **mapa de integraciones** (protocolo y esquema de seguridad), arquitectura de referencia, ciclo de vida, mantenimiento, soporte | Act. 6 | §6.4 |
| 6 | | 6.5 Infraestructura de TI: arquitectura de línea base, catálogo de elementos, capacidad, operación (monitoreo, ANS, mantenimiento, IPv6) | Act. 6 | §6.5 |
| 6 | | 6.6 Uso y apropiación: grupos de interés caracterizados, formación realizada, incentivos, plan de comunicaciones de TI | Act. 6 | §6.6 |
| 6 | | 6.7 Seguridad: evaluación de efectividad de controles por dominio (instrumento MSPI, temas del Anexo A de ISO 27001:2022) con calificación actual y objetivo | Act. 6 | §6.7 |
| — | DOFA por dominio (Actividad 6) | Fortalezas, debilidades, oportunidades y amenazas **por cada uno de los 7 dominios** | Act. 6 | §6.8 |
| — | Tendencias (Actividad 7) | Tendencia × procesos o servicios donde aplica | Act. 7 | §6.9 |
| 7 | **Situación objetivo** | 7.1 Estrategia de TI: misión y visión de TI, **objetivos estratégicos de TI** (qué hallazgos, riesgos u optimizaciones atienden), capacidades, servicios de TI (altas, cambios, bajas), **indicadores de TI** | Act. 8, 14 | §7.1 |
| 7 | | 7.2 Gobierno de TI: instancia de decisión propuesta, matriz de riesgos propuesta, políticas de TI, presupuesto, procesos de gestión de TI, estructura humana y RACI futura, gestión de proyectos | Act. 8 | §7.2 |
| 7 | | 7.3 Gestión de información; 7.4 Sistemas de información (mapa de integraciones objetivo, arquitectura de referencia); 7.5 Infraestructura (arquitectura objetivo, capacidad); uso y apropiación; seguridad | Act. 8, 10 | §7.3 a §7.7 |
| — | Brechas (Actividad 11 de la guía; en la plantilla alimentan el capítulo 8) | Catálogo de brechas | Act. 11 | §8.1 |
| — | Oportunidades y necesidades (patrón de MinCiencias) | Tabla de oportunidades | Act. 7, 9, 10 | §8.2 |
| — | Iniciativas de otros planes | Iniciativas con componente de TI de otros planes (o "no aplica" con razón) | Act. 12 | §8.3 |
| 8 | **Hoja de ruta y portafolio de proyectos** | Mapa de ruta de proyectos **priorizados con presupuesto, responsables y alcance** | Act. 13 | §9 (catálogo, fichas, presupuesto por fase, mapa de ruta) |
| — | Indicadores (Actividad 14) | Indicadores con hoja de vida | Act. 14A, 14B | §10 |
| — | Riesgos de TI | Matriz de riesgos con tratamiento | — | §11 |
| 9 | **Estrategia de comunicación del PETI** | Grupos de interés; actividades, canal, formato, responsable, frecuencia | Act. 17 | §12 |
| — | Gobierno y seguimiento del PETI | Equipo, instancias, aprobación y actualización (Act. 1, 16) | Act. 1, 16 | §13 |
| — | Glosario | Términos | — | §14 |
| — | Referencias bibliográficas | Fuentes citadas (APA 7) | — | §15 |
| — | Control de cambios (patrón de MinCiencias) | Tabla de versiones | — | §16 |
| — | Anexos | A: equivalencia con IDs del Anexo 1; B: procesos frente a marcos (COBIT, ISO 27001, ITIL) | — | Anexo A, Anexo B |

## Indicaciones de la plantilla que se olvidan

- "En el documento solo incluir el resumen [...] y dejar como anexo toda la información complementaria para facilitar la lectura." Aplica a servicios, SI, infraestructura y portafolio de servicios de TI.
- La construcción del lienzo estratégico "no debe ser visto como un requisito"; se llena de derecha a izquierda: segmentos, propuesta de valor, canales, relación, ingresos, recursos, actividades, socios, costos.
- En la situación actual, si algo no existe (misión de TI, mapa de procesos, catálogo), **se dice que no existe**; no se inventa.
- La evaluación de seguridad se presenta además en un gráfico (radar) de calificación actual frente a objetivo.
- Las iniciativas descritas en la situación objetivo "deben ser consistentes con el portafolio de iniciativas, proyectos y mapa de ruta".
- La hoja de ruta incluye las iniciativas de alcance sectorial. En una empresa privada el equivalente es lo que exija la casa matriz, un regulador del sector o un cliente con obligación contractual; si no hay, se declara.

## Indicadores predefinidos de la plantilla (7.1.6)

Ejemplos del producto tipo "Tablero de control", útiles para completar el §10 con fórmulas ya estandarizadas: nivel de ejecución del PETI (actividades ejecutadas / programadas), alineación estratégica de TI (objetivos de TI que soportan el plan / objetivos de TI), procesos con soporte de TI, satisfacción con la respuesta de TI, participación proactiva de TI en el comité directivo, nuevos servicios de TI, disponibilidad de SI, servicios del catálogo en operación, efectividad y oportunidad en la solución de incidentes, cumplimiento de ANS, proveedores con requerimientos y niveles de servicio definidos, cambios con control formal, cambios de emergencia, sistemas que no cumplen requisitos de seguridad, problemas resueltos a tiempo, tiempo a causa raíz, restauraciones exitosas, procesos críticos monitoreados, cubrimiento y horas de capacitación, proyectos a tiempo y en presupuesto, ejecución presupuestal. La lista completa con fórmulas está en el texto extraído de la plantilla (buscar "INDICADORES PREDEFINIDOS").
