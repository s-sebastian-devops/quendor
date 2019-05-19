#! /usr/bin/env python3

import os
import stat
import zipfile

try:
    from StringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO

package_name = "quendor"
package_directory = package_name
python_directive = "#!/usr/bin/env python3"

packed = StringIO()
packed_writer = zipfile.ZipFile(packed, "w", zipfile.ZIP_DEFLATED)

for dirpath, dirnames, fnames in os.walk(package_directory):
    for fname in fnames:
        fpath = os.path.join(dirpath, fname)
        packed_writer.write(fpath)

packed_writer.writestr(
    "__main__.py",
    """
from {} import __main__
if __name__ == '__main__':
    __main__.main()
""".format(
        package_name
    ),
)

packed_writer.close()

python_file = package_directory + ".py"

with open(python_file, "wb") as f:
    shebang = bytes((python_directive + "\n").encode("ascii"))
    f.write(shebang)
    f.write(packed.getvalue())

os.chmod(python_file, stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)
