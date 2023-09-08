

"""
   Todo List: блокнот для ежедневных задач

   * Записывать(добавлять) новые задачи (помыть кота)
   * Читать задачи из файла/базы данных(только базы
   данных могут обеспечить высокую производительность)
   * Изменять(обновлять)
   * Удалять

   * CRUD
   * Create (INSERT)
   * Read (SELECT)
   * Update (UPDATE)
   * Delete (DELETE)



   Релятивные(SQL - 95% родственны) - формализованные и строгие (excel)
   MySQL - 35%, best for PHP
   PostgreSQL - 25%, best for Python
   Oracle - 25%, best for Business(надёжность)   $
   MSSQL - 10%                                   $
   SQLite - ??%, best for mobile(встраиваемая - локальная - просто файл) - смартфоны
   ...

   СУБД - система управления базами данных
   https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

   Не релятивные(NO SQL)
   MongoDB, ClickHouse - (json, 10 000 000 000)
   Redis, MemCache - key-value (огромный словарь)
   RabbitMQ, Kafka - queue (очередь)



   СУБД[FOLDER] -> magazine(database)[WORKBOOK] -> news(table)[WORKSHEET] ->
   (id: serial(1, 2, 3...), title: var(VARCHAR), description: var(VARCHAR),
   price: double precision, is_actual: bool, datatime: time_stamp)[COLUMNS]
   """



