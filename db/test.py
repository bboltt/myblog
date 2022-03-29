from db.mysql import Session


def search_name_list():
    session = Session()
    sql = """
    select *
    from test.test
    """
    cursor = session.execute(sql)
    result = cursor.fetchall()
    session.close()
    return result
