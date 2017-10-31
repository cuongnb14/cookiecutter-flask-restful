class Paginator:
    """Class hold Pagination for sqlalchemy query"""
    def __init__(self, sqlalchemy_query, offset, limit):
        """

        :param sqlalchemy_query: sqlalchemy query
        :param offset: int offset of query
        :param limit: int limit of query
        """
        self.offset = offset if offset else 0
        self.limit = limit if limit else 10
        self.total = sqlalchemy_query.count()
        self.result = sqlalchemy_query.limit(self.limit).offset(self.offset)
