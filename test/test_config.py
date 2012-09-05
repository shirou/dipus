#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import pytest
import simplejson

from dipus import config

def write_config(data):
    path = "/tmp/dipus_config.test"
    with open(path, "w") as fp:
        fp.write(simplejson.dumps(data))
    return path

def test_config_default():
    path = write_config({})
    c = config.Config(path)
    assert c is not None
    assert c.port == 9876
    assert c.indexroot == "/tmp/dipus/index"
    assert c.host == "0.0.0.0"
    
    os.remove(path)

def test_config():
    test_dir = "/tmp/dipus_true"
    path = write_config({
        "port": 9090,
        "host": "127.0.0.1",
        "indexroot": test_dir
        })
    c = config.Config(path)
    assert c.port == 9090
    assert c.indexroot == test_dir
    assert c.host == "127.0.0.1"

    os.remove(path)
