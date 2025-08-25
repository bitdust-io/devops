#!/usr/bin/env python
# setup.py
#
# Copyright (C) 2008 Veselin Penev, http://bitdust.io
#
# This file (setup.py) is part of BitDust Software.
#
# BitDust is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BitDust Software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with BitDust Software.  If not, see <http://www.gnu.org/licenses/>.
#
# Please contact us if you have any questions at bitdust.io@gmail.com
from __future__ import absolute_import
from setuptools import setup

setup(
    name='bitdust',
    version='{version}',
    author='Veselin Penev, BitDust',
    author_email='bitdust.io@gmail.com',
    maintainer='Veselin Penev, BitDust',
    maintainer_email='veselin@bitdust.io',
    url='https://bitdust.io',
    description='p2p secure distributed storage and communication engine',
    long_description=open('README.txt', 'r').read(),
    long_description_content_type='text/markdown',
    download_url='https://bitdust.io',
    license='Copyright (C) 2008 Veselin Penev, https://bitdust.io',

    keywords='''p2p, peer to peer, backup, restore, storage, data, recover,
                distributed, online, python, twisted, messaging, websocket,
                encryption, crypto, protection''',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Twisted',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',
    ],

    packages=[
        'bitdust',
        'bitdust.access',
        'bitdust.automats',
        'bitdust.blockchain',
        'bitdust.broadcast',
        'bitdust.chat',
        'bitdust.coins',
        'bitdust.contacts',
        'bitdust.crypt',
        'bitdust.currency',
        'bitdust.customer',
        'bitdust.dht',
        'bitdust.interface',
        'bitdust.lib',
        'bitdust.logs',
        'bitdust.main',
        'bitdust.p2p',
        'bitdust.raid',
        'bitdust.services',
        'bitdust.storage',
        'bitdust.stream',
        'bitdust.stun',
        'bitdust.supplier',
        'bitdust.system',
        'bitdust.transport',
        'bitdust.transport.http',
        'bitdust.transport.proxy',
        'bitdust.transport.udp',
        'bitdust.transport.tcp',
        'bitdust.updates',
        'bitdust.userid',
        'bitdust_forks',
        'bitdust_forks.Bismuth',
        'bitdust_forks.CodernityDB',
        'bitdust_forks.CodernityDB3',
        'bitdust_forks.entangled',
        'bitdust_forks.entangled.kademlia',
        'bitdust_forks.parallelp',
        'bitdust_forks.parallelp.pp',
        'bitdust_forks.txrestapi',
        'bitdust_forks.txrestapi.txrestapi',
        'bitdust_forks.websocket',
    ],

    package_data={
        'bitdust': [
            '*.txt',
            '*.md',
            '*.json',
        ],
        'bitdust_forks': [
            'bitdust_forks/Bismuth/LICENSE',
            'bitdust_forks/Bismuth/README.md',
            'bitdust_forks/CodernityDB/README',
            'bitdust_forks/entangled/AUTHORS',
            'bitdust_forks/entangled/COPYING',
            'bitdust_forks/entangled/README',
            'bitdust_forks/parallelp/README',
            'bitdust_forks/parallelp/pp/AUTHORS',
            'bitdust_forks/parallelp/pp/CHANGELOG',
            'bitdust_forks/parallelp/pp/COPYING',
            'bitdust_forks/parallelp/pp/PKG-INFO',
            'bitdust_forks/parallelp/pp/README',
            'bitdust_forks/txrestapi/LICENSE',
            'bitdust_forks/txrestapi/README.rst',
            'bitdust_forks/websocket/LICENSE',
        ],
    },

    install_requires=[
        'Twisted==23.8.0',
        'zope.interface',
        'cryptography',
        'pycryptodomex',
        'service_identity',
        'pyparsing',
        'appdirs',
        'psutil',
        'cffi',
        'six',
        'virtualenv',
    ],

    scripts=[
        'scripts/bitdust',
        'scripts/bitdust_worker',
    ],

)
