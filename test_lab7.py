import book
import user
import library
import pytest 

@pytest.mark.unit
def test_borrow_book():

    book1 = book.Book('Orgullo y prejuicio','Tenoch Moreno', 2026,'ISBN001')
    assert book1.title == 'Orgullo y prejuicio'
    book1.borrow()
    assert book1.borrowed == True




@pytest.mark.unit
def test_borrow_x2_book():

    book1 = book.Book('Orgullo y prejuicio','Tenoch Moreno', '2026','ISBN001')
    assert book1.title == 'Orgullo y prejuicio'
    book1.borrow()
    assert book1.borrowed == True

    with pytest.raises(ValueError,match="The book is already borrowed"):
        book1.borrow()




@pytest.mark.unit
def test_return_book():

    book1 = book.Book('Orgullo y prejuicio','Tenoch Moreno', '2026','ISBN001')
    assert book1.title == 'Orgullo y prejuicio'
    book1.borrow()
    assert book1.borrowed == True
    book1.return_book()
    assert book1.borrowed == False




@pytest.mark.unit
def test_borrow_and_try_except():#la Prueba tiene que fallar po poner el try except en el book.py

    book1 = book.Book('Orgullo y prejuicio','Tenoch Moreno', '2026','ISBN001')
    assert book1.title == 'Orgullo y prejuicio'
    book1.borrow()
    assert book1.borrowed == True

    with pytest.raises(ValueError,match="The book is already borrowed"):
        book1.borrow()




@pytest.fixture
def lib_ini():
    lib=library.Library()
    book2 = book.Book('Orgullo y prejuicio','Tenoch Moreno', 2026,'ISBN001')
    lib.add_book(book2)
    Tenoch = user.User('Tenoch', 'ID001')
    lib.add_user(Tenoch)
    return lib

@pytest.mark.system
def test_library_init(lib_ini):
    lib = lib_ini
    lib.borrow_book('ID001', 'ISBN001')

    assert lib.books[0].borrowed == True



@pytest.mark.wip
def test_library_init_unexisted_ID(lib_ini):
    lib = lib_ini
    with pytest.raises(ValueError, match="User not found"):
        lib.borrow_book('ID001546', 'ISBN001')

    
    
    
 
