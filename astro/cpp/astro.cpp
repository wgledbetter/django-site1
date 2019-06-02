#include <iostream>
#include <string>

#include <pybind11/pybind11.h>

using namespace std;

const string bindfunction(int x){
    for(int i=0; i<x; i++){
        cout << "Wow. C++" << endl;
    }
    string s("A string from C++");
    return strcat("This is a string from C++: ", to_string(x).c_str());
}

// int main(){
//     bindfunction(4);
    
//     return 0;
// }

PYBIND11_MODULE(astro, m){
    m.def("bindfunction", &bindfunction, "A test bind function");
}