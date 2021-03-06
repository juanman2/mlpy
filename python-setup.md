_Python Setup notes_

* Installed python3 with brew
  This is a mistake actually, because it installed python 3.9.
   `brew install python3`
   In retrospect check to see if any old version of venv is running, if not install one.
   Then bootstrap everything with venv like this:
   ```
    virtualenv --system-site-packages -p python3.8 python-venv-3.8.5
	pip install --upgrade pip3
   ```
   then using this venv to all pip upgrades ... *phew*  I'm not even sure if this would work.
* Added pip
   ```shell
   git clone git@github.com:pypa/pip.git pip
   python3 setup.py install
   ```
* Added pymode.el to init.elisp
   https://realpython.com/emacs-the-best-python-editor/
* Created an env directory python-venv
   ```shell
   python3 -m venv env 
   source python/venv/env/bin/activate
   deactivate
   ```
* Python tools
	```shell
   pip3 -q install bcrypt
   pip3 install virtualenvwrapper
   pip3 install jupyter
   pip3 install torch torchvision
   pip install numpy pandas requests
   ```
   * Notebooks: Jupiter/ein notes
	   * ein start
	   * <ctrl-c> <ctrl-c>
	   * 
* TensorFlow Keras
https://margaretmz.medium.com/anaconda-jupyter-notebook-tensorflow-and-keras-b91f381405f8
  Careful here, you must be in a venv, go figure.  It has to do with 
  conflicting between MACs system python libraries and your own.
  ```shell
  virtualenv --system-site-packages -p python3.8 venv-3.8.6
  source venv-3.8.6/bin/activate 
  pip install --upgrade pip
  pip install --upgrade tensorflow
  pip install --upgrade Keras
  ```
* Jupyter in Emacs
  see: https://millejoh.github.io/emacs-ipython-notebook/#running-a-jupyter-notebook-server-from-emacs
  We added ein, and elpy to the emacs setup, but struggled with getting jupyter to use the 3.8.6 venv.
  To start jupyter in the correct venv:
  ```
  (venv-3.8.6) $ jupyter notebook --notebook-dir=~/src/juanman2/mlpy/notebook/ --no-browser &
  ```
  Then from emacs
  ```
  m-x ein:login
  ```
  
