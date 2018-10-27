import unittest
import testcode
from HtmlTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport

# 单元测试用于核实函数的某个方面没有问题；
# 测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。
# 良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。 
# 全覆盖式测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。
# 对于大型项目，要实现全覆盖可能很难。
# 通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。




class TestFunc(unittest.TestCase):
    def setUp(self):
        print("每个TestCase都会先先执行一遍setUp")
    
    def tearDown(self):
        print("每个TestCase结束后都会执行一遍tearDown")
    
    @classmethod
    def setUpClass(cls):
        print("测试suit开始前都会先先执行一遍setUpClass")
    
    @classmethod
    def tearDownClass(cls):
        print("测试suit结束后都会先先执行一遍tearDownClass")

    def test_fomat_name(self):
        """test format name"""
        print("test_fomat_name")
        name=testcode.get_formatted_name("Bai","Yang")
        self.assertEqual(name,"Bai Yang")
        name=testcode.get_formatted_name("Cao","qi","Wei")
        self.assertEqual(name,"Cao Wei Qi")
    
    def test_add(self):
        """test add"""
        print("test_add")
        val = testcode.add(1,2)
        self.assertEqual(val,3)
    
    def test_sub(self):
        """test sub"""
        print("test_sub")
        val = testcode.sub(1,2)
        if val != -1:
            return -1

    def test_store_response(self):
        """test class"""
        print("test_store_response")
        question = "What language did you first learn to speak?"
        my_survey = testcode.AnonymousSurvey(question)
        my_survey.store_response('English')
        my_survey.store_response('Chinese')
        self.assertIn('English', my_survey.responses)

    """ 测试如何跳过测试用例 """
    @unittest.skip("testskip：我就想跳过了，怎么地")
    def test_skip(self):
        print("测试skip不应该执行到这里")


    @unittest.skipIf(True,"testskipif：if 1,我就跳过了")
    def test_skipif(self):
        print("测试skipif不应该执行到这里")

    @unittest.skipUnless(False,"testskipif：Unless false,我就跳过了")
    def test_skipUnless(self):
        print("测试skipunless不应该执行到这里")

if __name__ == "__main__":
    """
    #默认启用方式一
    unittest.main() #默认执行顺序
    """

    """
    #顺序启用方式一
    suite = unittest.TestSuite()
    suite.addTest(TestFunc("test_fomat_name"))
    suite.addTest(TestFunc("test_add"))
    suite.addTest(TestFunc("test_store_response"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    """

    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestFunc))
    runner = HTMLTestRunner(output="result")
    runner.run(suite)
    """
    
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestFunc))
    with open('HTMLReport.txt', 'w') as f:
        runner = HTMLTestRunner(output="result",stream=f,report_title='Test Report',descriptions=True,verbosity=2)
        runner.run(suite)
    """

    """
    从文件中加载测试所有
    discover（）方法会自动根据测试目录test_dir 匹配查找测试用例文件，并将查找到的测试用例组装到测试套件中，、
    因此，可以直接通过run()方法执行discover，大大简化了测试用例的查找与执行
    """
    """
    #test_suite = unittest.defaultTestLoader.discover('./', pattern='testmain.py')
    test_suite = unittest.defaultTestLoader.discover('./', pattern="test*.py")
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
    """

    test_suite = unittest.defaultTestLoader.discover("./",pattern="test*.py")
    report_html = BeautifulReport(test_suite).report(filename='测试报告', description='搜索测试', log_path='.')  
    #result.report(filename='mpp的测试报告B', description='描述B', log_path='')  # 默认在当前路径下，可以加log_path
