# pip install GDAL==3.4.3 error



리눅스 상 설치 이슈.



Python Gdal install error gdal-config

```d
root@a14cd49c1aaf:/tmp/gdal-3.2.1# python3 -m pip install GDAL==3.4.3
Collecting GDAL==3.4.3
  Using cached GDAL-3.4.3.tar.gz (757 kB)
  Preparing metadata (setup.py) ... error
  error: subprocess-exited-with-error

  × python setup.py egg_info did not run successfully.
  │ exit code: 1
  ╰─> [131 lines of output]
      WARNING: numpy not available!  Array support will not be enabled
      running egg_info
      creating /tmp/pip-pip-egg-info-mxo_f4os/GDAL.egg-info
      writing /tmp/pip-pip-egg-info-mxo_f4os/GDAL.egg-info/PKG-INFO
      writing dependency_links to /tmp/pip-pip-egg-info-mxo_f4os/GDAL.egg-info/dependency_links.txt
      writing requirements to /tmp/pip-pip-egg-info-mxo_f4os/GDAL.egg-info/requires.txt
      writing top-level names to /tmp/pip-pip-egg-info-mxo_f4os/GDAL.egg-info/top_level.txt
      writing manifest file '/tmp/pip-pip-egg-info-mxo_f4os/GDAL.egg-info/SOURCES.txt'
      Traceback (most recent call last):
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 105, in fetch_config
          p = subprocess.Popen([command, args], stdout=subprocess.PIPE)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/usr/lib/python3.11/subprocess.py", line 1024, in __init__
          self._execute_child(args, executable, preexec_fn, close_fds,
        File "/usr/lib/python3.11/subprocess.py", line 1917, in _execute_child
          raise child_exception_type(errno_num, err_msg, err_filename)
      FileNotFoundError: [Errno 2] No such file or directory: '../../apps/gdal-config'

      During handling of the above exception, another exception occurred:

      Traceback (most recent call last):
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 188, in get_gdal_config
          return fetch_config(option, gdal_config=self.gdal_config)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 108, in fetch_config
          raise gdal_config_error(e)
      gdal_config_error: [Errno 2] No such file or directory: '../../apps/gdal-config'

      During handling of the above exception, another exception occurred:

      Traceback (most recent call last):
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 105, in fetch_config
          p = subprocess.Popen([command, args], stdout=subprocess.PIPE)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/usr/lib/python3.11/subprocess.py", line 1024, in __init__
          self._execute_child(args, executable, preexec_fn, close_fds,
        File "/usr/lib/python3.11/subprocess.py", line 1917, in _execute_child
          raise child_exception_type(errno_num, err_msg, err_filename)
      FileNotFoundError: [Errno 2] No such file or directory: 'gdal-config'

      During handling of the above exception, another exception occurred:

      Traceback (most recent call last):
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 195, in get_gdal_config
          return fetch_config(option)
                 ^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 108, in fetch_config
          raise gdal_config_error(e)
      gdal_config_error: [Errno 2] No such file or directory: 'gdal-config'

      During handling of the above exception, another exception occurred:

      Traceback (most recent call last):
        File "<string>", line 2, in <module>
        File "<pip-setuptools-caller>", line 34, in <module>
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 389, in <module>
          setup(**setup_kwargs)
        File "/usr/lib/python3/dist-packages/setuptools/__init__.py", line 153, in setup
          return distutils.core.setup(**attrs)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/usr/lib/python3.11/distutils/core.py", line 148, in setup
          dist.run_commands()
        File "/usr/lib/python3.11/distutils/dist.py", line 966, in run_commands
          self.run_command(cmd)
        File "/usr/lib/python3.11/distutils/dist.py", line 985, in run_command
          cmd_obj.run()
        File "/usr/lib/python3/dist-packages/setuptools/command/egg_info.py", line 299, in run
          self.find_sources()
        File "/usr/lib/python3/dist-packages/setuptools/command/egg_info.py", line 306, in find_sources
          mm.run()
        File "/usr/lib/python3/dist-packages/setuptools/command/egg_info.py", line 541, in run
          self.add_defaults()
        File "/usr/lib/python3/dist-packages/setuptools/command/egg_info.py", line 578, in add_defaults
          sdist.add_defaults(self)
        File "/usr/lib/python3.11/distutils/command/sdist.py", line 228, in add_defaults
          self._add_defaults_ext()
        File "/usr/lib/python3.11/distutils/command/sdist.py", line 311, in _add_defaults_ext
          build_ext = self.get_finalized_command('build_ext')
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/usr/lib/python3.11/distutils/cmd.py", line 299, in get_finalized_command
          cmd_obj.ensure_finalized()
        File "/usr/lib/python3.11/distutils/cmd.py", line 107, in ensure_finalized
          self.finalize_options()
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 258, in finalize_options
          self.gdaldir = self.get_gdal_config('prefix')
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 201, in get_gdal_config
          raise gdal_config_error(traceback_string + '\n' + msg)
      gdal_config_error: Traceback (most recent call last):
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 105, in fetch_config
          p = subprocess.Popen([command, args], stdout=subprocess.PIPE)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/usr/lib/python3.11/subprocess.py", line 1024, in __init__
          self._execute_child(args, executable, preexec_fn, close_fds,
        File "/usr/lib/python3.11/subprocess.py", line 1917, in _execute_child
          raise child_exception_type(errno_num, err_msg, err_filename)
      FileNotFoundError: [Errno 2] No such file or directory: '../../apps/gdal-config'

      During handling of the above exception, another exception occurred:

      Traceback (most recent call last):
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 188, in get_gdal_config
          return fetch_config(option, gdal_config=self.gdal_config)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 108, in fetch_config
          raise gdal_config_error(e)
      gdal_config_error: [Errno 2] No such file or directory: '../../apps/gdal-config'

      During handling of the above exception, another exception occurred:

      Traceback (most recent call last):
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 105, in fetch_config
          p = subprocess.Popen([command, args], stdout=subprocess.PIPE)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/usr/lib/python3.11/subprocess.py", line 1024, in __init__
          self._execute_child(args, executable, preexec_fn, close_fds,
        File "/usr/lib/python3.11/subprocess.py", line 1917, in _execute_child
          raise child_exception_type(errno_num, err_msg, err_filename)
      FileNotFoundError: [Errno 2] No such file or directory: 'gdal-config'

      During handling of the above exception, another exception occurred:

      Traceback (most recent call last):
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 195, in get_gdal_config
          return fetch_config(option)
                 ^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-install-pxriaxyj/gdal_37a54deca8a94dc5817c5f3fdab72ac3/setup.py", line 108, in fetch_config
          raise gdal_config_error(e)
      gdal_config_error: [Errno 2] No such file or directory: 'gdal-config'

      Could not find gdal-config. Make sure you have installed the GDAL native library and development headers.
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.

```

일단 이런 에러가 발생했다.

```bash
add-apt-repository ppa:ubuntugis/ppa

apt update && \
    apt install -y \
    gdal-bin \
    python3-gdal \
    libgdal-dev
```

보통은 GDAL이 리눅스나 운영체제에 설치되어있고 그 후에 Pip로 GDAL이 발생하는것이 기본이다.

위 커맨드를 실행하여 기본적인 gdal 종속성 관련 설치를 할 수 있다.





그러나.

내가 실행한 환경은

ubuntu22.04에서 

python3.11로 gdal을 설치하는 과정이다.

ubuntu22.04에서 설치를 해도 해당 apt관련 종속성이 python3.10을 타겟으로 하고 

python3.10 버전이 설치되면서 그 위에다 python3.10에 맞는 GDAL을 설치해버리는 이슈가 발생했다.

apt명령을 jammy 관련 릴리즈를 확인해보니 python3.10 이였다



따라서 ubuntu baseImage를 ubuntu23.04로 업데이트 하거나 카카오 apt 저장소를 해당 버전에 맞추어 변경하면 된다.

