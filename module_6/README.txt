User can choose 2 option for adding publication to output file:
	1 - by console;
	2 - from file.

By console: 
	1 - News; 
	2 - Advertising; 
	3 - Horoscope.

 News. User should print: 
 - publication text;
 - city.

 Advertising. User should print:
 - publication text; 
 - expiration date: must be in YYYY-MM-DD format and must be greater than or equal to current date.

 Horoscope. User should print:
 - publication text;
 - zodiac sign.

From file:

 User can choose his own file path or default folder.
 File path can be either relative or absolute (C:\Python_for_DQE\module_6\input.txt or module_6\input.txt).
 Must be in format:
 HEADER//publication text//extension(city or expiration date or zodiac sign)
 Blank line isn't considered to the entry.

 HEADER must start from "news/adv/hor" letters.
 Expiration date must be in YYYY-MM-DD format and must be greater than or equal to current date.

 All fail files are added to the document fail_{current_date_time}.txt for future reprocessing. 
 If all files are processed successfully and document fail_{current_date_time}.txt isn't created, 
	input file will be deleted.



