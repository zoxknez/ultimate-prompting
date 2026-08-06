class ImportService
  # Vulnerable: YAML.load (not YAML.safe_load) deserializes arbitrary Ruby
  # objects from the imported string, not just plain data. A crafted YAML
  # payload can instantiate arbitrary classes available in this process -
  # including ones whose constructors or coercion methods have side
  # effects - which is a well-documented path to remote code execution in
  # Ruby applications that call the unsafe form of YAML.load on
  # user-supplied input.
  def self.import_settings(yaml_string)
    YAML.load(yaml_string)
  end
end
