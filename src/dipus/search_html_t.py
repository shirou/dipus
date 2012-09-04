#!/usr/bin/env python
# -*- coding: utf-8 -*-

template = """{{#
    basic/search.html
    ~~~~~~~~~~~~~~~~~

    Template for the search page.

    :copyright: Copyright 2007-2011 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
#}}
{{% extends "layout.html" %}}
{{% set title = _('Search') %}}
{{% set script_files = script_files + ['_static/search_dipus.js'] %}}
{{% block extrahead %}}
  <script type="text/javascript">
  </script>
  {{{{ super() }}}}
{{% endblock %}}
{{% block body %}}
  <h1 id="search-documentation">{{{{ _('Search') }}}}</h1>
  <div id="fallback" class="admonition warning">
  <script type="text/javascript">$('#fallback').hide();</script>
  <p>
    {{% trans %}}Please activate JavaScript to enable the search
    functionality.{{% endtrans %}}
  </p>
  </div>
  <p>
    {{% trans %}}From here you can search these documents. Enter your search
    words into the box below and click "search". Note that the search
    function will automatically search for all of the words. Pages
    containing fewer words won't appear in the result list.{{% endtrans %}}
  </p>
  <form action="" method="get">
    <input type="text" name="q" value="" />
    <input type="submit" value="{{{{ _('search') }}}}" />
    <span id="search-progress" style="padding-left: 10px"></span>
  </form>
  {{% if search_performed %}}
    <h2>{{{{ _('Search Results') }}}}</h2>
    {{% if not search_results %}}
      <p>{{{{ _('Your search did not match any results.') }}}}</p>
    {{% endif %}}
  {{% endif %}}
  <div id="search-results">
  {{% if search_results %}}
    <ul>
    {{% for href, caption, context in search_results %}}
      <li><a href="{{{{ pathto(item.href) }}}}">{{{{ caption }}}}</a>
        <div class="context">{{{{ context|e }}}}</div>
      </li>
    {{% endfor %}}
    </ul>
  {{% endif %}}
  </div>
{{% endblock %}}
"""
