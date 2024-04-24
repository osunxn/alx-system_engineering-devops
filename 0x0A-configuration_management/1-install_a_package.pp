#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Or the version that works with Flask (2.1.0)
package {'werkzeug':
  ensure   => '2.0.2',
  provider => 'pip3',
}
