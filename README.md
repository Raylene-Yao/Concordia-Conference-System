pip install django-filter
pip install pymysql

Database: MySQL
Schema: ccs

Run: cmd and cd to the assignment directory
Run: python manage.py makemigrations
Run: python manage.py migrate
Insert data below to databse:
insert into conference( id, conference_name, conference_initial_date, conference_end_date)values(1,"conference_1","2022-07-25","2022-07-25");
insert into conference( id, conference_name, conference_initial_date, conference_end_date)values(2,"conference_2","2022-07-25","2022-07-26");
insert into conference( id, conference_name, conference_initial_date, conference_end_date)values(3,"conference_3","2022-07-25","2022-07-26");
insert into event( id, event_name, event_room, event_initial_date, event_end_date,event_initial_time, event_end_time,event_speaker, conference_id)values(1,"event1_1","room_1","2022-07-25","2022-07-25","13:00","15:00","speaker_1", 1);
insert into event( id, event_name, event_room, event_initial_date, event_end_date,event_initial_time, event_end_time,event_speaker, conference_id)values(2,"event2_1","room_2","2022-07-25","2022-07-25","13:00","15:00","speaker_2", 2);
insert into event( id, event_name, event_room, event_initial_date, event_end_date,event_initial_time, event_end_time,event_speaker, conference_id)values(3,"event2_2","room_1","2022-07-26","2022-07-26","12:00","14:00","speaker_1", 2);
insert into event( id, event_name, event_room, event_initial_date, event_end_date,event_initial_time, event_end_time,event_speaker, conference_id)values(4,"event3_1","room_3","2022-07-25","2022-07-25","14:00","16:00","speaker_3", 3);
insert into event( id, event_name, event_room, event_initial_date, event_end_date,event_initial_time, event_end_time,event_speaker, conference_id)values(5,"event3_2","room_3","2022-07-26","2022-07-26","13:00","15:00","speaker_2", 3);
Run: python manage.py runserver
Address: http://127.0.0.1:8000/system/conference or http://127.0.0.1:8000/system/event
