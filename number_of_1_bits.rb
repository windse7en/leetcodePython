require 'minitest/autorun'

def hamming_weight(n)
  n.to_s(2).count('1')
end

class TestResult < MiniTest::Unit::TestCase
  def test_output_result
    assert_equal 3, hamming_weight(11)
  end
end
