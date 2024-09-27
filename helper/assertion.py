def assert_equal(arg1, arg2):
    assert arg1 == arg2, str(arg1) + ' is not equal to ' + str(arg2)


def assert_not_equal(arg1, arg2):
    assert arg1 != arg2, str(arg1) + ' is equal to ' + str(arg2)


def assert_include(array, arg):
    assert arg in array, str(array) + ' not include ' + str(arg)


def assert_include_array(array1, array2):
    assert all(elem in array1 for elem in array2)


def assert_include_string(string, arg):
    assert arg in string, str(string) + ' not include ' + str(arg)


def assert_not_include(array, arg):
    assert arg not in array, str(array) + ' not include ' + str(arg)


def assert_equal_array(array1, array2):
    assert array1 == array2, '\n' + str(array1) + '\n' + str(array2)


def assert_equal_array_ignore_order(array1, array2):
    assert sorted(array1) == sorted(array2), '\n' + str(array1) + '\n' + str(array2)


def assert_sorted(array):
    assert array == sorted(array), '\n' + str(array) + '\n' + str(sorted(array))


def assert_reverse_sorted(array):
    assert array == sorted(array, reverse=True), '\n' + str(array) + '\n' + str(sorted(array, reverse=True))


def assert_empty(array):
    assert len(array) == 0


def assert_not_empty(array):
    assert len(array) != 0


def assert_at_least(arg1, arg2):
    assert len(arg1) > arg2, str(len(arg1)) + ' at least ' + str(arg2)


def assert_at_most(arg1, arg2):
    assert len(arg1) <= arg2, str(len(arg1)) + ' at least ' + str(arg2)


def assert_has_key(obj, key):
    assert key in obj, str(obj) + ' include ' + str(key)


def assert_has_not_key(obj, key):
    assert key not in obj, str(obj) + ' include ' + str(key)


def assert_equal_except(arg1, arg2, except_key):
    arg1[except_key] = None
    arg2[except_key] = None
    assert arg1 == arg2, '\n' + str(arg1) + '\n' + str(arg2)


def assert_between_values_all_elements_of_array(min, max, array):
    for element in array:
        assert min < int(element) < max, element + ' is not between ' + min + ' and ' + max


def assert_products_not_empty(response):
    assert len(response['products']) != 0, 'There is no products'
