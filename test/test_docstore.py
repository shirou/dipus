#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import time
import pytest

from dipus import docstore

INDEXROOT="/tmp/dipustest/index"
posted = {
    "_index": "test_index",
    "path": "test_path".decode("utf-8"),
    "title": "test_title".decode("utf-8"),
    "doc_url": "test_doc_url".decode("utf-8"),
    "message": "test_message".decode("utf-8")
    }
    
def test_openindex():
    indexdir = os.path.join(INDEXROOT, "test_index")
    ix = docstore.open_index(indexdir)
    assert ix.last_modified != -1
    assert 'title' in ix.schema.names()
    assert 'path' in ix.schema.names()
    assert 'doc_url' in ix.schema.names()
    assert 'content' in ix.schema.names()
    assert 'date' in ix.schema.names()
    shutil.rmtree(INDEXROOT)


def test_listindex():
    with pytest.raises(OSError):
        docstore.listindex(INDEXROOT)
    indexdir = os.path.join(INDEXROOT, "test_index")
    docstore.open_index(indexdir)
    assert len(docstore.listindex(INDEXROOT)) == 1
    indexdir = os.path.join(INDEXROOT, "test_index2")
    docstore.open_index(indexdir)
    assert len(docstore.listindex(INDEXROOT)) == 2
    indexdir = os.path.join(INDEXROOT, "test_index3")
    docstore.open_index(indexdir)
    assert len(docstore.listindex(INDEXROOT)) == 3

    shutil.rmtree(INDEXROOT)

def test_register():
    r = docstore.register(posted, INDEXROOT)

    assert r['ok'] == True
    assert r['_index'] == posted['_index']
    assert r['_path'] == posted['path']
    
    time.sleep(1)  # FIXME
    
    r = docstore.search(posted["_index"], "test", INDEXROOT)

    assert len(r) > 0

    shutil.rmtree(INDEXROOT)
    

def test_search():
    r = docstore.register(posted, INDEXROOT)
    time.sleep(1)  # FIXME

    r = docstore.search(posted["_index"], "hoge", INDEXROOT)
    assert len(r) == 0
    r = docstore.search(posted["_index"], "test", INDEXROOT)
    assert len(r) > 0
    r = docstore.search(posted["_index"], None, INDEXROOT)
    assert len(r) == 0

    shutil.rmtree(INDEXROOT)
