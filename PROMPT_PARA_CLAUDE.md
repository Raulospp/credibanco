# Cómo usar este paquete

Este paquete trae la configuración de Claude Code (skills, agentes, reglas y scripts) con la que otro grupo construyó un PETI que el profesor aprobó. Trae también la norma del MinTIC (guía, Anexo 1, Anexo 2), los dos PETI de referencia del profesor, un esqueleto del PETI con los 16 numerales de la plantilla y un archivo con lo que el profesor pregunta en la sustentación. No trae nada de la empresa del otro grupo.

## Pasos para ti (humano)

1. Decide dónde vas a trabajar:
   - **Opción A (recomendada si tu PETI está en otra carpeta):** abre Claude Code en la carpeta de tu proyecto y pega el prompt de abajo. Claude copiará lo necesario desde esta carpeta.
   - **Opción B:** usa esta misma carpeta como proyecto: copia aquí tu PETI actual y tus insumos, abre Claude Code aquí y pega el prompt.
2. Ten a mano: el nombre de la empresa, si es pública o privada, el alcance, el periodo del plan, y **las observaciones que te hizo el profesor** (cópialas en un archivo o pégalas cuando Claude te las pida).
3. Si tienes entrevistas o documentos internos de la empresa, ponlos en `docs/privado/` (esa carpeta no se sube a Git).
4. Después de que Claude termine la importación, **cierra y vuelve a abrir Claude Code** en la carpeta del proyecto para que cargue las skills y los agentes nuevos.
5. Pega el prompt de abajo, completando la ruta de la primera línea.

---

## Prompt (copiar desde aquí)

```text
Voy a trabajar mi PETI con una configuración de Claude Code que me pasó otro grupo (a ellos el profesor les aprobó el PETI). La configuración está en: <RUTA DE LA CARPETA Peti_raul>

Quiero que mi proyecto quede trabajando exactamente como el de ellos, pero para MI empresa. Haz lo siguiente, en orden, y no te saltes pasos:

1. LEE PRIMERO, SIN MODIFICAR NADA:
   - <RUTA>/.claude/CLAUDE.md (contexto y reglas del proyecto)
   - todas las skills en <RUTA>/.claude/skills/*/SKILL.md y sus archivos de apoyo
   - los agentes en <RUTA>/.claude/agents/
   - <RUTA>/.claude/rules/docs-peti.md y <RUTA>/.claude/settings.json
   - <RUTA>/docs/lecciones-profesor.md y <RUTA>/docs/peti_2026_2028.md (esqueleto)
   Luego revisa mi proyecto actual: qué archivos tengo, dónde está mi PETI (Markdown, Word o PDF), qué insumos tengo y si es un repositorio Git.

2. IMPORTA LA CONFIGURACIÓN a la raíz de mi proyecto (si mi proyecto ES la carpeta de la ruta, omite la copia):
   - Copia .claude/ completo, .gitignore (si ya tengo uno, fusiónalo), docs/lecciones-profesor.md, docs/registro-de-evidencias.md, docs/peti_2026_2028.md (esqueleto), scripts/generar_informe_uso_ia.py y README.md.
   - Copia a docs/ los archivos de la norma y los referentes SIN renombrarlos (los scripts los buscan por nombre): "MGGTI.GE.ES.01 - Guia de construccion PETI - Gobierno Digital-v. 3.0.pdf", "Anexo 1. Herramientas_para_la_construccion_del_PETI.xlsx", "Anexo 2. Plantilla PETI.docx", "Plan-Estratégico-de-Tecnologías-de-la-Información_2025-V02.pdf" y "articles-274095_recurso_1.pdf".
   - Crea docs/insumos/ y docs/privado/. Si tengo resúmenes o investigación sobre la empresa, muévelos a docs/insumos/. Si tengo entrevistas, documentos internos o datos de personas, muévelos a docs/privado/.
   - NO borres ni sobrescribas nada mío sin preguntarme. Si un archivo ya existe, dime y propón cómo fusionarlo.

3. PREGÚNTAME los datos del proyecto (usa preguntas concretas, todas de una vez) y completa la tabla "Datos del proyecto" de .claude/CLAUDE.md: organización, naturaleza (entidad pública colombiana o empresa privada: esto cambia qué partes de la guía aplican tal cual y cuáles se adaptan), sector, sedes o países, alcance, qué TI planea el PETI y qué queda fuera, horizonte, cómo firma el documento, instancia que aprueba, y qué evidencia restringida tengo. Completa también la sección "Hechos del contexto" y la fecha de hoy. Reemplaza los [COMPLETAR] del README con lo que ya se sepa.

4. VERIFICA EL ENTORNO: versión de Python; si falta python-docx, instálalo con pip; comprueba si hay pdftotext y, si no, instala pypdf. Ejecuta:
   python .claude/skills/guia-peti/scripts/extraer_referencias.py <una carpeta temporal>
   y confirma que genera guia.txt, plantilla.txt, anexo1.txt, minciencias.txt y mintic.txt. Si algo falla, arréglalo y anota en la sección "Herramientas locales" de CLAUDE.md lo que sea particular de mi equipo.

5. PIDE LAS OBSERVACIONES DEL PROFESOR sobre mi PETI actual y guárdalas en docs/observaciones-profesor.md (una fila por observación: observación, numeral afectado, estado). Son prioridad en todo lo que sigue.

6. MIGRA MI PETI AL ESQUELETO: carga las skills guia-peti y redaccion-peti. Pasa el contenido de mi PETI actual a docs/peti_2026_2028.md respetando los 16 numerales y las columnas de las tablas (son las que exige el Anexo 1). Reglas:
   - No inventes datos. Lo que mi PETI dice sin fuente se queda con la marca [EVIDENCIA: qué falta]; lo que falta del todo se queda como [COMPLETAR].
   - Todo lo de situación objetivo y portafolio va como PROPUESTO.
   - Registra en docs/registro-de-evidencias.md cada fuente que mi PETI ya cite y que puedas verificar abriéndola (skill evidencias-peti). Mis análisis propios (DOFA, costos, objetivos que formulamos nosotros) van como INT-001.
   - Mantén mi versión original sin tocar (renómbrala con sufijo _original si hace falta) y registra la migración en el §16 control de cambios.

7. AUDITA: ejecuta el script de trazabilidad (python .claude/skills/trazabilidad-peti/scripts/verificar_trazabilidad.py) y luego el comando /auditar-peti (si no aparece aún, lanza en paralelo los agentes auditor-conformidad, auditor-evidencias y verificador-fuentes y consolida como indica .claude/skills/auditar-peti/SKILL.md). Cruza el resultado con docs/observaciones-profesor.md y docs/lecciones-profesor.md.

8. ENTRÉGAME un resumen corto con: qué se importó, qué datos quedaron por completar, los hallazgos más graves de la auditoría, y un plan de corrección por paquetes (en orden: primero lo que pidió el profesor, luego lo que la guía exige y falta, luego trazabilidad, luego evidencia, luego forma). NO empieces a corregir hasta que yo lo apruebe.

Reglas durante todo el trabajo:
- Escribe en español, en el registro de un plan institucional (skill redaccion-peti).
- Nada de docs/privado/ se copia a archivos versionados, commits ni respuestas que vayan a un archivo.
- No hagas git push. Para commits usa /commit.
- Si algo de la configuración asume una empresa privada y la mía es pública (o al revés), ajusta la configuración y dime qué cambiaste.
```

---

## Después de la importación: cómo se trabaja

| Quiero… | Le digo a Claude |
|---|---|
| Saber qué exige la norma en un numeral | "¿Qué exige la guía para el §6.2?" (usa `guia-peti`) |
| Escribir o mejorar un numeral | "Redacta el §8.1 a partir del §6 y §7" (usa `redaccion-peti` + `trazabilidad-peti`) |
| Respaldar un dato | "Busca la fuente de que la empresa tiene X empleados y regístrala" (usa `evidencias-peti`) |
| Revisar que todo cuadre | "Corre la trazabilidad" |
| Revisar antes de entregar | `/auditar-peti` |
| Generar el Word | "Genera el Word de la versión actual" |
| Preparar la sustentación | "Arma docs/preparacion-sustentacion.md como dice la sección 5 de lecciones-profesor.md" |
| Guardar cambios | `/commit` |

Orden recomendado si hay que rehacer contenido: §2 alcance → §5 contexto → §6 situación actual + DOFA → §7 situación objetivo con metas → §8 brechas → §9 portafolio → §10 indicadores → §11 riesgos → §12-§13 → §4, §1, §3, §14-§15 → auditoría.
