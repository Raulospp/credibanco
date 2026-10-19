# Estilo natural: que el PETI suene escrito por un equipo de TI y no por un generador de texto

Estas reglas complementan las de `SKILL.md`. No buscan engañar a un detector; son criterios de buena escritura que evitan la prosa uniforme, genérica o de folleto. La regla de fondo es que **la forma sigue al contenido**, nunca a una receta.

Quien firma es un equipo de estudiantes que actúa como el área de TI de la organización. El texto tiene que sonar a alguien que conoce la operación y la explica con precisión, no a una página de marketing ni a un ensayo.

## 1. Tablas para datos, prosa para razonar

- Lo que se compara, se enumera o se mide va en tabla (brechas, proyectos, indicadores, riesgos, comunicaciones).
- Lo que explica por qué, qué implica o cómo se decide va en prosa. Un numeral hecho solo de viñetas en negrita no explica nada.
- No repitas en prosa lo que la tabla ya dice. Un párrafo antes de la tabla basta para decir qué muestra y qué conclusión sacar.

## 2. Variar párrafos y oraciones

- La longitud la decide la idea. Un párrafo de contexto puede tener cinco o seis oraciones; uno que presenta una tabla, una o dos.
- Alterna funciones: hecho, consecuencia, comparación, decisión.
- La oración corta sirve para la conclusión: "La adopción no es uniforme entre áreas." La larga, para la cadena causal que la explica.
- Señal de alerta: tres párrafos seguidos con la misma forma (tema, desarrollo, cierre con conector) y casi la misma longitud.

## 3. Patrones típicos de texto generado que se eliminan

| Patrón | Ejemplo | Corrección |
|---|---|---|
| Tríadas por costumbre | "gobernanza, ciberseguridad y excelencia" | Deja los elementos que de verdad aplican, sean uno, dos o cuatro. |
| "No solo… sino también…" | "no solo mejora la seguridad sino también la eficiencia" | Di las dos cosas o la que importa. |
| Negrita en cada frase | "**Liderazgo digital**: **Consolidar**…" | Negrita solo para el término que se define o el ID que se busca. |
| Viñeta con título y dos puntos en todo | "**Adopción**: …", "**Gobierno**: …" | Tabla o prosa. |
| Cierre que repite lo dicho | "En conclusión, el PETI permitirá…" | Se borra. |
| Abstracciones apiladas | "habilitar capacidades para potenciar la transformación" | Nombra la capacidad y el cambio concreto. |
| Rayas (—) para todo inciso | | Comas o paréntesis; raya solo para un inciso que de verdad lo pida. |
| Semáforos y emojis | 🔴 ✅ ⚠️ | Texto. |

## 4. Conectores solo cuando hay relación lógica

- Evita la cadena "Además", "Asimismo", "Por otra parte", "En este sentido", "Cabe destacar que", "Es importante señalar que", "De esta manera", "En consecuencia" al inicio de párrafo tras párrafo.
- Si el conector solo rellena, se elimina o se integra: "Asimismo, es importante destacar que el comité revisará…" → "El comité también revisará…".
- Ningún párrafo empieza con conector solo por costumbre; dos seguidos, nunca.

## 5. Voz impersonal e institucional

- No escribir "nosotros", "nuestro equipo", "los autores", "el equipo del PETI". El sujeto es la organización, el PETI, el comité, el proyecto, o la forma impersonal: "se propone", "se observó", "se prioriza".
- Varía el sujeto: "el plan", "la organización", "el área de TI", la instancia de gobierno del PETI. No repitas siempre la misma fórmula.
- El PETI no se elogia a sí mismo ("este ambicioso plan", "una hoja de ruta sólida").

## 6. Vocabulario: preciso, no rebuscado ni de consultoría

Se conservan los términos técnicos necesarios: gobierno de TI, arquitectura empresarial, brecha, línea base, ANS, catálogo de servicios, matriz RACI, IaC, CI/CD, SAST, DAST, SCA, RAG, observabilidad, atestación, SGSI, AIMS.

| Evitar | Preferir |
|---|---|
| apalancar, potenciar, impulsar (repetido) | apoyar, aumentar, permitir, o el verbo concreto |
| habilitar (repetido) | permitir, dar acceso a, preparar |
| robusto, integral, holístico | nombra la propiedad: redundante, cubre los 7 dominios, considera X y Y |
| sinergia, ecosistema (repetido) | relación, conjunto de herramientas, socios |
| de vanguardia, de punta, disruptivo | reciente, nuevo, o nada |
| maximizar el valor, generar valor (vacío) | el efecto medible: reducir el MTTR, evitar retrabajos |
| robustecer, fortalecer (repetido) | mejorar, ampliar, formalizar, documentar |
| llevar a cabo, realizar | hacer, ejecutar, aplicar |
| constituir, fungir como | ser, servir de |
| en aras de, con miras a | para |
| dicho(s), dicha(s) | este, ese, el |
| a nivel de | en, sobre, para |
| implementar (para todo) | desplegar, poner en marcha, adoptar, construir |
| eventualmente (por "finalmente") | finalmente, con el tiempo |
| asumir (por "suponer") | suponer |
| soportar (por "respaldar") | respaldar, dar soporte técnico a |

- Criterio: si un líder técnico no usaría la palabra al explicarle el plan al CTO en una reunión, se cambia por la común que diga lo mismo.
- Anglicismos de oficina ("deliverable", "roadmap", "stakeholder", "compliance", "baseline") se escriben en español: entregable, hoja de ruta, parte interesada, cumplimiento, línea base. Se aceptan los nombres propios de marcos y productos y las siglas técnicas estándar.

## Cómo recortar

- Primero lo que no aporta: conectores de relleno, adjetivos de folleto, frases que repiten una tabla o otro numeral.
- No se recortan IDs de evidencia, marcadores, fórmulas, metas ni las advertencias de alcance ("observado en la cuenta analizada", "propuesto").
- Después de recortar, relee: si quedó monótono, varía la longitud sin volver a alargar.

## Lista de revisión rápida

- [ ] Sin "nosotros", "los autores" ni autoelogios del plan.
- [ ] Sin adjetivos de folleto ni superlativos sin fuente.
- [ ] Ningún hecho sin ID; ninguna propuesta escrita como hecho.
- [ ] No hay tres párrafos o viñetas seguidas con la misma forma y longitud; no hay tríadas por costumbre.
- [ ] No hay dos párrafos seguidos que empiecen con conector.
- [ ] Ninguna palabra de la tabla "Evitar" sin razón técnica.
- [ ] Sin emojis ni semáforos; fechas sin ambigüedad; "85 %" con espacio.
- [ ] La voz de cada numeral coincide con su función (tabla de voces de `SKILL.md`).
