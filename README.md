```buildoutcfg
python3 -m venv pip_example
source pip_example/bin/activate
pip install setuptools
```

Then in the package location to install the package:
```
pip install .
pip install --upgrade .
```

To install the subdirectory package
```buildoutcfg
pip install --upgrade pip_package_example/analytics_library/
```

Now inside a python shell
```
pyexample.__version__
from pyexample import numpy_module
numpy_module.numpy_v_lists()
```

```buildoutcfg
from py_dir_example import numpy_subdir_module
numpy_subdir_module.numpy_v_lists_subdir()
```


