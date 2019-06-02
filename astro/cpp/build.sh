SOURCENAME=astrocpp.cpp
OUTNAME=astrocpp`python3-config --extension-suffix`
COMPILER=g++
PREARGS='-O3 -Wall -shared -std=c++17 -fPIC'
INCLUDES=`python3 -m pybind11 --includes`

rm $OUTNAME
rm ../$OUTNAME

$COMPILER $PREARGS $INCLUDES $SOURCENAME -o $OUTNAME

chmod 777 $OUTNAME
cp $OUTNAME ../$OUTNAME