# -*- coding: utf-8 -*-

"""
Use object-oriented Python to model a public library (w/ three classes: Library,
Shelf, & Book).

The library should be aware of a number of shelves. Each shelf should know what
books it contains. Make the book object have "enshelf" and "unshelf" methods
that control what shelf the book is sitting on. The library should have a method
to report all books it contains. Note: this should *not* be a Django (or any
other) app - just a single file with three classes (plus commands at the bottom
showing it works) is all that is needed. In addition to pushing this python file
to your Github account, please also setup a http://repl.it/languages/Python (so
it runs there) and enter the saved URL here.
"""

from __future__ import print_function
import json


class Library(object):
    """Library class that identifies the name of the library. Contains a method
    to report all books contained"""

    def __init__(self, library):
        """library is the name of the Library Branch"""
        self.library = library

    def list_books(library):
        """pass a library and return a list of books at the library sorted
        by what shelf they live on"""

        pass


class Shelf(Library):

    def __init__(self, shelf, library):
        super(Shelf, self).__init__(library)
        self.shelf = shelf


class Book(Shelf, Library):
    """Name of the book. Enshelf method allows the book to be placed on a
    particular shelf. Unshelf checks the book out."""

    def __init__(self, book, shelf, library):
        super(Book, self).__init__(shelf, library)
        self.book = book

    def enshelf(shelf):
        pass

    def unshelf():
        pass



sample_data = json.loads('[{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"fermentum risus,"},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"eget massa."},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"in faucibus orci"},{"Library":"Greenwood","Shelf":"Fiction","Book":"eu dui."},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"Mauris molestie pharetra nibh. Aliquam"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"egestas"},{"Library":"Ballard","Shelf":"Non-Fiction","Book":"vitae risus."},{"Library":"Ballard","Shelf":"Non-Fiction","Book":"orci quis"},{"Library":"Ballard","Shelf":"Self-help","Book":"nisi"},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"dis parturient montes, nascetur"},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"Aenean euismod mauris eu elit."},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"dolor. Nulla semper tellus id"},{"Library":"Greenwood","Shelf":"Checked-out","Book":"arcu. Morbi sit"},{"Library":"Greenwood","Shelf":"Checked-out","Book":"mi eleifend egestas."},{"Library":"Greenwood","Shelf":"Checked-out","Book":"eu arcu. Morbi sit"},{"Library":"Ballard","Shelf":"Checked-out","Book":"Integer eu"},{"Library":"Ballard","Shelf":"Fiction","Book":"interdum. Nunc"},{"Library":"Ballard","Shelf":"Fiction","Book":"faucibus ut, nulla."},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"cubilia Curae Donec tincidunt. Donec"},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"rutrum magna."},{"Library":"Downtown Seattle","Shelf":"Non-Fiction","Book":"a, aliquet vel, vulputate"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"lectus convallis"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"amet ultricies sem magna nec"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"at pretium aliquet,"},{"Library":"Ballard","Shelf":"Self-help","Book":"orci. Ut"},{"Library":"Ballard","Shelf":"Self-help","Book":"velit. Sed malesuada augue ut"},{"Library":"Ballard","Shelf":"Self-help","Book":"erat, eget tincidunt"},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"rhoncus id, mollis nec, cursus"},{"Library":"Downtown Seattle","Shelf":"Checked-out","Book":"eros turpis non enim."},{"Library":"Downtown Seattle","Shelf":"Checked-out","Book":"placerat,"},{"Library":"Greenwood","Shelf":"Checked-out","Book":"quam a felis ullamcorper viverra."},{"Library":"Greenwood","Shelf":"Checked-out","Book":"congue, elit sed consequat"},{"Library":"Greenwood","Shelf":"Fiction","Book":"id, libero. Donec"},{"Library":"Ballard","Shelf":"Fiction","Book":"massa. Integer vitae nibh."},{"Library":"Ballard","Shelf":"Fiction","Book":"aliquam eros turpis"},{"Library":"Ballard","Shelf":"Fiction","Book":"dis"},{"Library":"Downtown Seattle","Shelf":"Non-Fiction","Book":"eu lacus."},{"Library":"Downtown Seattle","Shelf":"Non-Fiction","Book":"risus."},{"Library":"Downtown Seattle","Shelf":"Non-Fiction","Book":"cursus"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"Etiam"},{"Library":"Greenwood","Shelf":"Self-help","Book":"vitae purus gravida sagittis."},{"Library":"Greenwood","Shelf":"Self-help","Book":"pede et risus."},{"Library":"Ballard","Shelf":"Self-help","Book":"eu nulla at sem molestie"},{"Library":"Ballard","Shelf":"Self-help","Book":"augue ut lacus. Nulla tincidunt,"},{"Library":"Ballard","Shelf":"Checked-out","Book":"arcu."},{"Library":"Downtown Seattle","Shelf":"Checked-out","Book":"pretium neque. Morbi quis"},{"Library":"Downtown Seattle","Shelf":"Checked-out","Book":"risus varius orci, in consequat"},{"Library":"Downtown Seattle","Shelf":"Checked-out","Book":"ut eros"},{"Library":"Greenwood","Shelf":"Fiction","Book":"egestas. Aliquam nec enim. Nunc"},{"Library":"Greenwood","Shelf":"Fiction","Book":"ultrices"},{"Library":"Greenwood","Shelf":"Fiction","Book":"Donec consectetuer mauris id sapien."},{"Library":"Ballard","Shelf":"Fiction","Book":"odio. Etiam ligula tortor, dictum"},{"Library":"Ballard","Shelf":"Non-Fiction","Book":"tincidunt. Donec vitae"},{"Library":"Ballard","Shelf":"Non-Fiction","Book":"montes,"},{"Library":"Downtown Seattle","Shelf":"Non-Fiction","Book":"faucibus ut, nulla. Cras eu"},{"Library":"Downtown Seattle","Shelf":"Non-Fiction","Book":"Aliquam nec"},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"Quisque ac libero"},{"Library":"Greenwood","Shelf":"Self-help","Book":"laoreet posuere, enim nisl elementum"},{"Library":"Greenwood","Shelf":"Self-help","Book":"vestibulum nec, euismod in,"},{"Library":"Greenwood","Shelf":"Self-help","Book":"consectetuer, cursus et,"},{"Library":"Ballard","Shelf":"Checked-out","Book":"est, mollis"},{"Library":"Ballard","Shelf":"Checked-out","Book":"Aenean massa. Integer"},{"Library":"Ballard","Shelf":"Checked-out","Book":"nec ligula consectetuer rhoncus."},{"Library":"Downtown Seattle","Shelf":"Checked-out","Book":"arcu vel quam dignissim pharetra."},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"tristique"},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"Donec consectetuer"},{"Library":"Greenwood","Shelf":"Fiction","Book":"lorem, sit amet ultricies sem"},{"Library":"Greenwood","Shelf":"Fiction","Book":"Quisque"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"at lacus. Quisque purus sapien,"},{"Library":"Ballard","Shelf":"Non-Fiction","Book":"tellus sem mollis"},{"Library":"Ballard","Shelf":"Non-Fiction","Book":"amet,"},{"Library":"Ballard","Shelf":"Non-Fiction","Book":"Quisque ac libero nec ligula"},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"ullamcorper."},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"laoreet lectus"},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"ut aliquam iaculis,"},{"Library":"Greenwood","Shelf":"Self-help","Book":"sociosqu"},{"Library":"Greenwood","Shelf":"Checked-out","Book":"justo faucibus lectus,"},{"Library":"Greenwood","Shelf":"Checked-out","Book":"mi. Aliquam"},{"Library":"Ballard","Shelf":"Checked-out","Book":"Vivamus non lorem vitae"},{"Library":"Ballard","Shelf":"Checked-out","Book":"ante bibendum ullamcorper."},{"Library":"Ballard","Shelf":"Fiction","Book":"eget laoreet posuere, enim"},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"id, ante."},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"dictum magna. Ut"},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"bibendum ullamcorper. Duis cursus, diam"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"pharetra. Nam ac"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"eu dui. Cum"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"dictum eu, placerat eget,"},{"Library":"Ballard","Shelf":"Non-Fiction","Book":"mi eleifend egestas. Sed pharetra,"},{"Library":"Ballard","Shelf":"Self-help","Book":"ultricies adipiscing, enim"},{"Library":"Ballard","Shelf":"Self-help","Book":"neque. Sed eget"},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"sagittis semper. Nam tempor"},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"posuere vulputate, lacus."},{"Library":"Downtown Seattle","Shelf":"Checked-out","Book":"sollicitudin a, malesuada id, erat."},{"Library":"Greenwood","Shelf":"Checked-out","Book":"Donec luctus aliquet odio."},{"Library":"Greenwood","Shelf":"Checked-out","Book":"sem elit,"},{"Library":"Greenwood","Shelf":"Checked-out","Book":"nibh lacinia"},{"Library":"Ballard","Shelf":"Fiction","Book":"Duis sit amet"},{"Library":"Ballard","Shelf":"Fiction","Book":"Pellentesque habitant morbi tristique"},{"Library":"Ballard","Shelf":"Fiction","Book":"montes, nascetur"},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"dolor quam, elementum"}]')


libraries = []
shelves = []
books = []

for i in range(len(sample_data)):
    libraries.append(sample_data[i]['Library'])
    shelves.append(sample_data[i]['Shelf'])
    books.append(sample_data[i]['Book'])


libraries = set(libraries)
shelves = set(shelves)

testbook1 = Book('test book', 'test shelf', 'test library')

