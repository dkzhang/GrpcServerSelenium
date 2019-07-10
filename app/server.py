# coding=utf-8

from concurrent import futures
import time
import logging

import grpc

import the_pb2
import the_pb2_grpc

from selenium import webdriver
firefox_capabilities ={
    "browserName": "firefox",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
    # "marionette": True,
}

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class QueryID(the_pb2_grpc.QueryIDServicer):

    def Query(self, request, context):
        # return the_pb2.IdUrlReply(url='Hello, %s!' % request.isbn)
        browser = webdriver.Remote("http://selenium-hub:4444/wd/hub", desired_capabilities=firefox_capabilities)
        browser.get('https://book.douban.com/subject_search?search_text= 9787115445353&cat=1001/')
        elem = browser.find_element_by_class_name("title-text")
        book_url = elem.get_attribute('href')
        print(book_url)
        browser.quit()
        return the_pb2.IdUrlReply(url=book_url)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    the_pb2_grpc.add_QueryIDServicer_to_server(QueryID(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()

