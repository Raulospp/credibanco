---
name: auditar-peti
description: Auditoría completa del PETI - ejecuta el script de trazabilidad, lanza en paralelo los agentes auditor-conformidad, auditor-evidencias y verificador-fuentes, y consolida sus hallazgos en un informe priorizado con plan de corrección. Usar cuando el usuario pide auditar, revisar a fondo o evaluar el PETI antes de una entrega.
disable-model-invocation: true
argument-hint: "[numerales opcionales, p. ej. 6-8] [--sin-web]"
---

# Auditoría del PETI

## Principio

La auditoría informa; no corrige. Produce un único informe con hallazgos verificables, sin duplicados y ordenados por lo que más le cuesta al PETI si no se arregla. Las correcciones se hacen después, con el usuario, usando `redaccion-peti`, `evidencias-peti` y `trazabilidad-peti`.

## Procedimiento

1. **Línea base**: `git status --short` (anota si el PETI tiene cambios sin confirmar) y la versión del encabezado de `docs/peti_2026_2028.md`.
2. **Trazabilidad**: ejecuta `python .claude/skills/trazabilidad-peti/scripts/verificar_trazabilidad.py` y guarda la salida para el informe.
3. **Agentes en paralelo** (un solo mensaje con tres llamadas a `Agent`), pasando a cada uno el alcance (`$ARGUMENTS` o el documento completo) y la versión:
   - `auditor-conformidad`: guía, plantilla, Anexo 1, marcos, forma.
   - `auditor-evidencias`: evidencia, clasificación, reidentificación, higiene de Git.
   - `verificador-fuentes`: afirmaciones públicas y marcos `[VERIFICAR]`. Omítelo si el usuario pasó `--sin-web`.
4. **Consolidar**:
   - Une los hallazgos que describen el mismo problema desde dos ángulos (por ejemplo, AE y AC sobre la misma meta sin línea base) y conserva la referencia a ambos IDs de origen.
   - Descarta lo que no tenga cita del PETI o fuente de la norma.
   - Comprueba tú mismo, abriendo el PETI, los hallazgos de severidad crítica o alta antes de incluirlos. Si un agente se equivocó, retíralo y dilo en una línea.
   - Cruza el resultado con `docs/lecciones-profesor.md`: si un punto débil conocido sigue abierto, súbelo de severidad.
5. **Priorizar** en este orden: (1) fugas de información restringida; (2) hechos falsos o contradichos; (3) requisitos de la guía ausentes; (4) trazabilidad rota; (5) evidencia débil; (6) forma.
6. **Plan de corrección**: agrupa los hallazgos en paquetes de trabajo que se puedan hacer en un cambio cada uno (por ejemplo, "Hoja de vida de los indicadores", "Costos y tiempos de brechas y proyectos", "Numeral de metodología"), con numerales afectados y skill a usar.

## Informe

Escríbelo en `docs/auditoria/auditoria-peti-v<versión>-<AAAA-MM-DD>.md` **solo después** de comprobar que no contiene material restringido (revisión de reidentificación de `evidencias-peti`). Si la auditoría necesitó detalles restringidos para explicarse, esa parte va a `docs/privado/` (ignorado por Git) y el informe versionado solo la referencia.

Estructura:

1. Resumen: versión auditada, fecha, alcance, hallazgos por severidad, veredicto en una oración (lista para entregar / requiere correcciones / requiere rehacer numerales).
2. Tabla consolidada: ID `AUD-01…`, severidad, numeral, hallazgo, origen (`AC-`, `AE-`, `VF-`, `T-`), corrección.
3. Plan de corrección por paquetes, en orden.
4. Anexos: salida del script de trazabilidad; tablas de conformidad por capítulo y por actividad; tabla de verificación de fuentes; filas propuestas para el registro.

Al terminar, muestra al usuario el resumen, los cinco hallazgos más graves y el primer paquete de corrección. No empieces a corregir sin que lo pida.
