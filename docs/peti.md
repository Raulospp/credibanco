# Plan Estratégico de Tecnologías de la Información (PETI) 2027-2030

Valor + S.A.S. — toda la organización

Versión 1.12 — 6 de octubre de 2026 — propuesta sujeta a aprobación


## Introducción

Valor + S.A.S. es una sociedad de economía mixta del Departamento de Antioquia, filial del IDEA, que integra soluciones de tecnología y procesos para entidades públicas: mesas de servicio, conectividad, ciberseguridad, recaudo, gestión documental y contact center (Informe de gestión 2025, pág. 3). En 2025 tuvo ingresos operacionales de 86.700 millones de pesos y 48 contratos activos, 60 % más que en 2024 (Informe de gestión 2025, págs. 129-130).

Este documento es el Plan Estratégico de Tecnologías de la Información (PETI) de Valor+ para las vigencias 2027 a 2030. Se construyó con la Guía MGGTI.GE.ES.03 v3.0 del MinTIC, su plantilla y sus herramientas, en el marco de la Política de Gobierno Digital (Decreto 767 de 2022) y del Marco de Referencia de Arquitectura Empresarial (MRAE). Como Valor+ tiene 98,95 % de capital público y aplica el MIPG, la guía se aplica casi tal cual. Reemplaza al PETI 2026-2027 de Valor+.

El plan contiene:

- el marco normativo y el contexto de la organización;
- la situación actual de los siete dominios de TI, con su DOFA y las tendencias;
- la situación objetivo, con seis objetivos de TI y once metas por año;
- 23 brechas y un portafolio de 17 proyectos en cuatro fases, con presupuesto estimado y mapa de ruta;
- once indicadores con hoja de vida, ocho riesgos y la estrategia de comunicación.

Los beneficios esperados a 2030 son:

- que la auditoría interna califique el proceso de Gestión de TI con 90 % o más, desde el 49 % de 2025 (KPI-01);
- que 13 de los 16 procesos tengan sistemas de información completos en lugar de hojas de cálculo (KPI-06);
- que todos los servicios de TI tengan acuerdos de nivel de servicio medidos (KPI-04);
- que la madurez de seguridad pase de 47 a 76 sobre 100 en la escala del MSPI (KPI-10);
- que la recuperación de los servicios críticos se pruebe con éxito cada año (KPI-09).

## Objetivo y Alcance

### Objetivo del Documento

Definir la estrategia de TI de Valor+ para las vigencias 2027 a 2030, alineada con los objetivos del Plan Estratégico Institucional (PEI) 2024-2027 y con las obligaciones que tiene la organización como sociedad de economía mixta con 98,95 % de capital público. El PETI 2027-2030 reemplaza al PETI 2026-2027 de Valor+, evalúa qué se logró con él y fija el plan de los cuatro años siguientes: brechas, proyectos, presupuesto, indicadores y riesgos.

### Alcance del documento

El PETI cubre toda la organización durante cuatro vigencias, de enero de 2027 a diciembre de 2030. Cada vigencia es una fase del plan y se integra al plan de acción de ese año, como lo pide el Decreto 612 de 2018. Aborda las cuatro fases de la guía del MinTIC (planear, analizar, construir y socializar) y los siete dominios de gestión de TI: estrategia de TI, gobierno de TI, gestión de información, sistemas de información, infraestructura de TI, uso y apropiación y seguridad de la información.

En Valor+ la tecnología cumple dos papeles: soporta la operación interna y es parte de lo que la empresa vende. Por eso el plan cubre dos cosas:

- La TI interna: estrategia y gobierno de TI, sistemas propios, infraestructura, mesa de servicios, seguridad, datos y uso y apropiación.
- El catálogo de servicios tecnológicos que Valor+ presta a sus clientes (mesas de servicio, centro de operaciones de seguridad, conectividad, desarrollo de software). Se lista y se mide con sus acuerdos de niveles de servicio (ANS).

Quedan fuera los proyectos específicos de cada cliente, por ejemplo la conectividad de sedes educativas rurales o la telemedicina de Contigo Antioquia Salud. Esos proyectos aparecen en el numeral 5 como contexto y como demanda sobre la TI de Valor+, pero no generan proyectos en el portafolio de este plan, porque su alcance, su presupuesto y su cronograma los fija cada contrato.

Alcance de la evidencia. El diagnóstico se construye solo con documentos públicos de Valor+: el PETI 2026-2027 (versión 4.0), los informes de gestión 2024 y 2025, los estados financieros a marzo de 2024 y su sitio web. Se completa con la página de filiales del IDEA y con las normas que aplican a la organización. No hubo entrevistas ni acceso a documentos internos. Por eso algunos datos (número de colaboradores de TI, presupuesto de TI detallado, inventario completo de equipos) se marcan como pendientes o se estiman y se dice que son estimaciones.

## Normatividad

La tabla recoge las normas que aplican a Valor+ por su naturaleza (sociedad de economía mixta con más de 90 % de capital público) y por sus servicios, y dice qué exige cada una a la TI. Las de referencia no son obligatorias; se usan como buena práctica.

Tabla: Marco normativo {T0}

| Norma | Qué exige a la TI de Valor+ | Aplicación |
|---|---|---|
| Ley 489 de 1998, arts. 39 y 97 | Con 90 % o más de capital público, Valor+ se rige como empresa industrial y comercial del Estado y hace parte de la Rama Ejecutiva | Aplica: es la razón por la que aplican las normas siguientes |
| Ley 1258 de 2008 | Régimen de la sociedad por acciones simplificada | Aplica (forma societaria) |
| Decreto 1083 de 2015, modificado por el Decreto 1499 de 2017 (MIPG) | Integrar la gestión, reportar el FURAG y tener Comité Institucional de Gestión y Desempeño, que aprueba el PETI | Aplica |
| Decreto 415 de 2016 (adiciona el Decreto 1083 de 2015) | Que el líder de TI esté en el nivel directivo y dependa del representante legal, para el fortalecimiento institucional en TI | Aplica y se cumple: la Gerencia de Tecnología, Innovación y Sostenibilidad depende de la Gerencia General (numeral 5.3) |
| Decreto 612 de 2018 | Integrar el PETI y los planes de seguridad y de tratamiento de riesgos al plan de acción, y publicarlos antes del 31 de enero | Aplica (numerales 8 y 9) |
| Decreto 1078 de 2015, modificado por el Decreto 767 de 2022 (Política de Gobierno Digital) | Arquitectura de TI, seguridad y privacidad, datos y servicios digitales | Aplica; los servicios ciudadanos digitales no, porque no hay trámites (numeral 5.1.7) |
| Decreto 620 de 2020 (servicios ciudadanos digitales) | Autenticación digital, interoperabilidad y carpeta ciudadana para los trámites | No aplica: Valor+ no tiene trámites para la ciudadanía (numeral 5.1.7) |
| Resolución 500 de 2021 del MinTIC (MSPI) | Modelo de Seguridad y Privacidad de la Información | Aplica (numerales 6.7 y 7.5) |
| Decreto 338 de 2022 y CONPES 3995 de 2020 | Gobernanza de la seguridad digital y reporte de incidentes | Aplica (P1.4) |
| Ley 1712 de 2014, Decreto 103 de 2015 y Resolución 1519 de 2020 del MinTIC | Publicación de información, accesibilidad web, costos de reproducción y datos abiertos | Aplica; Valor+ ya obtuvo 94 en el ITA (Informe de gestión 2025, pág. 12) |
| Ley 2195 de 2022 y Ley 1474 de 2011 | Programa de Transparencia y Ética Pública, antes Plan Anticorrupción | Aplica (numeral 8, otros planes) |
| Ley 1581 de 2012 | Protección de datos personales de clientes, ciudadanos y colaboradores | Aplica (P2.1) |
| Ley 594 de 2000, Decreto 1080 de 2015 y Acuerdo 001 de 2024 del Archivo General de la Nación | Gestión documental, documento electrónico y preservación digital | Aplica (P2.5) |
| Ley 1755 de 2015 | Términos de respuesta de las peticiones (PQRSD) | Aplica (canales del numeral 5.1.7) |
| Ley 87 de 1993 | Sistema de control interno y tercera línea de defensa | Aplica (numeral 7.2) |
| Ley 1150 de 2007, art. 14 | Régimen de contratación de las sociedades de economía mixta en competencia, con publicidad en el SECOP | Aplica a las compras de TI, según el manual de contratación de Valor+ |
| Resolución 2710 de 2017 del MinTIC, modificada por la Resolución 1126 de 2021 | Transición a IPv6; las entidades del orden territorial debían terminarla a más tardar el 31 de diciembre de 2022 | Aplica: el plazo venció y no se encontró evidencia de IPv6 en la red propia; diagnóstico en 2027 (P1.6) e implementación en 2028 (P2.4) |
| Ley 2294 de 2023 (Plan Nacional de Desarrollo 2022-2026) y Plan de Desarrollo de Antioquia 2024-2027 "Por Antioquia Firme" | Orientación de la transformación digital y la conectividad del departamento | Contexto (numeral 5) |
| CONPES 4144 de 2025 | Política nacional de inteligencia artificial | Referencia para la política de uso de IA (P2.1) |
| COBIT 2019, ITIL 4, ISO/IEC 27001:2022, ISO 22301:2019, MoReq | Buenas prácticas de gobierno, servicios, seguridad, continuidad y gestión documental | Referencia (Anexo B) |

## Metodología

El PETI se construyó con las cuatro fases y las diecisiete actividades de la Guía MGGTI.GE.ES.03 v3.0 del MinTIC, en orden, con su plantilla y las herramientas del Anexo 1.

- **Planear.** Actividades 1 a 3: equipo, presupuesto y cronograma de construcción del PETI (Anexo E).
- **Analizar.** Actividad 4, entorno organizacional (numeral 5); actividad 5, compromisos externos (numeral 5, motivadores); actividad 6, diagnóstico y DOFA por dominio (numeral 6); actividad 7, tendencias (numeral 6).
- **Construir.** Actividad 8, estrategia de TI (numeral 7.1); actividades 9 y 10, situación objetivo y oportunidades (numerales 7 y 8); actividad 11, brechas; actividad 12, otros planes; actividad 13, portafolio y mapa de ruta (numeral 8); actividad 14, indicadores (numeral 7.1.6); actividad 15, este documento.
- **Socializar.** Actividad 16, aprobación y publicación; actividad 17, plan de comunicación (numeral 9).

Por la naturaleza de Valor+, los elementos de la guía pensados para entidades públicas aplican así:

- MIPG, FURAG y Comité Institucional de Gestión y Desempeño: aplican tal cual. El Comité Institucional es la instancia que aprueba el PETI (Informe de gestión 2025, pág. 77). En el ejercicio académico, la revisión la hace el docente.
- Decreto 612 de 2018: aplica. Cada fase del plan es una vigencia (2027 a 2030) que entra al plan de acción de ese año, y el PETI se publica en el sitio web antes del 31 de enero.
- Actividad 12, otros planes: aplica (numeral 8, iniciativas de otros planes).
- Trámites y OPA: no aplican, porque Valor+ declara que no tiene trámites para la ciudadanía (numeral 5.1.7).
- Presupuesto para elaborar el PETI (actividad 2): lo elabora un equipo académico, sin costo para la organización (Anexo E).

Fuentes: documentos públicos de Valor+ (PETI 2026-2027, informes de gestión 2024 y 2025, estados financieros, sitio web), de la Gobernación de Antioquia y del IDEA, y las normas. Se citan por su nombre. No hubo entrevistas ni acceso a documentos internos, así que lo que no está en esas fuentes se marca como estimación del equipo o como pendiente.

## Contexto y Modelo operativo de la entidad

Los motivadores salen de lo que Valor+ publica sobre su estrategia y sus resultados, y de las normas que la obligan dentro del horizonte del plan. Cada uno dice qué le exige a la TI.

Tabla: Motivadores estratégicos {T1}

| Motivador | Qué le exige a la TI | Fuente |
|---|---|---|
| PEI 2024-2027, con cinco objetivos estratégicos y un avance de ejecución de 89,65 % al cierre de 2025 | Las iniciativas de TI se alinean con los cinco objetivos. El PEI vence en 2027, a mitad del horizonte de este PETI, así que el plan debe revisarse cuando se apruebe el PEI siguiente | Informe de gestión 2025, págs. 13 y 16 |
| Crecimiento del negocio: los ingresos operacionales pasaron de 54.054 millones de pesos en 2024 a 86.700 millones en 2025 (60 % más), y los contratos activos de 34 a 48 | La TI interna (mesa de servicios, sistemas de apoyo, seguridad) tiene que atender más contratos sin perder los ANS | Informe de gestión 2025, págs. 129-130 |
| Auditoría interna 2025: el proceso de Gestión de TI obtuvo 49 %, el puntaje más bajo de los procesos auditados | Las acciones de mejora abiertas en el Plan de Mejoramiento Institucional son prioridad del primer año del plan | Informe de gestión 2025, pág. 49 |
| Medición del desempeño institucional (FURAG 2024): índice de 74,7 puntos; Gobierno Digital 86,3 y Seguridad Digital 85,2 | Mantener o subir esas dos políticas. Talento humano (57,5) y gestión del conocimiento (64,4) son las dimensiones más bajas y tienen componente de TI | Informe de gestión 2025, págs. 9-11 |
| Índice de Transparencia y Acceso a la Información (ITA): 94 puntos en 2025 | Sostener la publicación de información en el sitio web, que opera la TI | Informe de gestión 2025, pág. 12 |
| Madurez de la gestión de proyectos en nivel 1 (inicial) y una oficina de gestión de proyectos (PMO) en construcción | Los proyectos de TI deben adoptar la metodología que defina la PMO | Informe de gestión 2025, págs. 36-37 |
| Gestión documental: tablas de retención y de valoración documental en revisión del Consejo Departamental de Archivo; sistema de gestión de documentos electrónicos de archivo (SGDEA) en diseño con la Gerencia de TI | Implementar el SGDEA y la preservación digital según el Acuerdo 001 de 2024 del Archivo General de la Nación | Informe de gestión 2025, págs. 76-77 |
| Seguridad digital: sistema de gestión de seguridad de la información en actualización, adopción del Modelo de Seguridad y Privacidad de la Información (MSPI) y meta de certificar la continuidad del negocio en ISO 22301:2019 | Continuar el MSPI (Resolución 500 de 2021) y la certificación en ISO 22301 | Informe de gestión 2025, pág. 89; PETI 2026-2027 de Valor+ |
| Auditoría de la Contraloría General de Antioquia a la vigencia 2024: control fiscal interno calificado con 2,0 (con deficiencias) | Mejorar la trazabilidad de la contratación y de los soportes de ejecución, que hoy dependen de hojas de cálculo | Informe de gestión 2025, pág. 126 |
| Plan de Desarrollo Departamental 2024-2027 "Por Antioquia Firme", aprobado por la Asamblea el 28 de mayo de 2024, con el legado "Firmes por la conectividad física y digital" (fibra óptica e internet satelital en las subregiones) | Demanda de servicios de conectividad, mesas de ayuda y seguridad para entidades del departamento. El plan departamental termina en 2027; el siguiente gobierno aprobará otro para 2028-2031, dentro del horizonte de este PETI | Gobernación de Antioquia, noticia de aprobación del Plan de Desarrollo 2024-2027; Informe de gestión 2025, págs. 89-90 |

### Contexto Institucional

Valor + S.A.S. es una sociedad por acciones simplificada de economía mixta del Departamento de Antioquia, del nivel descentralizado por servicios (Informe de gestión 2025, pág. 3). Es filial del Instituto para el Desarrollo de Antioquia (IDEA) (página de filiales del IDEA). Sus accionistas son el IDEA, con 98,95 %, y el Fondo de Empleados del IDEA (FEIDEA), con 1,05 % (Estados financieros a marzo de 2024, pág. 14). Con más de 90 % de capital público, se rige por las normas de las empresas industriales y comerciales del Estado (Ley 489 de 1998, art. 97, parágrafo), aplica el Modelo Integrado de Planeación y Gestión (MIPG) y tiene Comité Institucional de Gestión y Desempeño (Informe de gestión 2025, págs. 9 y 77).

Su objeto social es prestar, comercializar y asesorar soluciones para administrar información, recursos y comunicaciones: procesos de soporte, recaudo y facturación, administración de infraestructura tecnológica, servicios de BPO y contact center, conectividad y gerencia de proyectos (Informe de gestión 2025, pág. 3). Sus clientes son, sobre todo, entidades públicas de Antioquia: la Gobernación, el IDEA, alcaldías y entidades descentralizadas (Informe de gestión 2025, pág. 92).

#### Misión

"Somos creadores e integradores de soluciones basadas en tecnología y procesos, que contribuyen a la generación de valor en las empresas y entidades públicas, facilitando su transformación digital y contribuyendo a un futuro inclusivo y sostenible" (Informe de gestión 2025, pág. 4).

#### Visión

"Para 2027, seremos un referente en la integración de soluciones tecnológicas y sostenibles en la gestión pública" (Informe de gestión 2025, pág. 4). La visión termina en 2027, el primer año de este plan; el PETI se ajustará cuando la organización apruebe la siguiente.

#### Objetivos Estratégicos

Son los cinco objetivos del PEI 2024-2027, aprobado por el Comité Institucional de Gestión y Desempeño el 25 de noviembre de 2024, Acta 006 (Informe de gestión 2025, pág. 13; PETI 2026-2027 de Valor+, pág. 19). Se identifican como OC01 a OC05 para trazarlos con los objetivos de TI.

Tabla: Objetivos corporativos {T2}

| ID | Objetivo | Fuente |
|---|---|---|
| OC01 | Fortalecer la gobernanza para mejorar la transparencia, eficiencia y eficacia | OE1 del PEI 2024-2027 |
| OC02 | Articular la gestión institucional y el modelo organizacional para aumentar la productividad operativa | OE2 del PEI 2024-2027 |
| OC03 | Aumentar la sostenibilidad financiera a través de la diversificación de ingresos y la optimización de costos | OE3 del PEI 2024-2027 |
| OC04 | Mejorar la experiencia del cliente y aumentar la satisfacción para fomentar la lealtad y el crecimiento del negocio | OE4 del PEI 2024-2027 |
| OC05 | Consolidar a Valor+ como el principal aliado en el desarrollo e innovación tecnológica para el sector público en el departamento de Antioquia | OE5 del PEI 2024-2027 |

#### Metas de la entidad

El PEI se mide con indicadores estratégicos por proceso. Los resultados de 2025 sirven de línea base para el plan.

Tabla: Metas corporativas e indicadores de referencia {T3}

| Objetivo | Indicador | Meta 2025 | Resultado 2025 | Fuente |
|---|---|---|---|---|
| OC01 | Puntaje FURAG | 70 | 75 | Informe de gestión 2025, pág. 23 |
| OC01 | Puntaje ITA | 92 | 94 | Informe de gestión 2025, pág. 23 |
| OC02 | Ejecución del plan de acción institucional | ≥ 90 % | 54,84 % | Informe de gestión 2025, pág. 24 |
| OC03 | Facturación de ingresos frente a lo planeado | ≥ 80 % | 77,83 % | Informe de gestión 2025, pág. 16 |
| OC03 | Presupuesto de costos optimizado | ≥ 93 % | 80,72 % | Informe de gestión 2025, pág. 17 |
| OC04 | Cumplimiento de los ANS contractuales | ≥ 94 % | 95,71 % | Informe de gestión 2025, pág. 16 |
| OC04 | Índice de satisfacción del cliente | 100 % | 99 % | Informe de gestión 2025, pág. 92 |
| OC05 | Registros de propiedad intelectual aprobados | ≥ 4 | 2 | Informe de gestión 2025, pág. 17 |

La asignación de cada indicador a un objetivo es del equipo (análisis del equipo); el informe los presenta por proceso.

### Estructura Organizacional

El organigrama vigente se adoptó con la Decisión Empresarial 064 de agosto de 2024 (PETI 2026-2027 de Valor+, pág. 27). De la Gerencia General dependen la Oficina de Control Interno, la Coordinación de Comunicaciones, la Secretaría General, la Dirección de Planeación y Proyectos, la Dirección Comercial y de Mercadeo, la Gerencia Financiera, la Gerencia de Operaciones y la Gerencia de Tecnología, Innovación y Sostenibilidad (PETI 2026-2027 de Valor+, págs. 27-29).

Figura: Organigrama de Valor+ por áreas. Fuente: elaboración del equipo a partir del organigrama de la Decisión Empresarial 064 de 2024 (PETI 2026-2027 de Valor+, págs. 27-31) {img:docs/figuras/organigrama.png}

La Gerencia de Tecnología, Innovación y Sostenibilidad responde por la infraestructura, el software, el soporte a los colaboradores, la seguridad de la información y la innovación (PETI 2026-2027 de Valor+, pág. 29). Además de atender la TI interna, ejecuta proyectos para clientes, y por eso en el mapa de procesos la Gestión de TI es un proceso misional (Informe de gestión 2025, pág. 80). Se organiza en tres direcciones: Infraestructura, Servicios, y Desarrollo y Servicios (PETI 2026-2027 de Valor+, pág. 31). Según el conteo del equipo sobre ese organigrama, la gerencia tiene 76 cargos, de los cuales 49 son auxiliares operativos de la Dirección de Desarrollo y Servicios (análisis del equipo). El detalle de la estructura de TI va en el numeral 6.2.4.

Valor+ tenía 240 empleados en 2024 (Informe de gestión 2024, pág. 25). La cifra no incluye necesariamente al personal de los proyectos: solo el proyecto de Relación Estado-Ciudadano de la Gobernación tuvo 139 personas en 2025 (Informe de gestión 2025, pág. 103). El informe de 2025 no publica el total.

La sede administrativa es la sede Edatel, en Medellín, a la que la empresa se trasladó en 2024. También opera en la sede Tubos Rojos, en la sede de Impuesto Vehicular y su bodega, en la Gobernación de Antioquia, en el Nodo Departamental y en puntos externos (Informe de gestión 2024, págs. 39-40).

### Modelo Operativo

El mapa de procesos se actualizó con la Decisión Empresarial 113, aprobada en el Comité Institucional de Gestión y Desempeño en 2025 (Informe de gestión 2025, pág. 52). Tiene 16 procesos: 4 estratégicos, 2 estratégicos transversales, 3 misionales, 6 de apoyo y 1 de evaluación (Informe de gestión 2025, págs. 7-8). El mapa pone al cliente en el centro: alrededor están los misionales, luego los de apoyo y los estratégicos; los dos transversales (estrategia institucional y gestión de la arquitectura) rodean a todos, y el de evaluación cierra el círculo. El PETI 2026-2027 de Valor+ todavía describe el mapa anterior del PEI (págs. 24-26). Este plan usa el de 2025.

Figura: Mapa de procesos de Valor+. Fuente: Informe de gestión 2025, pág. 8 {img:docs/figuras/mapa_procesos.png}

#### 5.1 Descripción de los procesos

Los nombres y la clasificación salen del Informe de gestión 2025, que organiza sus capítulos por tipo de proceso. Los objetivos son un resumen del equipo a partir de ese informe y del PETI 2026-2027 de Valor+ (análisis del equipo).

#### 5.1.1 Procesos estratégicos

Tabla: Procesos estratégicos {T4}

| ID | Nombre | Objetivo |
|---|---|---|
| PE01 | Gestión de la estrategia institucional (transversal) | Formular el PEI y el plan de acción, y medir el desempeño institucional (FURAG, ITA) |
| PE02 | Gestión del riesgo y continuidad | Identificar y tratar los riesgos de la organización y asegurar la continuidad del negocio |
| PE03 | Gestión de proyectos | Formular y acompañar proyectos con una metodología común, a través de la PMO |
| PE04 | Gestión del capital humano | Gestionar el ingreso, el desarrollo, el bienestar y el cambio organizacional |
| PE05 | Gestión del conocimiento e innovación | Capacitar a los colaboradores y gestionar la innovación aplicada |
| PE06 | Gestión de la arquitectura empresarial (transversal) | Alinear procesos, estructura y tecnología, y coordinar las auditorías internas de calidad |

Fuente: Informe de gestión 2025, págs. 8-52. PE01 y PE06 son los dos estratégicos transversales del mapa.

#### 5.1.2 Procesos misionales

Tabla: Procesos misionales {T5}

| ID | Nombre | Objetivo |
|---|---|---|
| PM01 | Gestión de TI (Gerencia de Tecnología, Innovación y Sostenibilidad) | Prestar servicios tecnológicos a clientes (conectividad, mesas de ayuda, ciberseguridad, desarrollo) y operar la TI interna según los ANS |
| PM02 | Gestión comercial | Conseguir y retener clientes, estructurar propuestas y medir la satisfacción |
| PM03 | Gestión del servicio | Planear, ejecutar y controlar la operación de los servicios contratados: recaudo, BPO, contact center, gestión documental |

Fuente: Informe de gestión 2025, págs. 80, 92 y 99.

#### 5.1.3 Procesos de apoyo

Tabla: Procesos de apoyo {T6}

| ID | Nombre | Objetivo |
|---|---|---|
| PA01 | Gestión contractual | Celebrar y supervisar los contratos según el manual de contratación |
| PA02 | Gestión de compras | Adquirir bienes y servicios y gestionar a los proveedores |
| PA03 | Gestión de comunicaciones | Gestionar la comunicación interna y externa y la imagen institucional |
| PA04 | Gestión jurídica | Asesorar jurídicamente, defender a la entidad y gestionar el gobierno corporativo |
| PA05 | Gestión administrativa | Gestionar los recursos físicos, logísticos y documentales |
| PA06 | Gestión financiera | Gestionar presupuesto, contabilidad, tesorería, facturación y cartera |

Fuente: Informe de gestión 2025, págs. 52-80 y 126.

#### 5.1.4 Procesos de evaluación y control

Tabla: Procesos de evaluación y control {T7}

| ID | Nombre | Objetivo |
|---|---|---|
| PV01 | Gestión de seguimiento, control y evaluación a la gestión | Auditar los procesos, rendir los informes de ley, hacer seguimiento al Plan de Mejoramiento Institucional y relacionarse con los entes de control |

Fuente: Informe de gestión 2025, pág. 124.

#### 5.1.5 Alineación de TI con los procesos

Según el PETI 2026-2027 de Valor+, los procesos misionales de gestión del servicio no tienen sistemas de información propios: se manejan con hojas de Excel, lo que "genera una alta carga operativa y dificulta el control" (pág. 33). Los procesos estratégicos y de apoyo sí tienen sistemas, propios o contratados como software como servicio (SaaS) (pág. 34). El cubrimiento de la tabla es una valoración del equipo (análisis del equipo).

Tabla: Alineación de TI con los procesos institucionales {T8}

| ID | Proceso | Categoría | Sistema de información | Cubrimiento | Oportunidad de mejora con tecnología |
|---|---|---|---|---|---|
| PE01 | Estrategia institucional | Estratégico | FURAG, Power BI, Gestión Transparente | Parcial | Tablero integrado de indicadores del PEI y del plan de acción |
| PE02 | Riesgo y continuidad | Estratégico | Ninguno específico: matriz de riesgos parametrizada en 2025, sin software dedicado (Informe de gestión 2025, pág. 33) | Sin cobertura | Herramienta de gestión de riesgos y de continuidad |
| PE03 | Proyectos | Estratégico | Microsoft Planner y Project | Parcial | Gestión del portafolio de proyectos de la PMO |
| PE04 | Capital humano | Estratégico | ERP SICOF (nómina) | Parcial | Módulo de talento humano, ligado a SIGEP |
| PE05 | Conocimiento e innovación | Estratégico | Intranet, Office 365 | Parcial | Repositorio de conocimiento y lecciones aprendidas |
| PE06 | Arquitectura empresarial | Estratégico | Visio | Parcial | Repositorio de arquitectura y de procesos |
| PM01 | Gestión de TI | Misional | GLPI y OTRS (mesa de ayuda), FusionInventory | Parcial | Gestión de servicios de TI con catálogo y medición de ANS por cliente |
| PM02 | Comercial | Misional | Ninguno (Excel) | Sin cobertura | Sistema de gestión de clientes (CRM) |
| PM03 | Gestión del servicio | Misional | Ninguno propio (Excel); telefonía Asterisk, FreePBX y Estaqueue para contact center | Parcial | Gestión de procesos de negocio (BPMS) y automatización |
| PA01 | Contractual | Apoyo | SECOP I y II | Parcial | Expediente contractual electrónico y seguimiento a la supervisión |
| PA02 | Compras | Apoyo | SECOP | Parcial | Integración de compras con el ERP |
| PA03 | Comunicaciones | Apoyo | Sitio web, intranet, redes sociales, Adobe Creative Cloud | Total | — |
| PA04 | Jurídica | Apoyo | Ninguno específico: el informe reporta cuatro procesos judiciales activos en una tabla, sin sistema (Informe de gestión 2025, pág. 70) | Sin cobertura | Gestión de procesos judiciales y de actas de gobierno corporativo |
| PA05 | Administrativa | Apoyo | Sistema de gestión documental (Carriel, en implementación interna) | Parcial | SGDEA con requisitos MoReq |
| PA06 | Financiera | Apoyo | ERP SICOF (SaaS) | Total | Integración con facturación de los contratos |
| PV01 | Seguimiento, control y evaluación | Evaluación | Gestión Transparente (rendición a la Contraloría) (PETI 2026-2027 de Valor+, pág. 37) | Parcial | Seguimiento automatizado del Plan de Mejoramiento Institucional |

Fuentes de los sistemas: PETI 2026-2027 de Valor+, págs. 33-37 y 66-69; Informe de gestión 2025, pág. 35 (Carriel).

#### 5.1.6 Servicios Institucionales o de negocio

Valor+ organiza sus ingresos en seis líneas de negocio (Informe de gestión 2025, pág. 130). Las que tienen componente de TI son las que este plan cubre con su catálogo de servicios tecnológicos (numeral 6.1.3).

Tabla: Servicios de negocio {T4}

| ID | Línea de negocio | Ejemplos en 2025 | Rol de la TI de Valor+ |
|---|---|---|---|
| S01 | Estrategias tecnológicas del recaudo | Impuesto vehicular de Antioquia, Tasa de Seguridad y Convivencia, cobro para Hacienda y Movilidad de Medellín | Opera los sistemas contratados para el cliente y la telefonía del contact center |
| S02 | Automatización de la información | Gestión documental para la Gobernación, el IDEA, Envigado y el Pascual Bravo; catastro departamental | Software de gestión documental (Carriel) y aplicación catastral en nube privada |
| S03 | Estructuración y gerenciamiento de proyectos | Proyectos para el departamento y municipios | Acompañamiento técnico en proyectos con componente de TI |
| S04 | Soluciones tecnológicas y consultoría especializada | Mesas de servicio (Gobernación, IDEA, Ferrocarril de Antioquia), conectividad, desarrollo de software, Office 365 para Crediantioquia | Presta el servicio directamente: es el núcleo del catálogo de servicios de TI |
| S05 | Seguridad | Centro de operaciones de seguridad (SOC) para el IDEA, análisis de vulnerabilidades e IPv6 para la Lotería de Medellín | Presta el servicio directamente |
| S06 | Soluciones energéticas en tecnologías limpias | Alumbrado público en el departamento | Sin rol de TI; fuera del alcance |

Fuente: Informe de gestión 2025, págs. 80-92, 99-104 y 126-130.

Fichas de los servicios de negocio con componente de TI (tabla 6 de la plantilla). Los datos de usuarios atendidos, costos y tiempos de ciclo por servicio no se publican [EVIDENCIA: informes de supervisión de cada contrato].

Tabla: Servicio de negocio S01 Estrategias tecnológicas del recaudo {T11}

| ID | S01 |
|---|---|
| Nombre | Estrategias tecnológicas del recaudo |
| Descripción | Liquidación, facturación, cobro y recaudo de tributos para entidades públicas (impuesto vehicular, Tasa de Seguridad, cobro para Hacienda y Movilidad de Medellín) |
| Usuario objetivo | Gobernación de Antioquia, Alcaldía de Medellín, Envigado |
| Horario de prestación del servicio | Según contrato; contact center en horario de atención |
| Canal de acceso | Contact center, correo, SMS, IVR, puntos de atención |
| Oportunidades de mejora con TI | Seguimiento de ANS por contrato en la herramienta de gestión de servicios (P2.3); flujos del proceso de servicio (P3.1) |

Tabla: Servicio de negocio S02 Automatización de la información {T11}

| ID | S02 |
|---|---|
| Nombre | Automatización de la información |
| Descripción | Gestión documental y digitalización para entidades; catastro departamental |
| Usuario objetivo | IDEA, Indeportes, Gobernación, Envigado, Pascual Bravo |
| Horario de prestación del servicio | Días hábiles |
| Canal de acceso | Correo, mesa de ayuda, atención en sede del cliente |
| Oportunidades de mejora con TI | SGDEA propio con requisitos MoReq como producto (P2.5) |

Tabla: Servicio de negocio S03 Estructuración y gerenciamiento de proyectos {T11}

| ID | S03 |
|---|---|
| Nombre | Estructuración y gerenciamiento de proyectos |
| Descripción | Formulación y gerencia de proyectos para entidades territoriales |
| Usuario objetivo | Gobernación y municipios |
| Horario de prestación del servicio | Días hábiles |
| Canal de acceso | Reuniones, correo |
| Oportunidades de mejora con TI | Metodología de la PMO y seguimiento del portafolio (P1.2) |

Tabla: Servicio de negocio S04 Soluciones tecnológicas y consultoría especializada {T11}

| ID | S04 |
|---|---|
| Nombre | Soluciones tecnológicas y consultoría especializada |
| Descripción | Mesas de servicio, conectividad, desarrollo de software, servicios en la nube |
| Usuario objetivo | Gobernación, IDEA, Ferrocarril de Antioquia, Lotería de Medellín, Crediantioquia |
| Horario de prestación del servicio | Según ANS; mesas de servicio en horario contratado |
| Canal de acceso | Mesa de servicio, correo, portal |
| Oportunidades de mejora con TI | Catálogo único con ANS (P1.3) y herramienta de gestión de servicios (P2.3) |

Tabla: Servicio de negocio S05 Seguridad {T11}

| ID | S05 |
|---|---|
| Nombre | Seguridad |
| Descripción | Centro de operaciones de seguridad, pruebas de vulnerabilidad e IPv6 |
| Usuario objetivo | IDEA, Lotería de Medellín, municipios |
| Horario de prestación del servicio | 24 horas para el monitoreo del SOC |
| Canal de acceso | Portal y correo del SOC |
| Oportunidades de mejora con TI | SOC propio como base del servicio (P1.4, OPT-002) |

Fuente: Informe de gestión 2025, págs. 80-104 y 129-130; oportunidades: análisis del equipo.

#### 5.1.7 Trámites

No aplica. Valor+ declara en su sitio web que "no cuenta con trámites específicos para gestión de la ciudadanía" y que pone a disposición canales de atención para peticiones, quejas, reclamos, sugerencias y denuncias (PQRSD) (sitio web de Valor+, sección de transparencia). Es coherente con su naturaleza: presta servicios a entidades, no le exige trámites al ciudadano. Cuando atiende trámites, como los certificados catastrales, lo hace como operador de un trámite que es de la Gobernación de Antioquia (PETI 2026-2027 de Valor+, pág. 36).

Dos datos de las fuentes se aclaran así:

- La Instrucción Administrativa 060 de 2017, publicada en la misma sección con el título "fijan tasas aplicables a los trámites", fija los costos de reproducción de información pública (copias, grabación en medios digitales, autenticaciones), como lo exigen la Ley 1712 de 2014 y el Decreto 103 de 2015. No crea trámites ante la entidad (Instrucción Administrativa 060 de 2017, art. 1).
- Los "trámites" respondidos fuera de plazo que reporta el informe de gestión son peticiones regidas por la Ley 1755 de 2015 (Informe de gestión 2025, pág. 75).

Lo que la TI sí soporta en la atención al ciudadano son los canales de PQRSD: formulario electrónico en el sitio web, correo electrónico, línea telefónica y atención presencial en la sede Edatel, en Medellín (sitio web de Valor+, sección de transparencia). Se tienen en cuenta en los numerales 6.1.3 y 7.1.4.

#### 5.1.8 Otros Procedimientos administrativos - OPAs

No aplica, por la misma razón del numeral 5.1.7: la entidad no declara procedimientos administrativos propios dirigidos al ciudadano. La atención se canaliza por PQRSD.

## Análisis de la situación

## Situación Actual

Criterio de lectura. El diagnóstico usa solo documentos públicos (numeral 2), así que "no se encontró en la evidencia revisada" no equivale a "no existe en la organización". Cada hallazgo lleva un código corto entre paréntesis según su dominio (E estrategia, G gobierno, I información, S sistemas, T infraestructura, U uso y apropiación, SG seguridad). Esos códigos se usan en la DOFA y en el catálogo de brechas.

En resumen: la TI que Valor+ vende a sus clientes está medida y cumple sus ANS, mientras que la TI interna va detrás. Los procesos comercial y de servicio trabajan en hojas de cálculo, el ERP lleva dos años en selección, no hay gobierno de datos y la auditoría interna de 2025 calificó el proceso de Gestión de TI con 49 %, el puntaje más bajo de la empresa (Informe de gestión 2025, pág. 49).

### 6.1 Estrategia de TI

#### 6.1.1 Lienzo estratégico Modelo de TI

Tabla: Lienzo estratégico de TI {T1}

| Componente | Descripción |
|---|---|
| Segmentos de clientes | Internos: los 16 procesos y 240 empleados (Informe de gestión 2024, pág. 25). Externos: entidades públicas de Antioquia que contratan servicios tecnológicos (Gobernación, IDEA, alcaldías, Lotería de Medellín, Ferrocarril de Antioquia) (Informe de gestión 2025, págs. 80-92) |
| Propuesta de valor | Integrar soluciones de tecnología y procesos para entidades públicas, con operación medida por ANS: 95,71 % de cumplimiento de ANS contractuales en 2025 (Informe de gestión 2025, pág. 16) |
| Canales | Mesas de servicio, sitio web e intranet, contact center, correo y canales de PQRSD (PETI 2026-2027 de Valor+, págs. 35-37; sitio web de Valor+, sección de transparencia) |
| Relación con clientes | Contratos con ANS y supervisión; satisfacción del cliente de 99 % en 2025 (Informe de gestión 2025, pág. 92) |
| Flujo de ingresos | Servicios tecnológicos y de seguridad, automatización de la información y recaudo con soporte tecnológico (Informe de gestión 2025, pág. 130) |
| Recursos claves | Gerencia de Tecnología, Innovación y Sostenibilidad con tres direcciones; nubes AWS, Oracle Cloud y Azure; mesa de ayuda; telefonía IP del contact center (PETI 2026-2027 de Valor+, págs. 31, 48-51; Informe de gestión 2025, pág. 87) |
| Actividades claves | Implementar y operar soluciones para clientes, soportar la operación interna, gestionar la infraestructura y la seguridad (PETI 2026-2027 de Valor+, págs. 47-51) |
| Socios y aliados | Proveedores de plataformas en esquema SaaS y nubes públicas; en 2025 una sola alianza tecnológica formal (Informe de gestión 2025, pág. 89; PETI 2026-2027 de Valor+, pág. 48) |
| Estructura de costos | [EVIDENCIA: el presupuesto de TI no se publica por separado]. El presupuesto de inversión de toda la empresa en 2025 fue de 2.134 millones de pesos, con 94 % de ejecución (Informe de gestión 2025, pág. 157) |

#### 6.1.2 Misión y visión de TI

Misión de TI vigente: "Ser el aliado estratégico institucional en la generación de valor a través de las Tecnologías de la Información, contribuyendo al cumplimiento de las estrategias de VALOR+ mediante la materialización de proyectos e iniciativas de TI, orientadas a la transformación digital y al fortalecimiento de la gestión institucional en el territorio" (PETI 2026-2027 de Valor+, pág. 18).

Visión de TI vigente: posicionar la Gerencia de TI "al año 2026 2027" como "referente de la transformación digital de las Entidades Públicas de todo orden" (PETI 2026-2027 de Valor+, pág. 19). La visión vence con el plan actual y no tiene metas que permitan saber si se cumplió (E1).

#### 6.1.3 Servicios de TI

El PETI 2026-2027 aclara que "la Entidad no presentó en forma oficial su portafolio de servicios" y que el catálogo se armó con los servicios ejecutados en proyectos (pág. 33). No hay un catálogo formal con ANS por servicio para la TI interna (E2). Los servicios a clientes sí tienen ANS en cada contrato.

Tabla: Catálogo de servicios de TI identificado {T4}

| ID | Servicio | Usuarios | Medición actual | Fuente |
|---|---|---|---|---|
| ST01 | Mesa de ayuda interna (soporte a usuarios, incidentes, inventario) | Colaboradores | Oportunidad de atención 98,72 % (meta ≥ 95 %); ANS internos 94,71 % (meta ≥ 80 %) | Informe de gestión 2025, págs. 16-17; PETI 2026-2027 de Valor+, págs. 50 y 57 |
| ST02 | Ofimática, correo y colaboración (Office 365, OneDrive, Teams) | Colaboradores | Sin indicador | PETI 2026-2027 de Valor+, págs. 37, 49 y 70 |
| ST03 | Conectividad interna (LAN, WAN, VPN, internet) | Colaboradores y sedes | Disponibilidad de servicios críticos 100 % (meta ≥ 99 %) | PETI 2026-2027 de Valor+, pág. 38; Informe de gestión 2025, pág. 17 |
| ST04 | Telefonía IP y plataforma de contact center | Colaboradores y operación de clientes | Incluido en disponibilidad | PETI 2026-2027 de Valor+, págs. 36 y 58 |
| ST05 | Sitio web e intranet | Ciudadanos, clientes y colaboradores | ITA 94 puntos | PETI 2026-2027 de Valor+, pág. 57; Informe de gestión 2025, pág. 12 |
| ST06 | Soporte a sistemas de información (ERP en SaaS y aplicaciones de apoyo) | Áreas de apoyo | Sin indicador | PETI 2026-2027 de Valor+, págs. 49-50 |
| ST07 | Seguridad perimetral, de equipos y respaldo | Toda la organización | Ataques bloqueados 100 %; incidentes gestionados 100 % | Informe de gestión 2025, pág. 17; PETI 2026-2027 de Valor+, pág. 46 |
| SC01 | Mesas de servicio para clientes | Gobernación, IDEA, Ferrocarril de Antioquia y otros | ANS contractuales 95,71 % (meta ≥ 94 %) | Informe de gestión 2025, págs. 16 y 80 |
| SC02 | Centro de operaciones de seguridad (SOC) y pruebas de vulnerabilidad | IDEA, Lotería de Medellín | Avance del proyecto SOC IDEA: 37 % físico en 2025 | Informe de gestión 2025, págs. 80-81 y 91 |
| SC03 | Conectividad para territorios (satelital, wifi público) | Gobernación y municipios | Por contrato | Informe de gestión 2025, págs. 80 y 90 |
| SC04 | Desarrollo de software y asistentes con IA | IDEA, Lotería de Medellín, Gobernación | Por contrato | Informe de gestión 2025, págs. 91-92 |
| SC05 | Hosting y servicios en la nube | Fábrica de Licores de Antioquia, Crediantioquia | Por contrato | Informe de gestión 2025, pág. 161 |

Los proyectos de cada cliente quedan fuera del alcance (numeral 2). El catálogo SC se incluye porque usa la misma gerencia, la misma infraestructura y el mismo personal que la TI interna.

La ficha de cada servicio (tablas 8 a 38 de la plantilla), con su situación actual y la acción propuesta, está en el Anexo F. La plantilla pide dejar en el cuerpo el resumen y el detalle como anexo.

#### Objetivos de TI vigentes

El PETI 2026-2027 enuncia cuatro objetivos generales: optimizar procesos con digitalización y automatización; fortalecer la infraestructura; impulsar la innovación; y gestionar riesgos y ciberseguridad (pág. 82). No tienen indicador, meta ni línea base, y su mapa de ruta no asigna presupuesto ni fechas a las iniciativas (págs. 81-82) (E3). Tampoco incluye un análisis DOFA ni un catálogo de brechas con tiempo y costo, que la guía pide en las actividades 6 y 11 (E4). Este PETI 2027-2030 parte de esos vacíos.

#### 6.1.5 Capacidades de TI

Tabla: Capacidades de TI {T42}

| Categoría | Capacidad | Cuenta con la capacidad en la entidad |
|---|---|---|
| Estratégica | Habilitar y soportar la estrategia de TI y su alineación con la estrategia empresarial | Sí |
| Estratégica | Habilitar el gobierno digital para usuarios internos y externos | Sí |
| Transaccional | Desarrollar, mantener y gestionar sistemas de información para la operación | Parcial |
| Transaccional | Gestionar activos de información | Sí |
| Transaccional | Gestionar indicadores operativos del proceso y subprocesos | Parcial |
| Transaccional | Gestionar el subproceso (sin descripción en la fuente) | No |
| Soporte | Habilitar la operación continua y de calidad | Sí |
| Soporte | Adoptar mejores prácticas para las operaciones de TI | Sí |
| Arquitectura de TI | Gestionar y mantener la infraestructura tecnológica | Sí |
| Arquitectura de TI | Dar soporte en el uso de herramientas tecnológicas | Parcial |

Fuente: PETI 2026-2027 de Valor+, págs. 38-39 (autoevaluación de la organización). El equipo no comparte dos de las calificaciones. "Gestionar activos de información" figura como "Sí", pero el mismo documento reconoce que no hay catálogo de datos maestros ni responsables formales (pág. 54). "Habilitar la operación continua" figura como "Sí", cuando el plan de continuidad apenas terminó su primera fase en 2025 (Informe de gestión 2025, pág. 88). En el análisis se tratan como "Parcial" (E5).

#### 6.1.6 Indicadores de TI

La Gerencia de TI reporta nueve indicadores estratégicos al plan de acción. En 2025 cumplió 88,63 % en conjunto (Informe de gestión 2025, pág. 17).

Tabla: Indicadores de TI 2025 {T4}

| Indicador | Meta 2025 | Resultado 2025 | Estado |
|---|---|---|---|
| Cumplimiento de ANS contractuales | ≥ 94 % | 95,71 % | Cumple |
| Cumplimiento de ANS internos | ≥ 80 % | 94,71 % | Cumple |
| Facturación de ingresos efectuada | ≥ 80 % | 77,83 % | No cumple |
| Presupuesto de costos optimizado | ≥ 93 % | 80,72 % | No cumple |
| Disponibilidad de servicios críticos de TI | ≥ 99 % | 100 % | Cumple |
| Gestión de incidentes de seguridad informática | 100 % | 100 % | Cumple |
| Nivel de protección ante ataques informáticos | ≥ 99 % | 100 % | Cumple |
| Oportunidad de atención en servicios de TI | ≥ 95 % | 98,72 % | Cumple |
| Índice de registro de propiedad intelectual | ≥ 4 | 2 | No cumple |

Fuente: Informe de gestión 2025, págs. 16-17.

Figura: Indicadores de TI 2025, meta frente a resultado {img:docs/figuras/indicadores_ti_2025.png}

Los indicadores miden sobre todo operación (disponibilidad, tickets, ANS) y finanzas de los proyectos. No hay indicadores de gestión de la TI interna: avance de proyectos de TI, satisfacción de usuarios internos, calidad de datos, madurez de seguridad o apropiación (E6). Dos indicadores que el PETI 2026-2027 incluye en su tablero, el cumplimiento de acciones del Plan de Mejoramiento y el del plan de capacitaciones, figuran sin dato ("ND") (pág. 40).

### 6.2 Gobierno de TI

#### 6.2.1 Modelo de Gobierno de TI

##### Definición de la instancia de gobierno de TI

No se encontró una instancia dedicada a decidir sobre TI. Valor+ tiene estos comités que tocan temas de TI:

- el Comité Institucional de Gestión y Desempeño, que por el MIPG orienta las políticas de Gobierno Digital y Seguridad Digital (Decreto 1083 de 2015, modificado por el Decreto 1499 de 2017) y que aprobó el PEI con el Acta 006 de 2024 (Informe de gestión 2025, pág. 13);
- el Comité Directivo, del que hace parte el Comité de Compras y Contratación, que sesiona cada semana y revisa las compras según el manual de contratación (PETI 2026-2027 de Valor+, pág. 41);
- el Comité de Riesgos, creado en 2025 para la Alta Gerencia (Informe de gestión 2025, pág. 33);
- el Comité Primario de TI, interno de la gerencia, con frecuencia semanal "sugerida" (PETI 2026-2027 de Valor+, pág. 41).

El tablero mensual de indicadores de TI lo revisa Planeación (pág. 41). El PETI 2026-2027 menciona también un Comité de Seguridad que revisaría los resultados del SGSI (pág. 46), pero no se encontró su acto de creación ni registro de sus sesiones [EVIDENCIA: acta o decisión empresarial del Comité de Seguridad].

Así, las prioridades de inversión en TI se deciden en un comité de compras y no en una instancia que mire el portafolio completo (G1).

##### Definición y gestión de la Matriz riesgos de TI a nivel general

La matriz de riesgos de TI se reporta cada mes con tres líneas de defensa: la Gerencia de TI (primera), Planeación (segunda) y Control Interno (tercera) (PETI 2026-2027 de Valor+, pág. 41). El proceso de Gestión del Riesgo cumplió sus indicadores en 2025 (Informe de gestión 2025, pág. 24). Ese año se parametrizó una nueva matriz de riesgos institucional y se creó un Comité de Riesgos para la Alta Gerencia (Informe de gestión 2025, pág. 33). No se encontró una herramienta de gestión de riesgos; el PETI 2026-2027 la propone como sistema nuevo (pág. 68), así que la matriz se lleva, en apariencia, en hojas de cálculo (análisis del equipo) (G2).

##### Gestión y Supervisión del Presupuesto de Inversiones y gastos de Operación de las TIC

[EVIDENCIA: el presupuesto de TI no se publica por separado.] El presupuesto de inversión de la empresa fue de 2.134 millones de pesos en 2025, con 94 % de ejecución (Informe de gestión 2025, pág. 157). Los indicadores de TI miden el presupuesto de costos de los proyectos de tecnología para clientes (80,72 % frente a una meta de 93 %), no el gasto de la TI interna (Informe de gestión 2025, pág. 17) (G3).

#### 6.2.2 Políticas y estándares para la gestión de la gobernabilidad de TI

Tabla: Políticas de TI vigentes {T43}

| Política | Descripción |
|---|---|
| Seguridad y privacidad de la información | Control de acceso, gestión de activos, cumplimiento legal y protección de datos personales, gestión de incidentes. Las de incidentes "si bien están definidas, estas no son administradas de forma constante" (pág. 42) |
| Continuidad del negocio | Planes de continuidad, recuperación, contingencia y redundancia |
| Adquisición, desarrollo y mantenimiento de sistemas | Condiciones de desarrollo, mantenimiento y seguridad de los sistemas |
| Seguridad en las operaciones | Protección contra software malicioso, respaldos, monitoreo, control de software y vulnerabilidades |
| Principios de TI | Doce principios alineados con el MinTIC (excelencia del servicio al ciudadano, costo/beneficio, estandarización, interoperabilidad, seguridad digital, entre otros) |

Fuente: PETI 2026-2027 de Valor+, págs. 41-43.

Las políticas existen como documento, pero la de incidentes no se aplica de forma constante (SG1). No se encontraron políticas de datos (calidad, datos abiertos, datos maestros) ni de uso de inteligencia artificial, aunque la IA ya se usa en servicios a clientes (G4).

#### 6.2.3 Proceso de Gestión de TI

La Gerencia de TI agrupa sus actividades en tres categorías: estratégicas (análisis de los planes de desarrollo y del PEI, y gestión del portafolio de iniciativas de TI), de la cadena de valor (proyectos para clientes, sitios web, soporte técnico y gestión de infraestructura) y de apoyo (PETI 2026-2027 de Valor+, págs. 43 y 47-51).

El mismo documento reconoce que los proyectos "en su gran mayoría se han dirigido a proyectos de índole técnico" y que "poco se han implementado proyectos de cara a la mejora en la gestión y operación de la entidad" (pág. 43) (G5).

Tabla: Procesos de gestión de TI adoptados {T44}

| Proceso | Descripción | Documento de caracterización |
|---|---|---|
| Gestión estratégica de TI | Revisar los planes y formular el PETI; gestionar el portafolio de iniciativas | PETI 2026-2027 de Valor+, pág. 43 |
| Gestión de proyectos y servicios para clientes | Diseñar, contratar, implementar y operar soluciones para clientes con aliados SaaS y nube | Pág. 47 |
| Desarrollo de sitios web | Sitio web e intranet en AWS | Pág. 48 |
| Soporte técnico y mesa de servicios | Primer nivel, registro y solución de incidentes y requerimientos | Pág. 50 |
| Gestión de infraestructura | Servidores, almacenamiento, virtualización, respaldo, redes, DNS, DHCP; para Valor+ y para clientes | Págs. 48-51 |
| Gestión de cuentas y contraseñas | Altas, bajas y permisos de usuarios | Pág. 49 |

La auditoría interna de 2025 calificó el proceso de Gestión de TI con 49 %. En 2024 esa auditoría se había reprogramado por la reestructuración de la Decisión Empresarial 064 (Informe de gestión 2025, pág. 49; Informe de gestión 2024, pág. 13). El informe no detalla los hallazgos. La misma auditoría encontró procedimientos desactualizados tras los cambios de personal (Informe de gestión 2025, pág. 48). Con ese resultado, el de TI es el proceso que más necesita formalizarse (G6).

La plantilla agrupa los procedimientos de gestión de TI en siete grupos. La tabla dice cuáles se encontraron en Valor+ y si están documentados.

Tabla: Cadena de valor de gestión de TI frente a la plantilla {T44}

| Proceso | Descripción | Documento de caracterización |
|---|---|---|
| Gestión administrativa, de alineamiento, organización y planeación de TI | Existen planeación estratégica (PETI), gestión de proyectos y contratación de TI. No se encontraron gestión presupuestal de TI propia ni gestión de uso y apropiación | Parcial: PETI 2026-2027 de Valor+, págs. 43-44 |
| Gestión del ciclo de vida de los sistemas de información | Existen desarrollo con Scrum y adquisición de SaaS. No se encontraron procedimientos de requisitos, pruebas, control de cambios ni administración de ambientes | Parcial: pág. 44; numeral 6.4.5 |
| Gestión de la infraestructura de TI | Existen administración, monitoreo y soporte de infraestructura interna y de clientes, y mesa de servicio | Sí: págs. 48-51 |
| Administrar los datos | Existen respaldos y publicación en el sitio web. No se encontraron administración de bases de datos ni repositorios de contenido gobernados | Parcial: págs. 53-54 y 61 |
| Gestión de licenciamientos y suscripciones | Existe licenciamiento de Office 365, Adobe y SaaS. No se encontró un procedimiento de control de licencias | [EVIDENCIA: procedimiento de licenciamiento] |
| Gestión operativa de los servicios de TI | Existen ANS e incidentes en la mesa de ayuda. No se encontraron gestión de problemas, de cambios ni de capacidad | Parcial: págs. 40 y 50 |
| Administración de la seguridad y privacidad de la información | Existen SGSI, políticas, cuentas y contraseñas, pruebas de vulnerabilidad y equipos de seguridad. La gestión de incidentes no se aplica de forma constante | Sí, con debilidad en incidentes: págs. 42-47; Informe de gestión 2025, págs. 87-89 |

#### 6.2.4 Estructura y Organización humana de TI

La Gerencia de Tecnología, Innovación y Sostenibilidad depende de la Gerencia General y tiene tres direcciones (PETI 2026-2027 de Valor+, págs. 31 y 51).

Figura: Organigrama de la Gerencia de Tecnología, Innovación y Sostenibilidad. Fuente: PETI 2026-2027 de Valor+, pág. 31 {img:docs/figuras/organigrama_ti.png}

Tabla: Roles de TI identificados {T45}

| Rol | Cantidad | Funciones |
|---|---|---|
| Gerencia y apoyo administrativo | 2 | Dirección del área y apoyo administrativo |
| Dirección de Infraestructura | 11 | Infraestructura, soporte, activos y seguridad de la información |
| Dirección de Servicios | 6 | Gestión de los servicios de TI |
| Dirección de Desarrollo y Servicios | 57 | Desarrollo de soluciones y operación; incluye 49 auxiliares operativos |
| Total | 76 | |

Fuente: conteo del equipo sobre el organigrama de TI (PETI 2026-2027 de Valor+, pág. 31; análisis del equipo).

Casi dos de cada tres cargos son auxiliares operativos que, por su número, corresponden a la operación de servicios para clientes (análisis del equipo). La TI interna la atienden unas 27 personas. No hay un cargo dedicado a la seguridad de la información ni un responsable de datos: la seguridad es una función más del equipo de infraestructura (PETI 2026-2027 de Valor+, pág. 51) (G7). No se encontró una matriz RACI de TI: el término solo aparece en el glosario del PETI 2026-2027 (pág. 10) (G8).

#### 6.2.5 Esquema de toma decisiones

Las decisiones de TI escalan según criticidad, impacto y monto: Junta Directiva, Gerente General, Gerente de Tecnología y directores de subproceso (PETI 2026-2027 de Valor+, pág. 43). El esquema no define qué decisiones toma cada nivel ni con qué montos (G9). Valor+ sí tiene un Manual de Contratación con seis modalidades: convocatoria pública, convocatoria abreviada, contratación directa, aliado proveedor, aliado estratégico y contratación extraordinaria (Informe de gestión 2025, pág. 53). Sus cuantías no se encontraron publicadas [EVIDENCIA: manual de contratación vigente].

#### 6.2.6 Gestión de Proyectos

Los proyectos de TI usan un modelo híbrido: Scrum para los proyectos pequeños y de software, y la metodología tradicional del PMI para los grandes, con Microsoft Planner y Project como herramientas (PETI 2026-2027 de Valor+, pág. 44).

A nivel de empresa, la gestión de proyectos estaba en nivel 1 de madurez (inicial), sin metodología corporativa ni criterios comunes de priorización. En 2025 se reactivó el proceso y se diseñó una PMO en tres niveles: apoyo, control y estratégica (Informe de gestión 2025, págs. 34-37). Los proyectos de TI todavía no se gestionan con la metodología de la PMO (G10).

### 6.3 Gestión de Información

#### 6.3.1 Planeación y Gobierno de la gestión de Información

No hay un inventario o catálogo de datos maestros. Los funcionarios que producen la información lo hacen "sin una asignación formal del rol de responsable del dato" (PETI 2026-2027 de Valor+, pág. 54) (I1). No se encontraron política de gobierno de datos ni plan de datos abiertos, y una búsqueda del equipo en el portal datos.gov.co, en octubre de 2026, no devolvió conjuntos de datos publicados por Valor+ (I2). [VERIFICAR en la sección de transparencia del sitio web: registro de activos de información e índice de información clasificada y reservada, que la Ley 1712 de 2014 exige publicar.]

#### 6.3.2 Arquitectura de Información

La información se clasifica en confidencial y no confidencial. La mayor parte de los activos de información se guarda en el servidor de archivos local (unidad compartida V), en archivo físico y en el sitio web, "sin un esquema formal de catalogación o versionamiento" (PETI 2026-2027 de Valor+, págs. 53-54) (I3).

Tabla: Matriz de entidades de información frente a componentes de TI {T46}

| Entidad de información | ERP (SICOF) | Hojas de cálculo | Mesa de ayuda | Sitio web | Unidad V | Power BI | SECOP |
|---|---|---|---|---|---|---|---|
| Clientes y oportunidades | | C, L | | | L | | |
| Contratos | L | C, L | | | L | | C |
| ANS e incidentes | | L | C, L | | | L | |
| Facturación y cartera | C, L | L | | | | L | |
| Presupuesto | C, L | L | | | | L | |
| Colaboradores y nómina | C, L | | | | L | | |
| Activos | C, L | | C, L | | | | |
| Documentos e informes | | | | L | C, L | | |
| PQRSD | | L | | C | | | |
| Indicadores del PEI | | C | | | L | L | |

C: crea o actualiza; L: lee. Fuente: análisis del equipo con base en PETI 2026-2027 de Valor+, págs. 33-37 y 53-54. La matriz muestra el problema del numeral 6.3.3: varias entidades se crean en hojas de cálculo y no tienen un sistema maestro.

#### 6.3.3 Diseño de Componentes de información

La matriz CRUD de los activos (crear, leer, actualizar y eliminar) muestra que la mayoría de los procesos pueden leer y editar la información del ERP, el sitio web, la intranet y la unidad V, "lo que incrementa el riesgo de inconsistencias" (PETI 2026-2027 de Valor+, pág. 54). Los flujos de información "no evidencian canales, protocolos o interacciones" de retroalimentación entre procesos (pág. 56) (I4).

#### 6.3.4 Análisis y aprovechamiento de los componentes de información

Hay tableros en Power BI para indicadores y seguimiento de proyectos (PETI 2026-2027 de Valor+, pág. 34). Como los procesos misionales trabajan en Excel (pág. 33), los tableros dependen de consolidaciones manuales (análisis del equipo) (I5). En servicios a clientes Valor+ ya entrega analítica y asistentes con IA (Informe de gestión 2025, págs. 89-92), una capacidad que no aprovecha hacia adentro.

#### 6.3.5 Calidad y Seguridad de los componentes de información

No se encontraron reglas ni mediciones de calidad de datos (I6).

En gestión documental, en 2025 se actualizaron la política, el Programa de Gestión Documental y el PINAR (aprobado hasta 2027), y se formularon el Sistema Integrado de Conservación y el Plan de Preservación Digital. Quedan pendientes las tablas de retención y de valoración documental, que siguen en revisión del Consejo Departamental de Archivo, y el sistema de gestión de documentos electrónicos de archivo (SGDEA), que está en diseño con la Gerencia de TI bajo el modelo MoReq (Informe de gestión 2025, págs. 75-77) (I7).

### 6.4 Sistemas de Información

#### 6.4.1 Catálogo de los Sistemas de Información

El PETI 2026-2027 describe 18 sistemas en cinco categorías (págs. 56-59). Aquí se resumen en una sola tabla, sin ficha por sistema.

Tabla: Catálogo de sistemas de información {T4}

| Categoría | Sistema | Uso | Modelo |
|---|---|---|---|
| Direccionamiento estratégico | FURAG | Reporte del MIPG | Plataforma del Gobierno |
| Direccionamiento estratégico | Power BI y gestión de información geográfica | Tableros e indicadores | Nube (Microsoft) |
| Direccionamiento estratégico | Microsoft Visio | Modelado de procesos y arquitectura | Licencia |
| Misional de gestión | OTRS y GLPI, con FusionInventory | Mesa de ayuda e inventario de TI | Software libre, en servidores propios |
| Servicios digitales | Sitio web | Información, transparencia, PQRSD, pago en línea | AWS |
| Servicios digitales | Intranet | Comunicación interna | En sitio |
| Prestación de servicios (clientes) | Impuesto vehicular, mesa de ayuda de clientes, catastro departamental | Operación para la Gobernación | SaaS del proveedor, nube privada |
| Apoyo | ERP (SICOF) | Finanzas y nómina | SaaS |
| Apoyo | Asterisk, FreePBX, Estaqueue | Telefonía IP y contact center | Software libre, en sitio |
| Apoyo | Office 365, Adobe Creative Cloud | Ofimática, correo, diseño | Nube |
| Apoyo | Software de seguridad de equipos | Control de software y navegación | Licencia |
| Apoyo | SECOP I y II, Tienda Virtual del Estado, Gestión Transparente | Contratación pública y rendición a la Contraloría | Plataformas del Estado |
| Apoyo | Carriel | Gestión documental (en implementación interna) | Desarrollo con registro de propiedad intelectual de Valor+ |

Fuente: PETI 2026-2027 de Valor+, págs. 34-37 y 56-59; Informe de gestión 2025, págs. 17 y 35.

Los procesos comercial, de servicio, de riesgos, jurídico y de seguimiento no tienen sistema propio (numeral 5.1.5) (S1). El ERP actual cubre finanzas y nómina. Un ERP integrado está en estudio de mercado desde 2024 y se incluyó en el presupuesto de 2025, pero a enero de 2026 seguía en levantamiento de requisitos (PETI 2026-2027 de Valor+, págs. 77-78) (S2).

La ficha de cada sistema principal (tablas 44 a 51 de la plantilla), con la acción propuesta, está en el Anexo F.

#### 6.4.2 Capacidades funcionales de los Sistemas de Información

Tabla: Capacidades funcionales de los sistemas de información {T55}

| Función | ERP (SICOF) | Mesa de ayuda | Office 365 | Power BI | Sitio web | Excel |
|---|---|---|---|---|---|---|
| Contabilidad, presupuesto y nómina | Sí | No | No | No | No | No |
| Gestión comercial y de clientes (CRM) | No | No | No | No | No | Sí |
| Seguimiento de contratos y ANS de clientes | No | Parcial | No | Parcial | No | Sí |
| Facturación por proyecto | Parcial | No | No | No | No | Sí |
| Gestión de incidentes de TI | No | Sí | No | No | No | No |
| Atención de PQRSD | No | No | Parcial | No | Sí | No |
| Indicadores y tableros | No | Parcial | No | Sí | No | Sí |

Fuente: análisis del equipo con base en PETI 2026-2027 de Valor+, págs. 33-37 y 56-59.

La tabla muestra que Excel cubre las funciones del negocio que ningún sistema cubre (S1).

#### 6.4.3 Mapa de Integraciones de Sistemas de Información

No se encontró un mapa de integraciones. El PETI 2026-2027 describe los sistemas por separado y propone, como arquitectura futura, una capa de integración orientada a servicios (págs. 64-67). Con flujos sin canales ni protocolos (pág. 56) y procesos en Excel, los datos pasan entre el ERP, la mesa de ayuda y los tableros por exportación manual (análisis del equipo) (S3).

#### 6.4.4 Arquitectura de Referencia de Sistemas de Información

No hay una arquitectura de referencia adoptada. El PETI 2026-2027 propone una arquitectura multicapa con estándares .NET o J2EE (págs. 64-65), pero no se ha aplicado. Los sistemas actuales mezclan SaaS, software libre en servidores propios y plataformas del Estado (S4).

#### 6.4.5 Ciclo de vida de los Sistemas de Información

Tabla: Situación actual del ciclo de vida de los sistemas de información {T56}

| Actividad | Grado de madurez | Descripción hallazgo u oportunidad de mejora |
|---|---|---|
| Definición de requisitos | Bajo | El ERP lleva dos años en levantamiento de requisitos (PETI 2026-2027 de Valor+, pág. 78) |
| Selección y contratación | Medio | Hay principios de adquisición y un comité de compras semanal (págs. 41 y 72) |
| Desarrollo | Medio | Scrum para software; Carriel registrado como propiedad intelectual (pág. 44; Informe de gestión 2025, pág. 17) |
| Pruebas y paso a producción | Sin evidencia | [EVIDENCIA: no se encontró procedimiento de pruebas ni de control de cambios] |
| Retiro | Sin evidencia | Sin plan de retiro de sistemas legados |

#### 6.4.6 Mantenimiento de los Sistemas de Información

Tabla: Matriz de mantenimientos de sistemas de información {T57}

| Actividad | Grado de madurez | Descripción hallazgo u oportunidad de mejora |
|---|---|---|
| Mantenimiento de SaaS | Medio | Lo hace el proveedor según contrato (pág. 50) |
| Mantenimiento de software libre (mesa de ayuda, telefonía) | Bajo | El propio PETI recomienda actualizar la planta telefónica y buscarle contingencia (pág. 81) |
| Actualización de ofimática | Bajo | Hay licencias de versiones anteriores y libres por migrar a Office 365 (pág. 70) |

#### 6.4.7 Soporte de los Sistemas de Información

Tabla: Matriz de soportes de sistemas de información {T58}

| Actividad | Grado de madurez | Descripción hallazgo u oportunidad de mejora |
|---|---|---|
| Primer nivel | Medio | Mesa de ayuda interna con oportunidad de 98,72 % (Informe de gestión 2025, pág. 17) |
| Segundo y tercer nivel | Bajo | El modelo de escalamiento con terceros y fabricantes está recomendado, no implementado (pág. 78) |
| Herramienta de mesa de servicios | Bajo | OTRS y GLPI; el PETI recomienda reemplazarlas por una herramienta alineada con ITIL (pág. 79) (S5) |

### 6.5 Infraestructura de TI

#### 6.5.1 Arquitectura de Infraestructura tecnológica

La infraestructura es híbrida (T1):
- en la nube: el sitio web y servidores en AWS, servicios en Oracle Cloud y Azure, y Office 365 (PETI 2026-2027 de Valor+, págs. 48, 59 y 77; Informe de gestión 2025, pág. 87);
- en las sedes: el servidor de archivos (unidad V), el directorio activo, la intranet, la telefonía IP y los cuartos técnicos (PETI 2026-2027 de Valor+, págs. 53, 69 y 77).

Figura: Arquitectura de infraestructura actual de Valor+ {img:docs/figuras/infraestructura_actual.png}

Tabla: Servicios de infraestructura de TI {T59}

| ID servicios de infraestructura | Servicio de infraestructura | Descripción |
|---|---|---|
| SI01 | Cómputo y virtualización | Servidores físicos y virtuales, propios y en AWS |
| SI02 | Almacenamiento y archivos | Unidad V en sitio y OneDrive |
| SI03 | Respaldo | Copias periódicas de los servidores en AWS (pág. 61) |
| SI04 | Redes | LAN, WAN, VPN e internet en las sedes (pág. 38) |
| SI05 | Servicios base | Directorio activo, DNS, DHCP, FTP (pág. 49) |
| SI06 | Seguridad perimetral y de equipos | UTM en alta disponibilidad en comodato con el proveedor de internet, y antimalware en equipos (pág. 46) |
| SI07 | Telefonía | Planta IP con software libre (pág. 58) |

#### 6.5.2 Catálogo de Elementos de Infraestructura

Al 30 de diciembre de 2024 el ERP registraba 2.885 activos, 52 % de ellos tecnológicos (unos 1.500), repartidos en siete sedes y puntos (Informe de gestión 2024, pág. 40). El inventario de TI se lleva en GLPI con FusionInventory (PETI 2026-2027 de Valor+, pág. 36). [EVIDENCIA: no se publica el detalle por tipo de equipo ni su antigüedad.]

Tabla: Elementos de infraestructura de TI identificados {T60}

| Id | Elemento de infraestructura | Tipo | Servicio de infraestructura involucrado |
|---|---|---|---|
| IT01 | Servidores virtuales y sitio web en AWS | Infraestructura como servicio | SI01 Cómputo |
| IT02 | Servicios en Oracle Cloud y Azure | Infraestructura y plataforma como servicio | SI01 Cómputo |
| IT03 | Servidores físicos y virtualización en sede | Instalado en sitio [EVIDENCIA: cantidad] | SI01 Cómputo |
| IT04 | Servidor de archivos (unidad V) | Instalado en sitio | SI02 Almacenamiento |
| IT05 | OneDrive y SharePoint | Software como servicio | SI02 Almacenamiento |
| IT06 | Copias de respaldo de los servidores en AWS | Infraestructura como servicio | SI03 Respaldo |
| IT07 | Red LAN, WAN, VPN y canales de internet | Instalado en sitio y servicio de proveedor | SI04 Redes |
| IT08 | Directorio activo, DNS y DHCP | Instalado en sitio | SI05 Servicios base |
| IT09 | UTM en alta disponibilidad | Instalado en sitio, en comodato | SI06 Seguridad |
| IT10 | Antimalware de equipos de usuario | Licencia | SI06 Seguridad |
| IT11 | Planta telefónica IP (Asterisk, FreePBX) | Instalado en sitio, software libre | SI07 Telefonía |
| IT12 | Mesa de ayuda e inventario (OTRS, GLPI, FusionInventory) | Instalado en sitio, software libre | Soporte |
| IT13 | Equipos de usuario y periféricos | Instalado en sitio | Estaciones de trabajo |

Fuente: PETI 2026-2027 de Valor+, págs. 36, 46-61 y 69; Informe de gestión 2025, pág. 87.

#### 6.5.3 Administración de la capacidad de la Infraestructura tecnológica

No se encontró un plan de capacidad. El PETI 2026-2027 lo plantea como principio, "medir los niveles y los requerimientos de infraestructura (Capacity Planning)" (pág. 72), pero no reporta mediciones (T2). El paso de 34 a 48 contratos en un año (Informe de gestión 2025, pág. 130) hace más urgente planear la capacidad.

#### 6.5.3 Administración de la operación

Tabla: Operación de los servicios tecnológicos {T61}

| Identificador | Descripción | Sí | No |
|---|---|---|---|
| OP01 | Monitoreo de disponibilidad de servicios críticos | Sí | |
| OP02 | Centro de operaciones de red (NOC) | | No |
| OP03 | Centro de operaciones de seguridad propio | | No (en implementación, PETI 2026-2027 de Valor+, pág. 44) |
| OP04 | ANS de servicios de TI internos | Sí | |
| OP05 | Plan de recuperación ante desastres probado | | No (fases 2 y 3 previstas para 2026, Informe de gestión 2025, pág. 88) |
| OP06 | IPv6 en la infraestructura propia | | No se encontró evidencia. Valor+ implementó IPv6 para un cliente en 2025 (Informe de gestión 2025, pág. 91), pero el plazo para su propia red venció el 31 de diciembre de 2022 (Resolución 1126 de 2021) (T3) |

Tabla: Matriz de mantenimientos y servicio {T62}

| Identificador | Descripción | Sí | No |
|---|---|---|---|
| Acuerdos de nivel de servicio | Hay ANS en los contratos con clientes y para la mesa interna (indicadores de ANS, Informe de gestión 2025, pág. 16) | Sí | |
| Mesa de servicio | Herramienta, procedimientos y equipo de mesa de ayuda (PETI 2026-2027 de Valor+, pág. 50) | Sí | |
| Planes de mantenimiento | Mantenimiento de sedes y equipos (Informe de gestión 2025, pág. 80); no se encontró un plan de mantenimiento de infraestructura de TI | | No [EVIDENCIA] |

Tabla: Fases de implementación de IPv6 {T63}

| Identificador | Descripción | Sí | No |
|---|---|---|---|
| Fase de diagnóstico | No se encontró diagnóstico de IPv6 de la red propia | | No (sin evidencia pública) |
| Fase de implementación | Valor+ implementó IPv6 para un cliente en 2025 (Informe de gestión 2025, pág. 91), lo que demuestra la capacidad; no en su red | | No |
| Fase de pruebas | Sin evidencia en la red propia | | No |

### 6.6 Uso y Apropiación de TI

#### 6.6.1 Estrategia de Uso y Apropiación de TI

No hay una estrategia de uso y apropiación de TI documentada (U1). Lo que existe son acciones sueltas:
- un boletín mensual de ciberseguridad (Informe de gestión 2025, págs. 87-88);
- el plan de capacitación institucional, cuyo indicador figura sin dato en el tablero de TI (PETI 2026-2027 de Valor+, pág. 40);
- un plan de comunicaciones del PETI por intranet, correo, inducciones y sitio web (PETI 2026-2027 de Valor+, pág. 82).

En el FURAG, las dimensiones con componente de apropiación son las más bajas: talento humano (57,5) y gestión del conocimiento (64,4) (Informe de gestión 2025, pág. 10).

Tabla: Caracterización de grupos de interés {T64}

| Grupo | Descripción | Necesidad frente a la TI |
|---|---|---|
| Colaboradores | 240 empleados en 2024, en siete sedes y puntos (Informe de gestión 2024, págs. 25 y 40) | Herramientas que reemplacen las hojas de cálculo; capacitación |
| Clientes | Entidades públicas de Antioquia; 48 contratos activos en 2025 (Informe de gestión 2025, pág. 130) | Servicios con ANS cumplidos y reportes oportunos |
| Ciudadanos | Usuarios de los canales de PQRSD y del sitio web | Información pública accesible y respuestas a tiempo |
| Entes de control | Contraloría General de Antioquia, Función Pública, Procuraduría (ITA) | Trazabilidad y rendición de información |
| Accionista | IDEA | Resultados y sostenibilidad financiera |

Tabla: Formación y capacitación {T65}

| Id | Temática | Nombre | Objetivo | Duración | Grupo de impacto |
|---|---|---|---|---|---|
| F01 | Seguridad de la información | Boletín mensual de ciberseguridad | Informar sobre amenazas, phishing y buenas prácticas (Informe de gestión 2025, págs. 87-88) | Mensual | Todos los colaboradores |
| F02 | Gestión del conocimiento | Plan de capacitación institucional | Formación de los colaboradores (Informe de gestión 2025, pág. 48) | Anual | Todos los colaboradores |
| F04 | Contratación y seguridad | Jornadas de Gestión Jurídica | Supervisión contractual, uso de IA en la actividad contractual y seguridad informática (Informe de gestión 2025, págs. 69-70) | 2025 | Áreas que contratan |
| F03 | Uso de sistemas | Sin evidencia de formación en los sistemas de información | — | — | [EVIDENCIA: plan de capacitación en TI] |

### 6.7 Seguridad

Valor+ tiene un sistema de gestión de seguridad de la información (SGSI) documentado. En 2025 lo actualizó al MSPI de 2025 del MinTIC, con matriz de riesgos de seguridad, inventario de activos, declaración de aplicabilidad y gestión de incidentes; hizo pruebas de hacking ético, cuyos hallazgos se están remediando; y terminó la primera fase del plan de continuidad (Informe de gestión 2025, págs. 87-89).

En el FURAG, la política de Seguridad Digital obtuvo 85,2 (Informe de gestión 2025, pág. 11). Las debilidades son tres: la gestión de incidentes no se administra de forma constante (SG1); el SOC propio y la certificación ISO 22301 están en curso (SG2); y no hay un cargo dedicado a la seguridad (G7).

La calificación de la tabla es una estimación del equipo con la escala del instrumento del MSPI: 0 inexistente, 20 inicial, 40 repetible, 60 definido, 80 gestionado, 100 optimizado. Valor+ no publica su autoevaluación [EVIDENCIA: instrumento de evaluación del MSPI de Valor+]. La meta se justifica en el numeral 7.

Tabla: Evaluación de efectividad de controles {T66}

| No. | Tema | Calificación actual | Calificación objetivo | Evaluación de efectividad de control |
|---|---|---|---|---|
| 1 | Políticas y organización de la seguridad | 60 | 80 | Políticas definidas y actualizadas al MSPI 2025; sin cargo dedicado |
| 2 | Gestión de activos | 40 | 80 | Inventario actualizado; sin responsables formales de datos |
| 3 | Control de acceso | 60 | 80 | Política de cuentas y contraseñas aplicada |
| 4 | Seguridad de las personas | 40 | 60 | Boletín mensual; sin programa de formación medido |
| 5 | Seguridad física | 40 | 60 | Siete sedes y puntos; cuartos técnicos por adecuar (PETI 2026-2027 de Valor+, pág. 77) |
| 6 | Seguridad de las operaciones y comunicaciones | 60 | 80 | Perímetro en alta disponibilidad, 100 % de ataques bloqueados, hacking ético |
| 7 | Gestión de incidentes | 40 | 80 | Política definida pero no administrada de forma constante |
| 8 | Continuidad del negocio | 20 | 80 | Análisis de impacto hecho en 2025; plan sin implementar ni probar |
| 9 | Cumplimiento | 60 | 80 | MSPI, Ley 1581 y Ley 1712 atendidos; ITA 94 |

Fuente: estimación del equipo (análisis del equipo) con base en Informe de gestión 2025, págs. 11, 17 y 87-89; PETI 2026-2027 de Valor+, págs. 42-47.

#### Análisis DOFA

La DOFA resume el diagnóstico por dominio (actividad 6 de la guía). Los factores internos salen de los hallazgos de este numeral y los externos, de los motivadores del numeral 5.

Tabla: DOFA por dominio de TI {T4}

| Dominio | Fortalezas | Debilidades | Oportunidades | Amenazas |
|---|---|---|---|---|
| Estrategia | ANS de clientes cumplidos (95,71 %); TI como proceso misional | Visión y objetivos sin metas (E1, E3); sin catálogo formal (E2); indicadores solo operativos (E6) | PEI y Plan de Desarrollo departamental que demandan TI; crecimiento de contratos | Fin del PEI y del plan departamental en 2027 |
| Gobierno | Riesgos con tres líneas de defensa; comité de compras activo | Ninguna instancia revisa el portafolio de TI (G1); auditoría de TI en 49 % (G6); sin RACI ni cargo de seguridad (G7, G8) | PMO en construcción; FURAG con Gobierno Digital en 86,3 | Hallazgos de la Contraloría (control fiscal 2,0) |
| Información | Activos inventariados; PINAR y plan de preservación digital | Sin datos maestros ni responsables (I1); información en unidad local sin versiones (I3); calidad sin medir (I6) | Acuerdo 001 de 2024 del AGN; analítica e IA que ya vende | Pérdida o inconsistencia de información de contratos |
| Sistemas | ERP financiero en SaaS; desarrollo propio registrado (Carriel) | Procesos del negocio en Excel (S1); ERP integrado sin decidir (S2); sin integraciones (S3) | Oferta madura de ERP, CRM y BPMS en la nube | Dependencia de proveedores SaaS |
| Infraestructura | Nube en AWS, Oracle y Azure sin hallazgos críticos; disponibilidad 100 % | Servicios críticos aún en sitio (T1); sin plan de capacidad (T2); IPv6 atrasado frente al plazo de 2022 (T3) | Conectividad departamental; precios de nube | Fallas de sedes o del proveedor de internet |
| Uso y apropiación | Boletín de ciberseguridad; capacitación institucional | Sin estrategia de apropiación (U1) | Resultados del FURAG en talento humano y conocimiento como palanca | Rotación de personal y procedimientos desactualizados |
| Seguridad | SGSI actualizado al MSPI 2025; 100 % de ataques bloqueados | Incidentes sin gestión constante (SG1); continuidad y SOC en curso (SG2) | Demanda de SOC por municipios | Ransomware y phishing contra entidades públicas |

Fuente: elaboración del equipo a partir de los numerales 5 y 6.

La figura resume la DOFA en sus cuatro cuadrantes, con un factor clave por dominio (F1 a F7, D1 a D7) y los factores externos de más peso (O1 a O5, A1 a A5).

Figura: Matriz DOFA de TI de Valor+ {img:docs/figuras/dofa.png}

La matriz cruzada combina esos factores en cuatro tipos de estrategia: FO (usar fortalezas para aprovechar oportunidades), DO (superar debilidades con las oportunidades), FA (usar fortalezas para reducir amenazas) y DA (reducir debilidades y evitar amenazas). Cada estrategia lleva a los proyectos del numeral 8 que la ejecutan, así que la DOFA conecta el diagnóstico con el portafolio.

Figura: Matriz DOFA cruzada: estrategias y proyectos {img:docs/figuras/dofa_cruzada.png}

#### Tendencias tecnológicas

La guía pide cruzar las tendencias con los servicios y los procesos (actividad 7).

Tabla: Tendencias tecnológicas frente a servicios y procesos {T4}

| Tendencia | Evidencia en Valor+ | Servicios | Procesos | Uso previsto |
|---|---|---|---|---|
| Inteligencia artificial generativa | Asistentes virtuales para la Lotería de Medellín y la Tasa de Seguridad; chat y WhatsApp con IA para 17 secretarías (Informe de gestión 2025, págs. 91-92 y 103) | SC04 | PM01, PM03 | Usarla también en la atención interna y en PQRSD, con política de uso |
| Ciberseguridad gestionada (SOC) | SOC IDEA y SOC Municipios (Informe de gestión 2025, pág. 80; PETI 2026-2027 de Valor+, pág. 45) | SC02, ST07 | PM01, PE02 | SOC propio que también atienda la TI interna |
| Nube y SaaS | AWS, Oracle Cloud, Azure, Office 365 | ST02, ST06, SC05 | PA06, PM01 | Migrar los servicios que siguen en sitio |
| Automatización de procesos (BPMS, RPA) | Propuesta en el PETI 2026-2027 (pág. 68) | ST06 | PM02, PM03 | Reemplazar hojas de cálculo en comercial y servicio |
| Analítica de datos | Power BI; analítica para entes territoriales (Informe de gestión 2025, pág. 89) | ST05 | PE01 | Tablero del PEI con datos integrados |
| Conectividad satelital | 1.818 sedes educativas y 81 sedes de salud (Informe de gestión 2025, pág. 90) | SC03 | PM01 | Contexto de demanda; fuera del alcance de proyectos |

Fuente: elaboración del equipo.

## 7. Situación deseada u objetivo

Todo lo de este numeral es propuesto: lo formula el equipo (análisis del equipo) y queda sujeto a la aprobación del Comité Institucional de Gestión y Desempeño. Se construyó en tres pasos: se invirtió cada hallazgo del numeral 6, se tomó de los marcos de referencia cómo se resuelve (COBIT 2019, ITIL 4, MSPI, ISO/IEC 27001:2022), y se llevó a metas por año con su indicador. Cada elemento dice qué hallazgo atiende y qué proyecto del numeral 8 lo realiza.

### 7.1 Estrategia de TI

#### 7.1.1 Misión de TI

Proveer y gobernar la tecnología con la que Valor+ opera y presta sus servicios, con procesos digitales, datos confiables, infraestructura disponible y seguridad medida, para que la empresa cumpla su plan estratégico y entregue a sus clientes públicos servicios con los niveles acordados.

#### 7.1.2 Visión de TI

A 2030, la TI de Valor+ será gestionada como un conjunto de servicios con niveles acordados y medidos. Los procesos misionales y de apoyo estarán soportados en sistemas integrados y no en hojas de cálculo, y la seguridad de la información tendrá una madurez de 76 sobre 100 en la escala del MSPI. La TI interna tendrá el mismo nivel de servicio que la TI que la empresa vende.

Frente a la visión vigente (numeral 6.1.2), esta tiene fecha, se puede medir con las metas del numeral 7.1.3 y mira primero hacia adentro (atiende E1).

#### 7.1.3 Objetivos estratégicos de TI

Los objetivos de TI se derivan de los objetivos corporativos (numeral 5, OC01 a OC05) y de los hallazgos del numeral 6. Se redactan con verbo en infinitivo y se asocian a una perspectiva del cuadro de mando integral, como pide la actividad 8 de la guía.

Tabla: Definición de objetivos estratégicos de TI {T67}

| ID | Nombre | Descripción | Perspectiva | Objetivo corporativo | Hallazgos que atiende |
|---|---|---|---|---|---|
| OETI01 | Formalizar el gobierno y la gestión de la TI | Instancia de decisión de TI, responsabilidades, procesos de gestión documentados y presupuesto de TI visible | Procesos internos | OC01, OC02 | E3, E4, E5, G1, G2, G3, G5, G6, G7, G8, G9, G10 |
| OETI02 | Gestionar la TI como servicios con niveles acordados | Catálogo único de servicios de TI internos y vendidos, con ANS, responsable y satisfacción medida | Clientes | OC04, OC05 | E2, E6, S5 |
| OETI03 | Digitalizar los procesos misionales y de apoyo | Sistemas integrados que reemplacen las hojas de cálculo en los procesos comercial, de servicio, contractual y financiero | Procesos internos | OC02, OC03 | S1, S2, S3, S4, I7 |
| OETI04 | Gobernar y aprovechar los datos | Datos con responsable y reglas de calidad, información centralizada y analítica para decidir | Aprendizaje y crecimiento | OC01, OC04 | I1, I2, I3, I4, I5, I6, G4 |
| OETI05 | Asegurar una infraestructura disponible y recuperable | Servicios críticos en la nube o con contingencia, capacidad planeada, recuperación probada e IPv6 | Procesos internos | OC03, OC04 | T1, T2, T3, SG2 |
| OETI06 | Elevar la madurez de seguridad y la apropiación de la TI | MSPI operado y medido, incidentes gestionados y colaboradores formados | Aprendizaje y crecimiento | OC01, OC05 | SG1, SG2, U1, G7 |

Las metas están escalonadas: en 2027 van las que dependen solo de la organización (gobierno, catálogo, procedimientos, seguridad) y desde 2028 las que dependen de contratar e implantar sistemas. Donde no hay línea base pública, la meta de 2027 es medirla.

Tabla: Metas de los objetivos estratégicos de TI {T67}

| ID | Objetivo | Meta | Indicador | Línea base | Año 1 (2027) | Año 2 (2028) | Año 3 (2029) | Año 4 (2030) |
|---|---|---|---|---|---|---|---|---|
| METI01 | OETI01 | Subir la calificación de la auditoría interna al proceso de Gestión de TI | KPI-01 | 49 % (2025; Informe de gestión 2025, pág. 49) | 70 % | 80 % | 90 % | 90 % |
| METI02 | OETI01 | Terminar en la fecha planeada los proyectos del PETI de cada vigencia | KPI-02 | No aplica (plan nuevo) | 80 % | 80 % | 85 % | 90 % |
| METI03 | OETI01 | Mejorar el puntaje del FURAG en Gobierno Digital y Seguridad Digital (promedio) | KPI-03 | 85,75 (FURAG 2024: 86,3 y 85,2; Informe de gestión 2025, pág. 11) | 86 | 87 | 88 | 90 |
| METI04 | OETI02 | Medir con ANS los servicios del catálogo de TI | KPI-04 | 0 % (no hay catálogo formal; numeral 6.1.3) | 50 % | 80 % | 100 % | 100 % |
| METI05 | OETI02 | Mejorar la satisfacción de los usuarios internos con los servicios de TI | KPI-05 | Sin medición; se mide en 2027 | Línea base | ≥ 80 % | ≥ 85 % | ≥ 85 % |
| METI06 | OETI03 | Aumentar los procesos con cobertura total de sistemas de información | KPI-06 | 12,5 % (2 de 16; numeral 5.1.5) | 12,5 % | 37,5 % | 62,5 % | 81 % |
| METI07 | OETI04 | Asignar responsable y reglas de calidad a las entidades de información críticas | KPI-07 | 0 % (numeral 6.3.1) | Inventario | 40 % | 80 % | 100 % |
| METI08 | OETI05 | Migrar a la nube o dar contingencia a los servicios críticos que siguen en sitio | KPI-08 | 0 de 5 (numeral 6.5.1) | 0 % | 60 % | 100 % | 100 % |
| METI09 | OETI05 | Probar con éxito la recuperación de los servicios críticos | KPI-09 | 0 pruebas (numeral 6.5.3) | 1 | 2 | 2 | 2 |
| METI10 | OETI06 | Subir la madurez de seguridad de la información en la escala del MSPI | KPI-10 | 47 (estimación del equipo; numeral 6.7) | 55 | 63 | 70 | 76 |
| METI11 | OETI06 | Formar en uso de TI y seguridad a los colaboradores cada año | KPI-11 | Sin medición (numeral 6.6.1) | 40 % | 70 % | 85 % | 90 % |

El FURAG de una vigencia se publica al año siguiente: la meta de 2027 de METI03 se verifica con el FURAG que se reporta en 2028. La meta de 2027 de METI06 no sube porque el ERP integrado entra en producción en 2028 (proyecto P1.5).

#### 7.1.3 Capacidades de TI

Tabla: Capacidades de TI a fortalecer o desarrollar {T68}

| Categoría | Capacidad | Fortalecer o desarrollar |
|---|---|---|
| Estratégica | Gestionar el portafolio de TI y medir su ejecución | Fortalecer (OETI01) |
| Estratégica | Gestionar los servicios de TI con catálogo y ANS | Desarrollar (OETI02) |
| Transaccional | Desarrollar, mantener e integrar sistemas de información | Fortalecer (OETI03) |
| Transaccional | Gobernar los datos y su calidad | Desarrollar (OETI04) |
| Transaccional | Gestionar activos de información | Fortalecer (OETI04) |
| Soporte | Habilitar la operación continua y la recuperación | Fortalecer (OETI05) |
| Arquitectura de TI | Planear la capacidad de la infraestructura | Desarrollar (OETI05) |
| Arquitectura de TI | Apoyar el uso y la apropiación de la tecnología | Fortalecer (OETI06) |
| Seguridad | Gestionar incidentes y operar el SOC propio | Fortalecer (OETI06) |

#### 7.1.4 Servicios de TI

Se propone un catálogo único de servicios de TI, con un responsable y un ANS por servicio, que incluya los servicios internos y los que se venden (atiende E2; proyecto P1.3). Los ANS de los servicios vendidos siguen siendo los de cada contrato; el catálogo los reúne para medirlos con el mismo tablero.

Tabla: Servicios de TI: acciones propuestas {T11}

| ID | Servicio |
|---|---|
| ST01 | Mesa de ayuda interna. Acción: Modificar: herramienta de gestión de servicios con prácticas de ITIL 4 |
| ST02 | Ofimática, correo y colaboración. Acción: Modificar: todas las licencias en Office 365 y archivos en SharePoint |
| ST03 | Conectividad interna. Acción: Mantener; agregar monitoreo de red |
| ST04 | Telefonía y contact center. Acción: Modificar: telefonía en la nube con contingencia |
| ST05 | Sitio web e intranet. Acción: Modificar: intranet en la nube; PQRSD conectadas a la mesa de servicios |
| ST06 | Soporte a sistemas de información. Acción: Modificar: soporte de segundo y tercer nivel con proveedores, medido |
| ST07 | Seguridad, respaldo y recuperación. Acción: Modificar: SOC propio y recuperación probada |
| ST08 | Datos y analítica institucional. Acción: Crear |
| SC01 a SC05 | Servicios vendidos. Acción: Mantener; medir en el mismo catálogo |

Las fichas de cada servicio con la acción propuesta en cada atributo están en el Anexo F.

#### 7.1.6 Indicadores de TI

Hojas de vida de los indicadores (actividad 14, hojas 14A y 14B del Anexo 1). Hay un indicador por meta. Los rangos de bueno, intermedio y malo se calculan frente a la meta del año: bueno si la cumple, intermedio si queda a menos de 10 puntos y malo si queda más abajo. Los responsables son roles propuestos.

Tabla: Hojas de vida de los indicadores de TI {T100}

| ID INDICADOR | CATEGORÍA INDICADOR | NOMBRE | DESCRIPCIÓN | PERIODICIDAD | TIPO DE INDICADOR | FORMULA DE CÁLCULO | VARIABLE | FUENTE | UNIDAD DE MEDIDA | BUENO | INTERMEDIO | MALO | ROL RESPONSABLE SUGERIDO |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KPI-01 | Gobierno de TI; eficacia | Calificación de la auditoría al proceso de Gestión de TI | Mide METI01; proyectos P1.1, P1.2 | Anual | Estratégico | Puntaje del informe de auditoría interna | Puntaje obtenido | Informe de auditorías internas (Arquitectura Empresarial) | % | ≥ meta | Meta − 10 a meta | < meta − 10 | Gerente de TI |
| KPI-02 | Estrategia de TI; eficacia | Nivel de ejecución del PETI | Mide METI02; todo el portafolio | Semestral | Estratégico | (PT / PV) × 100 | PT: proyectos terminados en la fecha planeada; PV: proyectos que debían terminar en la vigencia | Informe de la PMO | % | ≥ meta | Meta − 10 a meta | < meta − 10 | Secretaría técnica del Comité de TI |
| KPI-03 | Gobierno de TI; eficacia | Puntaje FURAG de Gobierno Digital y Seguridad Digital | Mide METI03; proyectos P1.1, P1.4, P2.1 | Anual | Estratégico | (Puntaje Gobierno Digital + Puntaje Seguridad Digital) / 2 | Puntajes de las dos políticas | Resultados FURAG de Función Pública | Puntos | ≥ meta | Meta − 3 a meta | < meta − 3 | Director de Planeación y Proyectos |
| KPI-04 | Estrategia de TI; eficacia | Servicios de TI con ANS medido | Mide METI04; proyecto P1.3 | Semestral | Táctico | (SA / SC) × 100 | SA: servicios con ANS medido en el periodo; SC: servicios del catálogo | Catálogo y tablero de servicios de TI | % | ≥ meta | Meta − 10 a meta | < meta − 10 | Director de Servicios de TI |
| KPI-05 | Uso y apropiación; calidad | Satisfacción de usuarios internos con TI | Mide METI05; proyectos P1.3, P2.3 | Semestral | Táctico | (RS / RT) × 100 | RS: respuestas satisfechas o muy satisfechas; RT: respuestas | Encuesta en la herramienta de mesa de servicios | % | ≥ meta | Meta − 10 a meta | < meta − 10 | Director de Servicios de TI |
| KPI-06 | Sistemas de información; eficacia | Procesos con cobertura total de sistemas de información | Mide METI06; proyectos P1.5, P2.2, P2.5, P3.1 | Anual | Estratégico | (PC / 16) × 100 | PC: procesos del mapa con cobertura total | Matriz de alineación de TI con los procesos (numeral 5.1.5) | % | ≥ meta | Meta − 10 a meta | < meta − 10 | Director de Desarrollo y Servicios |
| KPI-07 | Información; calidad | Entidades de información críticas gobernadas | Mide METI07; proyecto P2.1 | Semestral | Táctico | (EG / EC) × 100 | EG: entidades críticas con responsable y reglas de calidad; EC: entidades críticas del catálogo | Catálogo de datos | % | ≥ meta | Meta − 10 a meta | < meta − 10 | Responsable de gobierno de datos |
| KPI-08 | Infraestructura; eficacia | Servicios en sitio migrados o con contingencia | Mide METI08; proyecto P2.4 | Semestral | Táctico | (SM / 5) × 100 | SM: servicios migrados o con contingencia en la nube | Inventario de infraestructura | % | ≥ meta | Meta − 20 a meta | < meta − 20 | Director de Infraestructura |
| KPI-09 | Infraestructura; eficacia | Pruebas de recuperación exitosas | Mide METI09; proyecto P1.6 | Anual | Operativo | Conteo de pruebas con RTO y RPO cumplidos | Pruebas exitosas en el año | Informes de prueba del plan de recuperación | Número | ≥ meta | Meta − 1 | 0 | Director de Infraestructura |
| KPI-10 | Seguridad; madurez | Madurez de seguridad de la información (MSPI) | Mide METI10; proyectos P1.4, P1.6, P2.1 | Anual | Estratégico | Promedio de las calificaciones de los temas del instrumento del MSPI | Calificación por tema (0 a 100) | Autoevaluación con el instrumento del MSPI | Puntos | ≥ meta | Meta − 5 a meta | < meta − 5 | Responsable de seguridad de la información |
| KPI-11 | Uso y apropiación; cobertura | Colaboradores formados en uso de TI y seguridad | Mide METI11; proyectos P1.4, P2.6 | Semestral | Táctico | (CF / CT) × 100 | CF: colaboradores con al menos una formación aprobada en el año; CT: colaboradores | Registros de capacitación de Capital Humano | % | ≥ meta | Meta − 10 a meta | < meta − 10 | Responsable de uso y apropiación |

Se mantienen además los nueve indicadores de TI que la empresa ya reporta al plan de acción (numeral 6.1.6), en especial disponibilidad de servicios críticos (≥ 99 %) y cumplimiento de ANS contractuales (≥ 94 %).

### 7.2 Gobierno de TI

El gobierno de TI propuesto usa las instancias que el MIPG ya le da a Valor+ y agrega las que faltan: un comité táctico de TI, responsabilidades asignadas y un esquema de decisiones con montos.

#### Instancias de decisión

- **Comité Institucional de Gestión y Desempeño** (existe): aprueba el PETI, sus actualizaciones y el presupuesto anual de TI, y hace seguimiento semestral a las políticas de Gobierno Digital y Seguridad Digital, como corresponde en el MIPG.
- **Comité de TI** (atiende G1; proyecto P1.1): no es un comité nuevo, sino una sesión mensual del Comité Directivo dedicada a TI y seguridad, igual que el Comité de Compras ya hace parte de él. Así lo sugiere la plantilla del MinTIC ("que haga parte del Comité Directivo de la entidad") y se evita crear otro comité, porque el Decreto 1499 de 2017 (art. 2.2.22.3.8) hace que el Comité Institucional sustituya los comités relacionados con el MIPG que no son obligatorios por ley. Esta sesión cumple también la función del Comité de Seguridad que menciona el PETI 2026-2027. Prioriza el portafolio, revisa los indicadores de TI, los riesgos de TI y los cambios de alcance. Lo preside la Gerencia General o su delegado. Lo integran la Gerencia de TI (secretaría técnica), la Dirección de Planeación y Proyectos (PMO), la Gerencia Financiera, la Gerencia de Operaciones y la Secretaría General. Control Interno asiste como invitado, sin voto.
- **Comité Primario de TI** (existe): se mantiene como instancia operativa semanal de la gerencia.
- **Comité de Compras y Contratación** (existe): sigue revisando la contratación, pero solo de iniciativas que el Comité de TI ya priorizó.

Tabla: Esquema de decisiones de TI propuesto {T101}

| Decisión | Gerente de TI | Comité de TI | Gerente General | Comité Institucional o Junta Directiva |
|---|---|---|---|---|
| Cambios operativos y compras dentro del presupuesto aprobado, hasta 50 SMMLV | Decide | Informa | | |
| Proyectos nuevos o cambios de alcance de proyectos del PETI | Propone | Decide | Informa | |
| Contratos de TI por encima de 50 SMMLV | Propone | Recomienda | Decide | |
| PETI, presupuesto anual de TI y cambios de prioridad entre objetivos | Propone | Recomienda | Presenta | Aprueba |

El umbral de 50 salarios mínimos es una propuesta del equipo (análisis del equipo) que debe ajustarse al manual de contratación de Valor+ (atiende G9).

#### Definición y gestión de la Matriz riesgos de TI a nivel general

Los riesgos de TI siguen en la matriz de riesgos institucional, con las tres líneas de defensa que ya funcionan (numeral 6.2.1). Se revisan cada mes en el Comité de TI, y los de nivel alto se escalan al Comité de Riesgos que la empresa creó en 2025 (Informe de gestión 2025, pág. 33). Se propone llevarla en una herramienta y no en hojas de cálculo (atiende G2; proyecto P3.1). La escala es del equipo: probabilidad e impacto en tres niveles (bajo, medio, alto).

Tabla: Matriz de riesgos de TI {T101}

| ID | Riesgo (causa → evento → consecuencia) | Probabilidad | Impacto | Nivel | Tratamiento | Proyecto | Propietario |
|---|---|---|---|---|---|---|---|
| R01 | Requisitos del ERP sin cerrar y sin patrocinio → la selección se alarga otra vigencia → los procesos siguen en Excel y las metas de OETI03 no se cumplen | Alta | Alto | Alto | Mitigar: alcance por fases y decisión en el Comité de TI en el primer semestre de 2027 | P1.5 | Gerente Financiero y Gerente de TI |
| R02 | Incidentes sin gestión constante y sin responsable dedicado → un ataque de ransomware o phishing no se contiene a tiempo → pérdida de información de clientes y sanciones | Media | Alto | Alto | Mitigar | P1.4 | Responsable de seguridad de la información |
| R03 | Plan de recuperación sin probar → una falla de sede o de proveedor deja fuera servicios críticos → incumplimiento de ANS con clientes | Media | Alto | Alto | Mitigar | P1.6, P2.4 | Director de Infraestructura |
| R04 | El crecimiento de contratos absorbe al personal de TI → los proyectos internos se aplazan → el PETI no se ejecuta | Alta | Medio | Alto | Mitigar: capacidad reservada para proyectos internos y seguimiento mensual | P1.1, P1.2 | Gerente de TI |
| R05 | Migración a la nube sin clasificar la información → datos confidenciales mal protegidos → incumplimiento de la Ley 1581 | Media | Medio | Medio | Mitigar | P2.1, P2.4 | Responsable de gobierno de datos |
| R06 | Baja adopción de los sistemas nuevos → los usuarios vuelven a Excel → la inversión no rinde | Media | Medio | Medio | Mitigar | P2.6 | Responsable de uso y apropiación |
| R07 | Cambio de administración departamental en 2028 → cambian las prioridades del accionista y de los clientes → recortes o cambios de alcance | Media | Medio | Medio | Aceptar: revisión anual del PETI en el Comité de TI y actualización en 2030 | P1.1, P4.1 | Gerente General |
| R08 | Dependencia de proveedores SaaS sin cláusulas de salida → aumento de precios o pérdida de datos al cambiar de proveedor | Baja | Medio | Bajo | Mitigar: cláusulas de portabilidad y ANS en los contratos | P1.5, P2.2 | Secretaría General |

#### 7.2.1 Políticas y estándares para la gestión de la gobernabilidad de TI

Tabla: Políticas de TI objetivo {T101}

| Política | Acción | Contenido mínimo | Proyecto |
|---|---|---|---|
| Seguridad y privacidad de la información | Modificar | Procedimiento de gestión de incidentes con responsables, tiempos y reporte al ColCERT cuando aplique | P1.4 |
| Gestión de servicios de TI | Crear | Catálogo, ANS, gestión de cambios y de problemas | P1.3 |
| Gobierno de datos | Crear | Responsables de datos, calidad, clasificación, datos abiertos y datos personales | P2.1 |
| Uso responsable de inteligencia artificial | Crear | Casos permitidos, datos que no se pueden usar, revisión humana, registro de los asistentes en uso | P2.1 |
| Adquisición de tecnología | Modificar | Nube primero, cláusulas de portabilidad y salida, evaluación de seguridad del proveedor | P1.1 |
| Continuidad del negocio | Modificar | Pruebas anuales con RTO y RPO definidos | P1.6 |
Lineamientos de política por dominio, que el Comité de TI adopta en P1.1 y P2.1:

#### Dominio de Estrategia

- Formular, hacer seguimiento y actualizar cada año el PETI, alineado con el PEI y el plan de acción.
- Todo proyecto de inversión en TI debe estar en el portafolio del PETI o ser aprobado por el Comité de TI.

#### Dominio de Gobierno

- Toda adquisición de tecnología pasa por el Comité de TI antes del Comité de Compras, con evaluación técnica, de seguridad y de salida del proveedor.
- La gestión de TI se rige por los procesos priorizados del numeral 7.2.3 y su RACI.

#### Dominio de Información

- Cada entidad de información tiene un responsable y un sistema maestro; los intercambios se hacen por API documentadas.
- Los datos personales se tratan según la Ley 1581 de 2012 y los datos públicos se publican según la Ley 1712 de 2014.

#### Dominio Sistemas de Información

- Nube primero: los sistemas nuevos se contratan como servicio salvo que el caso de negocio justifique otra cosa.
- Ningún proceso misional o de apoyo usa hojas de cálculo como sistema de registro cuando exista un sistema que lo cubra.

#### Dominio de Infraestructura TI

- Los servicios críticos tienen contingencia y prueba anual de recuperación.
- La capacidad se planea cada año con el crecimiento de contratos y usuarios.

#### Dominio Uso y Apropiación

- Cada sistema nuevo incluye formación y gestión del cambio en su presupuesto.
- Los directivos lideran la adopción de los sistemas en sus procesos.


#### Gestión y Supervisión del Presupuesto de Inversiones y gastos de Operación de las TIC

Se propone un presupuesto de TI propio dentro del presupuesto de la empresa, separado entre funcionamiento de la TI interna, inversión del PETI y costos de los proyectos para clientes (atiende G3; proyecto P1.1). El Comité de TI lo revisa cada trimestre. El presupuesto del portafolio por vigencia está en el numeral 8.

#### Gestión de asignación de Recursos Humanos

Cada mes el Comité Primario de TI revisa la carga del personal interno y de los contratistas de TI frente al portafolio y a los contratos con clientes, y propone al Comité de TI los ajustes. La capacidad para proyectos internos se reserva para que el crecimiento de contratos no la absorba (riesgo R04).

#### 7.2.3 Procesos de Gestión de TI

Se priorizan los procesos de COBIT 2019 que el diagnóstico muestra más débiles, con prácticas de ITIL 4 para los de servicio. La meta es que lleguen al nivel de capacidad 3 (proceso definido y documentado) en 2028 (proyecto P1.2). COBIT e ITIL no son obligatorios para Valor+: se usan como referencia para ordenar los procesos. La madurez oficial se mide con los instrumentos del Estado, el FURAG (METI03) y el MSPI (METI10).

Tabla: Procesos de gestión de TI a implementar o fortalecer {T102}

| Capacidad de TI | Nombre proceso | Acciones de mejora en los procesos |
|---|---|---|
| Gobierno | Marco de gestión de TI (COBIT APO01) | Documentar los procesos de TI y actualizar los procedimientos que la auditoría encontró desactualizados (G6) |
| Gobierno | Gestión del portafolio (APO05) | Priorización en el Comité de TI con la metodología de la PMO (G10) |
| Servicios | Acuerdos de servicio (APO09) y gestión de solicitudes e incidentes (DSS02) | Catálogo, ANS y herramienta de gestión de servicios (E2, S5) |
| Riesgos | Gestión del riesgo (APO12) | Riesgos de TI revisados en el Comité de TI (G2) |
| Seguridad | Gestión de la seguridad (APO13) | Operación del MSPI y gestión de incidentes (SG1) |
| Datos | Gestión de los datos (APO14) | Catálogo, responsables y calidad (I1, I6) |
| Soluciones | Construcción y adquisición de soluciones (BAI03) y gestión de cambios (BAI06) | Procedimiento de pruebas y paso a producción (numeral 6.4.5) |
| Continuidad | Gestión de la continuidad (DSS04) | Pruebas anuales de recuperación (SG2) |
| Desempeño | Seguimiento del desempeño (MEA01) | Tablero de indicadores del PETI (E6) |

#### 7.2.4 Estructura y Organización humana de TI

No se propone cambiar la estructura de tres direcciones. La gerencia de TI ya depende de la Gerencia General, como pide el Decreto 415 de 2016 para que el líder de TI esté en el nivel directivo. Se proponen tres roles nuevos y una matriz RACI (atiende G7 y G8; proyecto P1.1).

Tabla: Roles de TI y cambios propuestos {T103}

| Rol | Cantidad | Funciones | Acciones de mejora o cambios en el talento humano |
|---|---|---|---|
| Gerente de TI | 1 | Dirección de la TI | Secretaría técnica del Comité de TI |
| Responsable de seguridad de la información | 1 (nuevo) | Operar el MSPI, gestionar incidentes, coordinar el SOC | Cargo dedicado; por independencia, se recomienda que reporte a la Gerencia General o a Planeación y no a Infraestructura |
| Responsable de gobierno de datos | 1 (nuevo) | Catálogo de datos, calidad, datos abiertos | En la Dirección de Desarrollo y Servicios |
| Responsables de datos | Uno por proceso misional y de apoyo | Calidad y uso de los datos de su proceso | Rol asignado a líderes de proceso, no cargo nuevo |
| Responsable de cada servicio de TI | Uno por servicio | ANS y mejora del servicio | Rol asignado dentro de las direcciones |
| Responsable de uso y apropiación | 1 (rol) | Programa de formación y gestión del cambio | Rol compartido con Capital Humano |

Figura: Estructura de TI deseada {img:docs/figuras/organigrama_ti_objetivo.png}

Tabla: Matriz RACI de los procesos de gestión de TI {T103}

| Proceso | Gerencia de TI | Comité de TI | Planeación y Proyectos | Financiera | Líderes de proceso | Control Interno |
|---|---|---|---|---|---|---|
| Planeación estratégica de TI (PETI) | R | A | C | C | C | I |
| Portafolio y proyectos de TI | R | A | R | C | C | I |
| Presupuesto de TI | R | C | C | A | I | I |
| Gestión de servicios y ANS | A, R | I | I | I | C | I |
| Gestión de riesgos de TI | R | A | C | I | C | C |
| Seguridad de la información | A, R | I | C | I | C | C |
| Gobierno de datos | C | A | C | I | R | I |
| Auditoría del proceso de TI | C | I | R | I | I | A |

R: responsable de ejecutar; A: responsable de aprobar; C: consultado; I: informado.

#### 7.2.5 Gestión de Proyectos

Los proyectos del PETI se gestionan con la metodología de la PMO de Valor+ (Informe de gestión 2025, págs. 36-37), con Scrum para software y la guía del PMI para los proyectos grandes. Cada proyecto tiene ficha, cronograma, presupuesto y un indicador en el tablero del PETI (atiende G10; proyecto P1.2). La PMO reporta el avance del portafolio al Comité de TI cada mes.

La adopción del componente de gestión de proyectos del MRAE se hace a través de la PMO, en sus cuatro dominios:

#### Dominio Legal

Cada proyecto revisa con la Secretaría General la modalidad de contratación del manual de Valor+, la publicación en el SECOP y las cláusulas de datos, propiedad intelectual y salida del proveedor.

#### Dominio de Planeación

Cada proyecto tiene ficha con alcance, cronograma, presupuesto validado por la Gerencia Financiera, riesgos e indicador, aprobada por el Comité de TI.

#### Dominio de Ejecución

Scrum para software y la guía del PMI para implantaciones grandes; informe mensual de avance a la PMO.

#### Dominio de Control

La PMO compara cada mes el avance con lo planeado (KPI-02); Control Interno audita el portafolio dentro de su plan anual.

### 7.3 Gestión de Información

#### 7.3.1 Arquitectura de Información

Se propone un catálogo de entidades de información (clientes, contratos, ANS, facturas, proyectos, activos, colaboradores, PQRSD) con su sistema de origen, su responsable y su clasificación (atiende I1; proyecto P2.1). Cada entidad tiene un solo sistema maestro: el ERP para contratos y facturación, el CRM para clientes y la herramienta de gestión de servicios para incidentes y ANS. La información que hoy está en la unidad V pasa a SharePoint con permisos por proceso y control de versiones (atiende I3; proyecto P2.4).

#### 7.3.2 Servicios de Intercambio de datos

Los sistemas intercambian datos por una capa de integración con interfaces de programación (API) documentadas, y no por exportaciones manuales (atiende I4 y S3; proyecto P3.1). La información que deba publicarse como dato abierto se publica en el portal de datos abiertos del Estado, de acuerdo con la Ley 1712 de 2014 [VERIFICAR qué conjuntos aplican a Valor+].

#### 7.3.3 Gestión de la calidad y seguridad de la información

Cada entidad crítica tiene reglas de calidad (completitud, exactitud, oportunidad) medidas cada trimestre (atiende I6; KPI-07). Los datos se clasifican según el MSPI y la Ley 1581 de 2012. La gestión documental electrónica se implementa con el SGDEA cuando el Consejo Departamental de Archivo convalide las tablas de retención (atiende I7; proyecto P2.5).

#### 7.3.4 Análisis y aprovechamiento de la información

Se propone un tablero del PEI y de los contratos alimentado por los sistemas integrados, que reemplace las consolidaciones manuales (atiende I5; proyecto P3.2). Valor+ ya usa analítica e IA en servicios a clientes; se propone usarlas también hacia adentro, empezando por la atención de PQRSD y la mesa de ayuda, con la política de uso de IA vigente (proyecto P4.2).

#### 7.3.5 Desarrollo de capacidades para el uso de la información

Los responsables de datos y los usuarios de los tableros reciben formación en calidad de datos y en el uso de Power BI, dentro del programa de uso y apropiación (proyecto P2.6).

### 7.4 Sistemas de Información

#### 7.4.1 Catálogo objetivo de los sistemas de información

Tabla: Acciones sobre los sistemas de información {T47}

| Sistema | Acción |
|---|---|
| ERP (SICOF) | Modificar o reemplazar. Acción: ERP integrado con presupuesto público, contratos, facturación por proyecto, compras, nómina y activos |
| Hojas de cálculo de los procesos comercial y de servicio | Eliminar como sistema de registro. Acción: Reemplazadas por CRM y gestión de procesos |
| Sistema de gestión de clientes (CRM) | Crear. Acción: Oportunidades, propuestas, contratos, satisfacción y PQRSD de clientes |
| OTRS y GLPI | Reemplazar. Acción: Herramienta de gestión de servicios de TI con prácticas de ITIL 4, para la mesa interna y las de clientes |
| Gestión de procesos (BPMS) y automatización | Crear. Acción: Flujos de los procesos de servicio y contractual; tareas repetitivas automatizadas |
| Capa de integración | Crear. Acción: API entre ERP, CRM, gestión de servicios, SGDEA y tableros |
| Carriel | Modificar. Acción: Evaluarlo frente a los requisitos MoReq; si los cumple, es el SGDEA de Valor+ |
| Herramienta de gestión de riesgos | Crear. Acción: Matriz de riesgos institucional y de TI con planes de tratamiento |
| Intranet | Modificar. Acción: Migrada a SharePoint Online |
| Telefonía IP (Asterisk, FreePBX, Estaqueue) | Modificar. Acción: Telefonía en la nube o actualizada con contingencia |
| Power BI | Mantener. Acción: Conectado a los datos integrados |
| Sitio web | Mantener. Acción: PQRSD conectadas a la herramienta de gestión de servicios |
| SECOP, FURAG, Gestión Transparente | Mantener. Acción: Plataformas de norma |

#### 7.4.2 Mapa de Integraciones objetivo de los Sistemas de Información

Tabla: Matriz de integraciones objetivo {T101}

| Origen | Destino | Información | Mecanismo y seguridad | Proyecto |
|---|---|---|---|---|
| CRM | ERP | Clientes y contratos firmados | API por la capa de integración; autenticación OAuth 2.0 y cifrado TLS | P2.2, P3.1 |
| Gestión de servicios | ERP | Cumplimiento de ANS por contrato, para facturar | API; mismo esquema | P2.3, P3.1 |
| ERP | SGDEA | Expediente contractual y soportes de ejecución | API; mismo esquema | P2.5, P3.1 |
| Sitio web | Gestión de servicios | PQRSD radicadas | Formulario integrado; cifrado TLS | P2.3 |
| ERP, CRM y gestión de servicios | Power BI | Indicadores del PEI y de contratos | Conectores de lectura con cuentas de servicio | P3.2 |
| Directorio en la nube | Todos los sistemas | Identidad y acceso | Inicio de sesión único con segundo factor | P2.4 |

Figura: Arquitectura objetivo de sistemas e infraestructura de Valor+ {img:docs/figuras/arquitectura_objetivo.png}

#### 7.4.3 Arquitectura de Referencia

Principios propuestos: nube primero, con preferencia por soluciones SaaS; un solo sistema maestro por entidad de información; integración por API documentadas; identidad única con segundo factor; y cláusulas de salida y portabilidad en los contratos con proveedores (atiende S4). Estos principios recogen los del PETI 2026-2027 (pág. 72) y les agregan la integración y la identidad única.

#### 7.4.4 Ciclo de Vida de los Sistemas de Información

Se propone un procedimiento de ciclo de vida con cinco etapas, cada una con responsables y criterios de aceptación (proyecto P1.2).

Tabla: Ciclo de vida objetivo de los sistemas de información {T112}

| Actividad | Grado de madurez | Descripción hallazgo u oportunidad de mejora | Acción de mejora |
|---|---|---|---|
| Definición de requisitos | Bajo | El ERP lleva dos años en requisitos | Plantilla de requisitos y plazo máximo de un trimestre por proyecto (P1.2, P1.5) |
| Selección y contratación | Medio | Principios de adquisición y comité de compras | Evaluación técnica y de seguridad en el Comité de TI (P1.1) |
| Desarrollo | Medio | Scrum para software | Mantener; agregar revisión de seguridad del código (P1.4) |
| Pruebas y paso a producción | Sin evidencia | Sin procedimiento | Procedimiento de pruebas y control de cambios (P1.2) |
| Retiro | Sin evidencia | Sin plan de retiro | Plan de retiro de OTRS, GLPI y servidores en sitio (P2.3, P2.4) |

#### 7.4.4 Mantenimiento de los Sistemas de Información

Tabla: Mantenimiento objetivo de los sistemas de información {T113}

| Actividad | Grado de madurez | Descripción hallazgo u oportunidad de mejora | Acción de mejora |
|---|---|---|---|
| Mantenimiento de SaaS | Medio | Lo hace el proveedor según contrato | ANS de mantenimiento medidos en el catálogo (P1.3) |
| Mantenimiento de software libre | Bajo | Telefonía y mesa sin plan de actualización | Migración a la nube con contingencia (P2.3, P2.4) |
| Actualización de ofimática | Bajo | Versiones anteriores y libres | Todas las licencias en Office 365 (P2.4) |

#### 7.4.5 Soporte de los Sistemas de Información

Modelo de tres niveles, cada uno con ANS medido (proyectos P1.3 y P2.3).

Tabla: Soporte objetivo de los sistemas de información {T114}

| Actividad | Grado de madurez | Descripción hallazgo u oportunidad de mejora |
|---|---|---|
| Primer nivel | Medio | Mesa de servicios interna con la herramienta nueva y base de conocimiento |
| Segundo nivel | Bajo | Especialistas internos o del proveedor, con ANS en el contrato |
| Tercer nivel | Bajo | Fabricante, con ANS en el contrato de soporte |

### 7.5 Infraestructura TI

#### 7.5.1 Arquitectura de infraestructura tecnológica

La infraestructura objetivo mantiene el modelo híbrido, pero deja en las sedes solo lo que necesita estar en ellas: red, equipos de usuario y cuartos técnicos. Los cinco servicios críticos que hoy están en sitio pasan a la nube o quedan con contingencia en la nube (atiende T1; proyecto P2.4):

- el servidor de archivos, a SharePoint y OneDrive;
- el directorio activo, al directorio en la nube de Microsoft 365;
- la intranet, a SharePoint Online;
- la telefonía, a una solución en la nube con contingencia;
- la mesa de ayuda, a la herramienta SaaS de gestión de servicios.

Se propone además un centro de operaciones de red (NOC) que monitoree disponibilidad y capacidad, junto con el SOC propio (proyecto P3.3). La transición a IPv6 de la red propia se adelanta, porque su plazo legal venció en 2022: diagnóstico en 2027 (P1.6) e implementación en 2028 (P2.4) (atiende T3).

Tabla: Servicios de infraestructura de TI a fortalecer {T115}

| Servicio | Acción | Situación objetivo | Proyecto |
|---|---|---|---|
| SI01 Cómputo | Modificar | Servidores de Valor+ en la nube; nada crítico en sitio | P2.4 |
| SI02 Almacenamiento | Modificar | SharePoint y OneDrive con permisos por proceso | P2.4 |
| SI03 Respaldo | Modificar | Respaldo con pruebas de restauración trimestrales | P1.6 |
| SI04 Redes | Modificar | Redes segmentadas y monitoreadas por el NOC | P3.3 |
| SI05 Servicios base | Modificar | Directorio en la nube con inicio de sesión único | P2.4 |
| SI06 Seguridad perimetral | Mantener | Con monitoreo del SOC | P1.4 |
| SI07 Telefonía | Modificar | Telefonía en la nube con contingencia | P2.4 |

Tabla: Catálogo de elementos de infraestructura objetivo {T116}

| Id | Elemento de infraestructura | Tipo | Servicio de infraestructura involucrado | Acción de mejora |
|---|---|---|---|---|
| IT01 | Servidores virtuales y sitio web en AWS | Infraestructura como servicio | SI01 Cómputo | Mantener; plan de capacidad (P3.3) |
| IT02 | Servicios en Oracle Cloud y Azure | Infraestructura y plataforma como servicio | SI01 Cómputo | Mantener |
| IT03 | Servidores físicos en sede | Instalado en sitio | SI01 Cómputo | Retirar al migrar (P2.4) |
| IT04 | Servidor de archivos (unidad V) | Instalado en sitio | SI02 Almacenamiento | Migrar a SharePoint (P2.4) |
| IT05 | OneDrive y SharePoint | Software como servicio | SI02 Almacenamiento | Ampliar con permisos por proceso (P2.4) |
| IT06 | Respaldo en AWS | Infraestructura como servicio | SI03 Respaldo | Pruebas de restauración trimestrales (P1.6) |
| IT07 | Red LAN, WAN, VPN e internet | Instalado en sitio y proveedor | SI04 Redes | Segmentar y monitorear con NOC (P3.3) |
| IT08 | Directorio activo, DNS y DHCP | Instalado en sitio | SI05 Servicios base | Directorio en la nube con inicio de sesión único (P2.4) |
| IT09 | UTM en alta disponibilidad | Instalado en sitio | SI06 Seguridad | Mantener con monitoreo del SOC (P1.4) |
| IT10 | Antimalware de equipos | Licencia | SI06 Seguridad | Integrar al SOC (P1.4) |
| IT11 | Planta telefónica IP | Instalado en sitio | SI07 Telefonía | Migrar a la nube con contingencia (P2.4) |
| IT12 | OTRS y GLPI | Instalado en sitio | Soporte | Reemplazar por herramienta SaaS (P2.3) |
| IT13 | Equipos de usuario | Instalado en sitio | Estaciones de trabajo | Reposición por vida útil de 3 a 5 años (PETI 2026-2027 de Valor+, pág. 74) |

#### 7.5.2 Administración de la capacidad de la infraestructura tecnológica

Se propone un plan de capacidad anual que relacione el crecimiento de contratos y usuarios con la capacidad de red, nube y mesa de servicios, revisado en el Comité de TI (atiende T2; proyecto P3.3).

#### Situación objetivo de uso y apropiación de TI

Se propone un programa de uso y apropiación con tres frentes (atiende U1; proyecto P2.6). Se mide con KPI-05 y KPI-11:

- formación en los sistemas nuevos, al ritmo de cada implantación;
- formación anual en seguridad para todos los colaboradores;
- gestión del cambio con los líderes de proceso, coordinada con Capital Humano, para que los usuarios no vuelvan a las hojas de cálculo (riesgo R06).

#### Situación objetivo de seguridad de la información

A 2030 la seguridad de la información llega a 76 sobre 100 en la escala del MSPI (calificación objetivo del numeral 6.7). Para eso se proponen cinco acciones (atienden SG1, SG2 y G7):

- la gestión de incidentes con procedimiento, tiempos y reporte (proyecto P1.4);
- el SOC propio operando para la TI interna (P1.4);
- la recuperación probada cada año (P1.6);
- un responsable dedicado de seguridad de la información (P1.1);
- la evaluación anual con el instrumento del MSPI (KPI-10).

La certificación ISO 22301 que Valor+ planeó para 2026 (Informe de gestión 2025, pág. 89) se mantiene como meta si no se logra antes de 2027. Una certificación ISO/IEC 27001 se evaluará en 2029 con la madurez alcanzada, como decisión del Comité de TI, y no es meta de este plan.

## 8. Hoja de ruta y portafolio de proyectos

Este numeral reúne las brechas, las oportunidades, las iniciativas de otros planes y el portafolio de proyectos, con presupuesto, responsables, alcance y mapa de ruta. Todo es propuesto. Ningún proyecto pasa a ejecución sin patrocinador, caso de negocio, costo validado por la Gerencia Financiera y aprobación del Comité de TI. Los responsables son roles propuestos.

#### Catálogo de brechas

Método (actividad 11 de la guía): cada brecha compara la fila de un dominio del numeral 6 (situación actual) con la misma fila del numeral 7 (situación objetivo). La columna "Justificación" cita el código del hallazgo, y la acción es crear (no existe), modificar (existe pero no alcanza) o eliminar. Después se revisaron la DOFA y los motivadores del numeral 5 para no dejar nada por fuera.

Tabla: Catálogo de brechas {T101}

| ID | Elemento | Dominio | Acción | Justificación: hallazgo de origen (numeral 6) | Descripción de la situación objetivo (numeral 7) | Tiempo estimado | Costo estimado | Proyecto |
|---|---|---|---|---|---|---|---|---|
| BRE-001 | Comité de TI y esquema de decisiones con montos | Gobierno de TI | Crear | G1, G9: ningún comité revisa el portafolio de TI completo; el escalamiento no define montos | Sesión mensual de TI del Comité Directivo y tabla de decisiones (7.2) | 6 meses | Bajo | P1.1 |
| BRE-002 | Roles de seguridad y de gobierno de datos; matriz RACI | Gobierno de TI | Crear | G7, G8: sin cargo dedicado a seguridad ni responsable de datos; sin RACI | Dos roles nuevos y RACI (7.2.4) | 6 meses | Medio | P1.1 |
| BRE-003 | Presupuesto de TI propio | Gobierno de TI | Crear | G3: el presupuesto de TI no se ve por separado | Presupuesto de TI revisado cada trimestre (7.2) | 6 meses | Bajo | P1.1 |
| BRE-004 | Procesos de gestión de TI y procedimientos | Gobierno de TI | Modificar | G5, G6, E5: auditoría de TI en 49 %; procedimientos desactualizados; sin procedimiento de pruebas y cambios | Procesos COBIT priorizados en nivel 3 (7.2.3); ciclo de vida de SI (7.4.4) | 11 meses | Bajo | P1.2 |
| BRE-005 | Gestión de proyectos de TI | Gobierno de TI | Modificar | G10: los proyectos de TI no usan la metodología de la PMO | Proyectos con ficha y seguimiento mensual (7.2.5) | 11 meses | Bajo | P1.2 |
| BRE-006 | Plan estratégico de TI con metas | Estrategia de TI | Modificar | E1, E3, E4: visión sin metas, objetivos sin indicadores, sin DOFA ni catálogo de brechas | Este PETI, con revisión anual y actualización en 2030 | 48 meses | Bajo | P1.1, P4.1 |
| BRE-007 | Catálogo de servicios de TI con ANS | Estrategia de TI | Crear | E2: no hay catálogo oficial | Catálogo único, interno y vendido (7.1.4) | 10 meses | Bajo | P1.3 |
| BRE-008 | Indicadores de gestión de la TI interna | Estrategia de TI | Modificar | E6: solo indicadores operativos y financieros | KPI-01 a KPI-11 en un tablero (7.1.6) | 10 meses | Bajo | P1.3 |
| BRE-009 | Gestión de incidentes y SOC propio | Seguridad de la información | Modificar | SG1, SG2: política de incidentes no aplicada de forma constante; SOC en implementación | Procedimiento con tiempos y SOC operando (7.5) | 12 meses | Medio | P1.4 |
| BRE-010 | ERP integrado | Sistemas de información | Modificar | S2: ERP solo financiero; el integrado lleva dos años en requisitos | ERP con presupuesto público, contratos y facturación por proyecto (7.4.1) | 24 meses | Alto | P1.5 |
| BRE-011 | Continuidad y recuperación probada | Seguridad de la información | Modificar | SG2: análisis de impacto hecho; plan sin implementar ni probar | Pruebas anuales con RTO y RPO (7.5) | 12 meses | Medio | P1.6 |
| BRE-012 | Gobierno de datos y política de IA | Gestión de información | Crear | I1, I2, I6, G4: sin catálogo, responsables, calidad ni política de IA | Catálogo, responsables, reglas de calidad y políticas (7.3) | 12 meses | Bajo | P2.1 |
| BRE-013 | Sistema de gestión de clientes (CRM) | Sistemas de información | Crear | S1: el proceso comercial trabaja en Excel | CRM conectado al ERP (7.4.1) | 11 meses | Medio | P2.2 |
| BRE-014 | Herramienta de gestión de servicios de TI | Sistemas de información | Modificar | S5: OTRS y GLPI sin prácticas de ITIL ni medición por contrato | Herramienta SaaS para mesas internas y de clientes (7.4.1) | 9 meses | Medio | P2.3 |
| BRE-015 | Servicios críticos en sitio | Infraestructura de TI | Modificar | T1, I3: archivos, directorio, intranet, telefonía y mesa en las sedes; información sin versiones | Los cinco en la nube o con contingencia (7.5.1) | 18 meses | Medio | P2.4 |
| BRE-016 | Sistema de gestión de documentos electrónicos (SGDEA) | Gestión de información | Crear | I7: SGDEA en diseño; tablas documentales sin convalidar | SGDEA con requisitos MoReq (7.3.3) | 21 meses | Medio | P2.5 |
| BRE-017 | Estrategia de uso y apropiación | Uso y apropiación | Crear | U1: solo acciones sueltas; capacitación sin dato | Programa con formación y gestión del cambio (7.5) | 36 meses | Bajo | P2.6 |
| BRE-018 | Gestión de procesos (BPMS) en servicio y contratación | Sistemas de información | Crear | S1: el proceso de servicio trabaja en Excel | Flujos automatizados (7.4.1) | 18 meses | Alto | P3.1 |
| BRE-019 | Capa de integración y arquitectura de referencia | Sistemas de información | Crear | S3, S4, I4: sin integraciones ni arquitectura adoptada | API documentadas y principios de arquitectura (7.4.2, 7.4.3) | 18 meses | Medio | P3.1 |
| BRE-020 | Herramienta de gestión de riesgos | Gobierno de TI | Crear | G2: la matriz de riesgos se lleva sin herramienta | Riesgos institucionales y de TI en una herramienta (7.2) | 12 meses | Bajo | P3.1 |
| BRE-021 | Analítica institucional integrada | Gestión de información | Modificar | I5: tableros con consolidación manual | Tablero del PEI con datos integrados (7.3.4) | 12 meses | Medio | P3.2 |
| BRE-022 | Plan de capacidad y monitoreo de red | Infraestructura de TI | Crear | T2, numeral 6.5.3: sin plan de capacidad ni NOC | Plan anual de capacidad y NOC (7.5.1, 7.5.2) | 12 meses | Medio | P3.3 |
| BRE-023 | Protocolo IPv6 en la red propia | Infraestructura de TI | Modificar | T3: sin evidencia de IPv6 en la red propia; el plazo de la Resolución 1126 de 2021 venció el 31 de diciembre de 2022 | Red propia en IPv6, en convivencia con IPv4 (7.5.1) | 18 meses | Bajo | P1.6, P2.4 |

Escala de costo (análisis del equipo), ajustada al tamaño de Valor+: bajo, menos de 200 millones de pesos (trabajo interno y apoyo puntual); medio, de 200 a 700 millones (una herramienta o una consultoría); alto, más de 700 millones (una plataforma nueva con implantación). El tiempo es el esfuerzo estimado: semanas para un procedimiento, meses para un sistema de gestión, uno o dos años para implantar una plataforma.

Resultado: 23 brechas, 12 de crear y 11 de modificar. Ninguna es de eliminar. Las hojas de cálculo de los procesos comercial y de servicio dejan de ser sistema de registro, pero eso se logra al crear el CRM y el BPMS (BRE-013, BRE-018).

Tabla: Brechas por dominio y acción {T101}

| Dominio | Crear | Modificar | Total |
|---|---|---|---|
| Gobierno de TI | 4 | 2 | 6 |
| Estrategia de TI | 1 | 2 | 3 |
| Sistemas de información | 3 | 2 | 5 |
| Gestión de información | 2 | 1 | 3 |
| Infraestructura de TI | 1 | 2 | 3 |
| Seguridad de la información | 0 | 2 | 2 |
| Uso y apropiación | 1 | 0 | 1 |
| Total | 12 | 11 | 23 |

#### Oportunidades y necesidades de TI

| ID | Oportunidad | Origen | Proyecto |
|---|---|---|---|
| OPT-001 | Usar la IA que Valor+ ya entrega a clientes en su propia atención de PQRSD y en la mesa de ayuda | Tendencias (numeral 6); Informe de gestión 2025, págs. 91-92 y 103 | P4.2 |
| OPT-002 | Operar el SOC propio como base del servicio SOC para municipios, con una sola operación para la TI interna y la vendida | Tendencias (numeral 6); PETI 2026-2027 de Valor+, pág. 45 | P1.4 |

#### Iniciativas de otros planes

La actividad 12 aplica a Valor+. Como entidad con más de 90 % de capital público, debe integrar sus planes institucionales al plan de acción (Decreto 612 de 2018) y seguir la Política de Gobierno Digital (Decreto 767 de 2022). La guía pide identificar las iniciativas de esos planes que tienen componente de TI y llevarlas al portafolio, para que no queden dos planes haciendo lo mismo. Cada iniciativa queda a cargo de un proyecto del numeral 8, así que su costo ya está incluido en ese proyecto y no se suma aparte.

Tabla: Iniciativas de otros planes con componente de TI {T101}

| ID | Nombre | Plan asociado | Servicios | Descripción | Área líder | Metas estratégicas | Áreas involucradas | Tiempo | Fecha de inicio | Costo | Brechas |
|---|---|---|---|---|---|---|---|---|---|---|---|
| IPGD001 | Operación del MSPI y gestión de incidentes | Plan de Seguridad y Privacidad de la Información (Decreto 612 de 2018; Resolución 500 de 2021) | ST07, SC02 | Procedimiento de incidentes, SOC propio y autoevaluación anual del MSPI | Responsable de seguridad de la información | METI10 | Infraestructura, Planeación, Control Interno | 12 meses | Enero de 2027 | Incluido en P1.4 | BRE-009 |
| IPGD002 | Tratamiento de riesgos de seguridad y continuidad | Plan de Tratamiento de Riesgos de Seguridad y Privacidad de la Información (Decreto 612 de 2018) | ST07 | Riesgos de seguridad en la matriz institucional; plan de recuperación probado | Dirección de Infraestructura | METI09, METI10 | Gestión del Riesgo y Continuidad | 12 meses | Enero de 2027 | Incluido en P1.4 y P1.6 | BRE-009, BRE-011 |
| IPGD003 | SGDEA y preservación digital | Plan Institucional de Archivos (PINAR, aprobado hasta 2027; Informe de gestión 2025, pág. 76) | ST05 | Sistema de gestión de documentos electrónicos con requisitos MoReq y plan de preservación digital | Gestión Documental y Gerencia de TI | METI06 | Administrativa, Secretaría General | 21 meses | Abril de 2028 | Incluido en P2.5 | BRE-016 |
| IPGD004 | Formación en uso de TI y seguridad | Plan Institucional de Capacitación (Decreto 612 de 2018) | ST01, ST02 | Formación en los sistemas nuevos y formación anual en seguridad | Responsable de uso y apropiación | METI11 | Capital Humano | 36 meses | Enero de 2028 | Incluido en P2.6 | BRE-017 |
| IPGD005 | Publicación de información y datos abiertos | Programa de Transparencia y Ética Pública (Ley 2195 de 2022; antes Plan Anticorrupción) | ST05 | Información del sitio web al día, conjuntos de datos abiertos y registro de activos de información | Responsable de gobierno de datos | METI07 | Comunicaciones, Planeación | 12 meses | Enero de 2028 | Incluido en P2.1 | BRE-012 |
| IPGD006 | Habilitadores de la Política de Gobierno Digital | Política de Gobierno Digital (Decreto 767 de 2022) | Todos | Arquitectura de TI (este PETI), seguridad y privacidad (IPGD001) y datos (IPGD005). Los servicios ciudadanos digitales no aplican, porque Valor+ no tiene trámites (numeral 5.1.7) | Gerencia de TI | METI03 | Planeación y Proyectos | 48 meses | Enero de 2027 | Incluido en P1.1, P1.4 y P2.1 | BRE-006, BRE-009, BRE-012 |

#### Catálogo de proyectos

Los 17 proyectos agrupan las 23 brechas y las 2 oportunidades. Se ordenan por dependencia: primero gobierno y seguridad, que dependen solo de la organización; luego los sistemas, que dependen de contratar.

Tabla: Catálogo de proyectos {T101}

| ID | Proyecto | Dominio | Objetivo corporativo | Objetivo de TI | Meta | Brechas u oportunidad | Indicador | Área líder / áreas involucradas | Meses | Inicio y fin | Costo (millones de pesos) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1.1 | Modelo de gobierno de TI | Gobierno de TI | OC01 | OETI01 | METI01, METI03 | BRE-001, BRE-002, BRE-003, BRE-006 | KPI-01, KPI-03 | Gerencia de TI / Gerencia General, Planeación, Capital Humano | 6 meses | Enero a junio de 2027 | 60 |
| P1.2 | Procesos de gestión de TI y gestión de proyectos | Gobierno de TI | OC01, OC02 | OETI01 | METI01, METI02 | BRE-004, BRE-005 | KPI-01, KPI-02 | Gerencia de TI / Planeación y Proyectos (PMO), Arquitectura Empresarial | 11 meses | Febrero a diciembre de 2027 | 150 |
| P1.3 | Catálogo de servicios y tablero de TI | Estrategia de TI | OC04 | OETI02 | METI04, METI05 | BRE-007, BRE-008 | KPI-04, KPI-05 | Dirección de Servicios / Operaciones, clientes internos | 10 meses | Marzo a diciembre de 2027 | 80 |
| P1.4 | Gestión de incidentes y SOC propio | Seguridad de la información | OC01, OC05 | OETI06 | METI10, METI11 | BRE-009, OPT-002 | KPI-10, KPI-11 | Responsable de seguridad / Infraestructura, Riesgos | 12 meses | Enero a diciembre de 2027 | 350 |
| P1.5 | ERP integrado | Sistemas de información | OC02, OC03 | OETI03 | METI06 | BRE-010 | KPI-06 | Gerencia Financiera y Gerencia de TI / Secretaría General, Operaciones | 24 meses | Enero de 2027 a diciembre de 2028 | 1.500 |
| P1.6 | Continuidad y recuperación | Seguridad de la información | OC03, OC04 | OETI05 | METI09, METI10 | BRE-011, BRE-023 | KPI-09, KPI-10 | Dirección de Infraestructura / Riesgo y Continuidad | 12 meses | Enero a diciembre de 2027 | 250 |
| P2.1 | Gobierno de datos y política de IA | Gestión de información | OC01, OC04 | OETI04 | METI07 | BRE-012 | KPI-07 | Responsable de gobierno de datos / líderes de proceso, Secretaría General | 12 meses | Enero a diciembre de 2028 | 180 |
| P2.2 | Sistema de gestión de clientes (CRM) | Sistemas de información | OC04 | OETI03 | METI06 | BRE-013 | KPI-06 | Dirección Comercial y Gerencia de TI | 11 meses | Febrero a diciembre de 2028 | 400 |
| P2.3 | Herramienta de gestión de servicios de TI | Sistemas de información | OC04, OC05 | OETI02 | METI04, METI05 | BRE-014 | KPI-04, KPI-05 | Dirección de Servicios / Operaciones | 9 meses | Enero a septiembre de 2028 | 300 |
| P2.4 | Migración de servicios críticos a la nube | Infraestructura de TI | OC03 | OETI05 | METI08 | BRE-015, BRE-023 | KPI-08 | Dirección de Infraestructura / todas las áreas | 18 meses | Enero de 2028 a junio de 2029 | 500 |
| P2.5 | SGDEA | Gestión de información | OC01, OC02 | OETI03 | METI06 | BRE-016 | KPI-06 | Gestión Documental (Administrativa) y Gerencia de TI | 21 meses | Abril de 2028 a diciembre de 2029 | 450 |
| P2.6 | Programa de uso y apropiación | Uso y apropiación | OC02 | OETI06 | METI05, METI11 | BRE-017 | KPI-05, KPI-11 | Responsable de uso y apropiación / Capital Humano | 36 meses | Enero de 2028 a diciembre de 2030 | 240 |
| P3.1 | Gestión de procesos, integración y riesgos | Sistemas de información | OC02, OC03 | OETI03 | METI06 | BRE-018, BRE-019, BRE-020 | KPI-06 | Gerencia de TI / Operaciones, Secretaría General, Planeación | 18 meses | Enero de 2029 a junio de 2030 | 900 |
| P3.2 | Analítica institucional | Gestión de información | OC01 | OETI04 | METI06, METI07 | BRE-021 | KPI-06, KPI-07 | Planeación y Gerencia de TI | 12 meses | Abril de 2029 a marzo de 2030 | 200 |
| P3.3 | Capacidad y monitoreo de red (NOC) | Infraestructura de TI | OC03, OC04 | OETI05 | METI08 | BRE-022 | KPI-08 | Dirección de Infraestructura | 12 meses | Enero a diciembre de 2029 | 300 |
| P4.1 | Evaluación del PETI y formulación del siguiente | Estrategia de TI | OC01 | OETI01 | METI02 | BRE-006 | KPI-02 | Gerencia de TI / Comité de TI | 6 meses | Julio a diciembre de 2030 | 60 |
| P4.2 | IA en la atención de PQRSD y la mesa de ayuda | Gestión de información | OC04, OC05 | OETI04 | METI05 | OPT-001 | KPI-05 | Gerencia de TI / Atención al ciudadano, Comunicaciones | 12 meses | Enero a diciembre de 2030 | 250 |
| | Total | | | | | | | | | | 6.170 |

Los costos son órdenes de magnitud del equipo (análisis del equipo) y se validan con la Gerencia Financiera antes de aprobar cada proyecto. No incluyen los dos cargos nuevos de P1.1 (seguridad y gobierno de datos), que son gasto de funcionamiento: unos 200 millones de pesos al año desde el segundo semestre de 2027 [VERIFICAR con la escala salarial de Valor+].

#### Fichas de los proyectos de la fase 1

Tabla: Fichas de los proyectos de la fase 1 {T101}

| Proyecto | ¿Para qué? | ¿Por qué? | ¿Cómo? | Entregable | Meta |
|---|---|---|---|---|---|
| P1.1 | Que las decisiones de TI tengan instancia, responsables y presupuesto | Las decisiones pasan por el comité de compras y no hay responsable de seguridad (G1, G7) | Acta del Comité de TI, tabla de decisiones, RACI, perfiles de los dos cargos y estructura del presupuesto de TI; revisión anual del PETI | Comité sesionando desde abril de 2027; cargos provistos en el segundo semestre | METI01, METI03 |
| P1.2 | Subir la calificación de la auditoría de TI y gestionar los proyectos con método | Auditoría de TI en 49 %; procedimientos desactualizados (G6) | Documentar los procesos COBIT priorizados (7.2.3); cerrar las acciones del Plan de Mejoramiento; adoptar la metodología de la PMO | Manual de procesos de TI; fichas de proyecto | METI01 70 % en 2027 |
| P1.3 | Saber qué servicios presta la TI y con qué nivel | No hay catálogo oficial (E2) | Inventariar servicios, acordar ANS con las áreas, medir satisfacción y montar el tablero de KPI en Power BI | Catálogo publicado en la intranet; tablero mensual | METI04 50 % en 2027; línea base de METI05 |
| P1.4 | Que todo incidente de seguridad se detecte, atienda y reporte a tiempo | La política de incidentes no se aplica de forma constante (SG1) | Procedimiento de incidentes con tiempos; SOC propio con monitoreo de la TI interna; campaña anual de concientización | SOC operando; informe trimestral de incidentes | METI10 55 en 2027 |
| P1.5 | Reemplazar las hojas de cálculo de contratos, compras y facturación | El ERP actual solo cubre finanzas y nómina; el integrado lleva dos años en requisitos (S2) | Cierre de requisitos en el primer trimestre de 2027; contratación por convocatoria en el segundo; implantación por módulos en 2028 | ERP en producción en diciembre de 2028 | METI06 37,5 % en 2028 |
| P1.6 | Recuperar los servicios críticos dentro de los tiempos acordados y cerrar el atraso de IPv6 | El plan de continuidad no está implementado ni probado (SG2); el plazo de IPv6 venció en 2022 (T3) | Completar el SGCN con base en el análisis de impacto de 2025; plan de recuperación por servicio; primera prueba en 2027; diagnóstico de IPv6 de la red propia | Plan de recuperación aprobado y probado | METI09: una prueba exitosa en 2027 |

#### Descripción de los proyectos de las fases 2 a 4

- **P2.1 Gobierno de datos y política de IA.** Catálogo de entidades de información, responsables por proceso, reglas de calidad, clasificación, conjuntos de datos abiertos y política de uso de IA.
- **P2.2 CRM.** Oportunidades, propuestas, contratos, satisfacción y PQRSD de clientes, conectado al ERP.
- **P2.3 Herramienta de gestión de servicios.** Reemplaza OTRS y GLPI; atiende la mesa interna, las mesas de clientes y las PQRSD del sitio web; mide ANS por contrato.
- **P2.4 Migración a la nube.** Archivos a SharePoint, directorio en la nube con inicio de sesión único, intranet, telefonía y mesa de ayuda; cada servicio con contingencia. Incluye la implementación de IPv6 en la red propia con el diagnóstico de P1.6 (BRE-023).
- **P2.5 SGDEA.** Evalúa Carriel frente a MoReq y lo implanta, o contrata otro; depende de que el Consejo Departamental de Archivo convalide las tablas de retención.
- **P2.6 Uso y apropiación.** Formación en cada sistema nuevo, formación anual en seguridad y gestión del cambio con los líderes de proceso.
- **P3.1 Gestión de procesos, integración y riesgos.** Flujos de los procesos de servicio y contratación, capa de integración entre ERP, CRM, gestión de servicios y SGDEA, y herramienta de riesgos.
- **P3.2 Analítica institucional.** Tablero del PEI y de contratos sobre datos integrados.
- **P3.3 Capacidad y monitoreo de red.** Plan anual de capacidad y NOC.
- **P4.1 Evaluación del PETI.** Medición final de las metas y formulación del PETI siguiente, alineado con el nuevo PEI y el nuevo plan departamental.
- **P4.2 IA en PQRSD y mesa de ayuda.** Asistente para clasificar y responder solicitudes, con revisión humana, bajo la política de P2.1.

#### Presupuesto estimado por fase

Tabla: Presupuesto estimado del portafolio por vigencia {T101}

| Vigencia | Proyectos activos | Costo estimado (millones de pesos) |
|---|---|---|
| 2027 (fase 1) | P1.1 a P1.6 | 1.640 |
| 2028 (fase 2) | P1.5, P2.1 a P2.6 | 2.236 |
| 2029 (fase 3) | P2.4, P2.5, P2.6, P3.1 a P3.3 | 1.554 |
| 2030 (fase 4) | P2.6, P3.1, P3.2, P4.1, P4.2 | 740 |
| Total | 17 proyectos | 6.170 |

El costo de los proyectos que cruzan dos vigencias se repartió en proporción a sus meses (análisis del equipo).

Figura: Presupuesto estimado del portafolio por vigencia {img:docs/figuras/presupuesto_vigencias.png}

Como referencia, el presupuesto de inversión de toda la empresa fue de 2.134 millones de pesos en 2025 (Informe de gestión 2025, pág. 157), y los ingresos operacionales, de 86.700 millones (pág. 129). El portafolio equivale a unos 1.540 millones al año, cerca del 1,8 % de los ingresos de 2025. La vigencia 2028 supera el presupuesto de inversión de 2025. Si la Gerencia Financiera no puede ampliarlo, la opción es pasar P2.5 (SGDEA) a 2029, porque depende de una convalidación externa, y contratar el ERP y el CRM como servicio, con pagos anuales en lugar de una inversión inicial.

#### Mapa de ruta

Figura: Mapa de ruta del portafolio 2027-2030 {img:docs/figuras/mapa_ruta.png}

Tabla: Calendario del portafolio por trimestres {T101}

| Proyecto | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| P1.1 Modelo de gobierno de TI | T1-T2 | | | |
| P1.2 Procesos de gestión de TI | T1-T4 | | | |
| P1.3 Catálogo y tablero de TI | T1-T4 | | | |
| P1.4 Incidentes y SOC propio | T1-T4 | | | |
| P1.5 ERP integrado | T1-T4 | T1-T4 | | |
| P1.6 Continuidad y recuperación | T1-T4 | | | |
| P2.1 Gobierno de datos e IA | | T1-T4 | | |
| P2.2 CRM | | T1-T4 | | |
| P2.3 Gestión de servicios de TI | | T1-T3 | | |
| P2.4 Migración a la nube | | T1-T4 | T1-T2 | |
| P2.5 SGDEA | | T2-T4 | T1-T4 | |
| P2.6 Uso y apropiación | | T1-T4 | T1-T4 | T1-T4 |
| P3.1 Procesos, integración y riesgos | | | T1-T4 | T1-T2 |
| P3.2 Analítica institucional | | | T2-T4 | T1 |
| P3.3 Capacidad y NOC | | | T1-T4 | |
| P4.1 Evaluación del PETI | | | | T3-T4 |
| P4.2 IA en PQRSD y mesa | | | | T1-T4 |

Dependencias principales: P1.1 antes que todo (el Comité de TI prioriza el resto); P1.5 antes que P2.2 y P3.1 (el CRM y la integración se conectan al ERP); P2.1 antes que P4.2 (la IA necesita la política de datos); y P2.4 antes que P3.3 (la capacidad se planea sobre la infraestructura ya migrada).

#### Medición del portafolio

Cada proyecto tiene al menos un indicador (columna "Indicador" del catálogo) y cada indicador mide al menos un proyecto (hojas de vida del numeral 7.1.6). La PMO reporta el avance al Comité de TI cada mes y el Comité Institucional de Gestión y Desempeño revisa el PETI cada semestre. Los riesgos del portafolio están en la matriz del numeral 7.2 (R01 a R08).

## 9. Estrategia de comunicación del PETI

La comunicación busca que cada grupo sepa qué cambia para él, cuándo y qué se espera de su parte (actividad 17 de la guía). Parte del plan de comunicaciones del PETI 2026-2027 (pág. 82) y lo amplía a los grupos que el diagnóstico identificó (numeral 6.6.1).

#### Grupos de interés

Tabla: Grupos de interés del PETI {T101}

| Grupo | Interés en el PETI | Mensaje principal |
|---|---|---|
| Junta Directiva y Gerencia General | Inversión, riesgos y resultados | Qué se invierte cada año y qué metas se cumplen |
| Comité Institucional de Gestión y Desempeño | Aprobación y seguimiento en el MIPG | Avance de metas y de las políticas de Gobierno Digital y Seguridad Digital |
| Líderes de proceso | Sistemas nuevos, datos y cambios en su trabajo | Qué sistema reemplaza sus hojas de cálculo, cuándo y qué deben aportar |
| Colaboradores | Formación y herramientas | Calendario de capacitaciones y canales de soporte |
| Equipo de TI | Proyectos, roles y procesos | Prioridades del año y responsabilidades (RACI) |
| Clientes | Niveles de servicio | Mejoras en los servicios que contratan y cómo se miden |
| Ciudadanos y entes de control | Transparencia | PETI publicado y resultados anuales |
| IDEA (accionista) | Sostenibilidad y resultados | Resumen anual de inversión y resultados |

#### Plan de comunicación

Tabla: Plan de comunicación del PETI {T101}

| Actividad | Grupo | Canal | Formato | Responsable | Frecuencia |
|---|---|---|---|---|---|
| Presentación del PETI para aprobación | Comité Institucional de Gestión y Desempeño | Sesión del comité | Presentación y documento | Gerente de TI | Una vez (diciembre de 2026) y en cada actualización |
| Publicación del PETI | Ciudadanos, clientes y entes de control | Sitio web, sección de transparencia | Documento PDF | Coordinación de Comunicaciones | Antes del 31 de enero de cada año |
| Lanzamiento interno | Colaboradores | Intranet, correo y reunión general | Pieza gráfica y resumen de una página | Comunicaciones y Gerencia de TI | Enero de 2027 |
| Seguimiento del portafolio | Comité de TI | Sesión del comité | Tablero de indicadores | PMO | Mensual |
| Informe de avance | Comité Institucional y Gerencia General | Sesión del comité | Informe ejecutivo | Gerente de TI | Semestral |
| Anuncio de cada sistema nuevo | Líderes de proceso y usuarios | Correo, intranet y talleres | Guía de uso y calendario de formación | Responsable de uso y apropiación | Al inicio y al cierre de cada proyecto |
| Boletín de seguridad | Colaboradores | Correo | Boletín | Responsable de seguridad | Mensual |
| Resultados anuales | Junta Directiva e IDEA | Informe de gestión | Capítulo de TI | Gerente de TI | Anual |
| Inducción y reinducción | Colaboradores nuevos y antiguos | Programa de Capital Humano | Módulo del PETI | Capital Humano y Gerencia de TI | En cada inducción |

#### Gobierno, aprobación y actualización del PETI

- **Aprobación:** el Comité Institucional de Gestión y Desempeño aprueba el PETI con acta, antes de su publicación (Decreto 612 de 2018). Hasta entonces, todo el documento es una propuesta.
- **Seguimiento:** el Comité de TI revisa el portafolio cada mes (KPI-02) y el Comité Institucional revisa las metas cada semestre.
- **Actualización:** el PETI se revisa una vez al año, al preparar el plan de acción, y se actualiza cuando cambie el PEI (2027), cuando cambie el plan departamental (2028) o cuando un riesgo de la matriz se materialice. La evaluación final y la formulación del siguiente PETI son el proyecto P4.1.
- **Control de cambios:** cada versión se registra con número, fecha y numerales modificados.

## Glosario

- **ANS (acuerdo de nivel de servicio):** compromiso medible sobre un servicio, por ejemplo tiempo de atención o disponibilidad.
- **BPMS:** sistema para modelar, automatizar y medir procesos de negocio.
- **Brecha:** diferencia entre la situación actual y la objetivo de un elemento de TI, que se cierra al crearlo, modificarlo o eliminarlo.
- **COBIT 2019:** marco de gobierno y gestión de TI de ISACA.
- **CRM:** sistema de gestión de la relación con los clientes.
- **DOFA:** análisis de debilidades, oportunidades, fortalezas y amenazas.
- **ERP:** sistema que integra la gestión financiera, administrativa y de recursos de la empresa.
- **FURAG:** Formulario Único de Reporte y Avance de Gestión, con el que Función Pública mide el MIPG.
- **ITA:** Índice de Transparencia y Acceso a la Información de la Procuraduría.
- **ITIL 4:** marco de buenas prácticas de gestión de servicios de TI.
- **MIPG:** Modelo Integrado de Planeación y Gestión.
- **MoReq:** modelo de requisitos para sistemas de gestión de documentos electrónicos.
- **MRAE:** Marco de Referencia de Arquitectura Empresarial del MinTIC.
- **MSPI:** Modelo de Seguridad y Privacidad de la Información del MinTIC.
- **NOC:** centro de operaciones de red.
- **PEI:** Plan Estratégico Institucional de Valor+ 2024-2027.
- **PMO:** oficina de gestión de proyectos.
- **PQRSD:** peticiones, quejas, reclamos, sugerencias y denuncias.
- **RACI:** matriz que asigna quién ejecuta (R), quién aprueba (A), a quién se consulta (C) y a quién se informa (I).
- **RTO y RPO:** tiempo máximo para recuperar un servicio y pérdida máxima de datos aceptable.
- **SaaS:** software contratado como servicio en la nube.
- **SGDEA:** sistema de gestión de documentos electrónicos de archivo.
- **SOC:** centro de operaciones de seguridad.
- **SGSI:** sistema de gestión de seguridad de la información.

## Referencias Bibliográficas

Archivo General de la Nación. (2024). *Acuerdo 001 de 2024*.

Congreso de Colombia. (1993). *Ley 87 de 1993*.

Congreso de Colombia. (1998). *Ley 489 de 1998*.

Congreso de Colombia. (2000). *Ley 594 de 2000, Ley General de Archivos*.

Congreso de Colombia. (2007). *Ley 1150 de 2007*.

Congreso de Colombia. (2008). *Ley 1258 de 2008*.

Congreso de Colombia. (2011). *Ley 1474 de 2011*.

Congreso de Colombia. (2012). *Ley 1581 de 2012*.

Congreso de Colombia. (2014). *Ley 1712 de 2014*.

Congreso de Colombia. (2015). *Ley 1755 de 2015*.

Congreso de Colombia. (2022). *Ley 2195 de 2022*.

Congreso de Colombia. (2023). *Ley 2294 de 2023, Plan Nacional de Desarrollo 2022-2026*.

Consejo Nacional de Política Económica y Social. (2020). *Documento CONPES 3995: Política nacional de confianza y seguridad digital*.

Consejo Nacional de Política Económica y Social. (2025). *Documento CONPES 4144: Política nacional de inteligencia artificial*.

Gobernación de Antioquia. (2024). *Lista la hoja de ruta para Antioquia: el Plan de Desarrollo Departamental 2024-2027 "Por Antioquia Firme" fue aprobado en la Asamblea*. https://www.antioquia.gov.co/noticias-planeacion/lista-la-hoja-de-ruta-para-antioquia-el-plan-de-desarrollo-departamental-20242027-por-antioquia-firme-fue-aprobado-en-la-asamblea

Instituto para el Desarrollo de Antioquia. (s. f.). *Filiales IDEA*. https://www.idea.gov.co/filiales-idea/

ISACA. (2018). *COBIT 2019 Framework: Governance and Management Objectives*.

ISO. (2019). *ISO 22301:2019, Security and resilience. Business continuity management systems. Requirements*.

ISO/IEC. (2022). *ISO/IEC 27001:2022, Information security, cybersecurity and privacy protection. Information security management systems. Requirements*.

AXELOS. (2019). *ITIL Foundation: ITIL 4 Edition*.

Ministerio de Tecnologías de la Información y las Comunicaciones. (2017). *Resolución 2710 de 2017*.

Ministerio de Tecnologías de la Información y las Comunicaciones. (2020). *Resolución 1519 de 2020*.

Ministerio de Tecnologías de la Información y las Comunicaciones. (2021). *Resolución 500 de 2021, Modelo de Seguridad y Privacidad de la Información*.

Ministerio de Tecnologías de la Información y las Comunicaciones. (2023). *Guía para la construcción del PETI, MGGTI.GE.ES.03, versión 3.0*, con sus anexos 1 (herramientas) y 2 (plantilla).

Presidencia de la República. (2015). *Decreto 103 de 2015*.

Presidencia de la República. (2015). *Decreto 1078 de 2015, Decreto Único Reglamentario del Sector TIC*.

Presidencia de la República. (2015). *Decreto 1080 de 2015, Decreto Único Reglamentario del Sector Cultura*.

Presidencia de la República. (2015). *Decreto 1083 de 2015, Decreto Único Reglamentario del Sector Función Pública*.

Presidencia de la República. (2016). *Decreto 415 de 2016*.

Presidencia de la República. (2017). *Decreto 1499 de 2017*.

Presidencia de la República. (2020). *Decreto 620 de 2020*.

Presidencia de la República. (2018). *Decreto 612 de 2018*.

Presidencia de la República. (2022). *Decreto 338 de 2022*.

Presidencia de la República. (2022). *Decreto 767 de 2022*.

Valor + S.A.S. (2017). *Instrucción Administrativa 060 del 10 de octubre de 2017*. https://s3-site-vmas-cdn.s3.amazonaws.com/assets/2025/08/25100410/060-FIJAN-TASAS-APLICABLES-A-LOS-TRAMITES-10-10-2017.pdf

Valor + S.A.S. (2024). *Estados financieros a marzo de 2024*.

Valor + S.A.S. (2025). *Informe de gestión 2024*. https://s3-site-vmas-cdn.s3.amazonaws.com/assets/2025/02/12152920/Informe-de-gestion-2024-actualizado.pdf

Valor + S.A.S. (2026). *Informe de gestión 2025*, versión 2, 11 de marzo de 2026.

Valor + S.A.S. (2026). *Plan Estratégico de Tecnologías de la Información (PETI) 2026-2027*, DA01-PL-GETI, versión 4.0.

Valor + S.A.S. (s. f.). *Transparencia y acceso a la información pública*. https://valormas.gov.co/transparencia/

## Anexo A. Equivalencia con los identificadores del Anexo 1

Tabla: Equivalencia de identificadores {T101}

| Elemento | Identificador en este PETI | Identificador del Anexo 1 |
|---|---|---|
| Objetivos de TI | OETI01 a OETI06 | OETI01 a OETI06 |
| Metas de TI | METI01 a METI11 | METI01 a METI11 |
| Brechas | BRE-001 a BRE-023 | B001 a B023 |
| Proyectos | P1.1 a P4.2 | IT001 a IT017, en el orden del catálogo de proyectos del numeral 8 |
| Indicadores | KPI-01 a KPI-11 | IND.ES.01 a IND.ES.11 |

## Anexo B. Procesos del PETI frente a marcos de referencia

Tabla: Procesos del PETI frente a marcos de referencia {T101}

| Elemento del PETI | Proyecto | Marco | Referencia |
|---|---|---|---|
| Gobierno de TI y Comité de TI | P1.1 | COBIT 2019 | EDM01 Ensured Governance Framework Setting and Maintenance |
| Marco de gestión y procesos de TI | P1.2 | COBIT 2019 | APO01 Managed I&T Management Framework |
| Portafolio y proyectos | P1.2, numeral 8 | COBIT 2019 | APO05 Managed Portfolio; BAI01 Managed Programs |
| Presupuesto de TI | P1.1 | COBIT 2019 | APO06 Managed Budget and Costs |
| Catálogo y niveles de servicio | P1.3, P2.3 | COBIT 2019; ITIL 4 | APO09 Managed Service Agreements; prácticas de gestión del catálogo y de niveles de servicio |
| Riesgos de TI | Numeral 7.2, P3.1 | COBIT 2019 | APO12 Managed Risk |
| Seguridad de la información | P1.4 | COBIT 2019; MSPI | APO13 Managed Security; Resolución 500 de 2021 |
| Gobierno de datos | P2.1 | COBIT 2019 | APO14 Managed Data |
| Adquisición e implantación de sistemas | P1.5, P2.2, P3.1 | COBIT 2019 | BAI03 Managed Solutions Identification and Build |
| Cambio organizacional y apropiación | P2.6 | COBIT 2019 | BAI05 Managed Organizational Change |
| Cambios de TI | P1.2 | COBIT 2019; ITIL 4 | BAI06 Managed IT Changes; práctica de habilitación del cambio |
| Capacidad y disponibilidad | P3.3 | COBIT 2019 | BAI04 Managed Availability and Capacity |
| Incidentes y solicitudes | P1.4, P2.3 | COBIT 2019; ITIL 4 | DSS02 Managed Service Requests and Incidents; prácticas de mesa de servicios y gestión de incidentes |
| Continuidad | P1.6 | COBIT 2019; ISO 22301:2019 | DSS04 Managed Continuity |
| Uso de la nube | P2.4 | ISO/IEC 27001:2022 | 5.23 Seguridad de la información para el uso de servicios en la nube |
| Gestión de incidentes de seguridad | P1.4 | ISO/IEC 27001:2022 | 5.24 a 5.28 Gestión de incidentes de seguridad de la información |
| Gestión documental electrónica | P2.5 | MoReq; Acuerdo 001 de 2024 | Requisitos de SGDEA |
| Seguimiento del PETI | KPI-02, numeral 9 | COBIT 2019 | MEA01 Managed Performance and Conformance Monitoring |

## Anexo C. Arquitectura actual y objetivo

La guía es parte del MRAE: la situación actual por dominio (numeral 6) es la arquitectura actual, y la situación objetivo (numeral 7) es la arquitectura destino. Esta tabla las reordena por las capas de TOGAF.

Tabla: Arquitectura actual y objetivo por capa de TOGAF {T101}

| Capa | Arquitectura actual | Arquitectura objetivo | Proyectos |
|---|---|---|---|
| Negocio (procesos, roles, gobierno) | 16 procesos; comercial y servicio en Excel; sin comité de TI ni RACI; PMO en construcción | Comité de TI, RACI, procesos de TI documentados, procesos misionales digitalizados | P1.1, P1.2, P3.1 |
| Datos | Información en la unidad V sin versiones; sin catálogo ni responsables | Catálogo, responsables, calidad medida, SharePoint, SGDEA | P2.1, P2.4, P2.5 |
| Aplicaciones | ERP solo financiero; OTRS y GLPI; sin integraciones | ERP integrado, CRM, BPMS, herramienta de gestión de servicios, capa de integración | P1.5, P2.2, P2.3, P3.1 |
| Tecnología | Híbrida; cinco servicios críticos en sitio; sin plan de capacidad; IPv6 sin evidencia en la red propia | Nube primero; servicios críticos en la nube o con contingencia; NOC; IPv6 | P1.6, P2.4, P3.3 |
| Seguridad (transversal) | SGSI actualizado al MSPI 2025; incidentes sin gestión constante; recuperación sin probar | MSPI en 76 sobre 100; SOC propio; recuperación probada cada año | P1.4, P1.6 |

Las figuras de infraestructura actual (numeral 6.5.1) y de arquitectura objetivo (numeral 7.4.2) muestran estas dos vistas.

## Anexo D. Matriz de trazabilidad

Tabla: Matriz de trazabilidad {T101}

| Objetivo de TI | Objetivo corporativo | Metas | Brechas | Proyectos | Indicadores | Riesgos |
|---|---|---|---|---|---|---|
| OETI01 | OC01, OC02 | METI01, METI02, METI03 | BRE-001 a BRE-006, BRE-020 | P1.1, P1.2, P4.1 | KPI-01, KPI-02, KPI-03 | R04, R07 |
| OETI02 | OC04, OC05 | METI04, METI05 | BRE-007, BRE-008, BRE-014 | P1.3, P2.3 | KPI-04, KPI-05 | R06 |
| OETI03 | OC02, OC03 | METI06 | BRE-010, BRE-013, BRE-016, BRE-018, BRE-019 | P1.5, P2.2, P2.5, P3.1 | KPI-06 | R01, R08 |
| OETI04 | OC01, OC04 | METI07 | BRE-012, BRE-021, OPT-001 | P2.1, P3.2, P4.2 | KPI-07 | R05 |
| OETI05 | OC03, OC04 | METI08, METI09 | BRE-011, BRE-015, BRE-022, BRE-023 | P1.6, P2.4, P3.3 | KPI-08, KPI-09 | R03 |
| OETI06 | OC01, OC05 | METI10, METI11 | BRE-009, BRE-017, OPT-002 | P1.4, P2.6 | KPI-10, KPI-11 | R02, R06 |

Dos ejemplos completos de la cadena:

- OC03 "Aumentar la sostenibilidad financiera" → OETI03 "Digitalizar los procesos misionales y de apoyo" → METI06, procesos con cobertura total de 12,5 % a 81 % → KPI-06. El diagnóstico dice que el ERP solo cubre finanzas y nómina y que el integrado lleva dos años en requisitos (numeral 6.4.1, S2; PETI 2026-2027 de Valor+, págs. 77-78) → BRE-010, modificar, 24 meses, costo alto → P1.5, Gerencia Financiera y Gerencia de TI, enero de 2027 a diciembre de 2028 → mide KPI-06 → mitiga R01.
- OC01 "Fortalecer la gobernanza" → OETI06 "Elevar la madurez de seguridad y la apropiación" → METI10, madurez del MSPI de 47 a 76 → KPI-10. El diagnóstico dice que las políticas de incidentes "no son administradas de forma constante" (numeral 6.2.2, SG1; PETI 2026-2027 de Valor+, pág. 42) → BRE-009, modificar, 12 meses, costo medio → P1.4, responsable de seguridad, enero a diciembre de 2027 → mide KPI-10 → mitiga R02.

## Anexo E. Equipo, presupuesto y cronograma de elaboración del PETI

Equipo que elabora el PETI (actividad 1). Es un equipo académico de Gobierno y Servicios de TI que asume el rol del área de TI de Valor+; no pertenece a la organización.

Tabla: Equipo del PETI {T101}

| Integrante | Rol en el equipo | Numerales a cargo | Actividades de la guía |
|---|---|---|---|
| Hannyer Arce Ararat | Líder y coordinador | Introducción, objetivo y alcance, metodología, numeral 9 y consolidación | 1, 2, 3, 15, 16 y 17 |
| Kevin Steven Tabares Blanco | Contexto y normatividad | Normatividad, numeral 5, glosario y Anexo B | 4 y 5 |
| Raul Guillermo Orobio Ospina | Diagnóstico de estrategia, gobierno e información; evidencia | Numerales 6.1 a 6.3, referencias y registro de evidencias | 6 |
| Ever Jonatan Delgado Chaguendo | Diagnóstico de sistemas, infraestructura, uso y seguridad; arquitectura | Numerales 6.4 a 6.7, DOFA, tendencias y Anexo C | 6 y 7 |
| Juan Jose Muñoz | Situación objetivo y brechas | Numeral 7 y brechas, oportunidades y otros planes del numeral 8 | 8 a 12 |
| Luis Fernando Narvaes Marin | Portafolio, indicadores y riesgos | Numerales 7.1.6 y 7.2 (riesgos), portafolio y mapa de ruta, Anexos A y D | 13 y 14 |

Partes interesadas en la organización. Se nombran por área, según el organigrama de 2024; no se nombran personas.

Tabla: Partes interesadas en la organización {T101}

| Rol en el PETI | Área | Capacidad de decisión | Aporte |
|---|---|---|---|
| Patrocinador | Gerencia General | Alta | Respaldo, presupuesto y presidencia del Comité de TI |
| Instancia de aprobación | Comité Institucional de Gestión y Desempeño | Alta | Aprobación del PETI y seguimiento semestral |
| Responsable del plan | Gerencia de Tecnología, Innovación y Sostenibilidad | Media | Formulación, ejecución y seguimiento |
| Gestión de proyectos | Dirección de Planeación y Proyectos (PMO) | Media | Metodología y seguimiento del portafolio |
| Validación financiera | Gerencia Financiera | Media | Validación de costos y presupuesto de TI |
| Dueños de procesos y de datos | Gerencia de Operaciones, Dirección Comercial, Secretaría General | Media, en sus procesos | Requisitos y responsables de datos |
| Aseguramiento | Oficina de Control Interno | Baja: evalúa, no decide | Auditoría del avance |

Presupuesto para elaborar el PETI (actividad 2). El plan lo elabora el equipo académico, sin consultoría externa ni compra de herramientas. Su único recurso es el tiempo de los seis integrantes; no tiene costo para Valor+.

Tabla: Cronograma de construcción del PETI {T101}

| Fase | ID | Actividades | Fecha | Responsable | Salida |
|---|---|---|---|---|---|
| Planear | CR-01 | 1 a 3 | 5 de octubre de 2026 | Hannyer Arce Ararat | Equipo, presupuesto y cronograma |
| Analizar | CR-02 | 4 a 7 | 5 de octubre de 2026 | Kevin Steven Tabares Blanco, Raul Guillermo Orobio Ospina, Ever Jonatan Delgado Chaguendo | Numerales 5 y 6 |
| Construir | CR-03 | 8 a 15 | 5 de octubre de 2026 | Juan Jose Muñoz, Luis Fernando Narvaes Marin; consolidación: Hannyer Arce Ararat | Numerales 7 y 8 y este documento |

## Anexo F. Fichas de servicios y sistemas de información

La plantilla pide dejar en el cuerpo del documento el resumen (numerales 6.1.3, 6.4.1, 7.1.4 y 7.4.1) y el detalle como anexo. Cada ficha describe la situación actual y, en los atributos que cambian, la acción propuesta. Fuentes: PETI 2026-2027 de Valor+, págs. 33-61 y 70-81; Informe de gestión 2025, págs. 16-17 y 80-92.

#### Fichas de los servicios de TI

Tabla: Servicio de TI ST01 Mesa de ayuda interna {T11}

| Nombre | Mesa de ayuda interna |
|---|---|
| Descripción | Soporte a usuarios, incidentes, requerimientos e inventario de equipos |
| Categoría | Soporte |
| Usuario objetivo | Colaboradores |
| Horario de prestación del servicio | Días hábiles en horario laboral (horario no publicado) |
| Canal de soporte | Correo y herramienta OTRS/GLPI. Acción: Portal de autoservicio en la herramienta nueva (P2.3) |
| Acuerdo de nivel de servicio | Oportunidad ≥ 95 % (98,72 % en 2025); ANS internos ≥ 80 % (94,71 %). Acción: Se agrega satisfacción ≥ 85 % (KPI-05) |
| Hallazgos u oportunidades de mejora | Herramienta de software libre sin prácticas de ITIL (S5). Acción: Reemplazo de la herramienta (P2.3) |

Tabla: Servicio de TI ST02 Ofimática, correo y colaboración {T11}

| Nombre | Ofimática, correo y colaboración |
|---|---|
| Descripción | Office 365, Teams, OneDrive y SharePoint |
| Categoría | Colaboración |
| Usuario objetivo | Colaboradores |
| Horario de prestación del servicio | 24 horas, 7 días a la semana |
| Canal de soporte | Mesa de ayuda |
| Acuerdo de nivel de servicio | Sin ANS propio. Acción: ANS de disponibilidad del proveedor medido (P1.3) |
| Hallazgos u oportunidades de mejora | Licencias de versiones anteriores y libres por migrar (pág. 70). Acción: Todas las licencias en Office 365 (P2.4) |

Tabla: Servicio de TI ST03 Conectividad interna {T11}

| Nombre | Conectividad interna |
|---|---|
| Descripción | LAN, WAN, VPN e internet en las sedes |
| Categoría | Conectividad |
| Usuario objetivo | Colaboradores y sedes |
| Horario de prestación del servicio | 24 horas, 7 días a la semana |
| Canal de soporte | Mesa de ayuda |
| Acuerdo de nivel de servicio | Disponibilidad ≥ 99 % (100 % en 2025) |
| Hallazgos u oportunidades de mejora | Sin monitoreo de red ni plan de capacidad (T2). Acción: NOC y plan de capacidad (P3.3) |

Tabla: Servicio de TI ST04 Telefonía IP y contact center {T11}

| Nombre | Telefonía IP y contact center |
|---|---|
| Descripción | Planta telefónica y gestión de colas del contact center |
| Categoría | Comunicaciones |
| Usuario objetivo | Colaboradores y operación de clientes |
| Horario de prestación del servicio | Según la operación de cada contrato |
| Canal de soporte | Mesa de ayuda |
| Acuerdo de nivel de servicio | Incluido en disponibilidad de servicios críticos. Acción: Disponibilidad ≥ 99 % propia |
| Hallazgos u oportunidades de mejora | Planta en sitio sin contingencia (pág. 81). Acción: Telefonía en la nube con contingencia (P2.4) |

Tabla: Servicio de TI ST05 Sitio web e intranet {T11}

| Nombre | Sitio web e intranet |
|---|---|
| Descripción | Información institucional, transparencia, PQRSD y comunicación interna |
| Categoría | Servicios digitales |
| Usuario objetivo | Ciudadanos, clientes y colaboradores |
| Horario de prestación del servicio | 24 horas, 7 días a la semana |
| Canal de soporte | Formulario web y correo. Acción: PQRSD conectadas a la herramienta de servicios (P2.3) |
| Acuerdo de nivel de servicio | ITA 94 puntos. Acción: ITA ≥ 94 |
| Hallazgos u oportunidades de mejora | Intranet en sitio; PQRSD sin conexión a la mesa de servicios. Acción: Intranet en SharePoint (P2.4) |

Tabla: Servicio de TI ST06 Soporte a sistemas de información {T11}

| Nombre | Soporte a sistemas de información |
|---|---|
| Descripción | Soporte funcional y técnico del ERP y de las aplicaciones de apoyo |
| Categoría | Sistemas de información |
| Usuario objetivo | Áreas de apoyo |
| Horario de prestación del servicio | Días hábiles |
| Canal de soporte | Mesa de ayuda y proveedor |
| Acuerdo de nivel de servicio | Sin ANS propio. Acción: ANS por sistema (P1.3) |
| Hallazgos u oportunidades de mejora | Sin modelo de segundo y tercer nivel (pág. 78). Acción: Modelo de tres niveles (P2.3) |

Tabla: Servicio de TI ST07 Seguridad, respaldo y recuperación {T11}

| Nombre | Seguridad, respaldo y recuperación |
|---|---|
| Descripción | Perímetro, antimalware, respaldo y gestión de incidentes |
| Categoría | Seguridad |
| Usuario objetivo | Toda la organización |
| Horario de prestación del servicio | 24 horas, 7 días a la semana |
| Canal de soporte | Mesa de ayuda y correo de seguridad |
| Acuerdo de nivel de servicio | Ataques bloqueados ≥ 99 % (100 %); incidentes gestionados 100 %. Acción: Incidentes atendidos dentro del ANS ≥ 95 % |
| Hallazgos u oportunidades de mejora | Incidentes sin gestión constante (SG1); recuperación sin probar (SG2). Acción: SOC propio y pruebas de recuperación (P1.4, P1.6) |

Tabla: Servicio de TI SC01 Mesas de servicio para clientes {T11}

| Nombre | Mesas de servicio para clientes |
|---|---|
| Descripción | Operación de mesas de servicio para entidades públicas |
| Categoría | Servicio vendido |
| Usuario objetivo | Gobernación, IDEA, Ferrocarril de Antioquia y otros |
| Horario de prestación del servicio | Según contrato |
| Canal de soporte | Mesa de servicio del cliente |
| Acuerdo de nivel de servicio | ANS contractuales ≥ 94 % (95,71 % en 2025) |
| Hallazgos u oportunidades de mejora | Medición por contrato en hojas de cálculo. Acción: Medición en la herramienta de servicios y en el catálogo (P1.3, P2.3) |

Tabla: Servicio de TI SC02 SOC y pruebas de vulnerabilidad {T11}

| Nombre | SOC y pruebas de vulnerabilidad |
|---|---|
| Descripción | Monitoreo de seguridad y pruebas para entidades |
| Categoría | Servicio vendido |
| Usuario objetivo | IDEA, Lotería de Medellín, municipios |
| Horario de prestación del servicio | 24 horas para el monitoreo |
| Canal de soporte | Portal y correo del SOC |
| Acuerdo de nivel de servicio | Por contrato |
| Hallazgos u oportunidades de mejora | SOC IDEA con 37 % de avance físico en 2025. Acción: Operación única con el SOC propio (P1.4, OPT-002) |

Tabla: Servicio de TI SC03 Conectividad para territorios {T11}

| Nombre | Conectividad para territorios |
|---|---|
| Descripción | Conectividad satelital y wifi público |
| Categoría | Servicio vendido |
| Usuario objetivo | Gobernación y municipios |
| Horario de prestación del servicio | Según contrato |
| Canal de soporte | Mesa de servicio |
| Acuerdo de nivel de servicio | Por contrato |
| Hallazgos u oportunidades de mejora | Proyectos de cliente fuera del alcance de proyectos |

Tabla: Servicio de TI SC04 Desarrollo de software y asistentes con IA {T11}

| Nombre | Desarrollo de software y asistentes con IA |
|---|---|
| Descripción | Desarrollo y soluciones con IA para entidades |
| Categoría | Servicio vendido |
| Usuario objetivo | IDEA, Lotería de Medellín, Gobernación |
| Horario de prestación del servicio | Días hábiles |
| Canal de soporte | Gestión del proyecto |
| Acuerdo de nivel de servicio | Por contrato |
| Hallazgos u oportunidades de mejora | Sin política interna de uso de IA (G4). Acción: Política de uso de IA (P2.1) |

Tabla: Servicio de TI SC05 Hosting y servicios en la nube {T11}

| Nombre | Hosting y servicios en la nube |
|---|---|
| Descripción | Alojamiento y servicios en la nube para clientes |
| Categoría | Servicio vendido |
| Usuario objetivo | Fábrica de Licores de Antioquia, Crediantioquia |
| Horario de prestación del servicio | 24 horas, 7 días a la semana |
| Canal de soporte | Mesa de servicio |
| Acuerdo de nivel de servicio | Por contrato |
| Hallazgos u oportunidades de mejora | Ninguno publicado. Acción: Plan de capacidad (P3.3) |

#### Fichas de los sistemas de información

Tabla: Sistema de información ERP (SICOF) {T47}

| Nombre aplicación | ERP (SICOF) |
|---|---|
| Descripción funcional | Contabilidad, presupuesto, tesorería y nómina. Acción: Ampliar a contratos, compras, facturación por proyecto y presupuesto público |
| Información que gestiona | Datos financieros y de nómina; activos. Acción: Se agrega información de contratos y ANS |
| Tipo de software | Software como servicio. Acción: Se mantiene el modelo SaaS |
| Estado | Productivo. Acción: Se reemplaza o amplía (P1.5) |
| Esquema de licenciamiento | Suscripción. Acción: Se evalúa en la selección |
| Fabricante | Proveedor externo (SICOF). Acción: Se define en la contratación |
| Integraciones con otros sistemas | Ninguna documentada. Acción: API con CRM, gestión de servicios y SGDEA (P3.1) |
| Debilidades o hallazgos estructurales | Solo cubre finanzas y nómina (S2). Acción: ERP integrado (P1.5) |

Tabla: Sistema de información OTRS y GLPI {T47}

| Nombre aplicación | OTRS y GLPI |
|---|---|
| Descripción funcional | Mesa de ayuda e inventario de TI. Acción: Se reemplaza por herramienta de gestión de servicios |
| Información que gestiona | Incidentes, requerimientos, activos de TI. Acción: Se agregan ANS por contrato y PQRSD |
| Tipo de software | Software libre en servidores propios. Acción: SaaS |
| Estado | Productivo. Acción: Retiro al terminar P2.3 |
| Esquema de licenciamiento | Libre (GPL) |
| Fabricante | Comunidades de software libre |
| Integraciones con otros sistemas | FusionInventory. Acción: API con ERP y sitio web (P3.1) |
| Debilidades o hallazgos estructurales | Sin prácticas de ITIL ni medición por contrato (S5). Acción: Herramienta nueva (P2.3) |

Tabla: Sistema de información Sitio web {T47}

| Nombre aplicación | Sitio web |
|---|---|
| Descripción funcional | Información, transparencia, PQRSD y pago en línea |
| Información que gestiona | Información pública y PQRSD |
| Tipo de software | Desarrollo propio en AWS |
| Estado | Productivo |
| Esquema de licenciamiento | No aplica |
| Fabricante | Valor+ |
| Integraciones con otros sistemas | Módulo de pago en línea (PETI 2026-2027 de Valor+, pág. 57); el proveedor de pagos no se publica. Acción: Formulario de PQRSD conectado a la herramienta de servicios (P2.3) |
| Debilidades o hallazgos estructurales | PQRSD sin conexión a la mesa de servicios. Acción: Integración de PQRSD (P2.3) |

Tabla: Sistema de información Intranet {T47}

| Nombre aplicación | Intranet |
|---|---|
| Descripción funcional | Comunicación interna |
| Información que gestiona | Noticias, documentos y enlaces internos |
| Tipo de software | En sitio. Acción: SharePoint Online |
| Estado | Productivo. Acción: Se migra (P2.4) |
| Esquema de licenciamiento | No aplica. Acción: Office 365 |
| Fabricante | Valor+. Acción: Microsoft |
| Integraciones con otros sistemas | Ninguna. Acción: Identidad única (P2.4) |
| Debilidades o hallazgos estructurales | En servidor propio. Acción: Migración (P2.4) |

Tabla: Sistema de información Telefonía IP (Asterisk, FreePBX, Estaqueue) {T47}

| Nombre aplicación | Telefonía IP (Asterisk, FreePBX, Estaqueue) |
|---|---|
| Descripción funcional | Central telefónica y contact center. Acción: Se mantiene la función |
| Información que gestiona | Llamadas, colas y estadísticas |
| Tipo de software | Software libre en sitio. Acción: Solución en la nube |
| Estado | Productivo. Acción: Se migra (P2.4) |
| Esquema de licenciamiento | Libre (GPL). Acción: Se define en la contratación |
| Fabricante | Comunidades de software libre. Acción: Se define en la contratación |
| Integraciones con otros sistemas | Ninguna documentada. Acción: Integración con la herramienta de servicios |
| Debilidades o hallazgos estructurales | Sin contingencia (pág. 81). Acción: Contingencia (P2.4) |

Tabla: Sistema de información Carriel {T47}

| Nombre aplicación | Carriel |
|---|---|
| Descripción funcional | Gestión documental. Acción: Se evalúa como SGDEA |
| Información que gestiona | Documentos y procedimientos de la entidad. Acción: Se agregan expedientes electrónicos |
| Tipo de software | Desarrollo propio |
| Estado | En implementación interna. Acción: Productivo como SGDEA si cumple MoReq (P2.5) |
| Esquema de licenciamiento | Propiedad intelectual registrada |
| Fabricante | Valor+. Acción: Valor+ |
| Integraciones con otros sistemas | Ninguna. Acción: API con el ERP (P3.1) |
| Debilidades o hallazgos estructurales | Sin evaluación frente a MoReq. Acción: Evaluación MoReq (P2.5) |

Tabla: Sistema de información Power BI {T47}

| Nombre aplicación | Power BI |
|---|---|
| Descripción funcional | Tableros e indicadores |
| Información que gestiona | Indicadores de gestión y proyectos. Acción: Se agrega el tablero del PEI y del PETI |
| Tipo de software | Software como servicio |
| Estado | Productivo |
| Esquema de licenciamiento | Suscripción Microsoft |
| Fabricante | Microsoft |
| Integraciones con otros sistemas | Ninguna automática. Acción: Conectores con ERP, CRM y gestión de servicios (P3.2) |
| Debilidades o hallazgos estructurales | Depende de consolidación manual (I5). Acción: Analítica integrada (P3.2) |

Tabla: Sistema de información SECOP, FURAG y Gestión Transparente {T47}

| Nombre aplicación | SECOP, FURAG y Gestión Transparente |
|---|---|
| Descripción funcional | Contratación pública, reporte del MIPG y rendición a la Contraloría |
| Información que gestiona | Procesos de contratación, avance del MIPG, ejecución de recursos |
| Tipo de software | Plataformas del Estado |
| Estado | Productivo |
| Esquema de licenciamiento | Libre para entidades públicas |
| Fabricante | Colombia Compra Eficiente, Función Pública, Contraloría |
| Integraciones con otros sistemas | Ninguna |
| Debilidades o hallazgos estructurales | Carga manual. Acción: Se mantienen por norma |
