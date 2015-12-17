#!/usr/bin/env python
import datetime
start = datetime.datetime(1814, 5, 17, 13, 37, 14)
stop = datetime.datetime(2015, 9, 17, 17, 15)

print int((stop-start).total_seconds())