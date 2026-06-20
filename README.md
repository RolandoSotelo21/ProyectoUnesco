# Análisis Global sobre Seguridad de Periodistas e Impunidad Judicial  
### Proyecto End-to-End de Análisis de Datos utilizando datos abiertos de UNESCO

---

## Descripción del Proyecto

Este proyecto analiza casos de asesinatos de periodistas reportados por la UNESCO entre los años **1993 y 2026**, con el objetivo de identificar patrones globales relacionados con:

- Seguridad de periodistas a nivel mundial  
- Tasas de impunidad judicial  
- Impacto de las zonas de conflicto armado  
- Sectores de medios con mayor nivel de riesgo  
- Respuesta de gobiernos ante solicitudes judiciales  
- Tendencias geográficas y temporales  

El proyecto fue desarrollado simulando un caso real de negocio, cubriendo el flujo completo de análisis de datos: desde limpieza y transformación hasta generación de insights y visualización ejecutiva.

---

## Problema de Negocio

El ejercicio del periodismo representa un alto nivel de riesgo en diversas regiones del mundo, especialmente en países con conflictos armados, inestabilidad política o sistemas judiciales débiles.

Uno de los principales problemas identificados es la **impunidad**, es decir, la cantidad de casos donde no existe una resolución judicial efectiva.

Este proyecto busca responder preguntas como:

- ¿Qué países presentan mayor cantidad de asesinatos de periodistas?
- ¿Qué porcentaje de casos permanece sin resolver?
- ¿Existe relación entre trabajar en zonas de conflicto y la probabilidad de resolución judicial?
- ¿Qué tipo de medio presenta mayor exposición al riesgo?
- ¿Cuánto tiempo tarda, en promedio, una resolución judicial?

---

## Fuente de Datos

Fuente oficial:

https://data.unesco.org/explore/dataset/fej001/information/?disjunctive.nationality&disjunctive.gender&disjunctive.local&disjunctive.media&disjunctive.country_title_en&disjunctive.staff&disjunctive.enquiry_status&disjunctive.date_resolution&sort=date&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQVZHIiwieUF4aXMiOiJpZCIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6InJhbmdlLWN1c3RvbSJ9XSwieEF4aXMiOiJkYXRlIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoieWVhciIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd24iOiJnZW5kZXIiLCJzdGFja2VkIjoibm9ybWFsIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJmZWowMDEiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLm5hdGlvbmFsaXR5Ijp0cnVlLCJkaXNqdW5jdGl2ZS5nZW5kZXIiOnRydWUsImRpc2p1bmN0aXZlLmxvY2FsIjp0cnVlLCJkaXNqdW5jdGl2ZS5tZWRpYSI6dHJ1ZSwiZGlzanVuY3RpdmUuY291bnRyeV90aXRsZV9lbiI6dHJ1ZSwiZGlzanVuY3RpdmUuc3RhZmYiOnRydWUsImRpc2p1bmN0aXZlLmVucXVpcnlfc3RhdHVzIjp0cnVlLCJkaXNqdW5jdGl2ZS5kYXRlX3Jlc29sdXRpb24iOnRydWUsInNvcnQiOiJkYXRlIn19fV0sImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9

El dataset contiene registros históricos sobre asesinatos de periodistas y seguimiento judicial realizado por UNESCO.

### Características del Dataset

| Métrica | Valor |
|----------|-------|
| Registros | 1864 |
| Columnas | 41 |
| Cobertura | Global |
| Periodo | 1993 - 2026 |
| Países | +100 |

---

## Objetivo del Proyecto

Desarrollar un análisis exploratorio y estadístico que permita identificar factores asociados a la impunidad judicial en asesinatos de periodistas a nivel global.

Objetivos específicos:

- Identificar tendencias históricas de asesinatos  
- Detectar países con mayores niveles de riesgo  
- Calcular tasas globales de impunidad  
- Evaluar impacto de zonas de conflicto  
- Construir KPIs para monitoreo ejecutivo  
- Generar dashboard interactivo para análisis visual  

---

## Arquitectura del Proyecto

```text
Archivo CSV (UNESCO)
          ↓
Limpieza de Datos (Python)
          ↓
Transformación y Feature Engineering
          ↓
Análisis Exploratorio (EDA)
          ↓
Análisis Estadístico
          ↓
Consultas SQL
          ↓
Dashboard en Power BI
          ↓
Obtención de Insights
```

---

## Herramientas Utilizadas

### Lenguaje Principal

- SQL

### Librerías

- Pandas 
- NumPy  
- Matplotlib  
- Plotly  
- SciPy
- SQLAlchemy
- Jupyter environment

### Bases de Datos

- PostgreSQL

### Business Intelligence

- Power BI  

### Desarrollo

- Jupyter Notebook  
- Visual Studio Code  
- Git  
- GitHub  

---

## Proceso de Limpieza de Datos

El dataset original requirió un proceso de preprocesamiento antes del análisis.

Actividades realizadas:

- Eliminación de columnas irrelevantes o metadata  
- Conversión de variables tipo fecha  
- Conversión de edad a variable numérica  
- Eliminación de registros duplicados  
- Tratamiento de valores nulos  
- Estandarización de variables categóricas  
- Exportación del dataset limpio para análisis posterior  

---

## Ingeniería de Variables (Feature Engineering)

Se crearon variables adicionales para enriquecer el análisis.

| Variable | Descripción |
|-----------|-------------|
| year | Año extraído de la fecha del incidente |
| month | Mes del incidente |
| decade | Década del incidente |
| resolved | Variable binaria (1 = caso resuelto) |
| impunity | Variable binaria (1 = caso no resuelto) |
| resolution_days | Días transcurridos hasta resolución |

---

## Análisis Exploratorio de Datos (EDA)

Se analizaron múltiples dimensiones del dataset.

### Análisis Temporal

Preguntas analizadas:

- ¿Cómo evolucionaron los casos a lo largo del tiempo?
- ¿Qué años registraron más incidentes?

Visualización:

- Series temporales por año

---

### Análisis Geográfico

Preguntas analizadas:

- ¿Qué países concentran mayor cantidad de casos?
- ¿Qué regiones presentan mayor nivel de riesgo?

Visualización:

- Ranking por países  
- Mapa global interactivo  

---

### Perfil Demográfico

Preguntas analizadas:

- Distribución por género  
- Distribución por edad  

Visualización:

- Pie chart  
- Histograma  

---

### Análisis por Tipo de Medio

Categorías analizadas:

- Televisión  
- Radio  
- Medios impresos  
- Medios digitales  

Pregunta:

- ¿Qué tipo de medio presenta mayor vulnerabilidad?

Visualización:

- Gráfico de barras  

---

## Análisis Estadístico

Se realizó una prueba estadística para evaluar si trabajar en zonas de conflicto afecta la probabilidad de resolución judicial.

### Hipótesis planteada

**H0:** Las zonas de conflicto no afectan la probabilidad de resolución judicial  

**H1:** Las zonas de conflicto afectan significativamente la probabilidad de resolución judicial

Método aplicado:

- Prueba Chi-Cuadrado

Implementado utilizando:

- SciPy

---

## KPIs Analizados

Se construyeron indicadores clave para monitoreo ejecutivo.

| KPI | Descripción |
|-------|-------------|
| Total de Casos | Número total de asesinatos registrados |
| Países Afectados | Cantidad de países con registros |
| Tasa de Resolución | Porcentaje de casos resueltos |
| Tasa de Impunidad | Porcentaje de casos sin resolver |
| Tiempo Promedio de Resolución | Días promedio hasta cierre judicial |
| Casos en Zona de Conflicto | Porcentaje de casos ocurridos en conflicto |

---

## Hallazgos Principales

### 1. Alta tasa de impunidad global

Una gran proporción de casos registrados permanece sin resolución judicial.

---

### 2. Concentración geográfica

Un número reducido de países concentra la mayoría de casos reportados.

---

### 3. Impacto de zonas de conflicto

Los casos ocurridos en zonas de conflicto presentan menor probabilidad de resolución.

---

### 4. Diferencias según tipo de medio

Existen sectores de medios con mayor nivel de exposición al riesgo.

---

### 5. Procesos judiciales extensos

Los casos resueltos suelen requerir largos periodos antes de alcanzar una resolución definitiva.

---

## Análisis SQL

Se realizaron consultas analíticas para explorar patrones del dataset.

Ejemplo:

### Países con mayor cantidad de casos

```sql
SELECT
    country,
    COUNT(*) total_cases
FROM journalist_cases
GROUP BY country
ORDER BY total_cases DESC;
```

### Tasa de impunidad por país

```sql
SELECT
    country,
    COUNT(*) total_cases,
    AVG(impunity)*100 impunity_rate
FROM journalist_cases
GROUP BY country;
```

---

## Dashboard

Dashboard interactivo desarrollado en:

**Power BI**

Secciones principales:

### Resumen Ejecutivo

- Total de casos  
- Tasa de resolución  
- Tasa de impunidad  
- Países afectados  

### Análisis Geográfico

- Mapa global  
- Filtros por país y región  

### Análisis Judicial

- Casos resueltos vs no resueltos  
- Tiempo promedio de resolución  

### Análisis de Riesgo

- Zonas de conflicto  
- Género  
- Tipo de medio  
- Distribución por edad  

---

## Estructura del Proyecto

```text
journalist-safety-analysis/

data/
 ├── raw/
 └── processed/

notebooks/
 ├── 01_data_cleaning.ipynb
 ├── 02_eda.ipynb
 └── 03_statistical_analysis.ipynb

src/
 ├── clean_data.py
 ├── analysis.py
 ├── feature_engineering.py

sql/
 ├── create_tables.sql
 └── analysis_queries.sql

dashboard/

README.md
requirements.txt
```

---

## Habilidades Demostradas

Este proyecto demuestra competencias aplicadas a roles de analítica de datos.

- Limpieza y transformación de datos  
- SQL Analytics  
- Exploratory Data Analysis  
- Diseño de KPIs  
- Análisis estadístico  
- Visualización de datos  
- Diseño de dashboards  
- Storytelling con datos  
- Estructuración de proyectos end-to-end  

---

## Posibles Mejoras Futuras

- Modelo predictivo para estimar probabilidad de impunidad  
- Dashboard web interactivo usando :contentReference[oaicite:12]{index=12}  
- Automatización ETL  
- Sistema de scoring de riesgo por país  
- Implementación en entorno cloud  

---

## Autor

**Rolando Mateo Sotelo Mestanza** Data Analyst / Data Enginner Jr. | Data & Marketing Analyst 📍 Lima, Perú 

---
