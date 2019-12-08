#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' url handlers '

import re, time, json, logging, hashlib, base64, asyncio
from coroweb import get
from models import Blog
from models import User
from models import Comment
from apis import Page

def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p

@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = yield from Blog.findAll(orderBy='created_at desc')
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }

@get('/user')
def getuser(request):
    users = yield from User.findAll(orderBy='created_at desc')
    logging.info("user size:%d" % len(users))
    return {
        '__template__': 'User.html',
        'users':users
    }

@get('/comments')
def getcomments(request):
    comments = yield from Comment.findAll(orderBy='created_at desc')
    return {
        '__template__': 'comments.html',
        'comments':comments
    }

@get('/api/blogs')
def api_blogs(*, page='1'):
    page_index = get_page_index(page)
    num = yield from Blog.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blogs=())
    blogs = yield from Blog.findAll(orderBy='created_at desc',
                                    limit=(p.offset, p.limit))
    return dict(page=p, blogs=blogs)