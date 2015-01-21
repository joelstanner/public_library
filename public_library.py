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

https://github.com/poolbath1/public_library
http://repl.it/87c/4
"""

import json, random


class Library(object):
    """Library class that identifies the name of the library. Contains a method
    to report all books contained"""

    def __init__(self, library):
        """library is the name of the Library Branch"""
        self.library = library

    def list_books(self):
        """pass a library and return a list of books at that library"""
        library_books = []
        for book in books:
            if book.library == self.library:
                library_books.append((book.book, book.shelf))
        return library_books


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

    def enshelf(self, shelf):
        """enshelven the book unto a new shelf"""
        self.shelf = shelf

    def unshelf(self):
        """unshelf checks out the book"""
        self.shelf = 'Checked-out'
        return


# TESTS:

sample_data = json.loads('[{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"fermentum risus,"},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"eget massa."},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"in faucibus orci"},{"Library":"Greenwood","Shelf":"Fiction","Book":"eu dui."},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"Mauris molestie pharetra nibh. Aliquam"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"egestas"},{"Library":"Ballard","Shelf":"Non-Fiction","Book":"vitae risus."},{"Library":"Ballard","Shelf":"Non-Fiction","Book":"orci quis"},{"Library":"Ballard","Shelf":"Self-help","Book":"nisi"},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"dis parturient montes, nascetur"},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"Aenean euismod mauris eu elit."},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"dolor. Nulla semper tellus id"},{"Library":"Greenwood","Shelf":"Checked-out","Book":"arcu. Morbi sit"},{"Library":"Greenwood","Shelf":"Checked-out","Book":"mi eleifend egestas."},{"Library":"Greenwood","Shelf":"Checked-out","Book":"eu arcu. Morbi sit"},{"Library":"Ballard","Shelf":"Checked-out","Book":"Integer eu"},{"Library":"Ballard","Shelf":"Fiction","Book":"interdum. Nunc"},{"Library":"Ballard","Shelf":"Fiction","Book":"faucibus ut, nulla."},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"cubilia Curae Donec tincidunt. Donec"},{"Library":"Downtown Seattle","Shelf":"Fiction","Book":"rutrum magna."},{"Library":"Downtown Seattle","Shelf":"Non-Fiction","Book":"a, aliquet vel, vulputate"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"lectus convallis"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"amet ultricies sem magna nec"},{"Library":"Greenwood","Shelf":"Non-Fiction","Book":"at pretium aliquet,"},{"Library":"Ballard","Shelf":"Self-help","Book":"orci. Ut"},{"Library":"Ballard","Shelf":"Self-help","Book":"velit. Sed malesuada augue ut"},{"Library":"Ballard","Shelf":"Self-help","Book":"erat, eget tincidunt"},{"Library":"Downtown Seattle","Shelf":"Self-help","Book":"rhoncus id, mollis nec, cursus"},{"Library":"Downtown Seattle","Shelf":"Checked-out","Book":"eros turpis non enim."}]')

                   # Parse some sample data for tests
libraries = []     # This will be a unique set of libraries from the sample data
books = []         # --A list of new Book objects. For testing we'll populate
                   # the list from a JSON blob.

for i in range(len(sample_data)):
    books.append(Book(
        sample_data[i]['Book'],
        sample_data[i]['Shelf'],
        sample_data[i]['Library']))

    libraries.append(sample_data[i]['Library'])

# Make a list of Library objects from the set of unique libraries
libraries = [Library(library) for library in set(libraries)]

# call the list_books Library method to see what books are in the library:
template = "{0:50}{1:15}"
for lib in range(len(libraries)):
    print (libraries[lib].library + "'s book list\n").upper()
    print template.format("BOOK TITLE", "SHELF\n")
    for book, shelf in sorted(libraries[lib].list_books()):
        print template.format(str(book), str(shelf))
    print "\n-------\n\n"

# pick a random book, unshelf it, then enshelf it

rnd_book = books[random.randint(0, len(sample_data))]
rnd_book.unshelf()
print rnd_book.book + "\t", rnd_book.shelf, "   should be 'Checked-out'"
rnd_book.enshelf('Fiction')
print rnd_book.book + "\t", rnd_book.shelf, "       should be 'Fiction'"
