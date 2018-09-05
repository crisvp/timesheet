#!/usr/bin/env python

import os
import sqlite3
from datetime import datetime
from . import util


class TimesheetState(object):
    def __init__(self, filename):
        self.filename = filename
        self.conn = sqlite3.connect(self.filename,
                                    isolation_level=None)
        c = self.conn.cursor()
        c.execute('''
                  CREATE TABLE IF NOT EXISTS timer
                    (start_time TEXT, message TEXT)
                  ''')

    # Set start of timer and its message.
    def Set(self, start_time, message=''):
        assert isinstance(start_time, datetime)
        assert isinstance(message, str)

        c = self.conn.cursor()
        try:
            c.execute('BEGIN')
            c.execute('DELETE FROM timer')
            c.execute('INSERT INTO TIMER (start_time, message) VALUES '
                      '(?, ?)', (util.date2string(start_time), message))
            c.execute('COMMIT')
        except Exception:
            c.execute('ROLLBACK')
            raise
        finally:
            c.close()

    # Returns the (datetime, string message) if the time is set or None.
    def Get(self):
        if not os.path.exists(self.filename):
            return None

        c = self.conn.cursor()
        c.execute('SELECT start_time, message FROM timer')
        res = c.fetchone()
        c.close()

        if res is not None:
            return (util.string2date(res[0]), res[1])

        return None

    def Clear(self):
        c = self.conn.cursor()
        c.execute('DELETE FROM timer')
        c.close()
