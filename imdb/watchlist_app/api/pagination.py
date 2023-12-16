from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination


class WatchListPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'watchlist'
    page_size_query_param = '10'
    max_page_size = '20'
    last_page_strings = 'end'
    
    
class LimitOffSetPaganationAV(LimitOffsetPagination):
    default_limit = 5
    limit_query_param ='watchlist'
    max_limit = 6