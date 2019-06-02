#include <iostream>
#include <string>

#include <pybind11/pybind11.h>

using namespace std;

int bindfunction(int x){
    for(int i=0; i<x; i++){
        cout << "Wow. C++" << endl;
    }
    return x;
}

// int main(){
//     bindfunction(4);
    
//     return 0;
// }

PYBIND11_MODULE(astrocpp, m){
    m.def("bindfunction", &bindfunction, "A test bind function");
}