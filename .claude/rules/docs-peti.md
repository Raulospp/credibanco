---
paths:
  - "docs/**"
  - "README.md"
---

# Reglas para docs/ y README.md

- **Solo lectura**: la guía (`MGGTI…pdf`), `Anexo 1…xlsx`, `Anexo 2…docx` y los dos PETI de referencia (`Plan-Estratégico…pdf`, `articles-274095…pdf`). No se editan, renombran ni convierten en el mismo sitio.
- **Restringidos**: `docs/privado/` y `docs/evidencia-privada/`. Se leen para entender el AS-IS; no se copian a ningún archivo versionado, ni se listan ni enlazan desde el README o el PETI. Borradores que necesiten ese detalle van a `docs/privado/`.
- **Insumos `docs/insumos/*.md`**: resúmenes de investigación. Si traen citas `[n]` sin bibliografía o salieron de un chat con IA, no se usan como fuente de un hecho del PETI; se usan para saber qué buscar (skill `evidencias-peti`).
- **PETI** (`docs/peti_2026_2028.md`):
  - Antes de escribir un numeral, carga `guia-peti` y `redaccion-peti`.
  - Todo hecho nuevo tiene fila en `docs/registro-de-evidencias.md` y en el PETI se cita por su nombre de cita (sección "Nombres de cita en el PETI"); si no hay fuente, `[EVIDENCIA: …]`. No se usa el signo §: se escribe "numeral 7.1.6".
  - Todo cambio de contenido actualiza el control de cambios (§16) y la versión del encabezado. Cambios de formato puro (tildes, una tabla mal alineada) no suben versión, pero se agrupan en una entrada al cerrar la sesión.
  - Tras tocar §6 a §11, ejecuta el script de `trazabilidad-peti`.
  - No renumeres IDs ni cambies títulos de numerales sin pedirlo: el script y el índice se guían por los títulos.
- **Registro de evidencias**: una fila por fuente abierta. No se borran filas; si una fuente deja de ser válida, se marca en "Alcance / limitación" y se registra la sustituta.
- **README**: si cambian las cifras del PETI (brechas, proyectos, fases) o la lista de documentos clave, se actualiza en el mismo cambio. No lista archivos restringidos.
- **Auditorías**: los informes van a `docs/auditoria/` solo tras la revisión de reidentificación.
