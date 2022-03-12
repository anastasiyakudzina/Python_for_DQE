 There are 3 tables in the DB:
    'News';
    'Advertising';
    'Horoscope'
 The table 'News' contains following columns: 'NewsId', 'NewsBody', 'City', 'CurrentDate'
    Unique: 'NewsBody' + 'City'
 The table 'Advertising' contains following columns: 'AdvId', 'AdvBody', 'ActualUntil', 'DaysLeft'
    Unique: 'AdvBody'
 The table 'Horoscope' contains following columns: 'HorId', 'HorBody', 'ZodiacSign', 'Probability'
    Unique: 'HorBody', 'ZodiacSign'

 New line will be inserted if the row does not exist, or replaced the values
    ('CurrentDate' or 'ActualUntil'+'DaysLeft' or 'Probability') if it does.

 There is commented code on the 548 - 551 lines for checking the insert into the DB.



