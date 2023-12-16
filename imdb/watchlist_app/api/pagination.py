from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'watchlist'
    page_size_query_param = '10'
    max_page_size = '20'
    last_page_strings = 'end'