♟️ AJEFECH Tournament Scraper — BETA

Beta de un servicio que centraliza y ordena torneos oficiales de ajedrez en Chile, con foco inicial en torneos presenciales en Santiago.

El objetivo es transformar datos dispersos en información clara, filtrable y reutilizable.

🚧 Estado del proyecto

BETA funcional
El proyecto está en desarrollo activo. La base técnica ya funciona; nuevas features vienen en camino.

🧠 Qué problema resuelve

Los torneos oficiales existen, pero la información está dispersa.

No hay filtros claros por ciudad, modalidad o vigencia.

Consultar próximos eventos requiere revisar múltiples fuentes.

⚙️ Qué hace esta beta

Consume datos oficiales vía GraphQL

Normaliza y limpia la información

Filtra torneos presenciales en Santiago

Ordena por fecha

Guarda histórico en SQLite (sin duplicados)

Permite consultar los próximos torneos desde la base de datos

🏗️ Cómo funciona (pipeline)
GraphQL API
   ↓
Normalización de datos
   ↓
Filtros (Santiago / presencial / activo)
   ↓
SQLite (persistencia + dedupe)
   ↓
Consulta de próximos eventos

▶️ Cómo ejecutar
pip install -r requirements.txt
python src/main.py


La base de datos se crea automáticamente y los torneos quedan almacenados localmente.

📌 Próximos pasos

Export a CSV

Export a calendario (ICS)

Automatización diaria

CLI con argumentos

Feedback de usuarios

🤝 Feedback

Este proyecto está en beta.
Comentarios, sugerencias y observaciones técnicas son bienvenidas.
