# -*- coding:utf-8 -*-

import six


class AsBoolConverter(object):
    def __init__(self, true_values, false_values):
        self.true_values = true_values
        self.false_values = false_values

    def __call__(self, ss):
        if not isinstance(ss, six.string_types):
            return bool(ss)

        s = ss.strip().lower()
        if (s not in self.true_values) and (s not in self.false_values):
            raise ValueError(ss)

        return s in self.true_values
