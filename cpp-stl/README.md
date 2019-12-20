# C++ STL

## vector
 - access elements  
    |   method         |   description        |
    |--------|-------|
    |vec[i] |    access element where index = i       |
    |vec.at(i)|access element where index = i  |
    |vec.front()|return first element|
    |vec.back()|return last element|

- add or remove elements  
    |method|description|
    |---|---|
    |vec.push_back()|add new element to the rear of the vector|
    |vec.pop_back()|delete last element of vector|
    |vec.insert()|insert element(s) randomly into vector|
    |vec.erase()|delete element(s) in vector|
    |vec.clear()|clear everything in vector|
- get capacity/size
|method|description|
|---|---|
|vec.empty()|return true if vector is empty|
|vec.size()|return the aize of vector|
|vec.resize()|
|vec.capacity()|
|vec.reserve()|

- Iterator
|method|description|
|---|---|
|vec.begin()|
|vec.end()|
|vec.rbegin()|
|vec.rend()|

``` c++
#include <iostream>
#include <vector>

int main ()
{
  std::vector<int> vec;
  vec.push_back(1);
}
```
## set

## map
