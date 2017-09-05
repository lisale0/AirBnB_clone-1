echo 'insert into cities (id, created_at, updated_at, state_id, name) values ("12f07934-d0bb-4a0d-b120-fcba0d178ed2", '2011-10-24 10:00:00', '2011-10-24 10:00:00', "5dac1664-bf82-4e40-9c0d-59b83eff0", "ASDSD")' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py

echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py

echo 'create City state_id="5d28f610-a3e7-4c67-9352-1beee4257d7b" name="San_Francisco"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py

echo 'create User email="email.com" password="goodpass" first_name="lisa", last_name="leung"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py

echo 'create Review text="isgood" user_id="40f53d56-0cdf-4823-a289-81b1719d5031" place_id=""' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py


echo 'create Place user_id="40f53d56-0cdf-4823-a289-81b1719d5031" name="home" city_id="6733bed3-d55b-4fd3-ac9d-61b0353e3a76" description="coolplace"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py


echo 'create Review user_id="40f53d56-0cdf-4823-a289-81b1719d5031" text="nice" place_id="09cb5c42-bf20-4a7b-84a6-ccb7220f87b1"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py


echo 'create Amenity name="wifi"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd MYSQL_DB=hbnb_dev_db HBNB_MYSQL_HOST=localhost HBNB_TYPE_STORAGE=db ./console.py
