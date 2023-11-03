import pytest
from laba1.NightOne import *

#! Тесты, подписанные как xfail, не обязательно должны возвращать Pass

# Положительный тест
@pytest.mark.parametrize('shift', [pytest.param((1, 0, 2)),
                                    pytest.param((3, 4, 4)),
                                    (-1, 1, 3),
                                    (-1, 1, 1),
                                    pytest.param((14, 34, 10), marks=pytest.mark.xfail(reason="Cirles aren't intesected")),
                                    pytest.param((5, 90, 40), marks=pytest.mark.xfail(reason="Cirles aren't intesected")),
                                    pytest.param((6, 4, 3), marks=pytest.mark.xfail(reason="Cirles aren't intesected"))])
def test_intersection(shape, shift):
     shape_1 = Circle(*shift)
     assert shape.intersection(shape_1) == "Yes"

# Негативные тесты
@pytest.mark.parametrize("shift", [(10, 10, 10), (5, 90, 40), (6, 4, 3), (1, 1, 2), (-4, 3, 9)])
def test_intersectedGiveFalse(shape, shift):
     shape_1 = Circle(*shift)
     assert shape.intersection(shape_1) == "No"

def test_getters(shape):
     assert shape.getRadius() == 1
     assert shape.getShiftByAxisX() == 1
     assert shape.getShiftByAxisY() == 1

# Базовый тест для 2го задания
@pytest.mark.task_2
@pytest.mark.parametrize('number', [2240,
                                    475,
                                    pytest.param(999, marks=pytest.mark.xfail),
                                    pytest.param(0, marks=pytest.mark.xfail)])
def test_checkIsEvenOrNotInSumOfNumbers(number):
     assert checkIsEvenOrNotInSumOfNumbers(number) == "even"

# Базовый тест для 3го задания
@pytest.mark.task_3
@pytest.mark.parametrize('number', [2546,
                                    3475,
                                    pytest.param(4, marks=pytest.mark.xfail),
                                    pytest.param(0, marks=pytest.mark.xfail)])
def test_checkIsAmountOfDividersAreEvenOrNot(number):
     assert checkIsAmountOfDividersAreEvenOrNot(number) == "even"