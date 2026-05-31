import unittest

from MATA020TESTCASE import MATA020

suite = unittest.TestSuite()

suite.addTest(MATA020('test_MATA020_CT001_Inclusao'))
suite.addTest(MATA020('test_MATA020_CT002_Visualizacao'))
suite.addTest(MATA020('test_MATA020_CT003_Alteracao'))
suite.addTest(MATA020('test_MATA020_CT004_Exclusao'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
