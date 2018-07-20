#!/usr/bin/env python3
"""
   Download Jenkins plugins
"""

import os
import sys
import logging
import logging.handlers
import urllib
import urllib.request

PLUGINS = ['git 3.9.1']

JENKINS_URL = 'https://updates.jenkins-ci.org/download/plugins/'

if __name__ == "__main__":
    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.DEBUG)

    SYSLOG_HANDLER = logging.handlers.SysLogHandler(address='/dev/log')
    SYSLOG_FORMATTER = logging.Formatter(
        os.path.abspath(__file__) + ': %(message)s')
    SYSLOG_HANDLER.setFormatter(SYSLOG_FORMATTER)
    LOG.addHandler(SYSLOG_HANDLER)

    CONSOLE_HANDLER = logging.StreamHandler()
    CONSOLE_FORMATTER = logging.Formatter(
        '%(asctime)s ' + os.path.abspath(__file__) + ': %(message)s')
    CONSOLE_HANDLER.setFormatter(CONSOLE_FORMATTER)
    LOG.addHandler(CONSOLE_HANDLER)

    PLUGINS = [i.split() for i in PLUGINS]
    PLUGINS = {name: version for (name, version) in PLUGINS}

    LOG.debug('Starting script - install Jenkins plugins')

    try:
        for name, version in PLUGINS.items():
            link = JENKINS_URL + name + "/" + version + "/" + name + ".hpi"
            filename = "plugins/" + name + ".hpi"

            try:
                os.remove(filename)
            except FileNotFoundError:
                LOG.debug('File not exists: %s', filename)

            try:
                LOG.debug('%s', link)
                urllib.request.urlretrieve(link, filename)
            except urllib.error.HTTPError:
                LOG.debug('ERROR: PLUGIN DO NOT EXISTS: %s - %s', name, version)
                sys.exit(3)
    except KeyboardInterrupt:
        LOG.debug('Bye, exit by user')
    finally:
        LOG.debug('End of script')
