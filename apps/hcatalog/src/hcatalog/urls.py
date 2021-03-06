# Licensed to Hortonworks, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Hortonworks, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('hcatalog',
  url(r'^$', 'views.show_tables'),
  url(r'^get_tables$', 'views.get_tables'),
  url(r'^tables$', 'views.show_tables'),
  url(r'^pig_view/(?P<table>\w+)$', 'views.pig_view'),
  url(r'^hive_view/(?P<table>\w+)$', 'views.hive_view'),
  url(r'^execute/(?P<design_id>\d+)$', 'views.execute_query'),
  url(r'^table/(?P<table>\w+)$', 'views.describe_table'),
  url(r'^table/(?P<table>\w+)/load$', 'views.load_table'),
  url(r'^table/(?P<table>\w+)/read$', 'views.read_table'),
  url(r'^table/(?P<table>\w+)/drop$', 'views.drop_table'),
  url(r'^create/create_table$', 'create_table.create_table'),
  url(r'^create/import_wizard$', 'create_table.import_wizard'),
  url(r'^table/(?P<table>\w+)/browse_partition$', 'views.browse_partition'),
  url(r'^table/(?P<table>\w+)/drop_partition$', 'views.drop_partition'),
  url(r'^watch/(?P<id>\d+)$', 'views.watch_query'),
  url(r'^results/(?P<id>\d+)/(?P<first_row>\d+)/(?P<last_result_len>\d+)$', 'views.view_results'),
)
