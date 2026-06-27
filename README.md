# Análisis Global de Asesinatos de Periodistas, Impunidad Judicial y Responsabilidad Gubernamental (1993–2026)

Proyecto de análisis de datos basado en información pública de la UNESCO sobre periodistas asesinados a nivel mundial, el estado judicial de sus casos y la respuesta de los gobiernos a solicitudes oficiales de información.

---

## Descripción del Proyecto

La violencia contra periodistas representa una amenaza directa a la libertad de prensa y al acceso a información independiente. Sin embargo, en muchos países estos crímenes permanecen sin resolución judicial durante años o nunca llegan a ser esclarecidos.

Este proyecto tiene como objetivo analizar patrones globales relacionados con:

- asesinatos de periodistas a nivel mundial
- niveles de impunidad judicial por país y región
- impacto de las zonas de conflicto en la resolución de casos
- perfil de riesgo de las víctimas
- nivel de respuesta de los gobiernos ante solicitudes formales de UNESCO
- tendencias históricas y geográficas desde 1993

El proyecto fue desarrollado siguiendo un flujo completo de análisis de datos, desde limpieza y transformación hasta análisis estadístico, SQL y visualización en dashboard.

---

## Objetivos del Análisis

Identificar factores estructurales asociados a la violencia contra periodistas y responder preguntas relevantes desde una perspectiva analítica, judicial y geopolítica.

---

## Preguntas de Negocio

## 1. Perfil de las Víctimas y Factores de Riesgo

- ¿Qué tipo de medio de comunicación sufre más ataques violentos?

  - Prensa escrita
  - Televisión
  - Radio
  - Medios digitales
  - Plataformas mixtas

- ¿Cuál es la proporción de víctimas locales frente a periodistas extranjeros?

- ¿Existe diferencia de riesgo entre periodistas contratados (Staff) y colaboradores independientes (Freelance)?

- ¿Cómo ha evolucionado la distribución de género en los asesinatos a lo largo del tiempo?

---

## 2. Justicia e Impunidad Judicial

- ¿Qué porcentaje de casos han sido completamente resueltos por los sistemas judiciales nacionales?

- ¿Qué porcentaje de crímenes permanece sin resolución o en estado de impunidad?

- ¿Qué países presentan la mayor tasa de impunidad judicial?

- ¿Qué regiones del mundo presentan menor capacidad de resolución judicial?

- ¿Existe relación entre estar en una zona de conflicto y una menor probabilidad de resolución?

---

## 3. Responsabilidad Gubernamental

- ¿Qué gobiernos responden a las solicitudes formales realizadas por UNESCO?

- ¿Qué países presentan menor nivel de cooperación institucional?

- ¿Existe relación entre la respuesta gubernamental y una mayor tasa de resolución judicial?

- ¿Los países que responden oficialmente resuelven los casos con mayor rapidez?

---

## 4. Tendencias Temporales y Geográficas

- ¿El número anual de asesinatos está aumentando o disminuyendo globalmente?

- ¿Cuáles son los países con mayor acumulación histórica de casos?

- ¿Qué regiones representan actualmente los principales hotspots globales?

- ¿Existen patrones geográficos persistentes de violencia contra periodistas?

---

## Dataset Utilizado

Fuente oficial:

**UNESCO Observatory of Killed Journalists**

Fuente de datos pública:

[UNESCO](https://data.unesco.org/explore/dataset/fej001/table/?disjunctive.nationality&disjunctive.gender&disjunctive.local&disjunctive.media&disjunctive.country_title_en&disjunctive.staff&disjunctive.enquiry_status&disjunctive.date_resolution&sort=date&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQVZHIiwieUF4aXMiOiJpZCIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6InJhbmdlLWN1c3RvbSJ9XSwieEF4aXMiOiJkYXRlIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoieWVhciIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd24iOiJnZW5kZXIiLCJzdGFja2VkIjoibm9ybWFsIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJmZWowMDEiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLm5hdGlvbmFsaXR5Ijp0cnVlLCJkaXNqdW5jdGl2ZS5nZW5kZXIiOnRydWUsImRpc2p1bmN0aXZlLmxvY2FsIjp0cnVlLCJkaXNqdW5jdGl2ZS5tZWRpYSI6dHJ1ZSwiZGlzanVuY3RpdmUuY291bnRyeV90aXRsZV9lbiI6dHJ1ZSwiZGlzanVuY3RpdmUuc3RhZmYiOnRydWUsImRpc2p1bmN0aXZlLmVucXVpcnlfc3RhdHVzIjp0cnVlLCJkaXNqdW5jdGl2ZS5kYXRlX3Jlc29sdXRpb24iOnRydWUsInNvcnQiOiJkYXRlIn19fV0sImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9)

El dataset contiene información desde 1993 sobre:

- país del incidente
- fecha del asesinato
- nacionalidad
- género
- tipo de medio
- condición laboral
- zona de conflicto
- estado judicial del caso
- fecha de resolución
- solicitudes oficiales de UNESCO
- respuesta gubernamental
- información geográfica asociada

---

## Stack Tecnológico

Lenguajes y herramientas utilizadas:

- Python
- SQL
- Pandas
- NumPy
- Matplotlib
- Plotly
- Jupyter Notebook
- Power BI

Herramientas complementarias:

- Visual Studio Code → desarrollo y organización del proyecto
- Git → control de versiones
- GitHub Repository Hosting → documentación y portafolio
- Jupyter Notebook → análisis exploratorio y documentación técnica
- Microsoft Excel → validación rápida y revisión manual del dataset
- Microsoft Power BI → dashboard e indicadores ejecutivos

---

## Estructura del Proyecto

```text
journalist-impunity-analysis/

data/
 ├── raw/
 │    └── fej001.csv
 └── processed/
      ├── cleaned_unesco.csv
      └── sql_ready.csv

notebooks/
 ├── 01_data_cleaning.ipynb
 ├── 02_victim_risk_profile_analysis.ipynb
 ├── 03_judicial_impunity_analysis.ipynb
 ├── 04_government_accountability_analysis.ipynb
 └── 05_temporal_geographic_analysis.ipynb

src/
 ├── load_data.py
 ├── clean_data.py
 ├── feature_engineering.py
 ├── analysis.py

sql/
 ├── create_tables.sql
 ├── impunity_analysis.sql
 └── government_analysis.sql

dashboard/
 └── powerbi_dashboard.pbix

README.md
requirements.txt
main.py
```

---

## Pipeline Analítico

```text
Dataset Original CSV
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Análisis Exploratorio
        ↓
Análisis Estadístico
        ↓
Consultas SQL
        ↓
Dashboard en Power BI
        ↓
Insights y Conclusiones
```

---

## KPIs Principales

Indicadores principales analizados en el proyecto:

- Total de casos registrados
- Tasa global de resolución judicial
- Tasa global de impunidad
- Tiempo promedio hasta resolución judicial
- Tasa de respuesta gubernamental
- Proporción de periodistas locales vs extranjeros
- Distribución por medio de comunicación
- Tasa de resolución en zonas de conflicto
- Países con mayor índice de impunidad
- Tendencia anual de asesinatos

---

## Principales Técnicas Aplicadas

### Limpieza y Preparación

- manejo de valores nulos
- transformación de variables
- normalización de categorías
- feature engineering

### Python Analysis

- análisis exploratorio (EDA)
- groupby analysis
- crosstab analysis
- KPI calculation

### Statistical Analysis

- prueba Chi-Square
- análisis comparativo entre grupos
- análisis de tendencias temporales

### SQL Analysis

- agregaciones
- joins
- subqueries
- ranking de países

### Business Intelligence

Dashboard interactivo desarrollado en:

(proximamente)

---

## Insights Esperados

Al finalizar el proyecto se busca identificar:

- patrones globales de impunidad judicial
- regiones con mayores riesgos estructurales para periodistas
- impacto de conflictos armados en la justicia local
- sectores de medios más vulnerables
- nivel de cooperación institucional entre gobiernos y UNESCO
- evolución histórica de la violencia contra periodistas

---

## Objetivo Profesional del Proyecto

Proyecto desarrollado como parte de mi portafolio profesional orientado a posiciones relacionadas con:

- Data Analyst
- BI Analyst
- Analytics Engineer
- Business Intelligence Developer

Enfoque principal:

Transformar datos complejos en análisis accionables y visualizaciones orientadas a toma de decisiones.

---

## Autor

**Rolando Mateo Sotelo Mestanza** Data Analyst / Data Enginner Jr. | Data & Marketing Analyst 📍 Lima, Perú 

---
