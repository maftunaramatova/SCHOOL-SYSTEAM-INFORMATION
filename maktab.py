import sqlite3 as sql

with sql.connect("Maktab.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS oquvchilar(
        id INTEGER PRIMARY KEY,
        ism TEXT NOT NULL,
        familya TEXT NOT NULL,
        sinf TEXT NOT NULL,
        tugilgan_yil INTEGER ,
        telefon TEXT
    )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS fanlar(
        id INTEGER PRIMARY KEY,
        nomi TEXT NOT NULL UNIQUE,
        oqituvchi TEXT NOT NULL,
        haftalik_soat INTEGER     
    )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS baholar(
        id INTEGER PRIMARY KEY,
        oquvchi_id INTEGER NOT NULL,
        fan_id INTEGER NOT NULL,
        ball INTEGER NOT NULL,
        sana TEXT NOT NULL,
        FOREIGN KEY(oquvchi_id)REFERENCES oquvchilar(id),
        FOREIGN KEY(fan_id)    REFERENCES fanlar(id) 
    )""")
    
    oquvchilar = [
            (1,  'Dilnura',     'Qurambayeva',     '9-B', 2010, '+998909204577'),
            (2,  'Ruhshona',     'Ravshanboyeva',     '9-B', 2010, '+998509294577'),
            (3,  'Samadjon',     'Alimboyev',     '9-B', 2010, '+998909274547'),
            (4,  'Zuhra',     'Jumanazarova',     '9-B', 2010, '+998908254537'),
            (5,  'Mehroj',     'Otanazarov',     '9-B', 2010, '+998909299599'),
            (6,  'Ozoda',     'Xudayberganova',     '9-B', 2010, '+998909204577'),
            (7,  'Gulsevar',     'Sobirova',     '9-B', 2010, '+998909204577'),
            (8,  'Sarvara',     'Aminova',     '9-B', 2010, '+998909204577'),
            (9,  'Ruxshona',     'Quvandiqova',     '9-B', 2010, '+998909204577'),
            (10,  'Muhlisa',     'Yusupova',     '9-B', 2010, '+998909204577'),
            (11,  'Charosxon',     'Ikramova',     '9-B', 2010, '+998909204577'),
            (12,  'Maftuna',     'Ramatova',     '9-B', 2010, '+998909204577'),
            (13,  'Kamron',     'Darveshov',     '9-B', 2010, '+998909204577'),
            (14,  'Ahror',     'Zaripov',     '9-B', 2010, '+998909204577'),
            (15,  'Davlatyor',     'Ibadullayev',     '9-B', 2010, '+998909204577'),
            (16,  'Davlatmurod',     'Olimov',     '9-B', 2010, '+998909204577'),
            (17,  'Tillo',     'Sobirov',     '9-B', 2010, '+998909204577'),
            (18,  'Agabek',     'Rozibayev',     '9-B', 2010, '+998909204577'),
            (19,  'Shohrux',     'Komuljonov',     '9-B', 2010, '+998909204577'),
            (20,  'Salohiddin',     'Xojaniyazov',     '9-B', 2010, '+998909204577'),
            (21,  'Mirjalol',     'Nasullayev',     '9-B', 2010, '+998909204577'),
            (22,  'Bobur',     'Yusupov',     '9-B', 2010, '+998909290577'),
            (23,  'Umrbek',     'Seydametov',     '9-B', 2010, '+998909204577'),
            (24,  'Sevinch',     'Sadullayeva',     '9-B', 2011, '+998509204577'),
            (25,  'Amirbek',     'Madrimov',     '9-B', 2010, '+998909404577'),
            (26,  'Asror',     'Otoxonov',     '9-B', 2010, '+998909204577'),
            (27,  'Kamron',     'Sultanov',     '9-B', 2010, '+998909204577'),
            (28,  'Javohir',     'Bahtiyorov',     '9-B', 2010, '+998900204577'),
            (29,  'Shohjahon',     'Atahonov',     '9-B', 2010, '+998909204577'),            
            (30,  'Muhammad',     'Saparbayev',     '9-B', 2010, '+998909204577'), 
            (31,  'Aziz',     'Oktamov',     '9-B', 2010, '+998909204577'), 
            (32,  'Aziz',     'Aminov',     '9-B', 2010, '+998909204577'), 
        
    ]
    cur.executemany(
    "INSERT OR IGNORE INTO oquvchilar VALUES (?, ?, ?, ?, ?, ?)",
    oquvchilar
    )
    
    fanlar = [
        (1, 'Kelajak soati',  'Yusupova Gozal', 1),
        (2, 'Ona tili',  'Durdiyeva Dilorom', 3),
        (3, 'Jismoniy tarbiya', 'Yusupov Xurishid', 2),
        (4, 'Informatika',  'Azamov Dilshod', 2),
        (5, 'Chizmachilik',  'Ibadullayeva Nazokat', 2),
        (6, 'Algebra', 'Yoqubova Gulxayo ', 2),
        (7, 'Ingiliz tili',  'Allayarov Farhod', 3),
        (8, 'Texnologiya',  'Jorabekova Nasiba', 1),
        (9, 'Geometriya', 'Yoqubova Gulxayo', 2),
        (10, 'Fizika',  'Hoshimov Otkir', 2),
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO fanlar VALUES (?, ?, ?, ?)",
        fanlar
    )
    baholar = [
        
        (1,  1, 1, 92, '2026-04-05'),  (2,  1, 2, 78, '2026-04-08'),
        (3,  1, 3, 85, '2026-04-12'),  (4,  1, 5, 88, '2026-04-15'),
        (5,  1, 8, 95, '2026-04-18'),

        (6,  2, 1, 98, '2026-04-05'),  (7,  2, 2, 95, '2026-04-08'),
        (8,  2, 3, 90, '2026-04-12'),  (9,  2, 4, 96, '2026-04-14'),
        (10, 2, 5, 92, '2026-04-15'),

        (11, 3, 1, 65, '2026-04-05'),  (12, 3, 2, 70, '2026-04-08'),
        (13, 3, 3, 58, '2026-04-12'),  (14, 3, 6, 75, '2026-04-16'),

        (15, 4, 1, 88, '2026-04-05'),  (16, 4, 4, 94, '2026-04-14'),
        (17, 4, 5, 90, '2026-04-15'),  (18, 4, 6, 85, '2026-04-16'),

        (19, 5, 1, 72, '2026-04-05'),  (20, 5, 7, 80, '2026-04-17'),
        (21, 5, 8, 88, '2026-04-18'),

        (22, 6, 3, 95, '2026-04-12'),  (23, 6, 4, 92, '2026-04-14'),
        (24, 6, 6, 89, '2026-04-16'),

        (25, 7, 2, 82, '2026-04-08'),  (26, 7, 8, 91, '2026-04-18'),

        (27, 8, 1, 86, '2026-04-05'),  (28, 8, 5, 94, '2026-04-15'),
        (29, 8, 6, 88, '2026-04-16'),

        (30, 9, 2, 76, '2026-04-08'),  (31, 9, 7, 85, '2026-04-17'),

        (32, 10, 3, 89, '2026-04-12'), (33, 10, 4, 91, '2026-04-14'),
        (34, 10, 5, 87, '2026-04-15'),

        (35, 11, 1, 55, '2026-04-05'), (36, 11, 2, 60, '2026-04-08'),
        (37, 11, 8, 78, '2026-04-18'),

        (38, 12, 5, 96, '2026-04-15'), (39, 12, 6, 93, '2026-04-16'),
        (40, 12, 7, 90, '2026-04-17'),
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO baholar VALUES (?, ?, ?, ?, ?)",
        baholar
    )

    con.commit()
    
    def chiqar(sarlavha,qator):
        print("\n" + "=" * 65)
        print(f" {sarlavha}")
        print("=" * 65)
        if not qator:
            print("  (natija bo'sh)")
            return
        for q in qator:
            print(" ", q)

##ORDER BY-Saralash
#ORDER BY natijani ustun qiymati boyicha tatiblaydi.
#   ASC - o'sish tartibi (kishikdan kattaga) - default
#   DESC - kamayish tartibi (kattadan kichikka)

    cur.execute("""
        SELECT ism, familya, tugilgan_yil
        FROM oquvchilar
        ORDER BY tugilgan_yil
    """)
    
    chiqar("O'quvchilar tug'ilgan yili bo'yicha (kichikdan kattaga)"),
    cur.fetchall()

    
#Familya bo'yicha alifbo tartibida
    cur.execute("""
        SELECT familya, ism, sinf
        FROM oquvchilar_ro'yxati
        ORDER BY familya ASC        
    """)
    
    chiqar("O'quvchilar familyasi bo'yicha alifbo tartibida"),
    cur.fetchall()
    
#Bir nechta ustun bo'yicha sarlash:
#Avval sinf boyicha (9-A, 9-B, 9-D, 9-E),
##keyin har bir sinf ichida familya bo'yicha

    cur.execute("""
        SELECT sinf, familya, ism
        FROM oquvchilar
        ORDER BY sinf ASC, fa,ilya ASC        
    """)
    
    chiqar("Sinf bo'yicha guruhlangan, ichida familya tartibida"),
    cur.fetchall()
