#include <iostream>

int main(){
    const double PI = 3.14159; // with constant we can't change the value, that is a keyword
    double radius = 10;
    double circumference = 2 * PI * radius;

    std::cout << circumference << "cm";
    
    return 0;
}

// https://www.youtube.com/watch?v=-TkoO8Z07hI&ab_channel=BroCode
// 26min