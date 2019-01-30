from selenium.webdriver.chrome.webdriver import WebDriver
import allure
import unittest


class TestCalculator(unittest.TestCase):

    @allure.title('1.1.	При загрузке калькулятора поле ввода данных по умолчанию содержит 0')
    @allure.severity(allure.severity_level.MINOR)
    def test_11(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
        with allure.step('Проверка наличия цифры "0" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '0'

    @allure.title('2.1.1.При нажатии на кнопку "1" в поле для ввода данных отображается цифра "1"')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_211_button1(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            one = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '1']")
        with allure.step('Клик по кнопке "1"'):
            one.click()
        with allure.step('Проверка наличия цифры "1" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '1'

    @allure.title('2.1.1.При нажатии на кнопку "2" в поле для ввода данных отображается цифра "2"')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_221_button2(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            two = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '2']")
        with allure.step('Клик по кнопке "2"'):
            two.click()
        with allure.step('Проверка наличия цифры "2" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '2'

    @allure.title('2.1.1.При нажатии на кнопку "3" в поле для ввода данных отображается цифра "3"')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_221_button3(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            three = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '3']")
        with allure.step('Клик по кнопке "3"'):
            three.click()
        with allure.step('Проверка наличия цифры "3" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '3'

    @allure.title('2.1.1.При нажатии на кнопку "4" в поле для ввода данных отображается цифра "4"')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_221_button4(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            four = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '4']")
        with allure.step('Клик по кнопке "4"'):
            four.click()
        with allure.step('Проверка наличия цифры "4" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '4'

    @allure.title('2.1.1.При нажатии на кнопку "5" в поле для ввода данных отображается цифра "5"')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_221_button5(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            five = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '5']")
        with allure.step('Клик по кнопке "5"'):
            five.click()
        with allure.step('Проверка наличия цифры "5" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '5'

    @allure.title('2.1.1.При нажатии на кнопку "6" в поле для ввода данных отображается цифра "6"')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_221_button6(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            six = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '6']")
        with allure.step('Клик по кнопке "6"'):
            six.click()
        with allure.step('Проверка наличия цифры "6" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '6'

    @allure.title('2.1.1.При нажатии на кнопку "7" в поле для ввода данных отображается цифра "7"')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_221_button7(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            seven = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '7']")
        with allure.step('Клик по кнопке "7"'):
            seven.click()
        with allure.step('Проверка наличия цифры "7" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '7'

    @allure.title('2.1.1.При нажатии на кнопку "8" в поле для ввода данных отображается цифра "8"')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_221_button8(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            eight = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '8']")
        with allure.step('Клик по кнопке "8"'):
            eight.click()
        with allure.step('Проверка наличия цифры "8" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '8'

    @allure.title('2.1.1.При нажатии на кнопку "9" в поле для ввода данных отображается цифра "9"')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_221_button9(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            nine = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '9']")
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Проверка наличия цифры "9" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '9'

    @allure.title('2.1.1.При нажатии на кнопку "0" в поле для ввода данных отображается цифра "0"')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_221_button0(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            zero = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '0']")
        with allure.step('Клик по кнопке "0"'):
            zero.click()
        with allure.step('Проверка наличия цифры "0" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '0'

    @allure.title('2.1.2.Каждая последующая введенная цифра располагается справа от предыдущих')
    @allure.severity(allure.severity_level.NORMAL)
    def test_212(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            three = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '3']")
            four = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '4']")
            seven = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '7']")
        with allure.step('Клик по кнопке "7"'):
            seven.click()
        with allure.step('Клик по кнопке "3"'):
            three.click()
        with allure.step('Клик по кнопке "4"'):
            four.click()
        with allure.step('Проверка наличия символов "734" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '734'

    @allure.title('2.2.1.Точка-разделитель десятичной дроби	добавляется справа от цифры в поле для ввода данных')
    @allure.severity(allure.severity_level.NORMAL)
    def test_221(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            eight = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '8']")
            nine = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '9']")
            dot = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '.']")
        with allure.step('Клик по кнопке "8"'):
            eight.click()
        with allure.step('Клик по кнопке "точка"'):
            dot.click()
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Проверка наличия десятичной дроби "8.9" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '8.9'

    @allure.title('2.2.2.В числе может быть только одна точка-разделитель десятичной дроби')
    @allure.severity(allure.severity_level.NORMAL)
    def test_222(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            one = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '1']")
            four = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '4']")
            five = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '5']")
            dot = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '.']")
        with allure.step('Клик по кнопке "1"'):
            one.click()
        with allure.step('Клик по кнопке "1"'):
            one.click()
        with allure.step('Клик по кнопке "точка"'):
            dot.click()
        with allure.step('Клик по кнопке "5"'):
            five.click()
        with allure.step('Клик по кнопке "4"'):
            four.click()
        with allure.step('Клик по кнопке "точка"'):
            dot.click()
        with allure.step('Клик по кнопке "1"'):
            one.click()
        with allure.step('Проверка наличия десятичной дроби "11.541" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '11.541'

    @allure.title('3.1.1.Операция сложения с целыми числами работает корректно')
    @allure.severity(allure.severity_level.NORMAL)
    def test_311(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            zero = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '0']")
            nine = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '9']")
            plus = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '+']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "0"'):
            zero.click()
        with allure.step('Клик по кнопке "+"'):
            plus.click()
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Проверка выполнения операции сложения'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '9'

    @allure.title('3.1.2.Операция сложения с десятичными дробями работает корректно')
    @allure.severity(allure.severity_level.NORMAL)
    def test_312(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            zero = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '0']")
            three = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '3']")
            five = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '5']")
            six = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '6']")
            nine = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '9']")
            dot = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '.']")
            plus = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '+']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "6"'):
            six.click()
        with allure.step('Клик по кнопке "3"'):
            three.click()
        with allure.step('Клик по кнопке "точка"'):
            dot.click()
        with allure.step('Клик по кнопке "5"'):
            five.click()
        with allure.step('Клик по кнопке "+"'):
            plus.click()
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Клик по кнопке "точка"'):
            dot.click()
        with allure.step('Клик по кнопке "0"'):
            zero.click()
        with allure.step('Клик по кнопке "3"'):
            three.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Проверка выполнения операции сложения'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '72.53'

    @allure.title('3.2.1.Операция вычитания с целыми числами работает корректно')
    @allure.severity(allure.severity_level.NORMAL)
    def test_321(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            one = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '1']")
            two = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '2']")
            nine = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '9']")
            minus = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '-']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "1"'):
            one.click()
        with allure.step('Клик по кнопке "-"'):
            minus.click()
        with allure.step('Клик по кнопке "2"'):
            two.click()
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Клик по кнопке "2"'):
            two.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Проверка выполнения операции вычитания'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '-291'

    @allure.title('3.2.2.Операция вычитания с десятичными дробями работает корректно')
    @allure.severity(allure.severity_level.NORMAL)
    def test_322(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            zero = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '0']")
            one = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '1']")
            three = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '3']")
            five = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '5']")
            nine = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '9']")
            dot = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '.']")
            minus = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '-']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Клик по кнопке "3"'):
            three.click()
        with allure.step('Клик по кнопке "точка"'):
            dot.click()
        with allure.step('Клик по кнопке "0"'):
            zero.click()
        with allure.step('Клик по кнопке "5"'):
            five.click()
        with allure.step('Клик по кнопке "-"'):
            minus.click()
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Клик по кнопке "1"'):
            one.click()
        with allure.step('Клик по кнопке "точка"'):
            dot.click()
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Клик по кнопке "3"'):
            three.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Проверка выполнения операции вычитания'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '1.057'

    @allure.title('3.3.1.Операция умножения с целыми числами работает корректно')
    @allure.severity(allure.severity_level.NORMAL)
    def test_331(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            five = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '5']")
            nine = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '9']")
            multiplier = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = 'x']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "5"'):
            five.click()
        with allure.step('Клик по кнопке "X"'):
            multiplier.click()
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Проверка выполнения операции умножения'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '45'

    @allure.title('3.3.2.Операция умножения с десятичными дробями работает корректно')
    @allure.severity(allure.severity_level.NORMAL)
    def test_332(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            three = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '3']")
            five = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '5']")
            nine = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '9']")
            zero = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '0']")
            dot = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '.']")
            multiplier = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = 'x']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "3"'):
            three.click()
        with allure.step('Клик по кнопке "3"'):
            three.click()
        with allure.step('Клик по кнопке "точка"'):
            dot.click()
        with allure.step('Клик по кнопке "5"'):
            five.click()
        with allure.step('Клик по кнопке "x"'):
            multiplier.click()
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Клик по кнопке "точка"'):
            dot.click()
        with allure.step('Клик по кнопке "0"'):
            zero.click()
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Проверка выполнения операции вычитания'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '304.515'

    @allure.title('3.4.1.Операция деления с целыми числами работает корректно')
    @allure.severity(allure.severity_level.NORMAL)
    def test_341(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            one = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '1']")
            three = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '3']")
            eight = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '8']")
            divider = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '/']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "8"'):
            eight.click()
        with allure.step('Клик по кнопке "1"'):
            one.click()
        with allure.step('Клик по кнопке "/"'):
            divider.click()
        with allure.step('Клик по кнопке "3"'):
            three.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Проверка выполнения операции деления'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '27'

    @allure.title('3.4.2.Операция деления с десятичными дробями работает корректно')
    @allure.severity(allure.severity_level.NORMAL)
    def test_342(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            one = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '1']")
            two = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '2']")
            four = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '4']")
            five = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '5']")
            dot = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '.']")
            divider = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '/']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "2"'):
            two.click()
        with allure.step('Клик по кнопке "1"'):
            one.click()
        with allure.step('Клик по кнопке "точка"'):
            dot.click()
        with allure.step('Клик по кнопке "4"'):
            four.click()
        with allure.step('Клик по кнопке "5"'):
            five.click()
        with allure.step('Клик по кнопке "/"'):
            divider.click()
        with allure.step('Клик по кнопке "5"'):
            five.click()
        with allure.step('Клик по кнопке "точка"'):
            dot.click()
        with allure.step('Клик по кнопке "2"'):
            two.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Проверка выполнения операции вычитания'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '4.125'

    @allure.title('3.4.3.Деление на О')
    @allure.severity(allure.severity_level.NORMAL)
    def test_343(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            eight = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '8']")
            zero = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '0']")
            divider = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '/']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "8"'):
            eight.click()
        with allure.step('Клик по кнопке "/"'):
            divider.click()
        with allure.step('Клик по кнопке "0"'):
            zero.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Проверка выполнения операции деления'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == 'Error'

    @allure.title('3.5.1.Кнопка "С" очищает поле для ввода данных, там отображается ноль')
    @allure.severity(allure.severity_level.NORMAL)
    def test_351(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            one = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '1']")
            two = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '2']")
            five = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '5']")
            dot = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '.']")
            c = driver.find_element_by_xpath("//ul[@class = 'operations']/li[text() = 'C']")
        with allure.step('Клик по кнопке "2"'):
            two.click()
        with allure.step('Клик по кнопке "1"'):
            one.click()
        with allure.step('Клик по кнопке "точка"'):
            dot.click()
        with allure.step('Клик по кнопке "5"'):
            five.click()
        with allure.step('Клик по кнопке "C"'):
            c.click()
        with allure.step('Проверка наличия "0" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '0'

    @allure.title('3.5.2.При нажатии кнопка "С" полностью отменяет операцию')
    @allure.severity(allure.severity_level.NORMAL)
    def test_352(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            one = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '1']")
            two = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '2']")
            five = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '5']")
            seven = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '7']")
            plus = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '+']")
            c = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = 'C']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "2"'):
            two.click()
        with allure.step('Клик по кнопке "1"'):
            one.click()
        with allure.step('Клик по кнопке "+"'):
            plus.click()
        with allure.step('Клик по кнопке "5"'):
            five.click()
        with allure.step('Клик по кнопке "C"'):
            c.click()
        with allure.step('Клик по кнопке "7"'):
            seven.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Кнопка "С" стёрла содержимое и регистра индикации, и рабочего регистра, ожидаем число "7"'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '7'

    @allure.title('3.6.1.Кнопка "АС" очищает поле для ввода данных, там отображается ноль')
    @allure.severity(allure.severity_level.NORMAL)
    def test_361(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            two = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '2']")
            seven = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '5']")
            nine = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '.']")
            ac = driver.find_element_by_xpath("//ul[@class = 'operations']/li[text() = 'AC']")
        with allure.step('Клик по кнопке "2"'):
            two.click()
        with allure.step('Клик по кнопке "9"'):
            nine.click()
        with allure.step('Клик по кнопке "7"'):
            seven.click()
        with allure.step('Клик по кнопке "AC"'):
            ac.click()
        with allure.step('Проверка наличия "0" в поле ввода данных'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '0'

    @allure.title('3.6.2.При нажатии кнопка "AС" удаляет только последнее введённое число')
    @allure.severity(allure.severity_level.NORMAL)
    def test_362(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            one = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '1']")
            two = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '2']")
            five = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '5']")
            seven = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '7']")
            plus = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '+']")
            ac = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = 'C']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "2"'):
            two.click()
        with allure.step('Клик по кнопке "1"'):
            one.click()
        with allure.step('Клик по кнопке "+"'):
            plus.click()
        with allure.step('Клик по кнопке "5"'):
            five.click()
        with allure.step('Клик по кнопке "AC"'):
            ac.click()
        with allure.step('Клик по кнопке "7"'):
            seven.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Кнопка "AС" обнулила только регистр индикации, ожидаем число "28"'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '28'

    @allure.title('3.7.Операции сложения, вычитания, деления и умножения визуально никак не отображаются')
    @allure.severity(allure.severity_level.NORMAL)
    def test_37(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            plus = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '+']")
            minus = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '-']")
            multiplier = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = 'x']")
            divider = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '/']")
        with allure.step('Клик по кнопке "+"'):
            plus.click()
        with allure.step('Клик по кнопке "-"'):
            minus.click()
        with allure.step('Клик по кнопке "X"'):
            multiplier.click()
        with allure.step('Клик по кнопке "/"'):
            divider.click()
        with allure.step('В поле ввода пусто'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == ''

    @allure.title('4.1.	При нажатии на кнопку «равно» без предварительно введённой операции сложения, вычитания,'
                  'деления или умножения ничего не происходит')
    @allure.severity(allure.severity_level.NORMAL)
    def test_41(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            seven = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '7']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "7"'):
            seven.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('В поле ввода осталось чисто "7"'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '7'

    @allure.title('4.2.	При повторном нажатии на кнопку «равно» после выполнения операции повторяется предыдущая '
                  'операция с отображаемым результатом в качестве первого операнда и вторым операндом из предыдущего '
                  'действия в качестве второго')
    @allure.severity(allure.severity_level.NORMAL)
    def test_42(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            four = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '4']")
            seven = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '7']")
            plus = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '+']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "7"'):
            seven.click()
        with allure.step('Клик по кнопке "+"'):
            plus.click()
        with allure.step('Клик по кнопке "4"'):
            four.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('В поле ввода чисто "15"'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '15'

    @allure.title('4.3.	Если последовательно ввести несколько операций – учитывается только последняя')
    @allure.severity(allure.severity_level.NORMAL)
    def test_43(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            four = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '4']")
            seven = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '7']")
            plus = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '+']")
            minus = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '-']")
            multiplier = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = 'x']")
            divider = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '/']")
            equal = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '=']")
        with allure.step('Клик по кнопке "7"'):
            seven.click()
        with allure.step('Клик по кнопке "+"'):
            plus.click()
        with allure.step('Клик по кнопке "-"'):
            minus.click()
        with allure.step('Клик по кнопке "/"'):
            divider.click()
        with allure.step('Клик по кнопке "X"'):
            multiplier.click()
        with allure.step('Клик по кнопке "4"'):
            four.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('Клик по кнопке "="'):
            equal.click()
        with allure.step('В поле ввода чисто "28"'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '28'

    @allure.title('4.4.Отрицательные числа нельзя ввести, но они могут возникнуть в результате операций')
    @allure.severity(allure.severity_level.NORMAL)
    def test_44(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            four = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '4']")
            minus = driver.find_element_by_xpath("// ul[ @class = 'operations'] / li[text() = '-']")
        with allure.step('Клик по кнопке "-"'):
            minus.click()
        with allure.step('Клик по кнопке "4"'):
            four.click()
        with allure.step('В поле ввода чисто "4"'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '4'

    @allure.title('4.5.	Ввести 20тизначное число')
    @allure.severity(allure.severity_level.NORMAL)
    def test_45(self):
        with allure.step('Переход на веб-страницу http://qa-test.klika-tech.com'):
            driver = WebDriver(executable_path='C://Selenium//chromedriver.exe')
            driver.get('http://qa-test.klika-tech.com')
            five = driver.find_element_by_xpath("//ul[@class = 'digits']/li[text() = '5']")
        with allure.step('Клик по кнопке "5" 20 раз'):
            i = 1
            while i <= 20:
                five.click()
                i = i + 1
        with allure.step('В поле ввода чисто "55555555555555555555"'):
            displayresult = driver.find_element_by_xpath("// div[ @class = 'display']")
            assert displayresult.text == '55555555555555555555'
