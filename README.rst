Dipus
=========

Dipus is a simple full-text search server using `Whoosh <http://packages.python.org/Whoosh/>`_. Dipus is
integrated to the `Sphinx document builder <http://sphinx.pocoo.org/>`_ .

You can search document quickly and with N-gram.


How to install
--------------------

::

  % pip install dipus

Dependencies
+++++++++++++++

- Python 2.7
- Sphinx
- whoosh
- simplejson
- bottle

How to Use
--------------

Start dipus server
+++++++++++++++++++++++++++++++++++

::

  python -m dipus.websetup -c conf.json

conf.json example

::

  {
    "indexroot": "/path/to/index"
  }

Dipus server default url is "http://0.0.0.0:9876".

Register sphinx document
+++++++++++++++++++++++++++++++++++

1. Add extension to your conf.py

  ::

     extensions = ['dipus.dipusbuilder']

  and there are optional settings.

  ::

     #dipus_host_url = "http://192.0.2.20"
     #  url of dipus server
     #  Default is "http://localhost:9876" 
     
     #dipus_index = "test_rst"
     #  identifier of this document
     #  Default is same as 'project' in conf.py


2. Run builder

   ::

     % sphinx-build -b dipus source build

   CAUTION: builder will *overwrite* _static/search_dipus.js and _template/search_dipus.html.


3. copy search file

   Note: This required once when after you change conf.py dipus related values.

   ::

     % cp _template/search_dipus.html _template/search.html

   If you have created your own search.html, please merge it.


4. make html as usual

   ::

     % make html

Note about builder will be done quickly, as "fire-and-forget". But
indexing itself on the server is not so quick. Please be patient until
all your document will be indexed.


5. (optional) add dipus builder to Makefile

   Add line which invoke dipus builder in the html section in Makefile
   as blow.

   ::

      html:
      	$(SPHINXBUILD) -b dipus $(ALLSPHINXOPTS) $(BUILDDIR)/html
      	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
    
    Then, whenever type 'make html', documents are registerd.


Search from sphinx document
++++++++++++++++++++++++++++++++

Just open your search box and type.

Requirements
----------------

- Python 2.7 (sorry, not 3 currently)
- sphinx
- whoosh
- simplejson
- bottle


Security
------------

*Dipus is for the internal use only.* 

If you want to use at the public, use google.


TODO
-----

- test test test
- Security
- Python 3
- Admin Screen
- correct highlighting(a.k.a. snippet) on the search result
- logging
- search over multiple documents
- Analyzer selected by each document

