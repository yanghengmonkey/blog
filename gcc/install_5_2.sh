wget ftp://ftp.gnu.org/gnu/gcc/gcc-5.2.0/gcc-5.2.0.tar.bz2
tar xvf gcc-5.2.0.tar.bz2
./contrib/download_prerequisites
./configure --enable-languages=c,c++ --disable-multilib
make -j8
sudo make install

