require 'minitest/autorun'
require_relative 'input_presenter'

class InputPresenterTest < Minitest::Test
  def test_validate_input
    errors = InputPresenter.validate('{}')
    assert_equal(errors.count, 1)
    # TODO: better test… should be able to do something like this
    # assert_instance_of(JSON::Schema::ValidationError, errors.first) 
  end
end
