from akagi.iterators import CSVIterator, BinaryIterator

from enum import Enum


class FileFormat(Enum):
    CSV = 1
    BINARY = 2


class Iterator(object):

    @classmethod
    def get_iterator_class(cls, file_format):
        if file_format in [FileFormat.CSV, 'csv']:
            return CSVIterator
        elif file_format in [FileFormat.BINARY, 'binary']:
            return BinaryIterator
        else:
            raise Exception("Unsupported file format %(file_format)s." % locals())
