wget https://www.nasm.us/pub/nasm/releasebuilds/2.15.05/nasm-2.15.05.tar.bz2
tar xfj nasm-2.15.05.tar.bz2
cd nasm-2.15.05
./autogen.sh
./configure --prefix=/usr/local/ 
make 
sudo make install
#hash -d nasm
cd ..
rm nasm-2.15.05.tar.bz2