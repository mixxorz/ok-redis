0.1.2 (2016-07-28)
++++++++++++++++++

**Bugfixes**

-  Accessing a field or subkey on a Key that doesn't exist will now raise an
   AttributeError instead of returning None.

0.1.1 (2016-07-07)
++++++++++++++++++

**Features and Improvements**

-  The string representation of a `Key` is now the key itself.
-  Keys now accepts IDs that aren't strings.

0.1.0 (2016-06-26)
++++++++++++++++++

-  Initial release
