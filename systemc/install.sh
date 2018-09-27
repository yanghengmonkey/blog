wget http://www.accellera.org/images/downloads/standards/systemc/systemc-2.3.1a.tar.gz
tar xvf systemc-2.3.1a.tar.gz
cd systemc-2.3.1a
mkdir tmp
cd tmp
../configure --prefix=/usr/local/systemc-2.3.1
make
make install
export SYSTEMC_HOME=/usr/local/systemc-2.3.1
export LD_LIBRARY_PATH=/usr/local/systemc-2.3.1/lib-linux64:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/systemc-2.3.1/lib:$LD_LIBRARY_PATH
