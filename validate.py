import re

class Validate:
  def check_addr(self, address):
    [local, domain] = address.split('@')
    print(local, domain)
    p = re.compile("[^a-zA-Z!#\$%&'\*\+\-\/=\?\^_`\\{\|\}~]+")
    return not(bool(p.match(domain)))

  def validate_addr_spec(self, stream_in, stream_out):
    results = []
    for line in stream_in.readlines():
      results.append('ok' if self.check_addr(line) else 'ng')
    for result in results:
      stream_out.write(result + "\n")
