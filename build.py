#! /usr/bin/env python3

import os
import stat
import zipfile

try:
    from StringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO

package_directory = "quendor"
python_directive = "#!/usr/bin/env python3"

packed = StringIO()
packed_writer = zipfile.ZipFile(packed, "w", zipfile.ZIP_DEFLATED)

for file_name in os.listdir(package_directory):
    file_path = os.path.join(package_directory, file_name)

    if os.path.isdir(file_path):
        for file_name in os.listdir(file_path):
            file_path = os.path.join(file_path, file_name)

    if os.path.isfile(file_path):
        packed_writer.write(file_path)

packed_writer.writestr(
    "__main__.py",
    """
from quendor import __main__
if __name__ == '__main__':
    __main__.main()
""",
)

packed_writer.close()

python_file = package_directory + ".py"

with open(python_file, "wb") as f:
    shebang = bytes((python_directive + "\n").encode("ascii"))
    f.write(shebang)
    f.write(packed.getvalue())

os.chmod(python_file, stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)
