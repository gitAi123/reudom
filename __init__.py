#!/usr/bin/python
#
# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from .running.test_runner import main
from .case import TestCase
from .testdata import ddt, ddt_class
from .skip import skip
from requests import request
from requests import *
from unittest import TestCase
from .Crypto.Cipher import AES
__author__ = "Barry"

__version__ = "1.0.1"

__description__ = "Automated testing framework based on requests and unittest interface."

