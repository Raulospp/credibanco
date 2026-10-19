---
name: trazabilidad-peti
description: Usar cuando se crea, modifica o elimina una brecha, oportunidad, proyecto, indicador, riesgo u objetivo de TI en el PETI; cuando hay que comprobar que cada brecha tiene proyecto, cada proyecto tiene indicador y cada objetivo tiene metas; cuando se construye la matriz de trazabilidad o las fichas del portafolio; cuando se compara el PETI con los IDs y columnas del Anexo 1; o cuando el usuario sospecha que las cifras del README o de un numeral no cuadran.
argument-hint: "[ID o numeral]"
---

# Trazabilidad interna del PETI

## Principio

Un PETI se sostiene por una cadena que se puede recorrer en los dos sentidos:

```
motivador / hallazgo AS-IS (con evidencia)
        → objetivo estratégico de TI (con metas por año y línea base)
        → brecha (elemento, acción, dominio, tiempo, costo)
        → iniciativa o proyecto (fase, responsable, costo, entregable)
        → indicador (fórmula, línea base, meta, fuente, responsable)
        ↔ riesgo (qué lo materializa, qué proyecto o control lo trata)
```

Un eslabón suelto es un defecto: una brecha sin proyecto no se cierra, un proyecto sin brecha no se justifica, un proyecto sin indicador no se puede seguir y un objetivo sin meta no es un objetivo (guía, Actividades 8, 11, 13 y 14). El profesor pide recorrer esta cadena en voz alta con un ejemplo (ver `docs/lecciones-profesor.md`).

## Comprobación automática

```
python .claude/skills/trazabilidad-peti/scripts/verificar_trazabilidad.py
```

Por defecto lee `docs/peti_2026_2028.md`, `docs/registro-de-evidencias.md` y `README.md`. Imprime conteos, hallazgos `T-nn` por severidad, la matriz brecha → proyectos y las brechas por dominio. Comprueba: brechas y oportunidades sin proyecto; proyectos sin origen; IDs citados sin definir (incluida la evidencia contra el registro); viñetas de la situación actual sin ID; indicadores y riesgos sin vínculo; columnas del Anexo 1 que faltan en brechas, portafolio e indicadores; cifras del README. Ejecútalo antes y después de tocar cualquiera de esos numerales y reporta la diferencia.

El script encuentra los numerales por su título ("Situación actual", "Brechas y oportunidades", "Hoja de ruta y portafolio", "Indicadores", "Riesgos"): si cambias esos títulos, deja de verlos. No juzga calidad (si la brecha está bien justificada o la meta es realista); eso lo hacen el agente `auditor-conformidad` y la lectura.

## IDs: los del PETI y los del Anexo 1

| Elemento | PETI | Anexo 1 | Regla |
|---|---|---|---|
| Objetivo corporativo o institucional | `OC01…` | ID de objetivos institucionales (Act. 4A) | Si la organización los publica, se citan con `PUB-`; si los formula el equipo, con `INT-` |
| Objetivo estratégico de TI | `OETI01…` | `OETI01…` | Iguales |
| Meta de TI | `METI01…` | `METI01…` | Con línea base y años 1-2 (o 1-3 según el horizonte) (Act. 8) |
| Brecha | `BRE-001…` | `B001…` | Mantener `BRE-`; equivalencia en el Anexo A del PETI |
| Oportunidad | `OPT-001…` | — | Mantener |
| Proyecto | `P<fase>.<n>` | `IT001…` | Mantener `P1.1`; equivalencia en el Anexo A |
| Indicador | `KPI-01…` | `IND.ES.01…` | Mantener `KPI-`; la hoja de vida puede llevar ambos |
| Riesgo | `R01…` | — | Mantener |
| Evidencia | `PUB-/INT-/PRV-` (registro) | — | Ver `evidencias-peti` |

**No se renumera.** Si un elemento se elimina, su ID no se reutiliza; se deja constancia en el control de cambios. Un ID nuevo toma el siguiente número libre.

## Al crear o cambiar un elemento

| Si cambias… | Revisa también |
|---|---|
| Una brecha | Hallazgo de §6 que la origina (debe existir una fila en el diagnóstico); fila del TO-BE en §7; proyecto en §9; dominio; mapa de ruta; README |
| Un proyecto | Brecha u oportunidad; fase y meses en el mapa de ruta; indicador en §10; riesgo en §11; responsable (rol propuesto); costo |
| Un indicador | Proyecto u objetivo que mide; hoja de vida completa (fórmula, línea base, fuente de datos, responsable, frecuencia, meta, rangos, tipo) |
| Un riesgo | Proyecto o control que lo trata; propietario; riesgo residual |
| Un objetivo de TI | Objetivo corporativo que apoya (columna explícita); metas por año; proyectos que contribuyen |
| Una fecha o una fase | Mapa de ruta visual; dependencias (lo que requiere que otro termine antes); hitos externos (vencimientos de certificaciones, leyes que entran en vigencia) |
| Una meta del año 1 | Que los proyectos que la producen terminen antes del mes 12 |

## Contrato de salida

1. **Salida del script** (o su resumen) antes y después del cambio.
2. **Matriz de trazabilidad** del alcance pedido: objetivo → brecha → proyecto → indicador → riesgo, con "—" donde falte el eslabón.
3. **Cambios propuestos** para cerrar cada eslabón suelto, con el ID afectado y el numeral.

## Señales de alerta

- Un proyecto que atiende una brecha pero termina después de la fecha en que la brecha produce su daño (por ejemplo, renovar un certificado después de su vencimiento).
- Una meta del año 1 que depende de proyectos que empiezan en el año 2.
- Indicadores que no miden ningún proyecto y proyectos que no mide ningún indicador.
- Dominios del MRAE sin ninguna brecha: o el diagnóstico no encontró nada (decirlo) o falta análisis.
- Referencias cruzadas a numerales equivocados ("ver §11" cuando el contenido está en §12).
- Cifras del README distintas de las del PETI.
