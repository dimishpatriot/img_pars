# img_pars
программа для пакетного скачивания изображений.

**`реализованы механизмы:`**
1. подмена proxy и user-agent для получения свежего списка proxy с http://hideme.name для обхода защиты от парсинга. сохранение нового списка в файл
2. подмена proxy (по свежему списку) и user-agent для запросов к поисковой машине

_примечание: за все время использования 1 и 2 в такой конфигурации не один запрос не был детектирован как парсинг_
3. запросы трех типов к Яндексу (простой/расширеный/полный)
4. разбор поисковой выдачи и формирование файла ссылок (url_list.txt) до 100 изображений с 1 запроса, создание папки с именем запроса и сохранение в нее файла со ссылками
5. выбор одно- или многопоточного скачивания по ссылкам в файле с сохранением результата в ранее созданную именованую папку
 
 
**`в планах:`**
1. реализация запросов к гугл
2. увеличение поисковой выдачи >100 изображений
 
 
