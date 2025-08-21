# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

class MySQLPipeline:

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='books_db',
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()

        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                price VARCHAR(20),
                availability VARCHAR(50),
                rating VARCHAR(20)
            )
        """)
        self.conn.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        self.cursor.execute("""
            INSERT INTO books (title, price, availability, rating) 
            VALUES (%s, %s, %s, %s)
        """, (
            item['title'],
            item['price'],
            item['availability'],
            item['rating']
        ))
        self.conn.commit()
        return item
