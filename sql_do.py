"""
users记录用户的模式开关
kanamodel记录用户的qq，开关，现在答题总数， 开始的时间
usergoals记录用户qq，答题次数，分数，题目
bulid_db()新建数据库
get_all()查询数据库所有数据
get_kanagoals(cur)查询kanagoals所有数据
get_users(cur):查询users
usersinsert(_qq, _mode1, _model2, _model3, _model4, _model5):插入一行users数据
kanamodelinsert(_qq, _modeswitch, _count, _starttime) 插入一个kanamodel数据
usergoalsinsert(_qq, _time, _goals, _modelswitch) 插入一个分数数据
update_users(_qq, _model1, _model2, _model3, _model4, _model5)更新users数据，改model状态时用
update_kanamodel(_qq, _modeswitch, _count, _starttime)更新kanamodel状态，进入kana模式用
update_usergoals(_qq, _time, _goals, _modelswitch)更新分数数据， 结束kana一个循环时用
get_onekana(_qq)获取某一用户kana数据
get_oneusers(_qq)获取某一用户users数据
get_onegoals(_qq)获取某一用户goals数据
get_timu(_tihao)获取一个题目得到题号，平假名，片假名， 罗马字
"""

import sqlite3

def get_con(func):
    data_path = r"user_db.db"

    def sql_exc():
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = func(cur)
        cur.close()
        conn.commit()
        conn.close()
        return data

    return sql_exc


@get_con
def get_users(cur):
    # 查询users
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    return rows


@get_con
def get_kana_model(cur):
    # 查询kanamodel所有数据
    cur.execute("SELECT * FROM KANAMODEL")
    rows = cur.fetchall()
    return rows


@get_con
def get_kanagoals(cur):
    # 查询所有goals数据
    cur.execute("SELECT * FROM USERGOALS")
    rows = cur.fetchall()
    return rows


@get_con
def userstable(cur):
    cur.execute('''CREATE TABLE USERS 
              (
                QQ1 INT PRIMARY KEY, MODEL1 INT NULL, MODEL2 INT NULL, MODEL3 INT NULL, MODEL4 INT NULL, MODEL5 INT NULL
              )''')



@get_con
def kanamodeltable(cur):
    """DATETIME: YYYY-MM-DD HH:MM:SS.SSS"""
    cur.execute('''CREATE TABLE KANAMODEL 
              (
                QQ2 INT PRIMARY KEY, MODELSW INT NOT NULL, COUNT INT NOT NULL, STARTTIME TEXT NOT NULL
              )''')


@get_con
def kanatable(cur):
    """创建题库表"""
    cur.execute('''CREATE TABLE KANA 
              (
                TIHAO INT PRIMARY KEY, HIRAGANA VARCHAR(4) NOT NULL, KATAKANA VARCHAR(4) NOT NULL, ROUMAJI VARCHAR(4) NOT NULL
              )''')
    for i in [(1, 'あ', 'ア', 'a'), (2, 'い', 'イ', 'i'), (3, 'う', 'ウ', 'u'), (4, 'え', 'エ', 'e'), (5, 'お', 'オ', 'o'), (6, 'か', 'カ', 'ka'), (7, 'き', 'キ', 'ki'), (8, 'く', 'ク', 'ku'), (9, 'け', 'ケ', 'ke'), (10, 'こ', 'コ', 'ko'), (11, 'さ', 'サ', 'sa'), (12, 'し', 'シ', 'si'), (13, 'す', 'ス', 'su'), (14, 'せ', 'セ', 'se'), (15, 'そ', 'ソ', 'so'), (16, 'た', 'タ', 'ta'), (17, 'ち', 'チ', 'chi'), (18, 'つ', 'ツ', 'tsu'), (19, 'て', 'テ', 'te'), (20, 'と', 'ト', 'to'), (21, 'な', 'ナ', 'na'), (22, 'に', 'ニ', 'ni'), (23, 'ぬ', 'ヌ', 'nu'), (24, 'ね', 'ネ', 'ne'), (25, 'の', 'ノ', 'no'), (26, 'は', 'ハ', 'ha'), (27, 'ひ', 'ヒ', 'hi'), (28, 'ふ', 'フ', 'hu'), (29, 'へ', 'ヘ', 'he'), (30, 'ほ', 'ホ', 'ho'), (31, 'ま', 'マ', 'ma'), (32, 'み', 'ミ', 'mi'), (33, 'む', 'ム', 'mu'), (34, 'め', 'メ', 'me'), (35, 'も', 'モ', 'mo'), (36, 'や', 'ヤ', 'ya'), (37, 'ゆ', 'ユ', 'yu'), (38, 'よ', 'ヨ', 'yo'), (39, 'ら', 'ラ', 'ra'), (40, 'り', 'リ', 'ri'), (41, 'る', 'ル', 'ru'), (42, 'れ', 'レ', 're'), (43, 'ろ', 'ロ', 'ro'), (44, 'わ', 'ワ', 'wa'), (45, 'を', 'ヲ', 'o'), (46, 'ん', 'ン', 'nn')]:
        kanainsert(i[0], i[1], i[2], i[3])


@get_con
def get_kana(cur):
    # 查询kana_all
    cur.execute("SELECT * FROM kana")
    rows = cur.fetchall()
    return rows

@get_con
def usergoalstable(cur):
    cur.execute('''CREATE TABLE USERGOALS
              (
                QQ3 INT, TIME INT PRIMARY KEY ,  GOALS INT NULL, MODELswitch varchar(10)
              )''')


def bulid_db():
    """数据库初始化在此"""
    try:
        userstable()
    except:
        print('已有user表')
    try:
        usergoalstable()
    except:
        print('已有goals表')
    try:
        kanamodeltable()
    except:
        print('已有kanamodel表')
    try:
        kanatable()
    except:
        print("已有kana表")

def get_all():
    print('user' + str(get_users()))
    print('kanagoals' + str(get_kanagoals()))
    print('kana_model' + str(get_kana_model()))

def usersinsert(_qq, _mode1, _model2, _model3, _model4, _model5):
    """插入一行users数据"""
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq, _mode1, _model2, _model3, _model4, _model5,)
        ins = 'INSERT INTO users (qq1, model1, model2, model3, model4, model5) VALUES(?, ?, ?, ?, ?, ?)'
        cur.execute(ins, data)

    except:
        print('eroo userinsert')
    finally:
        cur.close()
        conn.commit()
        conn.close()

def kanainsert(_tihao, _hiragana, _katakana, _roumaji):
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_tihao, _hiragana, _katakana, _roumaji,)
        ins = "INSERT INTO KANA (TIHAO, HIRAGANA, KATAKANA, ROUMAJI) VALUES(?,?,?,?)"
        cur.execute(ins, data)

    except:
        print('eroo kanainsert')
    finally:
        cur.close()
        conn.commit()
        conn.close()

def kanamodelinsert(_qq, _modeswitch, _count, _starttime):
    # 插入一个kanamodel数据
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq, _modeswitch, _count, _starttime,)
        ins = 'INSERT INTO KANAMODEL (qq2, modelsw, count, starttime) VALUES(?, ?, ?, ?)'
        cur.execute(ins, data)

    except:
        print('eroo kanamodelinsert')
    finally:
        cur.close()
        conn.commit()
        conn.close()

def usergoalsinsert(_qq, _time, _goals, _modelswitch):
    # 插入一个分数数据
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq, _time, _goals, _modelswitch)
        ins = 'INSERT INTO USERGOALS (qq3, time, goals, modelswitch) VALUES(?, ?, ?, ?)'
        cur.execute(ins, data)

    except:
        print('eroo usergoalsinsert')
    finally:
        cur.close()
        conn.commit()
        conn.close()

def update_users(_qq, _model1, _model2, _model3, _model4, _model5):
    # 更新users数据，改model状态时用
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq, _model1, _model2, _model3, _model4, _model5,)
        ins = 'update users set model1 = ? where qq1 = ?'
        cur.execute(ins, (data[1],data[0]))
        ins = 'update users set model2 = ? where qq1 = ?'
        cur.execute(ins, (data[2], data[0]))
        ins = 'update users set model3 = ? where qq1 = ?'
        cur.execute(ins, (data[3], data[0]))
        ins = 'update users set model4 = ? where qq1 = ?'
        cur.execute(ins, (data[4], data[0]))
        ins = 'update users set model5 = ? where qq1 = ?'
        cur.execute(ins, (data[5], data[0]))

    except:
        print('eroo update_users')
    finally:
        cur.close()
        conn.commit()
        conn.close()

def update_kanamodel(_qq, _modeswitch, _count, _starttime):
    # 更新kanamodel状态，进入kana模式用
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq, _modeswitch, _count, _starttime)
        """qq2, modelsw, count, starttime"""
        ins = 'update kanamodel set modelsw = ? where qq2 = ?'
        cur.execute(ins, (data[1], data[0]))
        ins = 'update kanamodel set count = ? where qq2 = ?'
        cur.execute(ins, (data[2], data[0]))
        ins = 'update kanamodel set starttime = ? where qq2 = ?'
        cur.execute(ins, (data[3], data[0]))

    except:
        print("update_kanamodel")
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()

def update_usergoals(_qq, _time, _goals, _modelswitch):
    # 更新分数数据， 结束kana一个循环时用
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq, _time, _goals, _modelswitch)
        "qq3, time, goals, modelswitch"
        ins = 'update USERGOALS set goals = ? where time = ?'
        cur.execute(ins, (data[2], data[1]))
        ins = 'update USERGOALS set modelswitch = ? where time = ?'
        cur.execute(ins, (data[3], data[1]))
        #ins = 'update USERGOALS set qq3 = ? where time = ?'
        #cur.execute(ins, (data[1], data[0]))
  
    except:
        print('update_usergoals')
        return False
    finally:
        cur.close()
        conn.commit()
        conn.close()

def get_onegoals(_time):
    """获取某一时间用户goals数据"""
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_time,)
        "qq3, time, goals, modelswitch"
        ins = 'select * from USERGOALS where time = ?'
        cur.execute(ins, data)
        rows = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return rows
    except:
        cur.close()
        conn.commit()
        conn.close()
        return False

def get_one_allgoals(_qq):
    """获取某一用户goals数据"""
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq,)
        "qq3, time, goals, modelswitch"
        ins = 'select * from USERGOALS where qq3 = ?'
        cur.execute(ins, data)
        rows = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return rows

    except:
        cur.close()
        conn.commit()
        conn.close()
        return False

def get_timu(_tihao):
    """获取某假名"""
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_tihao,)
        "qq3, HIRAGANA, KATAKANA, ROUMAJI"
        ins = 'select * from KANA where TIHAO = ?'
        cur.execute(ins, data)
        rows = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return rows
    except:
        cur.close()
        conn.commit()
        conn.close()
        return False

def get_oneusers(_qq):
    # 获取某一用户users数据
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq,)
        ins = 'select * from USERS where qq1 = ?'
        cur.execute(ins, data)
        rows = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return rows
    except:
        cur.close()
        conn.commit()
        conn.close()
        return False


def get_onekana(_qq):
    # 获取某一用户kana数据
    try:
        data_path = r"user_db.db"
        conn = sqlite3.connect(data_path, check_same_thread = False)
        conn.text_factory = str
        cur = conn.cursor()
        data = (_qq,)
        ins = 'select * from kanamodel where qq2 = ?'
        cur.execute(ins, data)
        rows = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return rows
    except:
        cur.close()
        conn.commit()
        conn.close()
        print("wrong in get kana")
        return False
# u1 k2 g3
