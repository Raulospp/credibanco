---
name: evidencias-peti
description: Usar cuando hay que respaldar con evidencia una afirmación del PETI (AS-IS, motivadores, contexto de la organización, certificaciones, alianzas, cifras), buscar la fuente primaria de un dato, registrar una fuente nueva en docs/registro-de-evidencias.md, clasificar información como pública, interna, restringida o propuesta, decidir si algo de las entrevistas o de documentos internos puede aparecer en el PETI, hacer la revisión de reidentificación antes de compartir, o armar la sección de referencias bibliográficas.
argument-hint: "[afirmación, fuente o numeral]"
---

# Evidencia, clasificación y fuentes del PETI

## Principio

Una fuente que no se abrió no existe. Un hecho del PETI vale si tiene un ID en `docs/registro-de-evidencias.md` que apunte a una fuente abierta en una sesión, con fecha de consulta y alcance. Lo que no tiene ID es hipótesis. Esto es lo que separa un PETI defendible de un resumen de la página web de la organización o de lo que "dijo la IA".

La segunda mitad del principio es de confidencialidad: la evidencia restringida sostiene el diagnóstico, pero no se ve en el documento. Solo se ve su ID y lo que el alcance autorizado permite decir.

## Clasificación (del registro)

| Marca | Qué es | En el PETI |
|---|---|---|
| **Público** (`PUB-`) | Fuente abierta: sitio oficial de la organización, informe de gestión, comunicado, norma, registro público, página de un socio o de un organismo certificador | Se cita con ID; va a referencias bibliográficas |
| **Interno** (`INT-`) | Análisis del equipo del PETI (DOFA, objetivos formulados por el equipo, estimaciones, supuestos de costo, afirmaciones de ausencia) | Se cita con ID como "elaboración propia"; no se comparte fuera del equipo sin aprobación |
| **Restringido** (`PRV-`) | Entrevistas, documentos internos, arquitectura u operación de sistemas, información contractual o de personas | Solo el ID y el alcance autorizado; el archivo queda en `docs/privado/`, fuera de Git |
| **Propuesto** | Objetivo o decisión no aprobada | No se presenta como estado actual; responsable y puerta de decisión |

Crea `INT-001` con el primer análisis interno que se cite (DOFA, supuestos de costo, objetivos corporativos formulados por el equipo si la organización no los publica). Una afirmación de ausencia ("no existe catálogo de servicios") se respalda con `INT-` y se redacta "no se encontró en la evidencia revisada".

## Procedimiento para respaldar una afirmación

1. **Descomponer** la afirmación en la unidad verificable ("la empresa tiene 2.000 empleados en 5 sedes" → cifra, año, quién la publica, qué cuenta).
2. **Buscar si ya tiene ID** en el registro. Si lo tiene, revisa que el alcance cubra lo que el texto dice.
3. **Buscar la fuente de mayor jerarquía** (tabla siguiente) con `WebSearch` y ábrela con `WebFetch`. Los `docs/insumos/*.md` y las respuestas de chats con IA sirven solo como pista de qué buscar.
4. **Leer** el fragmento que respalda la afirmación y anotar URL, título, entidad, fecha de publicación y fecha de consulta.
5. **Clasificar** y **registrar** una fila nueva: ID, clasificación, fuente y fecha (con enlace), afirmación que puede soportar, alcance o limitación. El alcance dice también lo que la fuente **no** prueba.
6. **Reformular** la afirmación del PETI al tamaño de la evidencia. Si la fuente dice menos, el texto dice menos. Si la contradice, se reporta y se corrige el texto, nunca la fuente.

Si no hay acceso web en la sesión, entrega la afirmación con `[EVIDENCIA: qué buscar y dónde]` y no la registres.

## Jerarquía de fuentes

| Tema | Fuente preferida | Aceptable | Débil (no sostiene un hecho sola) |
|---|---|---|---|
| Datos de la organización, misión, visión, oferta | Sitio oficial, informe de gestión o de sostenibilidad, plan estratégico publicado | Comunicado de un socio o de la casa matriz | Blogs, agregadores, Wikipedia, perfiles de LinkedIn |
| Naturaleza jurídica, propiedad, tamaño | Registro mercantil (RUES), Superintendencia de Sociedades, reporte a bolsa, comunicado oficial | Prensa económica de referencia | Directorios comerciales |
| Entidad pública: planes, presupuesto, contratos | Sitio oficial de la entidad, SECOP, FURAG, datos abiertos | Informes de entes de control | Prensa |
| Certificaciones | Certificado o registro del organismo certificador, declaración oficial de la organización | Página de un cliente con número de certificado | Menciones en propuestas o blogs |
| Alianzas y reconocimientos | Página del socio o del analista que lo otorga | Comunicado de la organización | Notas de prensa pagadas |
| Operación interna (procesos, herramientas, roles) | Entrevistas y documentos del equipo (`PRV-`) | Ofertas de empleo oficiales (solo para "usa la tecnología X") | Suposición a partir de la industria |
| Marcos y normas | Emisor oficial (ISO, NIST, AICPA, ISACA, The Open Group, PeopleCert, MinTIC, Función Pública, Secretaría del Senado) | Resumen oficial del emisor | Blogs de consultoras |

## Revisión de reidentificación (antes de compartir o publicar)

Para cada mención de material restringido (entrevistas, documentos internos, sistemas):

1. ¿Aparece el nombre de una persona, un cliente, un proyecto, un sistema interno o una tabla? → se elimina o se generaliza por categoría ("la plataforma de gestión de proyectos", "un proveedor de nube").
2. ¿La combinación de **área + proveedor + tecnología + flujo + sede + rol + fecha** permitiría a alguien identificar a la persona entrevistada o a un cliente? → se generaliza el elemento más específico.
3. ¿Se atribuye a toda la organización algo que solo se observó en un área, sede o equipo? → se acota ("observado en el área analizada (PRV-001)").
4. ¿Hay copias literales de los archivos restringidos en el PETI, en un commit, en un artefacto o en un mensaje de agente? → se retiran y se avisa.
5. ¿Algún archivo restringido dejó de estar en `.gitignore` o aparece en `git status`? → se detiene todo y se avisa.

La revisión se reporta como tabla: fragmento (sin reproducir el dato sensible), riesgo, cambio propuesto.

## Contrato de salida

Por cada afirmación trabajada:

| Campo | Contenido |
|---|---|
| Afirmación | Texto exacto del PETI |
| Estado | respaldada / parcialmente respaldada / no encontrada / contradicha / restringida |
| ID | Existente o propuesto (fila nueva para el registro) |
| Enlace | URL abierta y fecha de consulta |
| Fragmento | Cita breve o dato con su ubicación |
| Alcance | Qué prueba y qué no |
| Redacción sugerida | Oración con el ID |

Más, si se pidió registrar: las filas listas para pegar en el registro.

## Referencias bibliográficas

El PETI necesita un numeral de referencias (§15; la plantilla lo pide). Se construye a partir de las filas `PUB-` del registro y de los marcos y normas nombrados, en APA 7, con el formato de [formato-referencias.md](formato-referencias.md). Las filas `PRV-` no van a la bibliografía; se mencionan en la metodología como "entrevistas y documentación interna, anonimizadas".

## Lo que esta skill no hace

- No da por verificada una fuente que no abrió.
- No copia contenido restringido a ningún archivo versionado, ni siquiera "anonimizado a mano".
- No reemplaza la aprobación del propietario de la información para publicar algo `INT-` o `PRV-`.
