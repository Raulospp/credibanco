# Lecciones de sustentaciones anteriores

Lo que el profesor pregunta en la revisión del PETI y los puntos débiles que ya le costaron correcciones a otros grupos. Sale de la experiencia de un grupo al que el PETI le fue bien con esta misma configuración. No es parte del PETI ni se entrega: es criterio de revisión (lo usan `auditor-conformidad` y `/auditar-peti`) y material de estudio.

## 1. Las cuatro preguntas que el profesor hace casi siempre

Hay que poder señalar el numeral de memoria y explicar **el método**, no solo el resultado.

### "¿Dónde está el AS-IS?"

AS-IS es la situación actual; la plantilla la llama "Situación actual" (capítulo 6). En la estructura de este repositorio está en:

| Dónde | Qué muestra |
|---|---|
| §5.4 Modelo operativo | Mapa de procesos, qué sistema soporta cada proceso y su cubrimiento (total, parcial, sin cobertura) |
| §6.1 a §6.7 | Diagnóstico de cada uno de los 7 dominios del MRAE: qué existe y qué no, cada afirmación con ID de evidencia |
| §6.8 y §6.9 | DOFA por dominio y tendencias |

Hay que saber decir **de dónde salió**: fuentes públicas (`PUB-`), entrevistas (`PRV-`) y análisis propio (`INT-`). Regla de la plantilla: si algo no existe, se dice que no existe; no se inventa.

Pregunta de seguimiento probable: *"¿Lo que vieron en un área es representativo de toda la organización?"* Respuesta: no, y por eso el alcance de la evidencia (§2.3) lo dice y todo lo de entrevistas se redacta como "observado en el área analizada". El plan lo compensa midiendo líneas base al inicio en toda la organización.

### "¿Dónde están las brechas y cómo las sacaron?"

Están en §8.1 y cada una llega a un proyecto en §9.

Método (guía, Actividad 11): una brecha es la diferencia entre la situación actual y la objetivo. Se pone lado a lado la fila de un dominio en §6 (AS-IS) y la misma fila en §7 (TO-BE). Donde no coinciden se anota el **elemento** que falta o cambia, la **acción** (crear si no existe, modificar si existe pero no sirve así, eliminar), el **tiempo** y el **costo** estimados. Después se revisan las debilidades y amenazas de la DOFA y los motivadores con plazo para no dejar nada por fuera.

Conviene tener preparada una tabla "Brecha | AS-IS: lo que encontramos | TO-BE: lo que queremos | Acción". **Cada brecha debe tener su fila en el diagnóstico**: una brecha que solo sale de la DOFA o de un motivador es un punto débil.

Pregunta de seguimiento probable: *"¿Por qué ese tiempo y ese costo?"* El tiempo es la estimación del esfuerzo (un procedimiento: semanas; un sistema de gestión con política, roles y controles: meses; un informe de auditoría con periodo de observación: un año). El costo usa rangos con umbrales declarados (INT-001), no cifras inventadas.

### "¿Dónde está el TO-BE?"

TO-BE es la situación objetivo (capítulo 7 de la plantilla); está en §7: misión y visión de TI, objetivos de TI con metas por año y la situación objetivo por dominio. Todo marcado como **propuesto**.

Cómo se construyó: (1) se invierte cada problema del AS-IS; (2) se busca en los marcos cómo se hace bien (COBIT, ISO 27001, ITIL, NIST); (3) se lleva a metas medibles (Actividad 8: verbo en infinitivo, SMART, perspectivas del Balanced Scorecard); (4) cada meta queda con un indicador en §10.

Pregunta de seguimiento probable: *"¿Es realista en el horizonte?"* Hay que mostrar que está escalonado: año 1, lo que depende de la organización (gobierno, procedimientos, estandarización); año 2, lo que depende de terceros o de madurez previa. Metas del año 1 intermedias.

### "¿Y la arquitectura?"

La guía del MinTIC es parte del Marco de Referencia de Arquitectura Empresarial (MRAE v3.0). La plantilla describe el AS-IS como "arquitectura actual de gestión de TI" y el TO-BE como "arquitectura destino"; los 7 dominios son las capas. Por eso **el AS-IS y el TO-BE por dominio son la arquitectura actual y la objetivo.**

Si piden la vista TOGAF, es la misma información reordenada. Conviene tenerla lista (en el PETI como anexo o en la presentación):

| Capa TOGAF | Arquitectura actual (AS-IS) | Arquitectura objetivo (TO-BE) | Proyectos |
|---|---|---|---|
| Negocio (procesos, roles, gobierno) | | | |
| Datos | | | |
| Aplicaciones | | | |
| Tecnología | | | |
| Seguridad (transversal) | | | |

Y un **diagrama de integraciones** AS-IS frente a TO-BE (Mermaid sirve), con los sistemas por categoría. Un grupo recibió la observación "no veo un diagrama de arquitectura": ponerlo al menos como anexo.

## 2. La cadena de trazabilidad (el profesor casi seguro la pide)

Objetivo corporativo → objetivo de TI → meta → indicador; y en paralelo: hallazgo del diagnóstico → brecha → proyecto → indicador → riesgo que mitiga.

Hay que tener **dos ejemplos completos** para decir en voz alta, con IDs reales del PETI. Plantilla:

> OC0n "…" → OETI0n "…" → METI0n "…" → KPI-nn. El diagnóstico (§6.x) dice que … (ID de evidencia) → BRE-0nn "…", acción crear/modificar, n meses, costo … → P1.n, responsable …, meses a-b → mide KPI-nn → mitiga R0n "…".

## 3. Puntos débiles que ya aparecieron (revisarlos antes de entregar)

| # | Punto débil | Dónde | Cómo evitarlo |
|---|---|---|---|
| 1 | DOFA consolidada en una sola tabla, no por dominio | §6.8 | Una fila por cada uno de los 7 dominios (la guía la pide por dominio) |
| 2 | Tabla de objetivos de TI sin la columna del objetivo corporativo que apoya | §7.1 | Columna "Objetivo corporativo" explícita |
| 3 | Meta del año 1 que depende de proyectos que empiezan en el año 2 | §7.1, §9 | Revisar calendario de cada meta; si no cuadra, poner 0 o intermedio en el año 1 |
| 4 | Meta de ejecución del PETI al mes 12 que no coincide con lo que el calendario da | §10 | Calcular: proyectos que terminan antes del mes 12 / total |
| 5 | Indicador que no mide ningún proyecto | §9, §10 | Columna "Mide" en §10 y "Indicador" en §9 |
| 6 | Hoja de vida del indicador sin "origen de los datos" o sin "tipo" | §10 | Todas las columnas de la hoja 14B del Anexo 1 |
| 7 | Referencias bibliográficas incompletas frente a lo citado | §15 | Toda `PUB-` citada y todo marco nombrado va a §15 |
| 8 | Faltan lienzo estratégico, catálogo de servicios de TI, capacidades de TI o calificación de seguridad | §6.1, §6.7 | Si no existen en la organización, decirlo; la calificación de seguridad se hace con el MSPI o los temas de ISO 27001 |
| 9 | Referencia cruzada a un numeral equivocado ("ver §11" cuando es §12) | Todo | Revisar al cerrar cada versión |
| 10 | Actividad 12 (otros planes de Gobierno Digital) no aparece | §4, §8.3 | Si es privada, declarar "no aplica" con razón |
| 11 | Objetivos corporativos y costos formulados por el equipo presentados como de la organización | §5.2, §8, §9 | Marcarlos `INT-` y decir que se validan con la dirección y Finanzas |
| 12 | Brechas sin fila explícita en el diagnóstico | §6, §8 | Toda brecha nace de un hallazgo de §6 |
| 13 | Proyecto que llega tarde para el riesgo que trata (p. ej. renovar una certificación después de su vencimiento) | §9, §11 | Poner esos proyectos en el mes 0 o 1, con plan de contingencia |
| 14 | Fechas ambiguas tipo `10/11/2026` | Todo | Fecha escrita en palabras y ambigüedad resuelta |

## 4. Lo que no se debe decir (ni escribir)

- Nada que identifique a personas entrevistadas, clientes o sistemas sensibles. Se dice "el área analizada (PRV-001)" y las herramientas por categoría.
- Que una práctica de un área es "lo que hace la organización".
- "Certificación SOC 2", "certificación NIST", o una norma como obligatoria sin comprobar que aplica.
- En empresa privada: que el PETI "cumple MIPG" o que lo aprobó un Comité Institucional de Gestión y Desempeño.
- Que el PETI o sus proyectos están aprobados: todo es propuesto hasta que la instancia de gobierno lo apruebe con acta.
- Cifras sin fuente "porque salieron de internet" o "de la IA".

## 5. Cómo preparar la sustentación

Cuando el PETI esté cerrado, pedir a Claude un `docs/preparacion-sustentacion.md` (no se entrega) con esta estructura, que fue la que funcionó:

1. **A. La organización explicada fácil**: qué es, cómo gana dinero o cumple su misión, tres hechos recientes que cambian la TI, y la distinción que más confunde (qué TI planea el PETI y cuál queda fuera).
2. **B. Las cuatro preguntas** de la sección 1 de este archivo, respondidas con los numerales e IDs reales.
3. **C. Lo que hay que saberse de memoria**: las tres normas y los dos referentes; tabla de cifras (objetivos, metas, brechas, proyectos por fase, indicadores, riesgos, presupuesto total); dos ejemplos de la cadena de trazabilidad; qué significa cada prefijo de evidencia.
4. **Numeral por numeral**: qué dice, por qué está ahí según la norma, de dónde salió y 2-3 preguntas probables con respuesta corta.
5. **Puntos débiles conocidos**: tabla punto, dónde, respuesta corta, corrección posible. Mejor decirlos antes de que los encuentren.
6. **Lo que no se debe decir**.
