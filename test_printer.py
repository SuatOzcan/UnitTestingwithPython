from unittest import TestCase
from printer import Printer, PrinterError

class TestPrinter(TestCase):
    def setUp(self): #This will run before each defined test below.
        self.printer = Printer(pages_per_s=2.0, capacity= 300)

    # @classmethod
    # def setUpClass(cls): #This will create only one printer, and the tests below will use the same printer.
    #     cls.printer = Printer(pages_per_s=2.0, capacity= 300)

    def test_print_within_capacity(self):
        #printer = Printer(pages_per_s=2.0, capacity=300)
        self.printer.print(25)

    def test_print_outside_of_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(400)
    
    def test_print_exact_capcity(self):
        #self.printer.print(300)
        self.printer.print(self.printer._capacity)
    
    def test_printer_speed(self):
        pages = 10
        expected = "The printer printed 10 pages in 5.00 seconds."
        result = self.printer.print(pages)
        self.assertEqual(result, expected)
    
    def test_speed_always_returns_two_decimals(self):
        fast_printer = Printer(pages_per_s=3.0, capacity=300)
        pages = 11
        expected = "The printer printed 11 pages in 3.67 seconds."
        #This is important because what Python actually returns from the 11/3 division is 3,66666.
        result = fast_printer.print(pages)
        self.assertEqual(result, expected)
    
    def test_multiple_printer_runs(self):
        self.printer.print(20)
        self.printer.print(40)
        self.printer.print(240)
    
    def test_multiple_printer_runs_end_with_error(self):
        self.printer.print(20)
        self.printer.print(40)
        self.printer.print(240)
        with self.assertRaises(PrinterError):
            self.printer.print(400)