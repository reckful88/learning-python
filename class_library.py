#!/usr/bin/env python
# -*- coding: utf-8 -*-

class library(object):
	def __init__(self,book,librarian):
		self.book = book
		self.librarian = librarian
	def run(self):
		print "welcome to library"
	def addbook(self,book,bookid,bookname):
		self.book = book
		self.bookid = bookid
		self.bookname = bookname
	def delbook(self,book,bookid,bookname):
		self.book = book
		self.bookid = bookid
		self.bookname = bookname	
	def findbook(self,book,bookid,bookname):
		self.book = book
		self.bookid = bookid
		self.bookname = bookname
	def borrowbook(self,book,bookid,bookname):
		self.book = book
		self.bookid = bookid
		self.bookname = bookname
class book(object):
	def __init__(self,name):
		self.name = name
class librarian(object):
	def __init__(self,name):
		self.name = name
