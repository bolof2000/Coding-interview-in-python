import unittest
from Solutions import coding_interview

class TestCodingInterview(unittest.TestCase):

    def test_anagram_solutions(self):

       result = coding_interview.anagram_solutions("bolfinde","finbolode")
       self.assertEqual(result, False)

    def test_reverse_array(self):
      result = coding_interview.reverse_array([1,2,3,4,5])
      self.assertEqual(result,[5,4,3,2,1])


if __name__ == '__main__':
  unittest.main()