#include <iostream>

// Namespace = provides a solution for preventing name conflicts in large projects
// Each entity needs a unique name. A namespace allows for identically named entities
// as long as the namespaces are different.
    
// // This code is wrong
// int main(){

//     int x = 0;
//     int x = 1;
//     return 0;
// }


namespace first{
    int x = 1;
}
namespace second{
    int x = 2;
}

int main(){
    using namespace second; // if we included this line we don't need pur std:: in the next lines; std instead of second
    std::cout << x; // second x

    return 0;

}