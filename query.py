#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import eUtils

term = 'drosophila[ORGN]+AND+chip-seq[ALL]'

connection = eUtils.fetch_XML(term=term, db='gds')
sys.stdout.write(connection.read())

