require 'json-schema'

class InputPresenter
  def self.validate(input)
    JSON::Validator.fully_validate('schema.json', input, errors_as_objects: true)
  end
end