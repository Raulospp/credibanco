# PETI: contexto permanente del proyecto

Trabajo académico de Gobierno de TI: el equipo construye el **Plan Estratégico de Tecnologías de la Información (PETI)** de una organización **siguiendo la metodología del MinTIC de Colombia**, como si la organización fuera la entidad que formula su plan. El documento se escribe en español, en el registro de un plan institucional, y lo firma el equipo en el rol de área de TI de la organización (ver "Datos del proyecto").

## Datos del proyecto

> Esta tabla es lo único específico de la organización. Las skills y los agentes dicen "la organización" y leen de aquí nombre, naturaleza, alcance y horizonte. Si un dato cambia, se cambia aquí.

| Campo | Valor |
|---|---|
| Organización | Valor + S.A.S. (nombre corto: Valor+) |
| Naturaleza | Sociedad por acciones simplificada de economía mixta del Departamento de Antioquia, de nivel descentralizado por servicios (Informe de gestión 2025, pág. 3), filial del Instituto para el Desarrollo de Antioquia (IDEA). Composición accionaria verificada: **IDEA 98,95 % y FEIDEA 1,05 %** (Estados financieros a marzo de 2024, pág. 14, distribución de utilidades por participación accionaria). Con 90 % o más de capital público se somete al régimen de las empresas industriales y comerciales del Estado (Ley 489 de 1998, art. 97, parágrafo) y le aplica el MIPG (Decreto 1499 de 2017); reporta el FURAG y tiene Comité Institucional de Gestión y Desempeño (Informe de gestión 2025, págs. 9, 23 y 77). La guía del MinTIC aplica casi tal cual, no como marco adaptado |
| Sector y actividad | Tecnología para el sector público de Antioquia: BPO, ITO (tercerización de TI), KPO, procesos tecnológicos y transformación digital que facilitan el acceso de los ciudadanos a servicios del Estado. Sede en Medellín; constituida el 6 de mayo de 2016 (fuentes por registrar) |
| Países o sedes en el alcance | Colombia, Antioquia: sede administrativa Edatel (Medellín), sede Tubos Rojos, sede y bodega de Impuesto Vehicular, puestos en la Gobernación de Antioquia, Nodo Departamental y puntos externos (Informe de gestión 2024, págs. 39-40). 240 empleados en 2024 (pág. 25) |
| Alcance del PETI | Toda la organización (Valor+, Medellín). Decidido por el usuario el 5 de octubre de 2026 |
| Qué TI planea el PETI | La TI con la que Valor+ opera: estrategia y gobierno de TI, sistemas internos, infraestructura propia, mesa de servicios, seguridad, datos y uso y apropiación, **más el catálogo de los servicios tecnológicos que presta** (mesas de servicio, SOC, conectividad, desarrollo), que se listan y se miden con sus niveles de servicio. Quedan fuera, como decisión de alcance, los proyectos específicos de cada cliente (Wifi municipios, SOC IDEA, Contigo Antioquia, Conectividad Educación, mesas de la Gobernación): van como contexto y demanda en el numeral 5 y no generan proyectos del portafolio. Decidido por el usuario el 5 de octubre de 2026 |
| Horizonte | Enero de 2027 a diciembre de 2030: 4 vigencias anuales, una fase por vigencia (fase 1 = 2027 … fase 4 = 2030), alineadas con el plan de acción integrado de cada año (Decreto 612 de 2018). El PETI se formula en octubre de 2026 y reemplaza al PETI 2026-2027 de la organización. Título: "PETI 2027-2030". Decidido por el usuario el 5 de octubre de 2026 |
| Enfoque | Actualización del PETI de la organización: los PETI publicados por Valor+ (2024 y 2026-2027) se usan como fuente primaria citada, se evalúa qué se cumplió y se formula un plan propio. No se copia su texto |
| Extensión y formato | Sigue la plantilla (capítulos, subtítulos y tablas) sin volverse un documento enorme: sin límite fijo de páginas, pero con texto corto, sin repetir información entre numerales y con gráficos donde la plantilla los pide o donde los PETI de Valor+ los usan. Decisión del usuario del 5 de octubre de 2026 |
| Firma del documento | "Equipo académico del PETI, en el rol del área de TI de Valor+" |
| Instancia que aprueba el PETI | Comité Institucional de Gestión y Desempeño de Valor+ (aplica por MIPG; confirmar su existencia en las fuentes). En el ejercicio académico, la revisión la hace el docente |
| Fuente del PETI | `docs/peti.md` |
| Word entregable | `docs/PETI_Valor+_v<versión>.docx` |
| Versión vigente | 1.12 (6 de octubre de 2026): documento completo con todos los elementos de la plantilla; 23 brechas (12 crear, 11 modificar), 17 proyectos, 11 indicadores, 8 riesgos, 6.170 millones de pesos. Anexo 1 diligenciado: `docs/Anexo 1. Herramientas PETI Valor+ v1.11.xlsx` (script `llenar_anexo1.py` adaptado a Valor+) |
| Evidencia restringida | Ninguna. `docs/privado/` está vacía |

## Qué es norma, qué es referencia y qué es insumo

| Rol | Archivo | Uso |
|---|---|---|
| **Norma (metodología)** | `docs/MGGTI.GE.ES.01 - Guia de construccion PETI - Gobierno Digital-v. 3.0.pdf` | Guía del MinTIC, v3.0 de noviembre de 2023. **Dentro del PDF el código es MGGTI.GE.ES.03**; el nombre del archivo dice .01. En el PETI se cita como MGGTI.GE.ES.03. Define 4 fases y 17 actividades. |
| **Norma (estructura)** | `docs/Anexo 2. Plantilla PETI.docx` | Plantilla oficial del documento PETI (cartilla MinTIC 2023). Define capítulos y contenido mínimo. |
| **Norma (herramientas)** | `docs/Anexo 1. Herramientas_para_la_construccion_del_PETI.xlsx` | Formatos por actividad: DOFA, tendencias, estrategia de TI, catálogo de brechas, catálogo de iniciativas, hoja de vida de indicadores, plan de comunicaciones. |
| Referente del profesor | `docs/Plan-Estratégico-de-Tecnologías-de-la-Información_2025-V02.pdf` | PETI 2023-2026 de MinCiencias. Orden de capítulos y ficha de proyecto. |
| Referente del profesor | `docs/articles-274095_recurso_1.pdf` | PETI del MinTIC: capacidades institucionales, catálogo de hallazgos, indicadores. |
| Lecciones | `docs/lecciones-profesor.md` | Lo que el profesor pregunta en la sustentación y los errores que ya le costaron nota a otros grupos. Leer antes de cerrar una versión. |
| **Entregable** | `docs/peti.md` → Word | PETI con los capítulos y subtítulos de la plantilla (1 a 9, glosario, referencias y anexos A a E). Se edita el Markdown y se regenera el Word con `.claude/skills/guia-peti/scripts/plantilla_peti.py` (existe un modo compacto opcional, `PETI_COMPACTO=1`, que deja saltos de página solo antes de las portadillas; no se usa en la versión vigente), que edita una copia de la plantilla: conserva portada, separadores, estilos y tablas, y quita textos guía y ejemplos. En el Markdown, `Tabla: descripción {Tnn}` indica qué tabla de la plantilla se clona. No se usa el signo § (decisión del usuario): se escribe "numeral 7.1.6". |
| Control de evidencia | `docs/registro-de-evidencias.md` | IDs de evidencia (`PUB-`, `INT-`, `PRV-`), clasificación y reglas de uso. |
| Insumos de investigación | `docs/insumos/*.md` | Resúmenes de investigación sobre la organización (propios o generados con IA). **Son pistas, no fuentes**: ninguna cifra sale de ahí sin fuente primaria registrada. |
| Fuentes públicas de la organización | `docs/insumos/*.pdf` | Documentos publicados por Valor+ (PETI 2024 y 2026-2027, informes de gestión, planes de transparencia) y por el IDEA. Son fuente primaria: se citan con su ID `PUB-` del registro. |
| **Restringido (local, fuera de Git)** | `docs/privado/`, `docs/evidencia-privada/` | Entrevistas, documentos internos, arquitectura de sistemas. Ver reglas abajo. |

El detalle de la norma está en la skill `guia-peti`; léela antes de escribir o auditar cualquier capítulo.

## Reglas de manejo de información (no negociables)

- Los archivos restringidos **se pueden leer** para entender el AS-IS, pero **nada que permita identificar a personas, clientes o sistemas internos sensibles** (nombres, combinaciones de proveedor + tecnología + flujo + sede + rol + fechas, nombres de tablas o componentes) se copia a un archivo versionado, a un commit, a un artefacto publicado ni a la respuesta de un subagente que vaya a un archivo. En el PETI solo aparece el ID (`PRV-001`) y el alcance autorizado.
- Lo observado en un área, sede o equipo concreto se redacta como "observado en <el área analizada> (PRV-001)", nunca como política de toda la organización.
- Cada hecho del AS-IS cita su fuente. En el PETI la cita es el nombre del documento ("Informe de gestión 2025, pág. 26"), no el ID; la equivalencia ID → nombre está en la sección "Nombres de cita en el PETI" del registro (decisión del usuario, 29 de septiembre de 2026). Lo que no lo tiene es hipótesis y se redacta como tal o se marca `[EVIDENCIA: qué falta]`.
- Toda iniciativa TO-BE es **Propuesta** hasta que tenga patrocinador, caso de negocio y aprobación. Los responsables del portafolio son roles propuestos.
- No se publica nada (artefacto, gist, PR público) con contenido del PETI sin que el usuario lo pida y sin pasar la revisión de reidentificación de `evidencias-peti`.

## Adaptación de la guía según la naturaleza de la organización

La guía del MinTIC está escrita para entidades públicas. **Valor+ tiene 98,95 % de capital público**, se rige como empresa industrial y comercial del Estado y le aplica el MIPG, así que **la guía y la plantilla aplican casi tal cual**. Nunca se omite en silencio un elemento de la plantilla: se cumple o se declara "no aplica" con la razón.

Elementos de la plantilla que sí aplican (a diferencia de una empresa privada):
- Aprobación por el **Comité Institucional de Gestión y Desempeño** (existe; Informe de gestión 2025, pág. 77).
- **MIPG y FURAG** (puntaje 75 en 2025), **Decreto 612 de 2018**: PETI integrado al plan de acción y publicado en el sitio web antes del 31 de enero.
- **Actividad 12, iniciativas de otros planes**: aplica (Política de Gobierno Digital: servicios ciudadanos digitales, interoperabilidad, seguridad digital, datos abiertos), y también los planes del Decreto 612 (seguridad y privacidad, tratamiento de riesgos, plan de acción).
- **MSPI** como modelo obligatorio de seguridad y privacidad (Resolución 500 de 2021).
- **Publicación en el sitio web** (transparencia, Ley 1712 de 2014).
- **Trámites y OPA**: verificar en las fuentes; Valor+ presta servicios a entidades, no al ciudadano, así que probablemente no tiene trámites inscritos en el SUIT. Si no los tiene, se declara "no aplica" con esa razón.

## Marco normativo aplicable a Valor+ (verificar cada uno con `marcos-referencia` antes de citarlo)

- Naturaleza: Ley 489 de 1998 (art. 39 y art. 97, parágrafo: 90 % o más de capital público = régimen de EICE); Ley 1258 de 2008 (S.A.S.).
- Gestión pública: Decreto 1499 de 2017 (MIPG, aplica con 90 % o más de capital público); Decreto 612 de 2018 (planes institucionales); Ley 87 de 1993 (control interno); control fiscal de la Contraloría General de Antioquia.
- Gobierno digital: Decreto 767 de 2022 (Política de Gobierno Digital; sujetos obligados: entidades del art. 39 de la Ley 489); Decreto 1078 de 2015 (DUR-TIC); MRAE del MinTIC; Ley 2294 de 2023 (PND).
- Seguridad digital: Resolución 500 de 2021 del MinTIC (MSPI); Decreto 338 de 2022 (gobernanza de la seguridad digital); CONPES 3995 de 2020.
- Transparencia y datos: Ley 1712 de 2014 (sujetos obligados incluyen sociedades de economía mixta); Resolución 1519 de 2020 (accesibilidad y transparencia web); Ley 1581 de 2012 (datos personales); Ley 2195 de 2022 y Ley 1474 de 2011 (anticorrupción).
- Gestión documental: Ley 594 de 2000 (archivo).
- Contratación: Ley 1150 de 2007, art. 14 (régimen privado para entidades en competencia) con los principios de la función pública y publicación en el SECOP; manual de contratación propio.
- Referencias (no obligatorias): COBIT 2019, ITIL 4, ISO/IEC 27001:2022, NIST CSF 2.0, ISO/IEC 42001, CONPES 4144 de 2025 (IA).

## Hechos del contexto que conviene no olvidar

- Equipo: 6 estudiantes de Gobierno y Servicios de TI. El profesor autorizó usar una empresa mixta.
- Este proyecto reemplaza al PETI de Credibanco, que está archivado en `Desktop/archivo peti/credibanco/` (fuera del proyecto). **Ningún dato de Credibanco se usa en este PETI.**
- Fuentes ya ubicadas (por registrar en `docs/registro-de-evidencias.md`): PETI 2024 versión 2.0 de Valor+ (138 páginas, estructura de la plantilla del MinTIC), PETI 2026-2027 de Valor+, informe de gestión 2024 (`https://s3-site-vmas-cdn.s3.amazonaws.com/assets/2025/02/12152920/Informe-de-gestion-2024-actualizado.pdf`), página de filiales del IDEA.
- El PETI 2024 de Valor+ trae texto copiado de otra entidad ("el data center del Ministerio") y propone certificarse en ISO 27001: verificar antes de citar cualquier afirmación suya como hecho.
- Hay cuestionamientos de prensa sobre contratos de 2016 y 2017 (Fundación Pares): no se usan en el PETI.
- El sitio valormas.gov.co bloquea la descarga automática; los documentos se bajan desde el navegador y se guardan en `docs/insumos/`.
- Fechas: nunca se escribe `dd/mm/aaaa` en el texto; se escribe "10 de noviembre de 2026".

## Convenciones del PETI

- IDs: objetivos corporativos o institucionales `OC01…`; objetivos de TI `OETI01…` y metas `METI01…`; brechas `BRE-001…`; oportunidades `OPT-001…`; proyectos `P<fase>.<n>`; indicadores `KPI-01…`; riesgos `R01…`; evidencia `PUB-/INT-/PRV-`. **No renumeres IDs existentes** sin que el usuario lo pida: otros capítulos los referencian. La equivalencia con los IDs del Anexo 1 (`B001`, `IT001`, `OETI01`, `METI01`, `IND.ES.01`) está en `trazabilidad-peti` y en el Anexo A del PETI.
- Todo cambio de contenido del PETI se registra en `docs/control-de-cambios.md` (historial completo). El documento ya no tiene sección de control de cambios; la versión va en la portada (decisión del usuario, 30 de septiembre de 2026). La numeración de la plantilla no se modifica: lo que la plantilla no numera va como subtítulo sin número (decisión del usuario, 30 de septiembre de 2026). Antes: "Control de cambios" con versión, fecha, numerales y descripción, y actualiza la versión del encabezado y de la tabla "Datos del proyecto".
- El README lista la estructura del repositorio y cifras del PETI (proyectos, brechas). Si cambias esas cifras en el PETI, actualiza el README en el mismo cambio.

## Cómo trabajar

| Tarea | Usa |
|---|---|
| Entender qué exige la guía o la plantilla para un capítulo | skill `guia-peti` |
| Redactar, reescribir, recortar o "humanizar" texto del PETI | skill `redaccion-peti` (incluye `estilo-natural.md`) |
| Buscar, registrar o citar una fuente; clasificar información; revisar reidentificación | skill `evidencias-peti` |
| Citar COBIT, TOGAF, ITIL, ISO 27001/42001, NIST, SOC 2, normas colombianas | skill `marcos-referencia` |
| Comprobar la cadena objetivo → brecha → proyecto → indicador → riesgo | skill `trazabilidad-peti` (tiene script) |
| Auditoría completa del PETI | `/auditar-peti` (orquesta los agentes) |
| Conformidad con guía, plantilla y Anexo 1 | agente `auditor-conformidad` |
| Evidencia, clasificación y reidentificación | agente `auditor-evidencias` |
| Verificar en la web afirmaciones públicas sobre la organización y los marcos | agente `verificador-fuentes` |
| Commit | `/commit` |

Orden recomendado para construir el PETI desde cero: §2 alcance → §5 contexto (con evidencia) → §6 situación actual por dominio + DOFA → §7 situación objetivo con metas → §8 brechas (comparando §6 y §7 fila por fila) → §9 portafolio → §10 indicadores → §11 riesgos → §12-§13 comunicación y gobierno → §4 metodología, §1 introducción, §3 marco normativo, §14-§15 glosario y referencias. Después, `/auditar-peti`.

## Herramientas locales

- `python` con `python-docx` (para el Word). Instalar con `pip install python-docx` si falta.
- `pdftotext` (Poppler; viene con Git Bash en algunas instalaciones) para leer los PDF. Si no está, `extraer_referencias.py` intenta con `pypdf` (`pip install pypdf`).
- Para leer los anexos `.docx`/`.xlsx` y los PDF sin pelear con la codificación, usa `python .claude/skills/guia-peti/scripts/extraer_referencias.py <carpeta temporal>`; escribe texto plano.
- Las rutas con tildes (el PDF de MinCiencias) fallan en `pdftotext` directo desde Bash; el script las resuelve.
- Equipo de Raul (verificado el 29 de septiembre de 2026): Python 3.13.1; `python-docx` instalado con pip en esa fecha; `pdftotext` disponible en `/mingw64/bin` (Git Bash), así que `pypdf` no hace falta. `extraer_referencias.py` generó los 5 textos sin errores.
- La carpeta del proyecto **no es un repositorio Git propio**: Git toma como raíz `C:\Users\Raul`, con otro remoto. Por decisión del usuario (29 de septiembre de 2026) se trabaja sin Git; no usar `/commit` hasta crear un repositorio propio con `git init` en la carpeta del proyecto.
- Los PDF de `docs/insumos/` se leen con `pdftotext -layout -enc UTF-8 <pdf> <txt>` a una carpeta temporal; sin `-enc UTF-8` las tildes salen dañadas en la consola.
